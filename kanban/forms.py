from django import forms

class TodoForm(forms.Form):

    text = forms.TextInput()

    class meta:
        fields = ("text",)
