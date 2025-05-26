from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from datetime import date
import random

DEPARTMENTS = [
    ("Engineering", "Engineering"),
    ("Support", "Support"),
    ("HR", "HR"),
    ("Finance", "Finance"),
]

def generate_login_id(first_name, last_name):
    base_id = first_name[0].lower() + last_name.lower()
    login_id = base_id
    while Employee.objects.filter(login_id=login_id).exists():
        login_id = base_id + str(random.randint(100, 999))
    return login_id

def generate_employee_id():
    last_id = Employee.objects.order_by('-id').first()
    if last_id:
        return f"EMP{last_id.id + 1:05}"
    return "EMP00001"

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True, default=generate_employee_id)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    login_id = models.CharField(max_length=50, unique=True, blank=True)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=20, choices=DEPARTMENTS)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    permanent_address = models.TextField()
    current_address = models.TextField()
    id_proof = models.FileField(
    upload_to='id_proofs/',
    validators=[FileExtensionValidator(['pdf'])],
    blank=True,
    null=True
)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = generate_employee_id()
        if not self.login_id:
            self.login_id = generate_login_id(self.first_name, self.last_name)
        super().save(*args, **kwargs)

    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
