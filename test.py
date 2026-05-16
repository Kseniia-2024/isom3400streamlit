import streamlit as st

st.title("Hong Kong University of Science and Technology 2026")
st.subheader("Marks Spring Sem")
st.write("Want predict you final GPA?")
wanted_GPA=st.number_input(min = 1.5,
                           max=4.3,
                           value=3.0)




