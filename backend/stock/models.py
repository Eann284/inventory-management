from django.db import models
from users.models import UserManagerModel
from wh_admin_logs.models import WarehouseAdminLogs
from products.models import Product

# Create your models here.


class AddStock(models.Model):
    add_id = models.CharField(max_length=50, primary_key=True)

    wh_id = models.ForeignKey(
        UserManagerModel,
        on_delete=models.CASCADE,
        db_column='wh_id',
        to_field='uid',
        related_name='add_stock'
        
    )

    wh_logs = models.ForeignKey(
        WarehouseAdminLogs,
        on_delete=models.CASCADE,
        db_column='wh_logs',
    )

    date = models.DateTimeField(auto_now_add=True)

    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column='product_id'
    )

    quantity = models.IntegerField()

    class Meta:
        db_table = 'add_stock'
        unique_together = [['wh_id','wh_logs']]