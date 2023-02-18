from django.db import models


class BlogPost(models.Model):
    """  post on blog  """

    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.title}"

    class Meta:
        verbose_name = "Wpis"
        verbose_name_plural = "Wpisy"


