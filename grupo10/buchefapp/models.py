from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


# Clases para las entidades
# Si no hay llave primaria, entonces se crea un id por defecto que cumple esa función
class User(AbstractUser):
  pronombres = [('La','La'),('El','El'), ('Le','Le'),('Otro','Otro')]
  pronombre = models.CharField(max_length=5,choices=pronombres)
  apodo = models.CharField(max_length=30)
  username = models.CharField(max_length=30, unique=True)


class Local(models.Model):
  nombre = models.CharField(max_length=100)
  direccion = models.CharField(max_length=100)
  avg_score = models.DecimalField(default= 0, max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
  suma = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
  total_reviews = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
  reviews_1 = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
  reviews_2 = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
  reviews_3 = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
  reviews_4 = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
  reviews_5 = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
  local_image = models.ImageField(upload_to="img/%y")
  

  def __str__(self):
    return self.nombre
  

class Review(models.Model):
  message = models.CharField(max_length=100)
  score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
  date = models.DateField()
  image = models.ImageField(upload_to="img/%y")
  user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
  local_id  = models.ForeignKey(Local, on_delete=models.CASCADE)

  def __str__(self):
    return self.message
  
class Category(models.Model):
  nombre = models.CharField(max_length=20)
  def __str__(self):
    return self.nombre

# Relaciones
class Review_Category(models.Model):
  review_id  = models.ForeignKey(Review, on_delete=models.CASCADE)
  category_id  = models.ForeignKey(Category, on_delete=models.CASCADE)
  def __str__(self):
    return (self.category_id, self.review_id)

class User_Review(models.Model):
  user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
  review_id  = models.ForeignKey(Review, on_delete=models.CASCADE)
  def __str__(self):
    return (self.user_id, self.review_id)

class Local_Category(models.Model):
  category_id  = models.ForeignKey(Category, on_delete=models.CASCADE)
  local_id  = models.ForeignKey(Local, on_delete=models.CASCADE)
  category_count = models.IntegerField(default= 1, validators=[MinValueValidator(0)])
  def __str__(self):
    return (self.category_id, self.local_id)


class Local_Review(models.Model):
  local_id  = models.ForeignKey(Local, on_delete=models.CASCADE)
  review_id  = models.ForeignKey(Review, on_delete=models.CASCADE)
  def __str__(self):
    return (self.local_id, self.review_id)
