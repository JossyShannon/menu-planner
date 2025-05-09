import streamlit as st
from url_upload import url
from file_upload import file
from create_meal_plan import meal_plan

st.title("Menu Planner")

if 'action' not in st.session_state:
    st.session_state.action = None

st.session_state.action = st.selectbox(label='What do you want to do today?',
                                       options=['Select',
                                                'Upload a new recipie from a URL',
                                                'Upload a new recipie from a file',
                                                'Create a meal plan'])

if st.session_state.action == 'Upload a new recipie from a URL':
    url()
elif st.session_state.action == 'Upload a new recipie from a file':
    st.write("Upload a new recipie from a file")
    file()
elif st.session_state.action == 'Create a meal plan':
    st.write("Create a meal plan")
    plan = meal_plan()
    st.table(plan[1])