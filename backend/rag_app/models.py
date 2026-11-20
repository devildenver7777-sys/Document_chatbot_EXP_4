import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta

class DocumentSession(models.Model):
    """
    Session model storing uploaded document metadata, parsed structured pages,
    and auditing counters (NFR-5, NFR-10, FR-13, FR-14).
    """
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(default=None, null=True, blank=True)

    document_name = models.CharField(max_length=255, default="No document uploaded")
    document_type = models.CharField(max_length=20, default="none")
    file_size_bytes = models.IntegerField(default=0)
    page_count = models.IntegerField(default=0)
    unreadable_pages = models.JSONField(default=list, blank=True)
    
    # Structured parsed pages: list of {page_number, title, sections, text}
    parsed_pages = models.JSONField(default=list, blank=True)
    
    # Audit counters (NFR-10)
    refusal_count = models.IntegerField(default=0)
    error_count = models.IntegerField(default=0)
    query_count = models.IntegerField(default=0)
    
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            # 24-hour expiration policy per NFR-5
            self.expires_at = timezone.now() + timedelta(hours=24)
        super().save(*args, **kwargs)

    def is_expired(self) -> bool:
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"Session {self.session_id} ({self.document_name})"


class ChatMessage(models.Model):
    """
    Stores conversational turns within a session (FR-10).
    """
    session = models.ForeignKey(DocumentSession, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=15, choices=[('user', 'User'), ('assistant', 'Assistant'), ('system', 'System')])
    content = models.TextField()
    citations = models.JSONField(default=list, blank=True)
    is_refusal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.session_id} - {self.role}: {self.content[:40]}"
