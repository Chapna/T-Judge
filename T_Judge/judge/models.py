from django.db import models


# Create your models here.

class Submit(models.Model):
    username = models.CharField()
    date_uploaded = models.DateField()
    status = models.CharField(choices=(('Compilation Error', 'ce'),
                                       ('Wrong Answer', 'wr'),
                                       ('Runtime Error', 're'),
                                       ('Time Limit Exceeded', 'tl'))
                              )
    source_code = models.FileField(upload_to='source_codes')
