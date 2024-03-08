from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Alumno, ExamenTeorico, Practica, ExamenTeoricoAlumno, PracticaAlumno, ProfesoresDisenioPractica, Profesor
from .seralizers import AlumnoSerializer, ExamenTeoricoSerializer, GroupSerializer, PracticaSerializer, ExamenTeoricoAlumnoSerializer, PracticaAlumnoSerializer, ProfesoresDisenioPracticaSerializer, ProfesorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import GroupsPermissions

# Viewsets para el CRUD de todas las Entidades
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [GroupsPermissions]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = self.serializer_class(queryset, many=True).data

        # Calcula el número de veces que cada alumno aparece en PracticaAlumno
        for data in serialized_data:
            alumno_id = data['id']
            count = PracticaAlumno.objects.filter(alumno_id=alumno_id).count()
            data['num_practicas'] = count

        return Response(serialized_data)

class ExamenTeoricoViewSet(viewsets.ModelViewSet):
    queryset = ExamenTeorico.objects.all()
    serializer_class = ExamenTeoricoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [GroupsPermissions]

class PracticaViewSet(viewsets.ModelViewSet):
    queryset = Practica.objects.all()
    serializer_class = PracticaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [GroupsPermissions]

class ExamenTeoricoAlumnoViewSet(viewsets.ModelViewSet):
    queryset = ExamenTeoricoAlumno.objects.all()
    serializer_class = ExamenTeoricoAlumnoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [GroupsPermissions]

class PracticaAlumnoViewSet(viewsets.ModelViewSet):
    queryset = PracticaAlumno.objects.all()
    serializer_class = PracticaAlumnoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [GroupsPermissions]

class ProfesoresDisenioPracticaViewSet(viewsets.ModelViewSet):
    queryset = ProfesoresDisenioPractica.objects.all()
    serializer_class = ProfesoresDisenioPracticaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [GroupsPermissions]

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [GroupsPermissions]

class UserGroupsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_groups = request.user.groups.all()
        serializer = GroupSerializer(user_groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)