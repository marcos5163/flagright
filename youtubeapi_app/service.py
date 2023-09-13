import asyncio
from asgiref.sync import sync_to_async
from googleapiclient.discovery import build
from .models import Video

# Sample API keys
API_KEYS = [
    'AIzaSyANyWSymok5K2sb9qwMZCNwljgV-B51XsQ',
    'AIzaSyAng2SCK0KfpjfhngukIY4nIgCFfj9ycKE', 
]

key_in_use = 0

@sync_to_async
def save_video_to_database(video_id, snippet, next_page_token):
    # Create and save the video object in the database
    try:
        Video.objects.create(
            video_id=video_id,
            title=snippet['title'],
            description=snippet['description'],
            published_datetime=snippet['publishedAt'],
            thumbnail_url=snippet['thumbnails']['default']['url'],
            next_page_token=next_page_token
        )
    except Exception:
        pass    

async def fetch_and_store_videos(next_page_token=None):
    global key_in_use
    
    # Initialize the YouTube API client
    youtube = build('youtube', 'v3', developerKey=API_KEYS[key_in_use])
    
    try:
        # Make API request to fetch videos
        request = await asyncio.to_thread(
            youtube.search().list,
            q='tech',
            type='video',
            part='id',
            maxResults=10,
            pageToken=next_page_token
        )
        response = request.execute()
    except Exception as e:
        if 'quota' in str(e).lower():
            key_in_use = (key_in_use + 1) % len(API_KEYS)  
            if key_in_use == 0:
                raise Exception("All API keys exhausted") 
            else:
                print(f"Switched to API key {key_in_use}")
            return await fetch_and_store_videos(next_page_token)
    
    next_page_token = response['nextPageToken']
    # Process and store videos in the database
    for item in response['items']:
        video_id = item['id']['videoId']
        print("Fetching details for video id:", video_id)
        video_info = await asyncio.to_thread(
            youtube.videos().list,
            part='snippet',
            id=video_id
        )

        snippet = video_info.execute()['items'][0]['snippet']
        # Use sync_to_async to save the video to the database
        await save_video_to_database(video_id, snippet, next_page_token)
