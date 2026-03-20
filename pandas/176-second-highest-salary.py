import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique = employee['salary'].drop_duplicates().nlargest(2)
    result = unique.iloc[1] if len(unique) >= 2 else None
    return pd.DataFrame({'SecondHighestSalary': [result]})