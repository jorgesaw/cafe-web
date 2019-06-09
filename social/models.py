from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Link(models.Model):
    key = models.SlugField(max_length=100, unique=True, help_text="Enter a key", verbose_name="Nombre clave")
    name = models.CharField(max_length=210, help_text="Enter a name", verbose_name="Red Social")
    url = models.URLField(max_length=210, null=True, blank=True, help_text="Enter a url", verbose_name="Enlace")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        ordering = ['name', ]
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"

    def get_absolute_url(self):
        """Returns the url to access a particular link instance."""
        return reverse_lazy('link-detail', args=[str(self.id)])

    def soft_delete(self):
        self.active = False
        self.save()

    def __str__(self):
        return self.name