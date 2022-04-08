# %%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

dir = '/home/fhd/projects/.DATASETS/TBI/'
path_data = os.path.join(dir, 'data.csv')
path_AIS = os.path.join(dir, 'AIS.csv')

data = pd.read_csv(path_data,index_col='ID')
AIS = pd.read_csv(path_AIS)
print(len(data))


# %%
#Defining nessary functions

def dropna(df:pd.DataFrame, col:list) ->pd.DataFrame:
    result = [True] * len(df)
    for c in col:
        result = list(map(lambda x,y: x and y, result, df[c].notna().values))
    return df[result]


# %%
'''
3346 (base) --> 3080 (GOSE) --> 3056 (Age) --> 3053 (Age) --> 3033(Hos LOS) --> 3020 (ICU LOS) --> 3008 (GCS) --> 3007 (GCSM0) --> 2145 (Marshall) --> 2083 (Rotterdam)
2040 (mechanism) --> 1759 (PR on Adm)
'''

# %%

list_to_drop = ['age','gender','Hos LOS','ICU LOS','GOSE0','GCS', 'GCSM0','Marshall','Rotterdam','mechanism','PR on Adm']
df = dropna(data, list_to_drop)


