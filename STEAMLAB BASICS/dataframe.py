import streamlit as st
import pandas as pd
import numpy as np
st.title("This is Dataframe Lab")
st.subheader("This is first dataframe")
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=['A', 'B', 'C'],
)
st.dataframe(df)
st.subheader("This is second dataframe")
df2  = pd.DataFrame(
    np.random.randn(50,20),
   columns = ('col %d'%i for i in range(20))
    
)
st.dataframe(df2)