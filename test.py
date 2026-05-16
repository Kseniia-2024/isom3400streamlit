import streamlit as st

st.title("Hong Kong University of Science and Technology 2026")
st.subheader("Marks Spring Sem")
st.write("Want predict you final GPA?")
wanted_GPA=st.number_input("Enter the targeted GPA: ",
                           min_value = 1.5,
                           max_value = 4.3,
                           value = 3.0)
subject = st.selectbox("Choose the subject to add: ",
                    ["ISOM2010", "ACCT2200", "LANG2068"])

if st.button("Submit"):
    st.success(f"Your wanted GPA: {wanted_GPA}, Total number of subjects: {color}")
else: 
  subject = st.selectbox("Choose the subject to add: ",
                    ["ISOM2010", "ACCT2200", "LANG2068"])
