import streamlit as st
import requests
from datetime import datetime, timedelta
import json

def getApi(url,params):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()  # Parse JSON data
        print(data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None



st.title('API1 : Bazi Calculate')

selected_date = st.date_input("Birth date", datetime.today(), min_value=datetime(1900, 1, 1).date())
date_input = selected_date.strftime('%Y-%m-%d')

cols = st.columns(5)
with cols[0]:
    hour = st.number_input("Select hour", min_value=0, max_value=23, value=7, step=1)
with cols[1]:
    minute = st.number_input("Select minute", min_value=0, max_value=59, value=55, step=1)
time_input = f"{hour:02d}:{minute:02d}"

sex = st.radio("Select your gender:", ("male", "female"))


checked = st.checkbox("Don't know born time")
if checked:
    time_input = None


with st.echo():
    url = 'https://api.dev.spmu.me/api/calculate_bazi'
    params = {
        "date_input" : date_input,
        "time_input" : time_input,
        "sex" : sex
    }
    
results = getApi(url,params)
# results  = AllBaziCalulate(date_input,time_input,sex)



cols = st.columns(2)
cols[0].json(results)

s = json.dumps(results,indent=4,ensure_ascii=False)
cols[1].write(s)

