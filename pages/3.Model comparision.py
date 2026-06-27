import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Model Comparison")

comparison_df = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "KNN",
        "SVM"
    ],
    "Accuracy": [80.62, 71.95, 81.43, 79.50, 80.85],
    "Precision": [0.66, 0.38, 0.64, 0.56, 0.66],
    "Recall": [0.25, 0.41, 0.36, 0.34, 0.27],
    "F1-Score": [0.37, 0.39, 0.46, 0.43, 0.38],
    "ROC-AUC": [0.7345, 0.6104, 0.7567, 0.7032, 0.7119]
})

st.header("Model Performance Comparison")

st.dataframe(comparison_df)

st.header("Accuracy Comparison")

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    comparison_df["Model"],
    comparison_df["Accuracy"]
)

ax.set_ylabel("Accuracy")
ax.set_title("Model Accuracy Comparison")

st.pyplot(fig)

st.header("ROC-AUC Comparison")

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    comparison_df["Model"],
    comparison_df["ROC-AUC"]
)

ax.set_ylabel("ROC-AUC")
ax.set_title("ROC-AUC Comparison")

st.pyplot(fig)

st.header("F1-Score Comparison")

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    comparison_df["Model"],
    comparison_df["F1-Score"]
)

ax.set_ylabel("F1-Score")
ax.set_title("Model F1-Score Comparison")

st.pyplot(fig)

best_model = comparison_df.loc[
    comparison_df["Accuracy"].idxmax(),
    "Model"
]

st.header("Best Model Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Best Accuracy", "81.43%")

with col2:
    st.metric("Best F1-Score", "0.46")

with col3:
    st.metric("Best ROC-AUC", "0.7567")

st.success(f"Best Performing Model: {best_model}")

st.markdown("""
### Why Random Forest?

Random Forest achieved the highest accuracy among all tested models.

**Advantages:**

- Handles complex relationships well
- Reduces overfitting through ensemble learning
- Works effectively with large datasets
- Provides robust performance on classification tasks
""")

