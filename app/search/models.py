from django.db import models
import pinyin

# Create your models here.
class Company(models.Model):
    slug = models.CharField(max_length = 100)
    name = models.CharField(max_length = 40)
    pinyin = models.CharField(max_length = 100,null=True,blank=True)
    isPremiumOnly = models.BooleanField()

    searchHitCount = models.BigIntegerField()

    def __str__(self):
        return self.name

    def _get_pinyin_by_name(self):
        company_pinyin = pinyin.get(self.name,format="strip")
        return company_pinyin

    def save(self,*args,**kwargs):
        if not self.pinyin:
            self.pinyin = self._get_pinyin_by_name()
        super().save(*args,**kwargs)
