from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.
class KirrURL(models.Model):
	"""docstring for KirrURL"""
	url = models.CharField(max_length=220,)
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	# everytime the  model is saved
	updated = models.DateTimeField(auto_now=True)
	# everytime the model is created 
	timestamp = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode()
		super(KirrURL,self).save(*args, **kwargs)
	def __str__(self):
		return str(self.url)
		