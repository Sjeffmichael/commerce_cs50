from dataclasses import field
from django import forms

from .models import Bid, Listing, Comment

class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = ['title_listing', 'description', 'listing_image', 'initial_bid', 'category']


class BidForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ['amount_to_bid']

        labels = {
            'amount_to_bid': 'Place your bid here:'
        }

        widgets = {
            'amount_to_bid': forms.NumberInput(
                attrs={
                    'class': 'form-control  shadow-none numberinput'
                }
            )
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
