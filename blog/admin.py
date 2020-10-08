from django.contrib import admin
from .models import Post

# Register your models here.
#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado', 'status')
    list_filter = ('status', 'autor', 'publicado', 'criado')
    search_fields = ('titulo', 'conteudo')
    date_hierarchy = 'publicado'
    prepopulated_fields = {'slug':('titulo',)}


''' Comandos no Shell para interagir com o usuário
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user = User.object.get(username='Naruto') 
dir(objeto) --> saber os atributos que podem ser usados.
'''

