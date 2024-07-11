from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    trailer_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return f'{self.title} - {self.description[:50]}'


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    num_tickets = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.movie.title}"
