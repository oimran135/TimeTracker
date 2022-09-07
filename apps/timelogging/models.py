from django.db import models

class UserDailyLogs(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(null=True, blank=True)


class UserProjectDailyLogs(models.Model):
    models.ForeignKey('project.UserProjectRole', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(null=True, blank=True)



