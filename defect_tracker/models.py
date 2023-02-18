from django.db import models

# Create your models here.


class Defect(models.Model):
    reason = models.CharField(max_length=250, blank=True, null=False)
    job_order_no = models.CharField(max_length=50, blank=False, null=False)
    defect_image = models.ImageField( upload_to="defects_images/",blank=True, null=True)
    created_at = models.TimeField(
        auto_now_add=True
    )
    