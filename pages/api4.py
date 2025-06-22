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


st.title('API4 : Next Week Energy')
st.write('วิเคราะห์พลังธาตุของแต่ละวันใน "สัปดาห์หน้า" (พร้อมชื่อวัน เสาวัน เสาปี เสาเดือน)')

with st.echo():
    url = 'https://api-dev.spmu.me/api/api4_next_week_energy'
    
params = {}
data = getApi(url,params)

st.write(data)
