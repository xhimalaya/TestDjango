from django.db import models

class WebUsers(models.Model):
	class Meta:
		verbose_name = "Web User"
		verbose_name_plural = "Web Users"

	emailid = models.EmailField(max_length=40, verbose_name="Email ID", unique=True, null=False, blank=False)
	passwd = models.CharField(max_length=100, verbose_name="Password", null=False, blank=False)

class RequestList(models.Model):
	class Meta:
		verbose_name = "Request List"
		verbose_name_plural = "Requests List"

	reqtype = models.CharField(max_length=20, verbose_name="Request Type", null=False, blank=False)
	reqdesc = models.TextField(verbose_name="Request Desc.", null=False, blank=False)
	reqdate = models.DateField(verbose_name="Request Date", null=False, blank=False, auto_now_add=True)
	city = models.CharField(max_length=30, verbose_name="City", null=False, blank=False)
	state = models.CharField(max_length=30, verbose_name="State", null=False, blank=False)
	pincode = models.CharField(max_length=6, verbose_name="Pincode", null=False, blank=False)
	countrycode = models.CharField(max_length=3, verbose_name="Country Code", null=False, blank=False)
	mobileno = models.CharField(max_length=10, verbose_name="Mobile No.", null=False, blank=False)
	remarks = models.TextField(verbose_name="Remarks", null=True, blank=True)
	status = models.CharField(max_length=20, verbose_name="Request Status", null=False, blank=False)
	updatedby = models.EmailField(max_length=40, verbose_name="Updated By", null=True, blank=True)