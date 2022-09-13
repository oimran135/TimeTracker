from django.db import models


class Project(models.Model):

    p_type_choices = (
        ("WEB", "Website Development"),
        ("ML", "Machine Learning"),
        ("DS", "Data Science/Engineering"),
        ("RE", "Robotics & Engineering"),
    )

    p_status_choices = (
        ("Live", "Project Ongoing"),
        ("Completed", "Project Completed"),
        ("Pipeline", "Project Pending Start"),
        ("Hiatus", "Project On-Hold")
    )

    title = models.CharField(max_length=30, unique=True)
    p_type = models.CharField(max_length=50, choices=p_type_choices, null=True, blank=True)
    desc = models.TextField(max_length=280, blank=True, null=True)
    p_status = models.CharField(max_length=50, choices=p_status_choices, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    project_dashboard_key = models.CharField(max_length=150, null=False, blank=False, default="420-666")


class UserRole(models.Model):
    title = models.CharField(max_length=30, unique=True)
    desc = models.TextField(max_length=280, blank=True, null=True)


class UserProjectRole(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
