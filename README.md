# flagright
flagright assignment 

1. Created a django application with postgres database, using django celery for runing cron job in background and redis as a celery broker.
2. Created a table `Video` to store video related with proper indexing on frequently queried columnns like `title`,`description` etc
3. Here [logic for fetching video data](https://github.com/marcos5163/flagright/blob/main/youtubeapi_app/service.py), `fetch_and_store_videos` is responsible for fetching videos data and save it in db, which supports mutiple api keys and switch api keys,
   if any particular key's limit exceeds.
4. Configured celery beat [link](https://github.com/marcos5163/flagright/blob/main/flagright_project/celery.py) to execute this task in every 10 seconds
5. Created an end points `dashboard/` for which gets the search query and render all video paginatedly accordingly.
6. Using django templates and forms for rendering dashboard, here is the html template for that [link](https://github.com/marcos5163/flagright/blob/main/youtubeapi_app/templates/youtubeapi_app/dashboard.html) User can search with title and desc.
7. After building docker-compose.yml, dashboard will be rendered at `localhost:8000/dashboard/`   
   
   
