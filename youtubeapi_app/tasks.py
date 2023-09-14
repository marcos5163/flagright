import asyncio
from celery import shared_task
from youtubeapi_app.service import fetch_and_store_videos
from .models import Video, MetaData

@shared_task
def fetching_youtube_vedio_data():
    
    task_to_be_executed = MetaData.objects.filter().first().flag
    if task_to_be_executed:
        video_data = Video.objects.all().order_by('-created_at').first() 
        
        next_page_token = None
        if video_data:
            next_page_token = video_data.next_page_token
        
        asyncio.run(fetch_and_store_videos(next_page_token))
    else:
        print("Skipping this task...")    
        
    