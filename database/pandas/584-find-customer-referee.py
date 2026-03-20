
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    mask = (customer['referee_id'] != 2) | (customer['referee_id'].isna())
    return customer[mask][['name']]
