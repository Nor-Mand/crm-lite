from django.db import models
from django_countries.fields import CountryField

INDUSTRY_CHOICES = [
    ('', '--- Select Industry ---'),
    ('AFSA', 'Accommodation and Food Service Activities'),
    ('IC', 'Information and Communication'),
    ('IT', 'Information Technology'),
    ('EGSACS', 'Electricity, Gas, Steam and Air Conditioning Supply'),
    ('CONST', 'Construction'),
    ('ASSA', 'Administrative and Support Service Activities'),
    ('PSTA', 'Professional, Scientific and Technical Activities'),
    ('MANU', 'Manufacturing'),
    ('WRT', 'Wholesale and Retail Trade'),
    ('REA', 'Real Estate Activities'),
    ('WSSWMRA', 'Water Supply; Sewerage, Waste Management and Remediation Activities'),
    ('MQ', 'Mining and Quarrying'),
    ('TS', 'Transportation and Storage'),
]


class Companies(models.Model):
    name = models.CharField("Company", max_length=255)
    tax_id = models.CharField("Tax ID", max_length=155)
    website = models.URLField("Website")
    industry_id = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    logo_company = models.ImageField(upload_to='profile_pictures/', default='', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        return super(Companies, self).save(*args, **kwargs)


class Partner(models.Model):
    full_name = models.CharField("Full Name", max_length=255)
    street = models.CharField("Address", max_length=255)
    phone = models.CharField("Phone number",max_length=255)
    email = models.EmailField("Email", unique=True)
    image_person = models.ImageField(upload_to='profile_pictures/', default='', blank=True)
    company_id= models.ForeignKey(Companies, on_delete=models.SET_NULL, null=True)
    country = CountryField("Country", blank_label='--- Select Country ---')

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.full_name = self.full_name.title()
        return super(Partner, self).save(*args, **kwargs)
