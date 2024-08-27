from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self) -> str:
        return self.title