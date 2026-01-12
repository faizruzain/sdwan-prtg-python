import pandas as pd
import random

# ===============================================================

device_id_dev = pd.read_csv('csv/device_id_new.csv').drop(columns=['hostname'])
print(device_id_dev)

data = (
    {
        'CPU 7(RAW)': 0,
        'Percent Available Memory 1 (Processor)(RAW)': 0,
        'Ping Time(RAW)': 0,
        'Minimum(RAW)': 0,
        'Maximum(RAW)': 0,
        'Packet Loss(RAW)': 0,
        'Temperature Slot 6 - Temp: CP-CPU(RAW)': 0,
        'Traffic Total (Volume)(RAW)': 0,
        'Traffic Total (Speed)(RAW)': 0,
        'Traffic In (Volume)(RAW)': 0,
        'Traffic Out (Volume)(RAW)': 0
    }
)

data_df = pd.DataFrame(data, index=[0])

for col in device_id_dev.columns:
    for data in device_id_dev.itertuples():
        for column in data_df.columns:
            for row in range(30):
                if column == 'Ping Time(RAW)' or column == 'Minimum(RAW)' or column == 'Maximum(RAW)':
                    data_df.loc[row, column] = random.randint(3, 5)
                elif column == 'Packet Loss(RAW)':
                    data_df.loc[row, column] = random.randint(1, 4)
                elif column == 'Temperature Slot 6 - Temp: CP-CPU(RAW)':
                    data_df.loc[row, column] = random.randint(30, 39)
                elif column == 'CPU 7(RAW)':
                    data_df.loc[row, column] = random.randint(1, 100)
                else:
                    data_df.loc[row, column] = random.randint(1000, 10000)
        # print(data_df)
        # print(f'dummy/{device_id_dev.iloc[data[0]].loc[col]}.csv')
        data_df.to_csv(f'dummy/{device_id_dev.iloc[data[0]].loc[col]}.csv', index=False)

# ===============================================================

# string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# serial_number = ''
# ip_address = '172.16.16.' # /24

# for i in range(12):
#     serial_number += string[random.randint(0, len(string)-1)]
# # print(serial_number)

# status = [
#     'Active',
#     'Dead',
# ]

# data = (
#     {
#         'device': '',
#         'ip_address': '',
#         'serial_number': '',
#         'status': ''
#     }
# )

# data_df = pd.DataFrame(data, index=[0])

# for column in data_df.columns:
#     for row in range(30):
#         for i in range(9):
#             serial_number += string[random.randint(0, len(string)-1)]
#         data_df.loc[row, 'device'] = row+1
#         data_df.loc[row, 'ip_address'] = f'{ip_address + str(row+1)}'
#         data_df.loc[row, 'serial_number'] = f'XYZ{serial_number}'
#         data_df.loc[row, 'status'] = status[random.randint(0, 1)]
#         serial_number = ''

# # filtering 'Dead'

# print(data_df.status)
