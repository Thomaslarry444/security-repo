import csv
import pandas as pd
from typing import Iterable 
from pprint import pprint
with open ('test_list.csv', newline='') as f:
    reader = csv.reader(f,delimiter=';', lineterminator='\n')
    device_list =list[reader]

print(device_list)