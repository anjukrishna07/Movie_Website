from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *

# Create your views here.

def home(request):
    return render(request,"admin_home.html")

def addmovie(request):
    genres = Genre.objects.all()
    context = {
        'genres':genres
    }
    if request.method == "POST":
        sample_genre_id = request.POST['genre']
        sample_name=request.POST['name']
        sample_date=request.POST['date']
        sample_image=request.FILES['image']
        sample_video=request.FILES['video']

        
        Movies.objects.create(
            genre_id = Genre.objects.get(id=sample_genre_id),
            name=sample_name,
            date=sample_date,
            image=sample_image,
            video=sample_video
        )




    return render(request,"add_movie.html", context)

def viewmovie(request):
    details=Movies.objects.all()
    context={'details':details}

    return render(request,"view_movie.html",context)



def edit_detail(request,movieid):
    details=Movies.objects.filter(id=movieid)
    context={'details':details}
    return render(request,"Edit_movie.html",context)



def Edit(request,movieid):
    if request.method == 'POST':
        sample_name=request.POST['name']
        sample_date=request.POST['date']
        sample_image=request.FILES['image']
        sample_video=request.FILES['video']

        Movies.objects.filter(id=movieid).update(
            name=sample_name,
            date=sample_date,
            image=sample_image,
            video=sample_video
        )
        return redirect("viewmovie")
    return render (request,"Edit_movie.html")



def view(request,movieid):
    details = Movies.objects.filter(id=movieid)
    context={'details':details}
    return render(request,'view_more.html', context)

def delete_details(request, id):
    Movies.objects.filter(id=id).delete()
    return redirect('viewmovie')




def addgenre(request):
    if request.method == "POST":
        sample_name=request.POST['name']
        sample_image=request.FILES['image']
      

        Genre.objects.create(
            name=sample_name,
            image=sample_image,
            
        )




    return render(request,"add_genre.html")



def viewgenre(request):
    details=Genre.objects.all()
    context={'details':details}

    return render(request,"view_genre.html",context)






def editgenrebutton(request):
    details=Genre.objects.all()
    context={'details':details}

    return render(request,"editgenre_button.html",context)




def editgenre(request,movid):
    details=Genre.objects.filter(id=movid)
    context={'details':details}
    return render(request,"Edit_genre.html",context)



def Editgen(request,movid):
    if request.method == 'POST':
        sample_name=request.POST['name']
        sample_image=request.FILES['image']
       

        Genre.objects.filter(id=movid).update(
            name=sample_name,
            image=sample_image,
           
        )
        return redirect("editgenrebutton")
    return render (request,"Edit_genre.html")



def delete_genre(request, id):
    Genre.objects.filter(id=id).delete()
    return redirect('viewgenre')





def viewuser(request):
    details=User.objects.all()
    context={'details':details}
    return render(request,'viewuser.html',context)




def viewcomplaint(request):
    details=Complaint.objects.all()
    context={'details':details}
    return render(request,'viewcomplaint.html',context)



def viewcontacts(request):
    details=contactus.objects.all()
    context={'details':details}
    return render(request,'view_contacts.html',context)















def Editprofiles(request,mid):
    details=User.objects.filter(id=mid)
    context={'details':details}
    return render(request,"view_account.html",context)



def Editprof(request,mid):
    if request.method == 'POST':
        sample_name=request.POST['name']
        sample_image=request.FILES['image']
       

        User.objects.filter(id=mid).update(
            name=sample_name,
            image=sample_image,
           
        )
        return redirect("userhome")
    return render (request,"view_account.html")




def viewcomments(request, movieid):
    movies = Movies.objects.filter(id=movieid)  # Returns a queryset

    if movies.exists():  # Ensure movie exists
        movie = movies.first()  # Get the first movie (should be only one)
        comments = Comment.objects.filter(movie=movie)  # Get related comments
    else:
        movie = None
        comments = []  # Empty list if no movie exists

    context = {
        'movie': movie,
        'comments': comments,  # Pass comments to the template
    }
    return render(request, 'viewcomments.html', context)

def deletecomment(request, id, movieid):
    Comment.objects.filter(id=id).delete()
    return redirect('viewcomments', movieid=movieid)






def admin_view_comments(request):
    comments = Comment.objects.all()  # Fetch all comments
    return render(request, 'admin_comments.html', {'comments': comments})

def delete_comment(request, commentid):
    comment = Comment.objects.filter(id=commentid).first()
    if comment:
        comment.delete()
    return redirect('admin_view_comments')



def viewreactions(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    
    # Fix filtering: use 'reaction' instead of 'type'
    likes_count = MovieReaction.objects.filter(movie=movie, reaction='like').count()
    dislikes_count = MovieReaction.objects.filter(movie=movie, reaction='dislike').count()
    
    reactions = MovieReaction.objects.filter(movie=movie)

    return render(request, 'viewreactions.html', {
        'movie': movie,
        'reactions': reactions,
        'likes_count': likes_count,
        'dislikes_count': dislikes_count
    })


def delete_reactions(request, reactionsid):
    MovieReaction.objects.filter(id=reactionsid).delete()
    return redirect('viewreactions')









def addpremium(request):
 
    if request.method == "POST":
        
        sample_name=request.POST['plan_name']
        sample_date=request.POST['duration_days']
        sample_price=request.POST['price']
      

        
        Premium.objects.create(
          
            plan_name=sample_name,
            duration_days=sample_date,
            price=sample_price,
            
        )




    return render(request,"add_premium.html")
