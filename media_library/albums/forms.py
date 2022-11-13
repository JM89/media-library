from datetime import date

from django.apps import AppConfig
from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput

from albums.models import Album


class AlbumsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'albums'


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'date_acquired': DateInput(attrs={"type": "date"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Date purchased cannot be in the past")
        return d
