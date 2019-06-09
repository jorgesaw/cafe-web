from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=210, help_text="Enter a title", verbose_name="Título")
    subtitle = models.CharField(max_length=210, help_text="Enter a subtitle", verbose_name="Subtítulo")
    content = models.TextField(help_text="Enter a content", verbose_name="Contenido")
    image = models.ImageField(upload_to='services_images', blank=True, verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        ordering = ['-created']
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def get_absolute_url(self):
        """Returns the url to access a particular service instance."""
        return reverse_lazy('service-detail', args=[str(self.id)])

    def soft_delete(self):
        self.active = False
        self.save()

    def __str__(self):
        return self.title
