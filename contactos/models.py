from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class co (models.Model):
	Nombre = models.CharField(max_length = 20)
	Apellido = models.CharField(max_length = 20)
	Telefono = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.Nombre

	def get_absolute_url(self):
		return reverse('co_edit', kwargs={'pk': self.pk})