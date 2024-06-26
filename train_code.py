# -*- coding: utf-8 -*-
"""train_code

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cjh6TT6ykWIOgHjDOewkBAPA6DmmgTPL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from scipy.stats import randint

# Load the dataset
df = pd.read_csv('/content/drug_consumption.csv')

# Function to replace CL values in Nicotine and Alcohol columns
def replace_clx(value):
    if value.startswith('CL'):
        return int(value[2:])
    else:
        return value

df['Nicotine'] = df['Nicotine'].apply(replace_clx)
df['Alcohol'] = df['Alcohol'].apply(replace_clx)

# Plot histograms for Nicotine and Alcohol usage
fig, axs = plt.subplots(1, 2, figsize=(13, 5))
axs[0].hist(df['Nicotine'], bins=10, edgecolor='k', alpha=0.7, label='Nicotine Usage')
axs[0].set_title('Nicotine Usage')

axs[1].hist(df['Alcohol'], bins=10, edgecolor='k', alpha=0.7, label='Alcohol Usage', color='lightcoral')
axs[1].set_title('Alcohol Usage')

plt.show()

# Treat Nicotine usage values for higher accuracy
def replace_s(value):
    if value <= 2:
        return 0
    else:
        return 1

df['Nicotine'] = df['Nicotine'].apply(replace_s)

# Define features and target variable
features = ['Age', 'Gender', 'Education', 'Country', 'Ethnicity', 'Nscore',
            'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS', 'Alcohol']

X = df[features]
y = df['Nicotine']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Simple Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Randomized hyperparameters search
param_dist = {'n_estimators': randint(50, 500),
              'max_depth': randint(1, 30)}

rf2 = RandomForestClassifier()

rand_search = RandomizedSearchCV(rf2, param_distributions=param_dist, n_iter=7)
rand_search.fit(X_train, y_train)
best_rf = rand_search.best_estimator_
y_pred2 = best_rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred2)
precision = precision_score(y_test, y_pred2)
recall = recall_score(y_test, y_pred2)
print(f'Accuracy: {accuracy}\nPrecision: {precision}\nRecall: {recall}')

# Plot confusion matrix
cm = confusion_matrix(y_test, y_pred2)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

# Plot feature importances
feature_importances = pd.Series(best_rf.feature_importances_, index=X_train.columns).sort_values(ascending=False)
feature_importances.plot.bar()

# Export the second model with better accuracy to a pickle file
with open('random_forest_model_better_accuracy.pkl', 'wb') as f:
    pickle.dump(best_rf, f)

