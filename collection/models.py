from django.db import models

# Create your models here.

class GolfItem(models.Model):
    # The list of specific options for the dropdown menu
    CATEGORY_CHOICES = [
        ('CLUB', 'Golf Club'),
        ('POSTER', 'Poster'),
        ('PICTURE', 'Picture'),
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField()
    # ImageField requires the Pillow library we installed earlier
    image = models.ImageField(upload_to='golf_media/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.description[:20]}..."