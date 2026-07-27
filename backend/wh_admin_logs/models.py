from django.db import models
from users.models import UserManagerModel

# Create your models here.

class WarehouseAdminLogs(models.Model):
    wh_id = models.ForeignKey(
        UserManagerModel,
        on_delete=models.CASCADE,
        db_column='wh_id',
        to_field='uid'
    )
    wh_logs = models.CharField(max_length=100, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    wh_proof = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.wh_id.name} - {self.wh_proof}"

    class Meta:
        db_table = 'wh_admin_logs'