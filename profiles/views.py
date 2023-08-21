# from django.shortcuts import render, redirect
# from django.views.generic.base import View
# from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profile/"

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             submitted_form.save()
#             return redirect("/profile")

#         return render(request, "profiles/create_profile.html", {"form": submitted_form})

class ProfileView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profile"
