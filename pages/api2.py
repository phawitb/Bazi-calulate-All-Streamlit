import streamlit as st
from datetime import datetime, timedelta, date
import json
import requests

def getApi(url,params):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()  # Parse JSON data
        print(data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


st.title('API2 : Current Energy')
st.write('แสดงพลังธาตุของปีปัจจุบันและพลังของแต่ละเดือน (เสาปีและเสาเดือน)')

with st.echo():
    url = 'https://api-dev.spmu.me/api/api2_current_energy'
params = {}
data = getApi(url,params)

st.write(data)

