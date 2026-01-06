import pandas as pd
import random

traffic_df = pd.read_csv('cleaned_csv/traffic.csv')
traffic_df = traffic_df.get(['Date Time', 'Traffic Total (Volume)(RAW)', 'Traffic Total (Speed)(RAW)', 'Traffic In (Volume)(RAW)', 'Traffic Out (Volume)(RAW)'])
traffic_df = traffic_df.drop(labels=[29, 30], axis=0)
print(traffic_df)
columns = traffic_df.columns
traffic_df = traffic_df.loc[0, columns] = [1]

# for _ in traffic_df.itertuples(index=True):
#     # index = _[0]
#     # location or columns = 1 to 5
#     print(_)
#     random_integer = []

#     for i in range(29):
#         random_integer.append(random.randint(1, 21))
    
#     traffic_df.loc[_[0], _[0]] = random_integer

print(traffic_df)