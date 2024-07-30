from django import forms
from django.forms import ModelForm


class SortForm(forms.Form):
    sort_choices = [
        ("default", "Default"),
        ("rate_ascending", "Ascending"),
        ("rate_descending", "Descending"),
    ]
    choice = forms.fields.ChoiceField(choices=sort_choices, required=True, label="Sort")


class ReviewForm(forms.Form):
    review = forms.fields.CharField(widget=forms.widgets.Textarea, label="Review")
    rating = forms.fields.IntegerField(label="Rating")
