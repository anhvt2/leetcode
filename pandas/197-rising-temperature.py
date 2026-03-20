import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.sort_values('recordDate')  # ensure chronology
    df['prev_temp'] = df['temperature'].shift(1) # yesterday temperature
    df['prev_date'] = df['recordDate'].shift(1) # yesterday's date
    mask = ( df['temperature'] > df['prev_temp']) & \
            (df['recordDate'] - df['prev_date'] == pd.Timedelta(days=1)) # consecutive day
    return df[mask][['id']]