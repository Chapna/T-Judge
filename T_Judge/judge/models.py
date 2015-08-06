from django.db import models


# Create your models here.

class Submit(models.Model):
    username = models.CharField(verbose_name='Username')
    upload_date = models.DateTimeField(verbose_name='Upload Date', auto_now_add=True)
    status = models.CharField(choices=(('Compilation Error', 'ce'),
                                       ('Wrong Answer', 'wr'),
                                       ('Runtime Error', 're'),
                                       ('Time Limit Exceeded', 'tl'))
                              , verbose_name='Status')
    source_code = models.FileField(upload_to='source_codes', verbose_name='Source Code')
    problem = models.ForeignKey('Problem')


class Problem(models.Model):
    pass


class Homework(models.Model):
    pass
