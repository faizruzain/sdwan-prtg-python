import pandas as pd
import random


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

for i in range(3):
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
    print(data_df)
    data_df.to_csv(f'output_csv/prtg_dummy_{i}.csv', index=False)



# url = f'/api/prtg?cpu_id=55723&mem_id=55724&ping_id=55722&temp_id=55725&traffic_id=55726'
# url = f'/api/prtg?cpu_id=55687&mem_id=55688&ping_id=55686&temp_id=55689&traffic_id=55690'
# url = f'/api/prtg?cpu_id=52839&mem_id=52840&ping_id=52849&temp_id=52841&traffic_id=52843'

# x = 'csv' in 'text/CSV; charset=UTF-8'.lower()

# print(x)






















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
#         for i in range(12):
#             serial_number += string[random.randint(0, len(string)-1)]
#         data_df.loc[row, 'device'] = row+1
#         data_df.loc[row, 'ip_address'] = f'{ip_address + str(row+1)}'
#         data_df.loc[row, 'serial_number'] = serial_number
#         data_df.loc[row, 'status'] = status[random.randint(0, 1)]
#         serial_number = ''

# print(data_df)
