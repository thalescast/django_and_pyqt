from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from .forms import FormUploadFile


class HomeView(TemplateView):
    template_name = "home.html"


class SuccessView(TemplateView):
    template_name = "success_upload.html"


@login_required
def my_logout(request):
    logout(request)
    return redirect('home')


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = FormUploadFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_upload')
    else:
        form = FormUploadFile()
    return render(request, 'file_upload.html', {'form': form})
