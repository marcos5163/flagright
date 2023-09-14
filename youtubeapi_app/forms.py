# youtubeapi_app/forms.py
from django import forms

class VideoFilterForm(forms.Form):
    search_query = forms.CharField(required=False, label='Search')
    sort_by = forms.CharField(
        required=False,
        label='Sort By',
    )
    flag = forms.CharField(required=False, label='flag')
