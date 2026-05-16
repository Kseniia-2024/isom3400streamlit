import streamlit as st
import time

st.title("Hong Kong University of Science and Technology")
st.header("Common Core Calculator Planner")
st.subheader("For BBA 2026")

tab1, tab2= st.tabs(["Common Core Courses", "GPA"])
with tab1:
    st.write("Want predict you Common Core GPA?")
    wanted_GPA=st.number_input("Enter the targeted common core GPA: ",
                               min_value = 1.5,
                               max_value = 4.3,
                               value = 3.0)
    subjectT, subjectS, subjectA, subjectH = st.columns(4)
    with subjectT:
        st.subheader("T-core")
        subjectT = st.selectbox("Choose the T-core subject to add: ",
                        ["ENTR1001", "ENGN1500", "ISOM2400"])
        Target_Mark_T = st.selectbox("Choose the T-core subject target mark: ",
                        ["A", "B", "C"])
    with subjectS:
        st.subheader("S-core")
        subjectS = st.selectbox("Choose the S-core subject to add: ",
                        ["IEDA1522", "PHYS1001", "CHEM2001", "BIOL1001", "SUST2500"])
        Target_Mark_S = st.selectbox("Choose the S-core subject target mark: ",
                        ["A", "B", "C"])
    with subjectA:
        st.subheader("A-core")
        subjectA = st.selectbox("Choose the A-core subject to add: ",
                        ["HUMA1576", "HUMA1011", "HUMA2100"])
        Target_Mark_A = st.selectbox("Choose the A-core subject target mark: ",
                        ["A", "B", "C"])
    with subjectH:
        st.subheader("H-core")
        subjectH = st.selectbox("Choose the H-core subject to add: ",
                        ["HUMA1006", "SOCS2500", "ISOM1001"])
        Target_Mark_H = st.selectbox("Choose the H-core subject target mark: ",
                        ["A", "B", "C"])
    if st.button("Submit"):
        st.success(f"Your wanted GPA: {wanted_GPA}, Total number of subjects: {count}")


with tab2:
    st.write("**Your targeted GPA for Common Core:**")
    st.subheader(wanted_GPA)
    st.write("List of subjects you choose:")
    subjects_list = [
        {"Subject": subjectT, "Target Mark": Target_Mark_T},
        {"Subject": subjectS, "Target Mark": Target_Mark_S},
        {"Subject": subjectA, "Target Mark": Target_Mark_A},
        {"Subject": subjectH, "Target Mark": Target_Mark_H}
    ]
    count=0
    for i in subjects_list:
        st.write(f"{i["Subject"]}: {i["Target Mark"]}")
        count+=1
        
    with st.expander("*Some motivation...*"):
        st.write("Do not **give up!** ... he-he")
    
    
    placeholder = st.empty()
    for i in range(5):
        placeholder.write(f"Loading you GPA... {i*20}% complete")
        time.sleep(1)
    
    placeholder.write("Data loading complete. Displaying your GPA.")
    Numbers = {"A": 4.0, "B": 3.0, "C": 2.0}
    total_score=0
    for i in subjects_list:
        Mark = i["Target Mark"]
        st.write(Mark)
        st.write(Numbers[Mark])
        if Mark == Numbers[Mark]:
            total_score += Numbers[Mark]
    GPA = total_score / len(subjects_list)
    st.subheader(GPA)
        
    
    
    
    
    
    
    
    
