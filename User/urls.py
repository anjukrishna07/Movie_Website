from django.urls import path
from User import views


urlpatterns = [
    path('',views.userhome,name='userhome'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('account',views.account,name='account'),
    path('usermovie',views.usermovie,name='usermovie'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('teams',views.teams,name='teams'),
    path('blog',views.blog,name='blog'),
    path('genreoption',views.genreoption,name='genreoption'),
    path('view_genre_based_movie/<int:genre_id>',views.view_genre_based_movie,name='view_genre_based_movie'),
    path('viewaccount',views.viewaccount,name='viewaccount'),
    path('Editmyprofile',views.Editmyprofile,name='Editmyprofile'),
    path('subscription',views.subscription,name='subscription'),
    path('payment',views.payment,name='payment'),
    path('gpay',views.gpay,name='gpay'),
    path('upi',views.upi,name='upi'),
   
    path('comment/<int:movie_id>/', views.comment, name='comment'),
    path('moviedetail/<int:id>/', views.movie_detail, name='moviedetail'),
    path('like/<int:movie_id>/', views.like_movie, name='like_movie'),
    path('dislike/<int:movie_id>/', views.dislike_movie, name='dislike_movie'),
    path('watch-later/', views.watch_later_list, name='watch_later_list'),
    path('toggle-watch-later/<int:movie_id>/', views.toggle_watch_later, name='toggle_watch_later'),
    path('movies',views.movies,name='movies'),
   
    path("subscribe/",views.subscribe, name="subscribe"), 
    path("payment/",views.payment_page, name="payment"),  
  
    

]



