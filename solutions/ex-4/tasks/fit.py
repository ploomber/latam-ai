# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import seaborn as sns
from sklearn.linear_model import LinearRegression
from pathlib import Path
import pickle
import pandas as pd


# %%
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
upstream = ['train-test-split']
product = None


# %%
X_test = pickle.loads(Path(upstream['train-test-split']['X_test']).read_bytes())
X_train = pickle.loads(Path(upstream['train-test-split']['X_train']).read_bytes())
y_test = pickle.loads(Path(upstream['train-test-split']['y_test']).read_bytes())
y_train = pickle.loads(Path(upstream['train-test-split']['y_train']).read_bytes())

# %% [markdown]
# ## Linear regression

# %%
lr = LinearRegression()

# %%
lr.fit(X_train, y_train)

# %%
y_pred = lr.predict(X_test)

# %%
sns.scatterplot(x=y_test, y=y_pred)

# %%
print(lr.score(X_test, y_test))
