import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, FileResponse
from django.views.static import serve

def index_view(request):
    index_path = settings.BASE_DIR.parent / 'frontend' / 'dist' / 'index.html'
    if os.path.exists(index_path):
        return FileResponse(open(index_path, 'rb'), content_type='text/html')
    return HttpResponse("Frontend dist not found. Please build frontend first.", status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rag_app.urls')),
    path('', index_view, name='index'),
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR.parent / 'frontend' / 'dist' / 'assets'}),
    re_path(r'^(?P<path>favicon\.svg|icons\.svg)$', serve, {'document_root': settings.BASE_DIR.parent / 'frontend' / 'dist'}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
