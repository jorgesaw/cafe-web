from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Enter a name", verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        ordering = ['-created']
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def get_absolute_url(self):
        """Returns the url to access a particular blog instance."""
        return reverse_lazy('blog-detail', args=[str(self.id)])

    def soft_delete(self):
        self.active = False
        self.save()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=210, help_text="Enter a title", verbose_name="Título")
    content = models.TextField(help_text="Enter a content", verbose_name="Contenido")
    published = models.DateTimeField(default=now, verbose_name="Fecha de publicación") 
    image = models.ImageField(upload_to='posts_images', null=True, blank=True, verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    active = models.BooleanField(default=True, verbose_name="Activo")

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")

    class Meta:
        ordering = ['-created']
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        return reverse_lazy('post-detail', args=[str(self.id)])

    def soft_delete(self):
        self.active = False
        self.save()

    def __str__(self):
        return self.title
