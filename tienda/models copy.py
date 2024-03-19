from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='imagenes', null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Marcas'

class Remoto(models.Model):
    codigo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='imagenes', null=True)

    TIPO = [
        ('tv_smart', 'TV Smart'),
        ('tv', 'TV'),
        ('canalera', 'Canalera'),
        ('directv', 'Directv'),
        ('smartbox', 'Smartbox'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO)

    def __str__(self):
        return "%s %s" % (self.codigo, self.marca)

    class Meta:
        verbose_name_plural = 'Remotos'

    