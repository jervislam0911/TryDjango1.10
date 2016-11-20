from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.
class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(KirrURLManager, self).all(*args, *kwargs)
		qs = qs_main.filter(active=True)
		return qs
	def refresh_shortcodes(self):
		qs = KirrURL.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save()
			new_codes +=1
		return "New codes made: {new_code}".format(new_code=new_codes)


class KirrURL(models.Model):
	"""docstring for KirrURL"""
	url = models.CharField(max_length=220,)
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	# everytime the  model is saved
	updated = models.DateTimeField(auto_now=True)
	# everytime the model is created 
	timestamp = models.DateTimeField(auto_now_add=True)
	# active url
	active  = models.BooleanField(default=True)
	objects = KirrURLManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode()
		super(KirrURL,self).save(*args, **kwargs)
	def __str__(self):
		return str(self.url)
		