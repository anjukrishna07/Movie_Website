from django.urls import path
from Admin import views


urlpatterns = [
    path('home',views.home,name='home'),
    path('addmovie',views.addmovie,name='addmovie'),
    path('viewmovie',views.viewmovie,name='viewmovie'),
    path('edit_detail/<int:movieid>',views.edit_detail,name='edit_detail'),
    path('Edit/<int:movieid>',views.Edit,name='Edit'),
    path('view/<int:movieid>',views.view,name='view'),
    path('delete_details/<int:id>',views.delete_details,name='delete_details'),
    path('addgenre',views.addgenre,name='addgenre'),
    path('viewgenre',views.viewgenre,name='viewgenre'),
    path('editgenre/<int:movid>',views.editgenre,name='editgenre'),
    path('Editgen/<int:movid>',views.Editgen,name='Editgen'),
    path('editgenrebutton',views.editgenrebutton,name='editgenrebutton'),
    path('delete_genre/<int:id>',views.delete_genre,name='delete_genre'),
    path('viewuser',views.viewuser,name='viewuser'), 
    path('viewcomplaint',views.viewcomplaint,name='viewcomplaint'), 
    path('viewcontacts',views.viewcontacts,name='viewcontacts'),
   
    path('viewcomments/<int:movieid>',views.viewcomments, name='viewcomments'),
    path('deletecomment/<int:id>/<int:movieid>',views.deletecomment, name='deletecomment'),

    path('viewcomments',views.admin_view_comments, name='admin_view_comments'),
    path('delete_comment/<int:commentid>',views.delete_comment, name='delete_comment'),
   

    path('viewreactions/<int:movie_id>/', views.viewreactions, name='viewreactions'),
    path('delete_reactions/<int:reactionsid>', views.delete_reactions, name='delete_reactions'),
    path('addpremium',views.addpremium,name='addpremium'),






]