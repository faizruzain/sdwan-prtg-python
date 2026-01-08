import pandas as pd
import random

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
serial_number = ''
ip_address = '172.16.16.' # /24

for i in range(12):
    serial_number += string[random.randint(0, len(string)-1)]
# print(serial_number)

status = [
    'Active',
    'Dead',
]

data = (
    {
        'device': '',
        'ip_address': '',
        'serial_number': '',
        'status': ''
    }
)

data_df = pd.DataFrame(data, index=[0])

for column in data_df.columns:
    for row in range(30):
        for i in range(12):
            serial_number += string[random.randint(0, len(string)-1)]
        data_df.loc[row, 'device'] = row+1
        data_df.loc[row, 'ip_address'] = f'{ip_address + str(row+1)}'
        data_df.loc[row, 'serial_number'] = serial_number
        data_df.loc[row, 'status'] = status[random.randint(0, 1)]
        serial_number = ''

print(data_df)
