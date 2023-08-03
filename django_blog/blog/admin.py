from django.contrib import admin
from .models import Post #Импорт модели публикации

#регистрация модели на странице администрирования сайта
admin.site.register(Post)