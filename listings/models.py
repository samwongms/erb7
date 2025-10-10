from django.db import models
from datetime import datetime
from doctors.models import Doctor
from . choices import district_choices, room_choices, rooms_choices
from taggit.managers import TaggableManager

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Listing(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=50, choices=district_choices.items())
    description = models.TextField(blank=True)
    services = TaggableManager(verbose_name="Services")
    service = models.IntegerField()
    room_type = models.CharField(max_length=200, choices=room_choices.items(), default='')
    screen = models.IntegerField()
    professionals = models.ManyToManyField(Subject, blank=True)
    professional = models.IntegerField()
    rooms = models.CharField(max_length=2, choices=rooms_choices.items())
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-list_date',)
        indexes = [models.Index(fields=['list_date'])]

    def __str__(self):
        return self.title
    
    def tag_list(self):
        return u", ".join(tag.name for tag in self.services.all())