from django.contrib import admin
from .models import Genero
from .models import Director
from .models import Pais
from .models import Pelicula
from .models import Cine


# Registro de modelos aqui 

admin.site.register(Genero)
admin.site.register(Director)
admin.site.register(Pais)
admin.site.register(Pelicula)
admin.site.register(Cine)