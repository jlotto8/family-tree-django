from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    
    # Relationships
    spouse = models.ForeignKey('self', 
                                null=True, 
                                blank=True, 
                                on_delete=models.SET_NULL, 
                                related_name='spouse_relationship')
    parent = models.ForeignKey('self', 
                                null=True, 
                                blank=True, 
                                on_delete=models.SET_NULL, 
                                related_name='children')

    def __str__(self):
        return self.name

    def get_children(self):
        return Person.objects.filter(parent=self)

    def get_spouse(self):
        return self.spouse