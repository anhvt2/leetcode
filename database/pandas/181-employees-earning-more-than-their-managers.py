import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(
        employee,
        left_on='managerId',
        right_on='id',
    ) # self-join on managerID
    # merged (example):
    #     id_x | name_x | salary_x | managerId_x | id_y | name_y | salary_y | managerId_y
    # -----|--------|----------|-------------|------|--------|----------|------------
    # 1    | Joe    | 70000    | 3           | 3    | Sam    | 60000    | None
    # 2    | Henry  | 80000    | 4           | 4    | Max    | 90000    | None
    # -----|--------|----------|-------------|------|--------|----------|------------
    return merged[merged['salary_x'] > merged['salary_y']][['name_x']].rename(columns={'name_x': 'Employee'})