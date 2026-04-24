import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# -------------------------------
# Title and Description
# -------------------------------
st.title("📊 Retail Business Dashboard")
st.header("Manage Input Section")
st.write("APlease enter the monthly salas target and select the region.")


sales_target = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
st.write(f"Your sales target is {sales_target}")

region = st.selectbox("Choose region:",
                      ["North", "South", "West", "East])
st.write(f"You selected: {option}")

if st.button("Submit"):
                       st.write("Button clicked!")
