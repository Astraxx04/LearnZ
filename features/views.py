from django.shortcuts import render, redirect

# Create your views here.
def feature_page(request):
    return render(request, "features/features.html")

def upload_view(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PDFUploadForm()
    return render(request, 'upload.html', {'form': form})

from django import forms

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(label='Select a PDF file')