from django import forms

class QueryForm(forms.Form):
    sql_text = forms.CharField(widget=forms.Textarea)
