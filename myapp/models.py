from django.db import models

class SotibOlish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    count = models.PositiveBigIntegerField()
    narx = models.PositiveBigIntegerField()
    all_sum = models.PositiveBigIntegerField(default=0, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Sotib olish"
        verbose_name_plural = "Sotib olish"

    def __str__(self):
        return self.name

    def all_price(self):
        return self.count*self.narx