from django.urls import path

from . import views

app_name = 'auctions'
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create-listing', views.ListingCreateView.as_view(), name='create_listing'),
    path('active-listings', views.ListingListView.as_view(), name='active_listings'),
    path('detail-listing/<int:pk>', views.ListingDetailView.as_view(), name='detail_listing'),
    path('create-comment', views.CommentCreateView.as_view(), name='create_comment'),
    path('add-to-watchlist', views.WatchListCreateView.as_view(), name='add_to_watchlist'),

]
