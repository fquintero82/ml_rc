import data_retrieval
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


#load data
usgs_code = '05387440'
df = get_rc(usgs_code)
# column discharge is the target
#split data into training and test
train, test = train_test_split(df, test_size=0.2)
#plt.scatter(df['stage'],df['discharge'],color="blue")
#check split visually
plt.xlabel('stage, in feet')
plt.ylabel('discharge, in cfs')
plt.scatter(train['stage'],train['discharge'],color="red",label='train')
plt.scatter(test['stage'],test['discharge'],color="green",label='test')
plt.legend()
plt.show()
plt.close('all')

#normalization
#in this project, because only one feature is available to predict
#the target, nornalization is not required. However data will be normalized
#for learning purposes

#normalization layer
normalizer= tf.keras.layers.Normalization(axis=-1)
a = np.array(train['stage']).reshape(84,-1)
normalizer.adapt(a)
print(normalizer.mean.numpy())