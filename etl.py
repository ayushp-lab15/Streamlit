
import streamlit as st
import pandas as pd

st.write('Write AVD')

data = {
        'Task': ['Extract', 'Transform', 'Load'],
        'Status': ['Completed', 'InProgress', 'Pending']
    }

df = pd.DataFrame(data)

st.write('ETL Pipeline Execution Status', df)


