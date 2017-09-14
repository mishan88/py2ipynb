
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer


# In[ ]:

# Dataの読み込み
data = load_breast_cancer()


# In[ ]:

dataframe = pd.DataFrame(data.data, columns=data.feature_names)
targetdata = pd.DataFrame(data.target, columns=['Result'])
df = pd.concat([dataframe, targetdata], axis=1)


# In[ ]:

df.describe()


# In[ ]:

print("This is 'quote'.")


# In[ ]:



