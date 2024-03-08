from rest_framework import serializers
from .models import Alumno, ExamenTeorico, Practica, ExamenTeoricoAlumno, PracticaAlumno, ProfesoresDisenioPractica, Profesor
from rest_framework.response import Response
from django.contrib.auth.models import Group


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = self.serializer_class(queryset, many=True).data

        # Calcula el número de practicas en que ha participado el Alumno
        for data in serialized_data:
            alumno_id = data['id']
            count = PracticaAlumno.objects.filter(alumno_id=alumno_id).count()
            data['num_practicas'] = count

        return Response(serialized_data)

class ExamenTeoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenTeorico
        fields = '__all__'

class PracticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practica
        fields = '__all__'

class ExamenTeoricoAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenTeoricoAlumno
        fields = '__all__'

class PracticaAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticaAlumno
        fields = '__all__'

class ProfesoresDisenioPracticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesoresDisenioPractica
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

# Para roles de grupo de usuarios
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')