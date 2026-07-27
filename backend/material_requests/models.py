from django.db import models
from users.models import UserManagerModel
from products.models import Product

# Create your models here.
class MaterialRequest(models.Model):
    APPROVAL_STATUS = [
        ('PENDING','Pending'),
        ('APPROVED','Approved'),
        ('NOT APPROVED','Not Approved'),
    ]

    RELEASE_STATUS = [
        ('PENDING','Pending'),
        ('RELEASED','Released'),
        ('NOT RELEASED','Not Released'),
    ]

    requestor_email = models.ForeignKey(
        UserManagerModel,
        on_delete=models.CASCADE,
        db_column='requestor_email',
        to_field='email',
        related_name='requests'
    )

    mrf_id = models.CharField(max_length=50, primary_key=True)

    date = models.DateTimeField(auto_now_add=True)

    approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='PENDING')

    approved_by = models.ForeignKey(
        UserManagerModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='approved_by',
        to_field='email',
        related_name='approved_requests'
    )

    release_status = models.CharField(max_length=20, choices=RELEASE_STATUS, default='PENDING')

    mrf_files = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"MRF - {self.mrf_id} - {self.requestor_email.name}"

    class Meta:
        db_table = 'material_request'


class Release(models.Model):
    mrf_id = models.ForeignKey(
        MaterialRequest,
        on_delete=models.CASCADE,
        db_column='mrf_id'
    )

    sub_id = models.CharField(max_length=50, primary_key=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column='product_id'
    )
    quantity = models.IntegerField()

    class Meta:
        db_table = 'release'
