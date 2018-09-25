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
        max_length=64, 
        choices=RANK_CHOICES, 
        default=SOLDIER,
    )
    position = models.CharField(max_length=64)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    receipt_date = models.DateField()
    promotion_date = models.DateField()
    rebuke = models.BooleanField()


