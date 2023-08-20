from django.shortcuts import render,redirect
from django.views.generic.base import View

# Create your views here.

class CreateProfileView(View):
    def get(self,request):
        return render(request,"profiles/create_profile.html")
    
    def post(self,request):
        print(request.FILES["image"])
        return redirect("/profile")
