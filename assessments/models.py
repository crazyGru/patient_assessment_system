from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()

    def age(self):
        from datetime import date
        return date.today().year - self.date_of_birth.year - ((date.today().month, date.today().day) < (self.date_of_birth.month, self.date_of_birth.day))
    

class Assessment(models.Model):
    assessment_type = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='assessments')
    assessment_date = models.DateField()
    questions_and_answers = models.JSONField()
    final_score = models.FloatField()