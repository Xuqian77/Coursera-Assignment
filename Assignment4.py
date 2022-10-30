import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('GDP and Electricity Cnsumption in Suzhou.csv')

plt.figure()
plt.plot(df['year'], df['GDP/(billion yuan)'],
         df['year'], df['electricity consumption/(hundred million kwh)'],
         df['year'], df['Energy Consumption per Unit of GDP / ( hundred million kwh/trillion yuan)'], linewidth=2)
plt.legend(loc = "best", fontsize = 8,
           labels=['GDP(billion yuan)', 'Electricity Consumption(hundred million kwh)',
                   "Energy Consumption per Unit of GDP(hundred million kwh/trillion yuan)"])

plt.xlabel('Years', alpha=0.8)
plt.ylabel("GDP or Electricity Consumption", alpha = 0.8)
plt.title("GDP and Electricity Consumption in Suzhou", alpha = 0.8)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
