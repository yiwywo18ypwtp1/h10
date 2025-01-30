from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tag_name}"


class Quote(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'"{self.writer}" | {self.text} | #{self.tag}'
