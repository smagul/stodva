from django.db import models


class Staff(models.Model):
    SOLDIER = 'ряд'
    JUNIOR_SERGEANT = 'мл.снт'
    SERGEANT = 'снт'
    SENIOR_SERGEANT = 'ст.снт'
    LIEUTENANT = 'лнт'
    SENIOR_LIEUTENANT = 'ст.лнт'
    CAPTAIN = 'кн'
    MAJOR = 'мр'
    LIEUTENANT_COLONEL = 'ппк'
    COLONEL = 'пк'

    RANK_CHOICES = (
        (SOLDIER, 'Рядовой'),
        (JUNIOR_SERGEANT, 'Младший сержант'),
        (SERGEANT, 'Сержант'),
        (SENIOR_SERGEANT, 'Старший сержант'),
        (LIEUTENANT, 'Лейтенант'),
        (SENIOR_LIEUTENANT, 'Старший лейтенант'),
        (CAPTAIN, 'Капитан'),
        (MAJOR, 'Майор'),
        (LIEUTENANT_COLONEL, 'Подполковник'),
        (COLONEL, 'Полковник'),
    )

    rank = models.CharField(
        verbose_name=('Звание'),
        max_length=64, 
        choices=RANK_CHOICES, 
        default=SOLDIER,
    )
    position = models.CharField(verbose_name=('Должность'), max_length=64)
    last_name = models.CharField(verbose_name=('Фамилия'), max_length=32)
    first_name = models.CharField(verbose_name=('Имя'), max_length=32)
    middle_name = models.CharField(verbose_name=('Отчество'), max_length=32)
    receipt_date = models.DateField(verbose_name=('Дата получения звания'))
    promotion_date = models.DateField(verbose_name=('Дата повышение'))
    rebuke = models.BooleanField(verbose_name=('Есть ли Выговор?'))

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


