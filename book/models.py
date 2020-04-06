from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length= 20)
    summary = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    publication_date = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['title', '-publication_date']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('book:book-detail', kwargs={'id' : self.id})

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('book:author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
