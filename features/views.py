from django.shortcuts import render

# Create your views here.
def feature_page(request):
    return render(request, "features/features.html")