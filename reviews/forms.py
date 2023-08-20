from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100, error_messages={
#         'required': "username mustnot be empty",
#         'max_length': "username must be shorter"
#     })
#     review_text = forms.CharField(label="Your feedback", widget = forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating", min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ('user_name', 'review_text', 'rating')
        labels = {
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name" : {
                "required" : "Your name must not be empty",
                "max_length": "Please Enter your name shorter",
            }
        }