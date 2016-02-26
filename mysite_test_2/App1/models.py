# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from sqlserver_ado.fields import DateField, DateTimeField, TimeField


class T_Test_For_Django(models.Model):
	class Meta:
		db_table=u'Position_DB].[PFP].[T_Test_For_Django'
		#db_table=u'"[172.22.131.85]"."Position_DB"."PFP"."T_Test_For_Django"'
		#db_table = u'[172.22.131.85].Position_DB.PFP\".\"T_Test_For_Django'
	item_id = models.IntegerField(primary_key=True, db_column='ID')
	A = models.CharField(max_length=50, db_column='Tag_System')
	B = models.CharField(max_length=50, db_column='Tag_Name')
	C = models.CharField(max_length=50, db_column='Tag_DataType')