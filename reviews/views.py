from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

# Create your views here.


def review(request):
    # if request.method == 'POST':
    #     entered_username = request.POST['username']

    #     if entered_username == "":
    #         return render(request, 'reviews/review.html',{
    #             'has_error': True,
    #         })
    #     print(entered_username)
    #     return redirect("/thank-you/")
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/thank-you/")
    else:
        form = ReviewForm()
    return render(
        request,
        "reviews/review.html",
        {
            "form": form,
        },
    )


def thank_you(request):
    return render(request, "reviews/thank_you.html")
