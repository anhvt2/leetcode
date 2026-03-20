import pandas as pd
def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    last_30 = activity[
        (activity['activity_date'] >= pd.Timestamp('2019-06-28')) &
        (activity['activity_date'] <= pd.Timestamp('2019-07-27'))
    ]
    result = last_30.groupby('user_id')['session_id'].nunique().reset_index() # count unique sessions per user
    result.columns = ['user_name', 'sessions_count']
    avg = round(result['sessions_count'].mean(), 2) if len(result) > 0 else 0 # average across users, default 0
    return pd.DataFrame({'average_sessions_per_user': [avg]})