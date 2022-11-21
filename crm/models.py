from django.utils.timezone import now
from django.db import models
from contacts.models import Partner, Companies


class Months(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField("Stage Name", max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        return super(Stage, self).save(*args, **kwargs)


class Lead(models.Model):
    name = models.CharField("Opportunity", max_length=255)
    expect_revenue = models.DecimalField("Expected Revenue", max_digits=10, decimal_places=2)
    date_deadline = models.DateField("Expected Closing")
    partner_id = models.ForeignKey(Partner, null=True, on_delete=models.SET_NULL)
    stage_id = models.ForeignKey(Stage, null=True, on_delete=models.SET_NULL)
    company_id = models.ForeignKey(Companies, null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(default=now, editable=False)
    description = models.TextField("Description", default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(expect_revenue__gte='0'), name='lead_expect_non_negative'),
        ]
