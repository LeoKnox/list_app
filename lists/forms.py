from django import forms

from .models import My_List

class ListForm(forms.ModelForm):
    class Meta:
        model = My_List

        fields = [
            'item',
            'qty',
            'subsititute',
            'urgent'
        ]