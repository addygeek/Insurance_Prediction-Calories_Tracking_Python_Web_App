import streamlit as st 

st.title("Layouts")

st.subheader("<-Sidebars in left side")

add_selectbox = st.sidebar.selectbox(
    "How to contact you?",
    ("Email","Home Phone","Mobile Phone")
) 

with st.sidebar:
    add_radio = st.radio("Chhose a Plan",
                         ("$1","$100","$200","$500"))
    
st.subheader("Coulumn layout")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Columns 1")
    st.write("Write the contents of the column")
with col2:
    st.write("Columns 2")
    st.write("Write the contents of the column")
with col3:
    st.write("Columns 3")
    st.write("Write the contents of the column")

st.subheader("Expanders")

st.bar_chart({"data":[1,2,3,4,5,6,7,8,9,10]})
with st.expander("Expand me to see the detials of data"):
    st.write("Expanded detials of data")