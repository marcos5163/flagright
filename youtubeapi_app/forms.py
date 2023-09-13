# youtubeapi_app/forms.py
from django import forms

class VideoFilterForm(forms.Form):
    search_query = forms.CharField(required=False, label='Search')
    sort_by = forms.ChoiceField(
        required=False,
        label='Sort By',
        choices=(
            ('-published_datetime', 'Published Date (Descending)'),
            ('published_datetime', 'Published Date (Ascending)'),
            # Add more sorting options as needed
        )
    )
