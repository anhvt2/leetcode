import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # left join to keep all buyers even with no orders
    merged = users.merge(orders,
        left_on='user_id',
        right_on='buyer_id',
        how='left'
        )

    # flag 2019 orders only
    merged['is_2019'] = (pd.to_datetime(merged['order_date']).dt.year == 2019)

    return (merged.groupby(['user_id', 'join_date'])['is_2019']
        .sum()
        .reset_index()
        .rename(columns={'user_id': 'buyer_id', 'is_2019': 'orders_in_2019'})
        .sort_values('buyer_id')
        )