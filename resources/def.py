import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# check data type and load data
def load_data(data):
    if data.name.endswith('.xls') or data.name.endswith('.xlsx'):
        df = pd.read_excel(data)
    elif data.name.endswith('.csv'):
        df = pd.read_csv(data)
    elif data.name.endswith('.json'):
        df = pd.read_json(data)
    else:
        st.error("File not supported")
        return None
    return df

def plot_data(df):
    # select x and y coordinates
    x = st.selectbox("X", df.columns)
    y = st.selectbox("Y", df.columns)

    # plot data
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig)