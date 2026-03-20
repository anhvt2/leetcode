def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    last_30 = activity[
        (activity['activity_date'] >= pd.Timestamp('2019-06-28')) &  # lower bound
        (activity['activity_date'] <= pd.Timestamp('2019-07-27'))    # upper bound ← missing!
    ]
    return (last_30.groupby('activity_date')['user_id']
                   .nunique()
                   .reset_index()
                   .rename(columns={'activity_date': 'day', 'user_id': 'active_users'}))