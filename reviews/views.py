from typing import Any, Dict
from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from .models import Review


# Create your views here.
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you/"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid()

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you/"


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(
#             request,
#             "reviews/review.html",
#             {
#                 "form": form,
#             },
#         )

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect("/thank-you/")
#         return render(request, "reviews/review.html", {
#             'form':form
#         })


# def review(request):
#     # if request.method == 'POST':
#     #     entered_username = request.POST['username']

#     #     if entered_username == "":
#     #         return render(request, 'reviews/review.html',{
#     #             'has_error': True,
#     #         })
#     #     print(entered_username)
#     #     return redirect("/thank-you/")
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/thank-you/")
#     else:
#         form = ReviewForm()
#     return render(
#         request,
#         "reviews/review.html",
#         {
#             "form": form,
#         },
#     )


class ThankYouView(TemplateView):
    # def get(self,request):
    #     return render(request, 'reviews/thank_you.html')
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Thank you for your feedback"
        return context


# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gte = 4)
    #     return data


# class ReviewDetailsView(TemplateView):
#     template_name = "reviews/review_details.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(id = review_id)
#         context["review"] = selected_review
#         return context


class ReviewDetailsView(DetailView):
    template_name = "reviews/review_details.html"
    model = Review


# def thank_you(request):
#     return render(request, "reviews/thank_you.html")
