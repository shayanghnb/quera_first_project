from django.db import models


class author(models.Model):
    name = models.CharField(max_length=100)


class bookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(author, on_delete=models.CASCADE, null=False)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
