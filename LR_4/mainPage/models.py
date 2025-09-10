from django.db import models

class StatusIncidents(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class CyberAttack(models.Model):
    attack_name = models.CharField(max_length=50)
    description = models.TextField(default = "")

    def __str__(self):
        return self.attack_name

class SourceIncident(models.Model):
    source = models.CharField(max_length=50)

    def __str__(self):
        return self.source

class Incidents(models.Model):
    nameOfIncident = models.TextField(null = False, blank = False)
    Description = models.TextField(null = False, blank = False)
    Source = models.ForeignKey(
        'mainPage.SourceIncident',
        on_delete=models.CASCADE
    )
    Attack = models.ForeignKey(
        'mainPage.CyberAttack',
        on_delete=models.CASCADE
    )
    Status = models.ForeignKey(
        'mainPage.StatusIncidents',
        on_delete=models.CASCADE
    )
    Date = models.DateField(auto_now_add=True)
    Author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )