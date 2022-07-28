from pyexpat import model
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import User, Listing, Comment, WatchList
from .forms import BidForm, ListingForm, CommentForm


def index(request):
    return render(request, "auctions/index.html")

# loginrequiredmixin
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")


class ListingCreateView(CreateView):
    model = Listing
    form_class = ListingForm
    success_url = reverse_lazy('auctions:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListingListView(ListView):
    template_name = 'auctions/listing_list.html'
    content_object_name = 'listings'
    paginate_by = 4

    def get_queryset(self):
        listings = Listing.objects.filter(closed=False)
        return listings


class ListingDetailView(DetailView, CreateView):
    template_name = 'auctions/listing_detail.html'
    model = Listing
    # form_class = BidForm

    # def get_queryset(self, pk):
    #     return Comment.objects.filter(id=pk)

    def get_context_data(self, pk):
        context = {}
        context['details'] = Listing.objects.get(id=pk)
        context['comments'] = Comment.objects.filter(listing_id=pk)
        context['form'] = BidForm
        return context


    def get(self, request, pk, *args, **kwargs):
        print(self.get_context_data(pk))
        return render(request, self.template_name, self.get_context_data(pk))



class CommentCreateView(CreateView):
    template_name = 'auctions/listing_detail.html'
    model = Comment
    form_class = BidForm
    success_url = reverse_lazy(f'auctions:index')

    def post(self, request, *args, **kwargs):
        print(request.POST.get('comment'))
        print(request.POST.get('listing'))
        
        comment_create = Comment.objects.create(
            comment = request.POST.get('comment'),
            user = self.request.user,
            listing = Listing.objects.get(id=request.POST.get('listing')),
            *args, 
            **kwargs
        )
        comment_create.save()
        return redirect('auctions:detail_listing', pk=request.POST.get('listing'))


class WatchListCreateView(CreateView):
    model = WatchList
    success_url = reverse_lazy(f'auctions:index')

    def post(self, request, *args, **kwargs):
        watchlist_create = WatchList.objects.create(
            user = self.request.user,
            listing = Listing.objects.get(id=request.POST.get('listing')),
            *args,
            **kwargs
        )
        watchlist_create.save()
        return redirect('auctions:detail_listing', pk=request.POST.get('listing'))
    

class WatchlistListView(ListView):
    template_name = 'auctions/listing_watchlist.html'
    content_object_name = 'listings'
    paginate_by = 4

    def get_queryset(self):
        listings = Listing.objects.filter(watchlist__user=self.request.user)
        return listings

    

