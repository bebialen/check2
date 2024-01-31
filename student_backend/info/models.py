from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    CLASS_CHOICES = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V'),
        ('VI', 'VI'),
        ('VII', 'VII'),
        ('VIII', 'VIII'),
        ('IX', 'IX'),
        ('X', 'X'),
        ('XI', 'XI'),
        ('XII', 'XII'),
    )
    student_class = models.CharField(max_length=5, choices=CLASS_CHOICES)
    DIVISION_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    division = models.CharField(max_length=1, choices=DIVISION_CHOICES)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    admission_number = models.CharField(max_length=10, unique=True, editable=False)  # This field is not editable

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.admission_number:
            last_student = Student.objects.order_by('-id').first()
            if last_student:
                last_admission_number = int(last_student.admission_number.split('-')[-1][1:])
                new_number = last_admission_number + 1
                self.admission_number = f"R-{new_number:03d}"
            else:
                self.admission_number = "R-001"
        super().save(*args, **kwargs)