from django.db import models

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=35)
    image=models.ImageField(upload_to="Movie")


class Movies(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=35)
    date=models.DateField()
    image=models.ImageField(upload_to="Movie")
    video=models.FileField(upload_to="Movievideo",null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    
class Premium(models.Model):
    plan_name=models.CharField(max_length=35)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()



