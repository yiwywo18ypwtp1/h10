from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    tag_name = models.CharField(max_length=25)


class Quote(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=1000)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=1, null=True, blank=True)

    def __str__(self):
        return f'"{self.writer}" | {self.title}'
