from django.db import models

class Contact(models.Model):

    class Meta: # include this to ensure build in IDE
        app_label = "hello"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)