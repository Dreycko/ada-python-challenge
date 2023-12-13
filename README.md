<img align="right" src="https://github.com/ada-school/module-template/blob/main/ada.png">


## Python Data Mentor 👩‍💻 👨‍💻 Code Challenge

Thank you 🙏 for taking the time to implement this coding challenge to build a fast microservice REST API using *Python* and any other technologies of your preference.

## Conditions

* Take 2-4 hours to implement your project.
* Use coding best practices.
* Create a fork of this repo and share your solution when finished.


## Coding Challenge  💻 

A bus company wants to start using technology and allow their users to book online tickets. Please help them build a [REST API Level 2](https://martinfowler.com/articles/richardsonMaturityModel.html#level2)(pereferible) that lets them control their trip bookings, supporting the following operations:
* Create a new booking with the following information: name, email, origin, destination, departure date and time and duration.
* Update an existing booking
* Find a booking using its ID.
* Delete an existing booking.

# Expected Quality Attributes:
* Using coding best practices.
* SOLID principles.
* Correct connection with a persistance layer.

# Desired technology stack:
* Python 
* [Flask](https://flask.palletsprojects.com/en/2.2.x/) / [Fast API](https://fastapi.tiangolo.com/) / [Django](https://www.djangoproject.com/) / Any other
* MongoDB / Postgress / SQLite  / Any other

## Submit your solution

Once you're done, please send us an email to [tech@ada-school.org](mailto:tech@ada-school.org) with the subject: TECH_CHALLENGE_[YOUR NAME] and do not forget to include the link to your repository with the solution. After you submit your code, we will review it and contact you to discuss next steps. 

Good luck! 💪


## Solucion 


### Pasos Completos para el Proyecto de Booking:

1. **Crea un directorio para tu proyecto y navega a él:**

   ```bash
   mkdir proyecto_booking
   cd proyecto_booking
   ```

2. **Crea un entorno virtual con `venv`:**

   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual:**

   - En sistemas basados en Unix (Linux/Mac):

     ```bash
     source venv/bin/activate
     ```

   - En Windows (PowerShell):

     ```bash
     .\venv\Scripts\Activate
     ```

     En Windows (Command Prompt):

     ```bash
     .\venv\Scripts\activate.bat
     ```

4. **Instala Django y Django REST Framework:**

   ```bash
   pip install django djangorestframework
   ```

5. **Crea un proyecto Django:**

   ```bash
   django-admin startproject bus_booking
   ```

6. **Navega al directorio del proyecto:**

   ```bash
   cd bus_booking
   ```

7. **Crea una aplicación Django:**

   ```bash
   python manage.py startapp bookings
   ```

8. **Actualiza la configuración del proyecto (`bus_booking/settings.py`):**

   Agrega `'bookings'` y `'rest_framework'` a la lista de `INSTALLED_APPS`:

   ```python
   # bus_booking/settings.py

   INSTALLED_APPS = [
       # ...
       'bookings',
       'rest_framework',
       # ...
   ]
   ```

9. **Define el modelo en `bookings/models.py`:**

   ```python
   # bookings/models.py

   from django.db import models

   class Booking(models.Model):
       name = models.CharField(max_length=255)
       email = models.EmailField()
       origin = models.CharField(max_length=255)
       destination = models.CharField(max_length=255)
       departure_datetime = models.DateTimeField()
       duration = models.PositiveIntegerField()

       def __str__(self):
           return f'{self.name} - {self.origin} a {self.destination}'
   ```

10. **Crea y aplica las migraciones:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

11. **Define el serializador en `bookings/serializers.py`:**

    ```python
    # bookings/serializers.py

    from rest_framework import serializers
    from .models import Booking

    class BookingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Booking
            fields = '__all__'
    ```

12. **Define las vistas en `bookings/views.py`:**

    ```python
    # bookings/views.py

    from rest_framework import generics
    from .models import Booking
    from .serializers import BookingSerializer

    class BookingListCreateView(generics.ListCreateAPIView):
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer

    class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer
    ```

13. **Configura las URL en `bus_booking/urls.py`:**

    ```python
    # bus_booking/urls.py

    from django.contrib import admin
    from django.urls import path, include
    from bookings.views import BookingListCreateView, BookingDetailView

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
        path('api/bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
        path('', BookingListCreateView.as_view(), name='booking-list'),
    ]
    ```

14. **Crea un superusuario:**

    ```bash
    python manage.py createsuperuser
    ```

    Sigue las instrucciones para proporcionar un nombre de usuario, correo electrónico y contraseña.

15. **Agrega el modelo al panel de administración:**

    Crea un archivo `admin.py` en el directorio `bookings`:

    ```python
    # bookings/admin.py

    from django.contrib import admin
    from .models import Booking

    admin.site.register(Booking)
    ```

16. **Ejecuta el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

17. **Accede a la interfaz de administración:**

    Visita `http://127.0.0.1:8000/admin/` y utiliza las credenciales del superusuario que se creo.
