from pyexpat import model
from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField('Username', max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField('Email', max_length=254, null=False, blank=False)
    password = models.CharField('Password', max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Category(models.Model):
    name_categorie = models.CharField('Name Categorie', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name_categorie


class Listing(models.Model):
    title_listing = models.CharField('Title Listing', max_length=100, null=False, blank=False)
    description = models.CharField('Description', max_length=500, null=False, blank=False)
    listing_image = models.ImageField('Image Listing', upload_to='auctions/', null=True, blank=True)
    initial_bid = models.FloatField('Initial Bid', default=0.00, null=False, blank=False)
    creation_date = models.DateTimeField('Creation Date', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    closed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'

    def __str__(self):
        return self.title_listing

class Bid(models.Model):
    amount_to_bid = models.FloatField('Amount to bid', default=0.00, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Bid'
        verbose_name_plural = 'Bids'


class Comment(models.Model):
    comment = models.TextField('Comment', max_length=500, null=False, blank=False)
    creation_date = models.DateTimeField("Creation Date", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'