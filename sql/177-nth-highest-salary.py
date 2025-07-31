import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    # Check if n is within bounds
    if 0 < N <= len(unique_salaries):
        value = unique_salaries.iloc[N-1]
    else:
        value = None

    return pd.DataFrame({f'getNthHighestSalary({N})': [value]})
