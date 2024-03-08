from django.db import models

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    grupo = models.CharField(max_length=1)

    def __str__(self):
        return self.cedula + ' ' + self.grupo + ' ' + self.nombres + ' ' + self.apellidos

class ExamenTeorico(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40)
    numPreguntas = models.IntegerField()
    fechaRealizacion = models.DateTimeField()
    profesorDisenio = models.ForeignKey('Profesor', on_delete=models.CASCADE)

class Practica(models.Model):
    DIFICULTADES = (
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40)
    dificultad = models.CharField(max_length=20, choices=DIFICULTADES)

class ExamenTeoricoAlumno(models.Model):
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    nota = models.FloatField()
    examen = models.ForeignKey('ExamenTeorico', on_delete=models.CASCADE)

class PracticaAlumno(models.Model):
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    practica = models.ForeignKey('Practica', on_delete=models.CASCADE)
    fechaRealizada = models.DateTimeField()
    nota = models.FloatField()

class ProfesoresDisenioPractica(models.Model):
    practica = models.ForeignKey('Practica', on_delete=models.CASCADE)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    fechaParticipaDisenio = models.DateTimeField()

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=40)
    nombres = models.CharField(max_length=40)