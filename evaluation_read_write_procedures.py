import pandas as pd
import time
import random
import string
import numpy as np
import pyarrow as pa
import pyarrow.csv as csv
from datetime import datetime

# Reading with dataframe
t11 = time.time()
pd_df = pd.read_csv('/Users/joseangelmolina/PycharmProjects/Laboratory_Data_Science/data/business.csv')
t12 = time.time()


t21 = time.time()
df_pa_1 = csv.read_csv('/Users/joseangelmolina/PycharmProjects/Laboratory_Data_Science/data/business.csv')
t22 = time.time()

t31 = time.time()
pd_df.to_csv('/Users/joseangelmolina/PycharmProjects/Laboratory_Data_Science/data/business2.csv')
t32 = time.time()


t41 = time.time()
csv.write_csv(df_pa_1, '/Users/joseangelmolina/PycharmProjects/Laboratory_Data_Science/data/business3.csv')
t42 = time.time()

print(f'Read pandas {t12-t11}s')
print(f'Read pyarrow {t22-t21}s')
print(f'Write pandas {t32-t31}s')
print(f'Write pyarrow {t42-t41}s')
