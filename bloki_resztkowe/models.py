from django.db import models
from django.utils import timezone

# Create your models here.
class Pianka(models.Model):
    typ = models.CharField(max_length=10)
    kolor = models.CharField(max_length=10)
    
    def __str__(self):
        return self.typ

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Pianka'
        verbose_name_plural = 'Piankas'


class Nesting(models.Model):    
    pianka = models.ForeignKey(Pianka, on_delete="CASCADE")
    data_dodania = models.DateTimeField(blank=False, auto_now_add=True)
    data_zatwierdzenia = models.DateTimeField(blank=True, null=True, default=None)
    data_zakonczenia = models.DateTimeField(blank=True, null=True, default=None)
    barcode = models.CharField(max_length=50, blank=True)
    zatwierdzony = models.BooleanField(default=False)
    zakonczony = models.BooleanField(default=False)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    
    def zatwierdz(self):
        self.zatwierdzony = True
        self.data_zatwierdzenia = timezone.now()
        self.save()
        return True

    def zakoncz(self):
        self.zakonczony = True
        self.data_zakonczenia = timezone.now()
        self.save()
        return True
    
    def __str__(self):
        zlaczenie = (str(x) for x in (self.pianka, self.x, self.y, self.z))
        return_string = " / ".join(zlaczenie)
        return return_string

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Nesting'
        verbose_name_plural = 'Nestings'

class Errorlog(models.Model):
    error = models.TextField()
    transakcja = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Errorlog'
        verbose_name_plural = 'Errorlogs'