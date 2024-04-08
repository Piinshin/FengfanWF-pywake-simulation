import pandas as pd
import numpy as np
from py_wake.examples.data.hornsrev1 import Hornsrev1Site, V80, wt_x, wt_y, wt16_x, wt16_y
from py_wake.wind_turbines.power_ct_functions import PowerCtTabular
from py_wake import NOJ
from py_wake.wind_turbines import WindTurbine
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

windTurbines = wt_IEA15
site = Hornsrev1Site()
noj = NOJ(site,windTurbines)

simulationResult = noj(wt16_x,wt16_y)
#print(simulationResult.aep())
#print ("Total AEP: %f GWh"%simulationResult.aep().sum())
AEP=simulationResult.aep()
plt.figure()
windTurbines.plot(wt16_x,wt16_y)
c =plt.scatter(wt16_x, wt16_y, c=AEP.sum(['wd','ws']))
plt.colorbar(c, label='AEP [GWh]')
plt.title('AEP of each turbine')
plt.xlabel('x [m]')
plt.ylabel('[m]')
plt.show()

wind_speed = 10
wind_direction = 90

plt.figure()
flow_map = simulationResult.flow_map(ws=wind_speed, wd=wind_direction)
plt.figure(figsize=(18,10))
flow_map.plot_wake_map()
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Wake map for' + f' {wind_speed} m/s and {wind_direction} deg')
plt.show()