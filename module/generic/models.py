from django.db import models

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

MEDIA_CHOICES = (
    ('1', 'Magazine'),
    ('2', 'Radio Station'),
    ('3', 'Journal'),
    ('4', 'TV Station'),
    ('5', 'Newspaper'),
    ('6', 'Website'),
)

# Create your models here.
class crud(models.Model):
	name = models.CharField(max_length=100)
	color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
	email = models.EmailField(max_length=70,blank=True)
	content = models.TextField()
	gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
	media_choice = models.CharField(max_length=25,choices=MEDIA_CHOICES)
	
	def __str__(self):
		return self.email
	