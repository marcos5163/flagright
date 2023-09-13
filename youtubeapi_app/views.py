# youtubeapi_app/views.py
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Video
from .forms import VideoFilterForm

def dashboard(request):
    videos = Video.objects.all()

    # Filter videos based on search query
    search_query = request.GET.get('search_query')
    if search_query:
        videos = videos.filter(title__icontains=search_query)

    # Sort videos based on user selection
    sort_by = request.GET.get('sort_by')
    if sort_by:
        videos = videos.order_by(sort_by)

    # Pagination
    paginator = Paginator(videos, 10)  # Show 10 videos per page
    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    context = {
        'videos': videos,
        'form': VideoFilterForm(initial={'search_query': search_query, 'sort_by': sort_by}),
    }

    return render(request, 'youtubeapi_app/dashboard.html', context)
