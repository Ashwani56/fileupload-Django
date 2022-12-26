from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import MovieForm
from .models import Movies

# Create your views here.
def index(request):
    return render(request,'index.html')
def upload(request):
	if request.method == "POST":
		form = MovieForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("upload")
	form = MovieForm()
	movies = Movies.objects.all()
	return render(request=request, template_name="upload.html", context={'form':form, 'movies':movies})  