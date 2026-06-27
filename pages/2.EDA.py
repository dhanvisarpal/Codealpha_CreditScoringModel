import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\user\default of credit card clients.csv",header=1)

st.title("Exploratory Data Analysis")

st.header("Target Variable Distribution")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    x="default payment next month",
    data=df,
    ax=ax
)

st.pyplot(fig)

st.info("""
Most customers did not default on their credit card payments.
The dataset is moderately imbalanced.
""")

st.header("Age Distribution")

fig,ax=plt.subplots(figsize=(8,5))

sns.histplot(
    df["AGE"],
    bins=20,
    kde=True,
    ax=ax
)
st.pyplot(fig)
st.info("""
Most customers are concentrated in the young and middle-age groups.
""")

st.header("Credit Limit Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    df["LIMIT_BAL"],
    bins=30,
    kde=True,
    ax=ax
)
st.pyplot(fig)

st.info("""
The distribution is positively skewed, indicating a few customers have very high credit limits.
""")


st.header("Outlier Detection")

fig, ax = plt.subplots(figsize=(10,4))

sns.boxplot(
    x=df["LIMIT_BAL"],
    ax=ax
)

ax.set_title("Boxplot of Credit Limit")

st.pyplot(fig)

st.info("""
The boxplot highlights potential outliers and the spread of credit limits.
""")

st.header("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(14,10))

sns.heatmap(
    df.corr(),
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)

st.info("""
The heatmap shows relationships among variables.
Features with higher correlation to the target variable may be useful predictors.
""")

st.header("Key Insights")

st.success("""
1. The dataset contains more non-default customers than default customers.

2. Customer age is concentrated around young and middle-age groups.

3. Credit limits show positive skewness.

4. Outliers are present in credit limit values.

5. Repayment history variables are expected to be strong predictors of default risk.
""")
