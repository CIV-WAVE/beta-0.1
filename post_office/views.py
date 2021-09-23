from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import generic

from .forms import UserForm
from . import models


def home(request):
    return render(request, 'post_office/home.html')


def passport_application(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            # Create Passport
            models.Passport.objects.create(
                user=user,
                name=user.username,
                key=user.password,
            )

            login(request, user)
            return redirect('post_office:home')

    else:
        form = UserForm()

    return render(request, 'post_office/passport_application.html', {'form': form})


def passport_list(request):
    passports = models.Passport.objects.all()
    return render(request, 'post_office/passport_list.html', {'passports': passports})


class PassportDetailView(generic.DetailView):
    model = models.Passport
    template_name = 'post_office/passport_detail.html'
    context_object_name = 'passport'
