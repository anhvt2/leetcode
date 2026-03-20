import pandas as pd

def average_selling_price(
    prices: pd.DataFrame, 
    units_sold: pd.DataFrame
    ) -> pd.DataFrame:
    merged = prices.merge(units_sold, 
                        on='product_id',
                        how='left',
                        )

    # keep only sales within the valid price period
    mask = ((merged['purchase_date'] >= merged['start_date']) &
            (merged['purchase_date'] <= merged['end_date'])
        )
    valid = merged[mask]

    # handle empty case - no sales at all
    if valid.empty:
        return (prices[['product_id']].drop_duplicates()
                                        .assign(average_price=0)
            )

    result = (valid.groupby('product_id')
        .apply(lambda x: round(
                    (x['price'] * x['units']).sum() / x['units'].sum(), 2
                )
            )
        .reset_index()
        .rename(columns={0: 'average_price'}))

    # left join back to include products with no sales -> price = 0
    return (prices[['product_id']].drop_duplicates()
                                .merge(result, on='product_id', how='left')
                                .fillna({'average_price': 0})
        )

    