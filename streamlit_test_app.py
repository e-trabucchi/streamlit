import streamlit as st
import pandas as pd
import numpy as np
import random

footballers = pd.read_csv("/workspaces/streamlit/Listone_Fantapazz.csv", sep=';')
teams = pd.Categorical(["","Team1","Team2","Team3","Team4","Team5","Team6","Team7","Team8","Team9","Team10"])
footballers["Team"] = teams[0]
add = pd.DataFrame([
    ['','','','','Team1'],
    ['','','','','Team2'],
    ['','','','','Team3'],
    ['','','','','Team4'],
    ['','','','','Team5'],
    ['','','','','Team6'],
    ['','','','','Team7'],
    ['','','','','Team8'],
    ['','','','','Team9'],
    ['','','','','Team10']
    ], 
    columns=footballers.columns
)
footballers = pd.concat([footballers, add])
footballers["Team"] = footballers["Team"].astype('category')
st.title("Test")
st.data_editor(
    footballers[~footballers['Squadra'].isnull()].loc[lambda footballers: footballers['Squadra'] != '', :],
    column_config={
        "category": st.column_config.SelectboxColumn(
            "Team",
            width="medium",
            options=teams
        )
    },
    hide_index=True
)
# st.button('Hit me')
# st.checkbox('Check me out')
# st.radio('Pick one:', ['nose','ear'])
# st.selectbox('Select', [1,2,3])
# st.multiselect('Multiselect', [1,2,3])
# st.slider('Slide me', min_value=0, max_value=10)
# st.select_slider('Slide to select', options=[1,'2'])
# st.text_input('Enter some text')
# st.number_input('Enter a number')
# st.text_area('Area for textual entry')
# st.date_input('Date input')
# st.time_input('Time entry')
# st.file_uploader('File uploader')
# st.download_button('On the dl', data)
# st.camera_input("一二三,茄子!")
# st.color_picker('Pick a color')