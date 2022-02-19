from django.db import models

class WorkOutMenu(models.Model):
    DAY_OF_WEEK = (
        ('Sun', '日曜日'),
        ('Mon', '月曜日'),
        ('Tue', '火曜日'),
        ('Wed', '水曜日'),
        ('Thu', '木曜日'),
        ('Fri', '金曜日'),
        ('Sat', '土曜日'),
    )
    TYPE = (
        ('free', 'フリーウエイト'),
        ('machine', 'マシンウエイト'),
        ('bodyweight', '自重'),
    )
    PARTS = (
        ('arm','腕'),
        ('chest','胸'),
        ('shoulder','肩'),
        ('back','背中'),
        ('abdominal','腹筋'),
        ('leg','足'),
        ('others','その他'),
    )
    DETAILPARTS = (
        ('Biceps','上腕二頭筋'),
        ('Triceps','上腕三頭筋'),
        ('Forearm','前腕'),
        ('pectoralis_major','大胸筋'),
        ('upper_pectoralis_major','大胸筋上部'),
        ('lower_pectoralis_major','大胸筋下部'),
    )
    name = models.CharField(verbose_name='トレーニング名', max_length=50)
    sets = models.IntegerField(verbose_name='セット数')
    day_of_week = models.CharField(verbose_name='トレーニング曜日', max_length=3, choices=DAY_OF_WEEK, null=True, blank=True)
    workout_type = models.CharField(verbose_name='トレーニングタイプ', max_length=10, choices=TYPE)
    parts = models.CharField(verbose_name='部位', max_length=10, choices=PARTS)
    reps = models.IntegerField(verbose_name='回数')
    weight = models.IntegerField(verbose_name='重量')
    memo = models.TextField(verbose_name='メモ', null=True, blank=True)

    def __str__(self):
        return self.name

class WorkOutRecord(models.Model):
    record_date = models.DateField(verbose_name='記録日', auto_now_add=True)
    menu = models.ForeignKey(WorkOutMenu, verbose_name='トレーニング名', on_delete=models.CASCADE)
    sets = models.IntegerField(verbose_name='セット数')
    memo = models.TextField(verbose_name='メモ', null=True, blank=True)

    def __str__(self):
        return str(self.record_date)+'：'+str(self.menu.name)

class WorkOutDetailRecord(models.Model):
    menu = models.ForeignKey(WorkOutRecord, on_delete=models.CASCADE)
    reps = models.IntegerField(verbose_name='回数', null=True, blank=True)
    weight = models.IntegerField(verbose_name='重量', null=True, blank=True)

    def __str__(self):
        return str(self.menu.record_date)+'：'+self.menu.menu.name+'：'+str(self.reps)+'回：'+str(self.weight)+'kg'