import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start = (activity[activity['activity_type'] == 'start']
            .set_index(['machine_id', 'process_id'])['timestamp'])
    end = (activity[activity['activity_type'] == 'end']
            .set_index(['machine_id', 'process_id'])['timestamp'])
    diff = (end - start).reset_index()

    return (diff.groupby('machine_id')['timestamp']
                .mean()
                .round(3)
                .reset_index()
                .rename(columns={'timestamp': 'processing_time'})
        )