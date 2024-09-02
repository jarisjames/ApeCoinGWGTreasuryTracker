from django.shortcuts import render
from django.db import connection
from decimal import Decimal

def wallet_dashboard(request):
    with connection.cursor() as cursor:
        # Fetch wallet data including all columns
        cursor.execute("""
            SELECT wallet_name, wallet_address, token_name, token_price, token_amount, usd_value, staking_pool, staked_balance, staked_rewards, staked_usd_value
            FROM ApeCoinData
        """)
        wallet_data = cursor.fetchall()

    # Convert wallet_data to a list of lists for easier manipulation
    wallet_data = [list(row) for row in wallet_data]

    # Calculate the total USD value including staked for each wallet and rearrange columns
    rearranged_data = []
    for row in wallet_data:
        usd_value = Decimal(row[5] or 0)  # USD Value
        staked_usd_value = Decimal(row[9] or 0)  # Staked USD Value
        total_usd_value = usd_value + staked_usd_value
        
        # Create new row with rearranged columns
        new_row = [
            total_usd_value.quantize(Decimal('0.01')),  # Total USD Value (Including Staked)
            usd_value.quantize(Decimal('0.01')),  # USD Value
            staked_usd_value.quantize(Decimal('0.01')),  # Staked USD Value
            row[0],  # Wallet Name
            row[1],  # Wallet Address
            row[2],  # Token Name
            row[3],  # Token Price
            row[4],  # Token Amount
            row[6],  # Staking Pool
            row[7],  # Staked Balance
            row[8],  # Staked Rewards
        ]
        rearranged_data.append(new_row)

    # Calculate the overall total USD value
    total_usd_value = sum(row[0] for row in rearranged_data)

    context = {
        'wallet_data': rearranged_data,
        'total_usd_value': total_usd_value.quantize(Decimal('0.01'))
    }
    return render(request, 'dashboard/wallet_dashboard.html', context)
