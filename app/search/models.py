from django.db import models
import pinyin

# Create your models here.
class Company(models.Model):
    slug = models.CharField(max_length = 100)
    name = models.CharField(max_length = 40)
    pinyin = models.CharField(max_length = 100,null=True,blank=True)
    isPremiumOnly = models.BooleanField()

    def __str__(self):
        return self.name

    def _get_pinyin_by_name(self):
        company_pinyin = pinyin.get(self.name,format="strip")
        return company_pinyin

    def save(self,*args,**kwargs):
        if not self.pinyin:
            self.pinyin = self._get_pinyin_by_name()
        super().save(*args,**kwargs)

class Search(models.Model):
    slug = models.ForeignKey(Company,on_delete=models.CASCADE)
    week = models.CharField(max_length = 40) # June 4,1989 as 19890602(as 02 is the Week number)
    search_hit = models.BigIntegerField()

    def __str__(self):
        return self.slug
