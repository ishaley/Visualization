from django.db import models


class UserLoanOrder(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    loan_time = models.IntegerField(default=0)
    from_app = models.IntegerField(default=0)
