from django.shortcuts import render,redirect
from User.models import *
from Admin.models import *
import datetime
# Create your views here.

def userhome(request):
    name = request.session['user_name']
    context = {'name':name}
    return render(request,"userhome.html", context)





def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email, password=password).exists():
            data = User.objects.filter(email=email, password=password).values('id', 'name', 'email', 'phone').first()

            request.session['user_id'] = data['id']
            request.session['user_name'] = data['name']
            request.session['user_email'] = data['email']
            request.session['user_phone'] = data['phone']

            # Subscription check
      
            if UserSubscription.objects.filter(user_id=data['id'], is_active=True).exists():
                
                subscription_details = UserSubscription.objects.get(user_id=data['id'], is_active=True)
                
                if not subscription_details.end_date > datetime.datetime.now().date():
                    
                    UserSubscription.objects.filter(user_id=data['id'], is_active=True).update(is_active=False)
                    return redirect('subscription')
                else:
                    
                    return redirect('usermovie')
            return redirect('subscription')
                
            # return redirect('usermovie')

    return render(request, "loginpage.html")



def account(request):
    if request.method =='POST':
        cname=request.POST['cname']
        cemail=request.POST['cemail']
        cphone=request.POST['cphone']
        categories=request.POST['categories']
       
       
        contactus.objects.create(
            cname=cname,
            cemail=cemail,
            cphone=cphone,
            categories=categories,
        ),
    name = request.session['user_name']
    context = {'name':name}
        
    return render(request,"account.html",context)
  

def usermovie(request):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']

    # Subscription check
    user_subscription = UserSubscription.objects.filter(user_id=user_id, is_active=True).order_by('-end_date').first()

    if not user_subscription or user_subscription.end_date < timezone.now().date():
        return redirect('subscription')  # Redirect if no active or expired subscription

    # Fetch all movies if subscription is valid
    details = Movies.objects.all()
    name = request.session['user_name']
    context = {'details': details, 'name': name}
    return render(request, "usermovie.html", context)


def about(request):
    if request.method =='POST':
        cname=request.POST['cname']
        cemail=request.POST['cemail']
        cphone=request.POST['cphone']
        categories=request.POST['categories']
       
       
        contactus.objects.create(
            cname=cname,
            cemail=cemail,
            cphone=cphone,
            categories=categories,
        )
    return render(request,"about.html")

def contact(request):
    if request.method =='POST':
        names=request.POST['names']
        phones=request.POST['phones']
        emails=request.POST['emails']
        messages=request.POST['messages']
       
       
        Complaint.objects.create(
            names=names,
            phones=phones,
            emails=emails,
            messages=messages
        )

    return render(request,"contact.html")



def teams(request):
    if request.method =='POST':
        cname=request.POST['cname']
        cemail=request.POST['cemail']
        cphone=request.POST['cphone']
        categories=request.POST['categories']
       
       
        contactus.objects.create(
            cname=cname,
            cemail=cemail,
            cphone=cphone,
            categories=categories,
        )
    return render(request,"teams.html")



def blog(request):
    return render(request,"blog.html")


def genreoption(request):
    genre =Genre.objects.all()
    context={
        'genres':genre
    }
    return render(request,"genreoption.html",context)



def view_genre_based_movie(request,genre_id):
    filtered_movie = Movies.objects.filter(genre_id=genre_id)
    name = request.session['user_name']
    context = {
        'filtered_movie' : filtered_movie,
        'name':name

    }


    
   
    return render(request, "view_genre_based_movie.html",context)



def viewaccount(request):
    
    id = request.session['user_id']
    data =User.objects.filter(id=id).values().first()
    context= {'data':data}
 


  
    return render(request,"view_account.html",context)







def logout(request):
    del request.session['user_id']
    return redirect('userhome')



def Editmyprofile(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']

        User.objects.update(
            name=name,
            email=email,
            phone=phone,
        )
    return render(request,"view_account.html")




def subscription(request):
    return render(request,"subscription.html")




def payment(request):
    return render(request,"payment.html")



def gpay(request):
    return render(request,"gpay.html")




def upi(request):
    return render(request,"upi.html")







    
    



def comment(request, movie_id):
    movie = Movies.objects.filter(id=movie_id).first()  # Fetch movie or return None
    if not movie:
        return redirect('userhome')  # Redirect if movie doesn't exist

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        user_id = request.session.get('user_id')  # Fetch user_id from session
        user_name = request.session.get('user_name')  # Fetch user_name safely

        if comment_text and user_id:
            # Fetch the User instance correctly using the ID
            user = User.objects.filter(id=user_id).first()

            if user:  # Ensure user exists in the database
                Comment.objects.create(
                    movie=movie,  # Associate the comment with the correct movie
                    user=user,  # Assign the correct User instance
                    comments=comment_text
                )

        # Ensure correct redirection based on URL pattern
        return redirect('moviedetail', id=movie.id)

    # Show latest comments first
    comments = Comment.objects.filter(movie=movie).order_by('-created_at')
    
    return render(request, "movie_comment.html", {'movie': movie, 'comments': comments})



def like_movie(request, movie_id):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']
    movie_list = Movies.objects.filter(id=movie_id)

    if not movie_list.exists():
        return redirect('moviedetail', id=movie_id)

    movie = movie_list.first()

    reactions = MovieReaction.objects.filter(user_id=user_id, movie=movie)

    if reactions.exists():
        reaction = reactions.first()
        if reaction.reaction == "like":
            reaction.delete()
            movie.likes -= 1
        else:
            reaction.reaction = "like"
            reaction.save()
            movie.likes += 1
            movie.dislikes -= 1
    else:
        MovieReaction.objects.create(user_id=user_id, movie=movie, reaction="like")
        movie.likes += 1

    movie.save()
    return redirect('moviedetail', id=movie.id)


def dislike_movie(request, movie_id):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']
    movie_list = Movies.objects.filter(id=movie_id)

    if not movie_list.exists():
        return redirect('moviedetail', id=movie_id)

    movie = movie_list.first()

    reactions = MovieReaction.objects.filter(user_id=user_id, movie=movie)

    if reactions.exists():
        reaction = reactions.first()
        if reaction.reaction == "dislike":
            reaction.delete()
            movie.dislikes -= 1
        else:
            reaction.reaction = "dislike"
            reaction.save()
            movie.dislikes += 1
            movie.likes -= 1
    else:
        MovieReaction.objects.create(user_id=user_id, movie=movie, reaction="dislike")
        movie.dislikes += 1

    movie.save()
    return redirect('moviedetail', id=movie.id)




def movie_detail(request, id):
    if 'user_id' not in request.session:
        return redirect('login')

    # Fetch the movie details
    moviedtl = Movies.objects.filter(id=id).first()
    if not moviedtl:
        return redirect('usermovie')

    context = {'moviedtl': moviedtl}
    return render(request, "movie_detail.html", context)





def toggle_watch_later(request, movie_id):
    if 'user_id' not in request.session:
        return redirect('login')

    user = User.objects.filter(id=request.session['user_id']).first()
    movie = Movies.objects.filter(id=movie_id).first()

    if user and movie:
        watch_later_entry = WatchLater.objects.filter(user=user, movie=movie)
        if watch_later_entry.exists():
            watch_later_entry.delete()  # Remove movie if it exists
        else:
            WatchLater.objects.create(user=user, movie=movie)  # Add movie if not exists

    return redirect('moviedetail', id=movie.id)  # ✅ Redirects back to movie detail page





def watch_later_list(request):
    if 'user_id' not in request.session:
        return redirect('login')

    user = User.objects.filter(id=request.session['user_id']).first()
    watch_later_movies = Movies.objects.filter(watchlater__user=user) if user else []

    return render(request, 'watch_later.html', {'watch_later_movies': watch_later_movies})



def movies(request):
  

    details=Movies.objects.all()
    name = request.session['user_name']
    context = {'details':details,'name':name}
    return render(request,"movies.html",context)


from django.utils import timezone
from datetime import timedelta




def subscribe(request):
    if request.method == "POST":
        plan_id = request.POST.get("plan_id")

        # ✅ Debugging: Check if plan_id is received
        if not plan_id:
            return render(request, "payment.html", {"error": "No plan selected"})

        # ✅ Get user from session
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("login")  # Redirect to login if user not authenticated

        # ✅ Fetch user object
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return redirect("login")  # Redirect if user does not exist

        # ✅ Get Subscription plan
        try:
            plan = Premium.objects.get(id=plan_id)
        except Premium.DoesNotExist:
            return render(request, "payment.html", {"error": "Invalid plan selected"})

        # ✅ Calculate subscription period
        start_date = timezone.now().date()
        end_date = start_date + timedelta(days=plan.duration_days)

        # ✅ Save the subscription
        user_subscription, created = UserSubscription.objects.update_or_create(
            user=user,
            defaults={
                "subscription": plan,
                "start_date": start_date,
                "end_date": end_date,
                "is_active": True,
                "is_paid": True,  # Assuming payment is successful
            }
        )

        print(f"Subscription {'created' if created else 'updated'} successfully!")

        return redirect("subscription")  # Redirect to subscription page

    # ✅ Fetch available plans for selection
    plans = Premium.objects.all()
    return render(request, "payment.html", {"plans": plans})







def payment_page(request):
    plans = Premium.objects.all()
    print(plans)
    return render(request, "payment.html", {"plans": plans})





from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User

def send_welcome_email(user):
    """Send a welcome email after user registration."""
    template = render_to_string('email_template.html', {'name': user.first_name})
    
    email = EmailMessage(
        subject="Welcome to Play Show!",
        body=template,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    email.content_subtype = "html"  # Ensure HTML formatting
    email.fail_silently = False
    email.send()

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if not User.objects.filter(email=email).exists():
                # Create new user
                user = User.objects.create(
                    first_name=name,  # Store 'name' in 'first_name' field
                    email=email,
                    username=email  # Use email as username
                )
                user.set_password(password)  # Hash password
                user.save()

                # Send welcome email
                send_welcome_email(user)
                
                return redirect('login')
            else:
                return redirect('register')
        else:
            return redirect('register')

    return render(request, 'Registerpage.html')  # Ensure the form renders for GET requests
