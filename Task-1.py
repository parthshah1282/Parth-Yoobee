import numpy as np
temp = np.array([18.5,19,20,25.0,2,30,13.9])
avg_temp = np.mean(temp)
print("Averrage temperture for a week", avg_temp)
Highest = np.max(temp)
print("Highest temperature", Highest)
Lowest = np.min(temp)
print("Lowest temperature", Lowest)
fahrenhit = temp * 9/5 + 32
print("Temp in fahrenhit",fahrenhit)
above_20_index = np.where(temp>20)
print("days where the temperature was above 20°C",above_20_index[0])