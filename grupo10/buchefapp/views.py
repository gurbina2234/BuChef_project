from PIL import Image
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from buchefapp.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from buchefapp.forms import AgregarForm, ReviewForm
from django.contrib import messages
from buchefapp.utils.validations import validate_review

"""Handles the resgiter of an user after pressing the button, 
or being redirected.
"""

def register_user(request):
    if request.method == 'GET': #Si estamos cargando la página
     return render(request, "buchefapp/register_user.html") #Mostrar el template

    elif request.method == 'POST': #Si estamos recibiendo el form de registro
     #Tomar los elementos del formulario que vienen en request.POST
     nombre = request.POST['nombre']
     contraseña = request.POST['contraseña']
     apodo = request.POST['apodo']
     pronombre = request.POST['pronombre']
     mail = request.POST['mail']

    if not nombre or not contraseña or not apodo or not pronombre or not mail:
            messages.error(request, 'Por favor completa todos los campos.')
            return render(request, "buchefapp/register_user.html")
        
        # Validar longitud de la contraseña
    if len(contraseña) < 8:
        messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
        return render(request, "buchefapp/register_user.html")
    
    if User.objects.filter(username=nombre).exists():
        messages.error(request, 'El nombre de usuario ya está en uso. Por favor elige otro.')
        return render(request, "buchefapp/register_user.html")
    # Crear el nuevo usuario
    try:
        user = User.objects.create_user(username=nombre, password=contraseña, email=mail, apodo=apodo, pronombre=pronombre)
        messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
        return render(request, "buchefapp/register_user.html")
    except Exception as e:
        messages.error(request, "Error en el registro!")
        return render(request, "buchefapp/register_user.html")

"""Handles the login of an user after pressing the button, 
If the user exists logs in, if not takes them to the register page
"""

def login_user(request):
    if request.method == 'GET':
        return render(request,"buchefapp/login.html")
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            #returns home
            return HttpResponseRedirect('home')
        else:
            # Verificar si el usuario existe
            if User.objects.filter(username=username).exists():
                messages.error(request, "Contraseña incorrecta.")
            else:
                messages.error(request, "El usuario no existe, crea una cuenta!")
            return render(request, "buchefapp/login.html")
        
""" Handles the logout of an user, upon pressing the button redirects to home page"""
def logout_user(request):
    logout(request)
    #place holder, similar logic for empty path to home page later on
    return HttpResponseRedirect('home')

""" Function for rendering the home page with the restaurant cards"""

def home(request,categoria=None):
    if request.method == 'GET':
        locales = Local.objects.all().order_by('-avg_score')
        if categoria:
            locales_ids = locales.values_list('id', flat=True)
            ids_to_render = []
            for id in locales_ids: 
                local_category = Local_Category.objects.filter(local_id=id).order_by('-category_count')[:3].values_list('category_id', flat=True)
                for cat in local_category:
                    if (categoria == cat):
                        ids_to_render.append(Local.objects.get(id = id))
                        break
        else:
            ids_to_render = locales

        categorias = Category.objects.all()            
          
        return render(request,"buchefapp/home.html",{'locales':ids_to_render, 'categorias': categorias})
        
    
@login_required
def review(request, local_id): 
    #se renderiza el template del form
    if request.method == 'GET':
        #se inicializa el form y las categorias 
        form = ReviewForm()
        categories = Category.objects.all()
        return render(request, 'buchefapp/review.html', {'local_id': local_id, 'form': form, 'categories': categories})
    #se mandan los datos del form a la base 
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        categories = Category.objects.all()
        if form.is_valid():
        # lista: se obtienen las categorias y los elementos del form
            score = form.cleaned_data['score']
            message = form.cleaned_data['message']
            date = form.cleaned_data['date']
            image = form.cleaned_data['image']
            categorias = request.POST.getlist('category')
            user = request.user
            local = Local.objects.get(pk=local_id)

            if not validate_review(request, score, message, date, categorias):
                print("Error en la validación")
                return render(request, 'buchefapp/review.html', {'local_id': local_id, 'form': form, 'categories': categories})
            
            if (score == 1):
                local.reviews_1 += 1
            if (score == 2):
                local.reviews_2 += 1
            if (score == 3):
                local.reviews_3 += 1
            if (score == 4):
                local.reviews_4 += 1
            if (score == 5):
                local.reviews_5 += 1
                
                
            review_instance = Review.objects.create(message = message, score = score, date = date,
                                                    image = image, user_id = user, local_id = local)
            
            # se crea una instancia de cada categoria seleccionada
            for cat_id in categorias:
                category_instance = Category.objects.get(id = cat_id)
                # se almacena la relacion entre la review y la categoria
                Review_Category.objects.create(review_id = review_instance, category_id = category_instance)

                if Local_Category.objects.filter(local_id = local, category_id = category_instance).exists():
                    local_category = Local_Category.objects.get(local_id = local, category_id = category_instance)
                    local_category.category_count += 1
                    local_category.save()
                else:
                    #se carga en la tabla local_category, deberia cambiar nombre en la base de datos a local_user
                    Local_Category.objects.create(local_id = local, category_id = category_instance)
                

            
            #se carga en la tabla local_review
            Local_Review.objects.create(local_id = local, review_id = review_instance)
            #se carga en la tabla user_review
            User_Review.objects.create(user_id = user, review_id = review_instance)

            local.suma += score
            local.total_reviews += 1
            local.avg_score = local.suma / local.total_reviews
            local.save()

            #se redirecciona a restaurant en caso de cargar los archivos a la base de datos correctamente
            return HttpResponseRedirect(reverse('buchefapp:restaurant', kwargs={'local_id': local_id}))
        else:
            print(form.errors)
            return render(request, 'buchefapp/review.html', {'local_id': local_id, 'form': form, 'categories': categories, 'errors': form.errors})
    #renderiza si algo falla    
    categories = Category.objects.all()
    #se renderiza la template de review nuevamente en caso de error
    return render(request, 'buchefapp/review.html', {'local_id': local_id, 'form': form, 'categories': categories})

"""Handles the page of a local/restaurant and its render"""
def restaurant(request, local_id):
    if request.method == 'GET':
        local = get_object_or_404(Local, id=local_id) #id, nombre, direction, avg_score, suma, total_reviews
        if (local.total_reviews != 0):
            porcentaje_1 = (local.reviews_1/local.total_reviews) * 100
            porcentaje_2 = (local.reviews_2/local.total_reviews) * 100
            porcentaje_3 = (local.reviews_3/local.total_reviews) * 100
            porcentaje_4 = (local.reviews_4/local.total_reviews) * 100
            porcentaje_5 = (local.reviews_5/local.total_reviews) * 100
        else:
            porcentaje_1 = 0
            porcentaje_2 = 0
            porcentaje_3 = 0
            porcentaje_4 = 0
            porcentaje_5 = 0

        porcentajes = {
            'Porcentaje_1': porcentaje_1,
            'Porcentaje_2': porcentaje_2,
            'Porcentaje_3': porcentaje_3,
            'Porcentaje_4': porcentaje_4,
            'Porcentaje_5': porcentaje_5
        }
        reviews = Review.objects.filter(local_id = local_id)
        categories = []
        local_category = Local_Category.objects.filter(local_id=local_id).order_by('-category_count')[:3].values_list('category_id', flat=True)
        for cat in local_category:
            categories.append(Category.objects.get(id = cat).nombre)
            
        #
        #
        reviews = Review.objects.filter(local_id_id = local_id).select_related('user_id')
        return render(request,"buchefapp/restaurant.html", {'local':local, 'porcentajes': porcentajes, 'reviews':reviews, 'categorias_local': categories})

@login_required        
def agregar_local(request):
    if request.method == "POST":
        form = AgregarForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            direccion = form.cleaned_data['direccion']
            local_image = form.cleaned_data['local_image']
            
            # Guardar el objeto Local con la imagen si se proporcionó
            if local_image:
                local_instance = form.save(commit=False)
                local_instance.local_image = local_image
            else:
                # Establecer una imagen por defecto
                default_image_path = 'img/24/no-photo.jpg'  # Ruta a tu imagen por defecto
                local_instance = form.save(commit=False)
                local_instance.local_image = default_image_path
            
            local_instance.save()
            return HttpResponseRedirect(reverse('buchefapp:home'))
    else:
        form = AgregarForm()
    
    return render(request, 'buchefapp/agregar.html', {'form': form})
