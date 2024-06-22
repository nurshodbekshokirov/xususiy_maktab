from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class Foydalanuvchi(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('teacher', 'Oqituvchi'),
        ('parent', 'Ota-ona'),
        ('student', 'Oquvchi'),
    ]
    roli = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # related_name'larni qo'shing
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='foydalanuvchilar',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='foydalanuvchilar',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Oqituvchi(models.Model):
    foydalanuvchi = models.OneToOneField(Foydalanuvchi, on_delete=models.CASCADE)
    ismi = models.CharField(max_length=150)
    fan = models.CharField(max_length=100)
    telefon_raqami = models.CharField(max_length=15)
    email = models.EmailField()

    def clean(self):
        if self.foydalanuvchi.roli != 'teacher':
            raise ValidationError('Foydalanuvchi roli Oqituvchi bo\'lishi kerak.')

    def __str__(self):
        return self.ismi

class OtaOna(models.Model):
    foydalanuvchi = models.OneToOneField(Foydalanuvchi, on_delete=models.CASCADE)
    ismi = models.CharField(max_length=150)
    tugilgan_sana = models.DateField()
    telefon_raqami = models.CharField(max_length=15)
    email = models.EmailField()

    def clean(self):
        if self.foydalanuvchi.roli != 'parent':
            raise ValidationError('Foydalanuvchi roli Ota-ona bo\'lishi kerak.')

    def __str__(self):
        return self.ismi

class Oquvchi(models.Model):
    foydalanuvchi = models.OneToOneField(Foydalanuvchi, on_delete=models.CASCADE)
    sinfi = models.ForeignKey('asosiy.Sinf', on_delete=models.CASCADE, null=True)
    ismi = models.CharField(max_length=100)
    tugilgan_sanasi = models.DateField()
    ota_ona = models.ForeignKey(OtaOna, on_delete=models.CASCADE)

    def clean(self):
        if self.foydalanuvchi.roli != 'student':
            raise ValidationError('Foydalanuvchi roli Oquvchi bo\'lishi kerak.')

    def __str__(self):
        return self.ismi
