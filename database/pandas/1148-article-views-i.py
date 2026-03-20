import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    mask = (views['author_id'] == views['viewer_id']) # author_id == viewer_id
    return (views[mask][['author_id']]
                .drop_duplicates()
                .rename(columns={'author_id': 'id'})
                .sort_values('id')
        )