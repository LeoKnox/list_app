from django import forms

from .models import My_List

class ListForm(forms.Form):
    class Meta:
        model = My_List

        fields = [
            'item',
            'qty',
            'substitute',
            'urgent'
        ]