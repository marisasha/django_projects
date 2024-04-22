
python -m venv env


call env/scripts/activate


pip install django pillow


django-admin startproject django_settings .


django-admin startapp django_app





python manage.py makemigrations
python manage.py migrate


python manage.py createsuperuser


python manage.py runserver