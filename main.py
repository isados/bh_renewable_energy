# %%
import pandas as pd
folder = 'data'
wind_file = folder + '/' + 'wind_daily_2022.csv'
solar_file = folder + '/' + 'solar_daily_2022.csv'
triple_vars_file = folder + '/' + 'triple_vars_monthly.csv'

# %%
def split_df(*, data, var_columns):
    return (
            data[['month', val_col]].rename(columns={val_col: 'value'})
        for val_col in var_columns
    )
wind = pd.read_csv(wind_file)
solar = pd.read_csv(solar_file)
triple = pd.read_csv(triple_vars_file)
temp, wind_speed, humidity_per = split_df(data=triple, var_columns=[
    'temp_degrees_celcius','wind_speed_m/s','humidity_%'

])
temp.to_csv('data/temp_in_celcius_monthly_2022.csv', index=False)
wind_speed.to_csv('data/wind_speed_metre_per_second_monthly_2022.csv', index=False)
humidity_per.to_csv('data/humidity_percent_monthly_2022.csv', index=False)
temp,wind_speed
