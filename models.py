from django.db import models
try:
	from mptt.models import MPTTModel, TreeForeignKey
except ImportError:
	raise ImportError('django-mptt is a requirement for this app')

class LocationType(MPTTModel):
	name = models.CharField(max_length=100)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

	class Meta:
		verbose_name = 'Type'
	
	def __unicode__(self):
		return self.name

class Location(MPTTModel):
	type = models.ForeignKey(LocationType, related_name='locations', blank=True, null=True)
	name = models.CharField(max_length=100, help_text='Name of location', db_index=True)
	code = models.CharField(max_length=30, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

	class Meta:
		ordering = ['name']