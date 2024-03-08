from django.contrib import admin
from .models import Alumno, ExamenTeorico, Practica, ExamenTeoricoAlumno, PracticaAlumno, ProfesoresDisenioPractica, Profesor

# Register your models here.
admin.site.register(Alumno)
admin.site.register(ExamenTeorico)
admin.site.register(Practica)
admin.site.register(ExamenTeoricoAlumno)
admin.site.register(PracticaAlumno)
admin.site.register(ProfesoresDisenioPractica)
admin.site.register(Profesor)
