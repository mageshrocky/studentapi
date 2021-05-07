from django.db import models


# Create your models here.

class StudentDetails(models.Model):
    Name = models.CharField(max_length=255)
    Roll_Number = models.IntegerField(primary_key=True)

    def __int__(self):
        return self.Roll_Number


class Subject(models.Model):
    roll_no = models.OneToOneField(StudentDetails, on_delete=models.CASCADE)
    English = models.IntegerField(default=0)
    Maths = models.IntegerField(default=0)
    Science = models.IntegerField(default=0)
    Optional_subject = models.IntegerField(default=0)

    def __int__(self):
        return self.roll_no
