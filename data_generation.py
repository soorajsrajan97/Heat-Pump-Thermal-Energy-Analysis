import pandas as pd
import numpy as np
np.random.seed(42)
hours = pd.date_range('2024-01-01', periods=8760, freq='H')  # Full year

# create synthetic temperature and demand data

temp_C = 10 + 15*np.sin(2*np.pi*hours.dayofyear/365) + np.random.normal(0,3,8760)
df_load = pd.DataFrame({
    'timestamp': hours,
    'temp_C': temp_C,
    'hour': hours.hour,
    'demand_kW': 100 + 50*np.sin(2*np.pi*hours.hour/24) - 2*(temp_C-10) + np.random.normal(0,10,8760)
})
df_load.to_csv('hourly_heat_demand.csv', index=False)
print(df_load.head())  # Verify: cold nights → high demand[page:45]
