
from django import forms


class MyfileUploadForm(forms.Form):
    # file_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    files_data1 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    files_data2 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    files_data3 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    files_data4 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
