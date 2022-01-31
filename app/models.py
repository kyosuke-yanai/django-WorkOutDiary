from django.db import models

class WorkOutRecord(models.Model):
    record_date = models.DateField(verbose_name='記録日', auto_now_add=True)
    menu = models.CharField(verbose_name='トレーニング名', max_length=20)
    sets = models.IntegerField(verbose_name='セット数')
    memo = models.TextField(verbose_name='メモ', null=True, blank=True)

    def __str__(self):
        return str(self.record_date)+'：'+self.menu

class WorkOutRepsRecord(models.Model):
    menu = models.ForeignKey(WorkOutRecord, on_delete=models.CASCADE)
    reps = models.IntegerField(verbose_name='回数', null=True, blank=True)
    weight = models.IntegerField(verbose_name='重量', null=True, blank=True)

    def __str__(self):
        return str(self.menu.record_date)+'：'+self.menu.menu+'：'+str(self.reps)+'回：'+str(self.weight)+'kg'