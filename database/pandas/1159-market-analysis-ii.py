import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # rank each seller's orders by date
    orders['rn'] = (orders.sort_values('order_date')
                          .groupby('seller_id')['order_date']
                          .rank(method='first'))

    # keep only 2nd sale per seller
    second = orders[orders['rn'] == 2][['seller_id', 'item_id']]

    # join items to get brand of 2nd sale
    second = second.merge(items, on='item_id', how='left')

    # left join to keep all users
    merged = users.merge(second, left_on='user_id', right_on='seller_id', how='left')

    # compare brands
    merged['2nd_item_fav_brand'] = (
        merged['item_brand'] == merged['favorite_brand']
    ).map({True: 'yes', False: 'no'}).fillna('no')

    return (merged[['user_id', '2nd_item_fav_brand']]
                  .rename(columns={'user_id': 'seller_id'})
                  .sort_values('seller_id'))