
# Create your views here.

# ----------------------- Function Based View---------------------------

from django.shortcuts import render, redirect, get_object_or_404
from .profileForm import ProfileForm
from django.urls import reverse
from django.http import HttpResponse
from .models import Profile
import os




def profileCreate(request):
    if request.method=='POST':
        pform=ProfileForm(request.POST,request.FILES)
        print(pform)
        if pform.is_valid():
            pform.save()
            return redirect(reverse('profileapp:profile_list'))
    else:
        pform= ProfileForm()
    return render(request,'profile/create_profile.html',{'form':pform})

# Retrieve task list
def profileList(request):
    prdata = Profile.objects.all()
    return render(request, "profile/profile_list.html", { "data": prdata})

# Update a single task
def profileUpdate(request, pk):
    prdata = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(instance=prdata, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("profileapp:profile_detail", args=[pk,]))
    else:
        form = ProfileForm(instance=prdata)

    return render(request, "profile/create_profile.html", { "form": form, "object": prdata})

# Retrieve a single task
def profileDetail(request, pk):
    prdata = get_object_or_404(Profile, pk=pk)
    return render(request, "profile/profile_detail.html", { "data": prdata })


def profileDelete(request, pk):
    #prdata = get_object_or_404(Profile, pk=pk)
    prdata=Profile.objects.filter(pk=pk).first()
    if prdata:
        return redirect(reverse('profileapp:profile_condelete',args=[pk]))
    
    return redirect(reverse("profileapp:profile_list"))

def confirmDelete(request,pk):
    prdata=Profile.objects.filter(pk=pk).first()
    if request.method=='POST':
        if prdata:
            if prdata.profilePicture:
                path = prdata.profilePicture.path
                if os.path.exists(path):
                    os.remove(path)

            if prdata.cv:
                path = prdata.cv.path
                if os.path.exists(path):
                    os.remove(path)

            if prdata.shortVideo:
                path = prdata.shortVideo.path
                if os.path.exists(path):
                    os.remove(path)

            prdata.delete()
            return redirect(reverse('profileapp:profile_list'))
    return render(request,'profile/profile_confdelete.html',{'data':prdata})


# ---------------------------------------------------------------------


# --------------------------- Class Based View -------------------------
"""
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .profileForm import ProfileForm
from .models import Profile

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/create_profile.html'
    success_url = reverse_lazy('profileapp:profile_list')

class ProfileListView(ListView):
    model = Profile
    template_name = 'profile/profile_list.html'
    context_object_name = 'data'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'data'

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/create_profile.html'
    context_object_name = 'object'
    success_url = reverse_lazy('profileapp:profile_list')

import os
from django.urls import reverse_lazy
from django.views.generic import View, RedirectView, TemplateView
from django.shortcuts import redirect, get_object_or_404
from .models import Profile
from django.shortcuts import render

class ProfileDeleteView(RedirectView):
    def get_redirect_url(self, pk):
        profile = get_object_or_404(Profile, pk=pk)
        return reverse_lazy('profileapp:profile_condelete', args=[profile.pk])

class ConfirmDeleteView(View):
    template_name = 'profile/profile_confdelete.html'

    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        return render(request, self.template_name, {'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        if profile.profilePicture:
            path = profile.profilePicture.path
            if os.path.exists(path):
                os.remove(path)
        
        if profile.cv:
            path = profile.cv.path
            if os.path.exists(path):
                os.remove(path)
        
        if profile.shortVideo:
            path = profile.shortVideo.path
            if os.path.exists(path):
                os.remove(path)

        profile.delete()
        return redirect(reverse_lazy('profileapp:profile_list'))

profile_delete_view = ProfileDeleteView.as_view()
confirm_delete_view = ConfirmDeleteView.as_view()
"""

