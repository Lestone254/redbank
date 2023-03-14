from django.db import models
# Create your models here.

class Hospital(models.Model):
	Name=models.TextField()
	Longitude=models.CharField(max_length=100)
	Latitude=models.CharField(max_length=100)


class Group(models.Model):
	Name=models.CharField(max_length=100)

class Supply(models.Model):
	Hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE)
	Group=models.ForeignKey(Group, on_delete=models.CASCADE)
	Amount=models.IntegerField()