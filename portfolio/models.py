from __future__ import unicode_literals


from django.db import models

class Pers_Info(models.Model):
	name = models.CharField(max_length=32)
	entry = models.CharField(max_length=11)
	branch = models.CharField(max_length=32)
	dob = models.DateField("Date Of Birth")
	Age = models.IntegerField(default=0)
	contact_no = models.IntegerField(default=0)
	contact_id = models.CharField(max_length=32)
	def __str__(self):
		return self.entry