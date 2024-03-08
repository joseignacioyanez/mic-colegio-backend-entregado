from rest_framework.routers import DefaultRouter
from api.views import AlumnoViewSet, ExamenTeoricoViewSet, PracticaViewSet, ExamenTeoricoAlumnoViewSet, PracticaAlumnoViewSet, ProfesoresDisenioPracticaViewSet, ProfesorViewSet

router = DefaultRouter()
router.register('alumnos', AlumnoViewSet, basename='alumnos')
router.register('examenes-teoricos', ExamenTeoricoViewSet, basename='examenes-teoricos')
router.register('practicas', PracticaViewSet, basename='practicas')
router.register('examenes-teoricos-alumnos', ExamenTeoricoAlumnoViewSet, basename='examenes-teoricos-alumnos')
router.register('practicas-alumnos', PracticaAlumnoViewSet, basename='practicas-alumnos')
router.register('profesores-disenio-practicas', ProfesoresDisenioPracticaViewSet, basename='profesores-disenio-practicas')
router.register('profesores', ProfesorViewSet, basename='profesores')

urlpatterns = router.urls