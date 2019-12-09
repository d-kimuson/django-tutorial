from django.db import models


class Message(models.Model):
    content = models.CharField(
        unique=True,
        max_length=128
    )

    def __repr__(self):
        return f"{self.pk}. {self.content}"

    __str__ = __repr__
