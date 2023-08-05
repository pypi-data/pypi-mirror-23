from asyncorm import models


class Organization(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(null=True)
    uuid = models.Uuid4Field(uuid_type='v1')


class Developer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    age = models.IntegerField(default=25)
    org = models.ManyToManyField(foreign_key='Organization')


class Client(models.Model):
    name = models.CharField(max_length=10)
    dev = models.ForeignKey(foreign_key='Developer')
    appoinment = models.ForeignKey(foreign_key='Appointment', null=True)


class Appointment(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField(null=True)
    uuid = models.Uuid4Field()
