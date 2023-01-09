from django import forms

class MyFileForm(forms.Form):
    file_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    file=forms.FileField(widget=forms.FileInput(attrs={'class':'form-file-control'}))

class MyQuizForm(forms.Form):
    quiz_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    link=forms.URLField(widget=forms.URLInput(attrs={'class':'form-control'}))