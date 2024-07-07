import streamlit as st 
import pandas as pd 
import numpy as np

df = pd.DataFrame(
    np.random.randn(10,5),
    columns= ('col %d'%i for i in range(5))
)

st.subheader("This is a Table demonstration below")

st.table(df)

st.write("Those who still wondering whats differ btw Table and Datafram then see the below is st.dataframe(df) and above was st.table(df) ")

st.dataframe(df)

st.write("Lets try to represent in JSON format as well")

st.json(
    {
        "col 1": [1,2,3,4,5],
        "col 2": [10,20,30,40,50],
        "col 3": [100,200,300,400,500]
    }
)