from django.db import models

class Sinf(models.Model):
    nomi = models.CharField(max_length=100)
    oqituvchi = models.ForeignKey('users.Foydalanuvchi', on_delete=models.CASCADE, null=True, limit_choices_to={'roli': 'teacher'})

    def __str__(self):
        return self.nomi

class Davomat(models.Model):
    HOLAT_CHOICES = [
        ('present', 'Mavjud'),
        ('absent', 'Yo\'q'),
        ('late', 'Kechikkan'),
    ]
    oquvchi = models.ForeignKey('users.Oquvchi', on_delete=models.CASCADE)
    sana = models.DateField()
    holati = models.CharField(max_length=10, choices=HOLAT_CHOICES)

    def __str__(self):
        return f"{self.oquvchi.ismi} - {self.sana} - {self.holati}"

class Vazifa(models.Model):
    sinfi = models.ForeignKey(Sinf, on_delete=models.CASCADE)
    mavzu = models.CharField(max_length=200)
    tavsif = models.TextField()
    muddati = models.DateField()

    def __str__(self):
        return self.mavzu

class Tolov(models.Model):
    HOLAT_CHOICES = [
        ('paid', 'To\'langan'),
        ('pending', 'Kutilmoqda'),
        ('failed', 'Xato'),
    ]
    foydalanuvchi = models.ForeignKey('users.Foydalanuvchi', on_delete=models.CASCADE)
    miqdori = models.DecimalField(max_digits=10, decimal_places=2)
    sana = models.DateField()
    holati = models.CharField(max_length=10, choices=HOLAT_CHOICES)
    stripe_payment_intent = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.foydalanuvchi.username} - {self.miqdori} - {self.holati}"

class YangilikVaElon(models.Model):
    mavzu = models.CharField(max_length=200)
    matn = models.TextField()
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)
    yangilangan_vaqt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mavzu
