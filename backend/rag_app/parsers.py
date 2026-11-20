"""
Document parsers and validators for Document-Grounded Gemini Chatbot.
Supports PDF, DOCX, TXT, and Markdown (MD).
Enforces SRS FR-2, FR-3, FR-4, 6.3, 6.4.
"""

import os
import re
from typing import Dict, List, Any, Tuple
from pypdf import PdfReader
import docx

MAX_FILE_SIZE_BYTES = 50 * 1024 * 1024  # 50 MB (FR-2)
MAX_PAGE_COUNT = 300                     # 300 pages (FR-2)
SUPPORTED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.md'}

class ParsingError(Exception):
    pass

class FileValidationError(Exception):
    pass

def validate_uploaded_file(file_obj) -> Tuple[str, int]:
    """
    Validates file extension and size before reading or passing to model (FR-2, FR-3).
    Returns (extension, size_bytes).
    """
    file_name = file_obj.name.strip()
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()

    if ext not in SUPPORTED_EXTENSIONS:
        raise FileValidationError(
            f"Unsupported file format '{ext}'. Allowed formats: PDF, DOCX, TXT, and Markdown (MD). (FR-3)"
        )

    file_size = file_obj.size
    if file_size > MAX_FILE_SIZE_BYTES:
        size_mb = file_size / (1024 * 1024)
        raise FileValidationError(
            f"File size exceeds 50 MB limit (current: {size_mb:.2f} MB). (FR-2, FR-3)"
        )

    return ext, file_size


def parse_pdf(file_path: str) -> Dict[str, Any]:
    """
    Extracts text from PDF retaining page numbers, detecting unreadable pages (FR-4, 6.3).
    """
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    if total_pages > MAX_PAGE_COUNT:
        raise FileValidationError(
            f"Document exceeds 300 pages limit (current: {total_pages} pages). (FR-2, FR-3)"
        )

    pages = []
    unreadable_pages = []

    for idx, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
            text = text.strip()
            if not text:
                unreadable_pages.append(idx)
            
            # Detect section titles/headings
            sections = extract_headings_from_text(text)
            pages.append({
                "page_number": idx,
                "title": sections[0] if sections else f"Page {idx}",
                "sections": sections,
                "text": text
            })
        except Exception:
            unreadable_pages.append(idx)
            pages.append({
                "page_number": idx,
                "title": f"Page {idx} (Unreadable)",
                "sections": [],
                "text": ""
            })

    return {
        "page_count": total_pages,
        "unreadable_pages": unreadable_pages,
        "pages": pages
    }


def parse_docx(file_path: str) -> Dict[str, Any]:
    """
    Extracts text from DOCX retaining sections/headings and approximate page chunks (FR-4, 6.3).
    """
    doc = docx.Document(file_path)
    paragraphs = []
    current_heading = "Introduction"
    pages = []
    current_page_text = []
    page_num = 1
    unreadable_pages = []

    # Standard ~400 words per page estimation for docx
    words_per_page = 400
    current_word_count = 0

    for p in doc.paragraphs:
        txt = p.text.strip()
        if not txt:
            continue
        if p.style and p.style.name.startswith("Heading"):
            current_heading = txt
        current_page_text.append(txt)
        current_word_count += len(txt.split())

        if current_word_count >= words_per_page:
            full_text = "\n".join(current_page_text)
            sections = extract_headings_from_text(full_text)
            pages.append({
                "page_number": page_num,
                "title": sections[0] if sections else f"Section {page_num}",
                "sections": sections,
                "text": full_text
            })
            page_num += 1
            current_page_text = []
            current_word_count = 0

    if current_page_text:
        full_text = "\n".join(current_page_text)
        sections = extract_headings_from_text(full_text)
        pages.append({
            "page_number": page_num,
            "title": sections[0] if sections else f"Section {page_num}",
            "sections": sections,
            "text": full_text
        })

    if not pages:
        pages.append({
            "page_number": 1,
            "title": "Empty Document",
            "sections": [],
            "text": ""
        })
        unreadable_pages.append(1)

    if len(pages) > MAX_PAGE_COUNT:
        raise FileValidationError(
            f"Document exceeds 300 pages limit (estimated: {len(pages)} pages). (FR-2, FR-3)"
        )

    return {
        "page_count": len(pages),
        "unreadable_pages": unreadable_pages,
        "pages": pages
    }


def parse_text_or_markdown(file_path: str) -> Dict[str, Any]:
    """
    Extracts text from TXT or MD files, chunking by headings or ~500 word page boundaries.
    """
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    if not content.strip():
        return {
            "page_count": 1,
            "unreadable_pages": [1],
            "pages": [{"page_number": 1, "title": "Empty Document", "sections": [], "text": ""}]
        }

    lines = content.splitlines()
    pages = []
    current_chunk = []
    current_words = 0
    page_num = 1
    unreadable_pages = []

    for line in lines:
        current_chunk.append(line)
        current_words += len(line.split())
        # Break on explicit markdown h1/h2 or ~450 words
        if (line.startswith("# ") or line.startswith("## ") or current_words >= 450) and len(current_chunk) > 5:
            txt = "\n".join(current_chunk).strip()
            sections = extract_headings_from_text(txt)
            pages.append({
                "page_number": page_num,
                "title": sections[0] if sections else f"Page {page_num}",
                "sections": sections,
                "text": txt
            })
            page_num += 1
            current_chunk = []
            current_words = 0

    if current_chunk:
        txt = "\n".join(current_chunk).strip()
        sections = extract_headings_from_text(txt)
        pages.append({
            "page_number": page_num,
            "title": sections[0] if sections else f"Page {page_num}",
            "sections": sections,
            "text": txt
        })

    if len(pages) > MAX_PAGE_COUNT:
        raise FileValidationError(
            f"Document exceeds 300 pages limit (estimated: {len(pages)} pages). (FR-2, FR-3)"
        )

    return {
        "page_count": len(pages),
        "unreadable_pages": unreadable_pages,
        "pages": pages
    }


def extract_headings_from_text(text: str) -> List[str]:
    """
    Extracts policy or section headings from text.
    """
    headings = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.match(r'^(Policy\s+\d+|Section\s+\d+|Preface|Contents|Procedures|Review and Revision|#[#\s]*)', line, re.IGNORECASE):
            clean_head = re.sub(r'^[#\s]+', '', line).strip()
            if clean_head and clean_head not in headings:
                headings.append(clean_head)
    return headings


def parse_document(file_path: str, ext: str) -> Dict[str, Any]:
    """
    Unified entry point for document parsing.
    """
    ext = ext.lower()
    if ext == '.pdf':
        return parse_pdf(file_path)
    elif ext == '.docx':
        return parse_docx(file_path)
    elif ext in ['.txt', '.md']:
        return parse_text_or_markdown(file_path)
    else:
        raise FileValidationError(f"Unsupported format '{ext}'.")
