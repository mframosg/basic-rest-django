# Proyecto Django - API de Usuarios por Género

Este proyecto es un ejemplo de cómo crear una API REST simple con Django que separa usuarios por géneros. La API tiene dos endpoints que devuelven listas de nombres de usuarios masculinos y femeninos.

## Requisitos

- Python 3.x

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/tu_usuario/basic-rest-django.git
    cd basic-rest-django
    ```

2. Crea un entorno virtual y actívalo:

    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias desde `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

## Paso a paso del código realizado

1. Añade las siguientes aplicaciones a tu proyecto Django:

    - `'rest_framework'`
    - `'users'`

    Abre el archivo `myproject/settings.py` y asegúrate de que las aplicaciones estén listadas en `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'users',
    ]
    ```

2. Configura las rutas del proyecto para incluir las rutas de la aplicación `users`. Abre `myproject/urls.py` y añade el siguiente código:

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('users/', include('users.urls')),
    ]
    ```

3. Define las rutas en la aplicación `users`. Crea un archivo `users/urls.py` y añade las rutas para la vista `UserByGender`:

    ```python
    from django.urls import path
    from .views import UserByGender

    urlpatterns = [
        path('<str:gender>/', UserByGender.as_view()),
    ]
    ```

4. Implementa la vista `UserByGender` en `users/views.py` para manejar las peticiones y devolver las listas de nombres según el género:

    ```python
    from rest_framework.views import APIView
    from rest_framework.response import Response

    class UserByGender(APIView):
        def get(self, request, gender):
            names = {
                "men": ["Juan", "Pedro", "Pablo", "Jose"],
                "women": ["Maria"]
            }
            return Response({gender: names.get(gender, [])})
    ```

## Uso

1. Ejecuta el servidor de desarrollo de Django:

    ```sh
    python manage.py runserver
    ```

2. Prueba los endpoints en tu navegador web o con una herramienta como `curl` o Postman.

   - Obtener usuarios masculinos:

     ```
     http://127.0.0.1:8000/users/men/
     ```

     Respuesta:

     ```json
     {
         "men": ["Juan", "Pedro", "Pablo", "Jose"]
     }
     ```

   - Obtener usuarios femeninos:

     ```
     http://127.0.0.1:8000/users/women/
     ```

     Respuesta:

     ```json
     {
         "women": ["Maria"]
     }
     ```
