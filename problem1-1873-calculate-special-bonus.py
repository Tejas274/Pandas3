import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    for i in range(0,len(employees)):
        e_id = employees['employee_id'][i]
        e_name = employees['name'][i]
        if(e_id %2 == 0) or (e_name[0] == 'M'):
           employees['salary'][i] = 0

    df = employees[['employee_id','salary']]

    return df.sort_values(by = ['employee_id']).rename(columns = {'salary':'bonus'})


###better sol

import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda x: x['salary'] if x['employee_id'] % 2 and not x['name'].startswith('M') else 0,
        axis=1)

    return employees[['employee_id', 'bonus']].sort_values(by=['employee_id'])





