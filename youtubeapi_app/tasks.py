import asyncio
from celery import shared_task
from youtubeapi_app.service import fetch_and_store_videos
from .models import Video

@shared_task
def fetching_youtube_vedio_data():
    
    video_data = Video.objects.all().order_by('-created_at').first() 
    
    next_page_token = None
    if video_data:
        next_page_token = video_data.next_page_token
    
    asyncio.run(fetch_and_store_videos(next_page_token))
        
    