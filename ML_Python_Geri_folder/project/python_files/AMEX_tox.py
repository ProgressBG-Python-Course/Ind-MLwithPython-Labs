import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.naive_bayes import GaussianNB

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def load_data(file_name):
	df = pd.read_csv(file_name)
	return df

def deal_with_NaN_vlaues(df, threshold=0.8):
	"""deal_with_NaN_vlaues

	Arguments:
		df {DataFrame} -- DataFrame Object

	Keyword Arguments:
		threshold {float} -- drop columns and rows with missing values > threshold (default: {0.8})
	"""
	# print('NaN values in DF, sorted descending:')
	# print(df.isna().sum().sort_values(ascending=False))

	# print('NaN values percentage in DF, sorted descending:')
	# print(df.isna().mean().round(4).sort_values(ascending=False))

	#Drop columns with missing value rate higher than threshold:
	col_tresh_as_int = int(round(threshold*df.shape[0]))
	df = df.dropna(axis=1, thresh=col_tresh_as_int)

	#Drop rows with missing value rate higher than threshold:
	row_tresh_as_int = int(round(threshold*df.shape[1]))
	df = df.dropna(axis=0, thresh=row_tresh_as_int)

	return df


def standardScale(df):
	from sklearn.preprocessing import StandardScaler

	scaler = StandardScaler().fit(df)
	print(scaler.mean_)

	scaled = scaler.transform(df)

	return pd.DataFrame(scaled) # if we want to have DF, not ndarr

	# df_scaled = scaler.transform(df)


if __name__ == "__main__":
	df = load_data('ames_datapreprocessing_knime.csv')
	print(f'df shape original: {df.shape}')

	### separate input data from target:
	# remove all rows, where NaN values are in the Target column:
	df = df.dropna(how='any', subset=['AmesResult'])
	print(f'df shape after NaN clear: {df.shape}')

	y = df['AmesResult']
	X = df.drop(columns=['AmesResult'])
	print(f'X shape: {X.shape}')
	print(f'y shape: {y.shape}')

	### clean data
	# standard NaN values clean:
	X = deal_with_NaN_vlaues(X, threshold=0.8)
	print(f'X shape: {X.shape}')

	# show columns with non-numerical data:
	for column in X.columns:
		if X[column].dtype == 'object':
			print(f'{column} has non-numerical data')

	# drop Structure column:
	X = X.drop(columns=['Structure'])
	print(f'X shape: {X.shape}')
	print(f'type of X: {type(X)}')


	### scale data:
	X = standardScale(X)
	print(f'X info: {X.info}')

