from django import forms
from . models import mytable
class myform(forms.modelform):
    class meta:
        model=mytablefield=[
            "title"
            "description",
        ]