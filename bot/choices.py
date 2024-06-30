from django.db import models


class OrganizationChoice(models.TextChoices):
    SCHOOL = 'Maktab', 'Maktab'
    PRIVATE_UNIVERSITY = 'Xususiy universitet', 'Xususiy universitet'
    STATE_UNIVERSITY = 'Davlat universitet', 'Davlat universitet'
    EDUCATION_CENTER = 'O\'quv markaz', 'O\'quv markaz'