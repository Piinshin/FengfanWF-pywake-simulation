from py_wake.wind_turbines.power_ct_functions import PowerCtTabular
from py_wake.wind_turbines import WindTurbine
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##DATA download from NERL website
WT_tabular=pd.read_csv('IEA_15MW_240_RWT.csv')
print(WT_tabular.columns)
u = np.array(WT_tabular.WindSpeed)
ct =np.array(WT_tabular.Ct)
power =np.array(WT_tabular.Power)

##define wind turbine in pywake class as "wt_IEA15'
wt_IEA15 = WindTurbine(name='IEA15MW',
                    diameter=150,
                    hub_height=240,
                    powerCtFunction=PowerCtTabular(u,power,'kW',ct))

#plot a
ws = np.arange(3,25)
plt.xlabel('Wind speed [m/s]')
plt.ylabel('Power [MW]')
plt.title('IEA15 MW power curve')
plt.plot(ws, wt_IEA15.power(ws)/1000000,'-')
plt.ylim(0, 16)
plt.show()
