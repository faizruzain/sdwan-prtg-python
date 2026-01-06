import pandas as pd
import random

get = ['Traffic Total (Volume)(RAW)', 'Traffic Total (Speed)(RAW)', 'Traffic In (Volume)(RAW)', 'Traffic Out (Volume)(RAW)']

traffic_df = pd.read_csv('cleaned_csv/traffic.csv')
traffic_df = traffic_df.get(get)
traffic_df = traffic_df.drop(labels=[29, 30], axis=0)

for col in traffic_df.columns:

    for _ in traffic_df.itertuples(index=True):
        # index = _[0]
        # location or columns = 1 to 5
        traffic_df.loc[_[0], col] = random.randint(1, 300)

print(traffic_df)
traffic_df.to_csv('output_csv/random3.csv', index=False)