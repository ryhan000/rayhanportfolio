from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    objective = models.TextField(max_length=100)
    designation = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profile_images = models.ImageField(upload_to="images/reviews/", null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+8801XXXXXXXXX'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17)
    email = models.CharField(max_length=100)
    birth_day = models.DateField()
    MARITAL_STATUS_TYPE = (
        ('married', 'Married'),
        ('unmarried', 'Unmarried')
    )
    marital_status = models.CharField(choices=MARITAL_STATUS_TYPE, max_length=12, null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # projectPicture = None

    def __str__(self):
        return self.title


class ProjectPicture(models.Model):
    picture = models.ImageField(upload_to='images/reviews/', blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
