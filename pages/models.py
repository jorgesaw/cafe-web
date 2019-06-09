from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=210, help_text="Enter a title", verbose_name="Título")
    content = RichTextField(help_text="Enter a content", verbose_name="Contenido")
    order = models.SmallIntegerField(default=0, verbose_name="Orden")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "pagina"
        verbose_name_plural = "paginas"

    def get_absolute_url(self):
        """Returns the url to access a particular page instance."""
        return reverse_lazy('page-detail', args=[str(self.id)])

    def soft_delete(self):
        self.active = False
        self.save()

    def __str__(self):
        return self.title
