from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
import random
import string


# Variables
code_length = 10


# Functions
def generate_passport_code():
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=code_length))
        if Passport.objects.filter(code=code).count() == 0:
            break

    return code


class Passport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, editable=False)

    name = models.CharField(max_length=100, unique=True, editable=False)
    birthday = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=code_length, default=generate_passport_code, editable=False)
    key = models.CharField(max_length=100, editable=False)
    slug = AutoSlugField(populate_from='code', editable=False)

    class Meta:
        ordering = ['-birthday', ]
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('passport_detail', kwargs={'slug': self.slug})

    def slugify_function(self, content):
        return content
