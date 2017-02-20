from django.db import models
from .utils import create_shortcode
# Create your models here.



class KirrURLManager(models.Manager):
	def all(self,*args,**kwargs):
		qs_main = super(KirrURLManager, self).all(*args,**kwargs)
		qs = qs_main.filter(active=False)
		return qs

	def refresh_shortcodes(self):
		qs = KirrURL.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(self)
			q.save()
			new_codes +=1
		return "New codes made: {i}".format(i=new_codes)



class KirrURL(models.Model):
	url = models.CharField(max_length=220,)
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	update = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(KirrURL,self).save(*args,**kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
