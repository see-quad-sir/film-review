from django import forms


class SortForm(forms.Form):
    sort_choices = [
        ("default", "Default"),
        ("rate_ascending", "Ascending"),
        ("rate_descending", "Descending"),
    ]
    choice = forms.fields.ChoiceField(choices=sort_choices, required=True, label="Sort")
