from django.forms import ModelForm
from rate.models import Rating

class RatingForm(ModelForm):
    form_class = Rating


    class Meta:
        model = Rating
        fields = "__all__"