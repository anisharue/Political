from django.db import models


class Post(models.Model):
    """
    Model representing a blog post.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    signature = models.CharField(max_length=100, default='Sydney White')
    date = models.DateField()

    def __str__(self):
        """
        Returns a string representation of the blog post's title.
        """
        return self.title
