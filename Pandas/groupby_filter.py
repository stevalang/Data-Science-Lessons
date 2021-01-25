import pandas as pd
import numpy as np

temps = pd.DataFrame({  'time':['morning', 'noon', 'night',
                                'morning', 'noon', 'night',
                                'morning', 'noon', 'night',
                                'morning', 'noon', 'night'], 
                        'city':['Denver','Denver','Denver',
                             'Austin','Austin','Austin',
                             'NYC','NYC','NYC',
                             'SFO','SFO','SFO'],
                        'temp':[46,57,52,
                                51,68,53,
                                32,32,33,
                                53,71,71], 
                        'temp1':[46,57,52,
                                51,68,53,
                                32,32,33,
                                53,71,71]})

grouped_temps = temps.groupby('city')

# for name, group in grouped_temps:
#     print(name)
#     print(group)

# Filter
# print(grouped_temps.filter(lambda x: x.std() <= 6))

# Transform, create temp_celsius column
# temps['temp_celsius'] = grouped_temps['temp'].transform(lambda x: )
temps['temp_adjusted'] = grouped_temps['temp'].transform(lambda x: x * .9 if x.mean() > 53 else x )

# for name, group in grouped_temps['temp']:
#         print(name)
#         print(group)


temps = temps.drop('temp1', axis=1)

print(temps)

