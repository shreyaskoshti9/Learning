from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    STATUS = (('EXP', 'Experienced'), ('FRE', 'Fresher'))
    EXP_YEAR = (('0','0'), ('1-3', '1-3'), ('3-5','3-5'), ('>5', '>5'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    addr1 = models.CharField(max_length=500)
    addr2 = models.CharField(max_length=300)
    empId = models.IntegerField()
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS)
    experience = models.CharField(max_length=10, choices=EXP_YEAR)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='userImages')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.empId}'