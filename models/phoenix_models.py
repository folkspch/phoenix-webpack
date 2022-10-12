from django.db import models

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    mobile_phone = models.CharField(max_length=16)
    password = models.CharField(max_length=128)
    national_id = models.CharField(max_length=16, null=True, blank=True, default=None)
    dob = models.DateField(null=True, blank=True, default=None)
    role = models.CharField(max_length=4)
    code = models.CharField(max_length=16, null=True, blank=True, default=None)
    status = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    activated_at = models.DateTimeField(null=True, blank=True, default=None)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)
    terminated_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.first_name) + ' '  + str(self.last_name) + ' (' + str(self.role) + ')' + ' (' + str(self.status) + ')'
