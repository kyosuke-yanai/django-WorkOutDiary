from django.db import models

class WorkOutMenu(models.Model):
    name = models.CharField(verbose_name='トレーニング名', max_length=50)
    sets = models.IntegerField(verbose_name='セット数')
    reps = models.IntegerField(verbose_name='回数')
    weight = models.IntegerField(verbose_name='重量')
    memo = models.TextField(verbose_name='メモ', null=True, blank=True)

    def __str__(self):
        return self.name

class WorkOutRecord(models.Model):
    record_date = models.DateField(verbose_name='記録日', auto_now_add=True)
    menu = models.ForeignKey(WorkOutMenu, on_delete=models.CASCADE)
    memo = models.TextField(verbose_name='メモ', null=True, blank=True)

    def __str__(self):
        return str(self.record_date)+'：'+str(self.menu.name)

class WorkOutRepsRecord(models.Model):
    menu = models.ForeignKey(WorkOutRecord, on_delete=models.CASCADE)
    reps = models.IntegerField(verbose_name='回数', null=True, blank=True)
    weight = models.IntegerField(verbose_name='重量', null=True, blank=True)

    def __str__(self):
        return str(self.menu.record_date)+'：'+self.menu.menu.name+'：'+str(self.reps)+'回：'+str(self.weight)+'kg'