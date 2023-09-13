from django.db import models


class Video(models.Model):
    """
    Video model for storing video related data, indexing fields that are commanly used queries.
    """
    video_id = models.CharField(max_length=50, unique=True, db_index=True)  
    title = models.CharField(max_length=200, db_index=True) 
    description = models.TextField(db_index=True) 
    published_datetime = models.DateTimeField(db_index=True)
    thumbnail_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    next_page_token = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.title
    
    