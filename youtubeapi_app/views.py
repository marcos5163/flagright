# youtubeapi_app/views.py
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Video, MetaData
from .forms import VideoFilterForm
from django.db.models import Q

def dashboard(request):
    videos = Video.objects.all().order_by('published_datetime')

    # Filter videos based on search query
    search_query = request.GET.get('search_query')
    if search_query:
        videos = videos.filter(Q(title__icontains=search_query)| Q(description__icontains=search_query))

    # Sort videos based on user selection
    sort_by = request.GET.get('sort_by')

    flag = request.GET.get('flag')

    meta_data = MetaData.objects.filter().first()

    if flag == 'pause':
        if meta_data:
            meta_data.flag = False
            meta_data.save()
        else:
            MetaData.objects.create(flag=True)    
    elif flag == 'resume':
        if meta_data:
            meta_data.flag = True
            meta_data.save()  
    

    if sort_by=='published_datetime_dsc':
        sort_by = '-published_datetime'
    elif sort_by=='published_datetime_asc':
        sort_by = 'published_datetime'   
    
    
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
        'video_count': Video.objects.all().count(),
        'form': VideoFilterForm(initial={'search_query': search_query, 'sort_by': sort_by}),
    }

    return render(request, 'youtubeapi_app/dashboard.html', context)
