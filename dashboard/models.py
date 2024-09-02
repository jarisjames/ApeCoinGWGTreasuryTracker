from django.db import models

class ApeCoinData(models.Model):
    wallet_name = models.CharField(max_length=255)
    wallet_address = models.CharField(max_length=255)
    token_name = models.CharField(max_length=255, null=True)
    token_price = models.DecimalField(max_digits=20, decimal_places=8, null=True)
    token_amount = models.DecimalField(max_digits=20, decimal_places=8, null=True)
    usd_value = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    staking_pool = models.CharField(max_length=255, null=True)
    staked_balance = models.DecimalField(max_digits=20, decimal_places=8, null=True)
    staked_rewards = models.DecimalField(max_digits=20, decimal_places=8, null=True)
    staked_usd_value = models.DecimalField(max_digits=20, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.wallet_name} - {self.token_name}"
