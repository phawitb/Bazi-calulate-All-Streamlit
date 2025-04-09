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


st.title('API3 : Five Year Forecast	')
st.write('ทำนายพลังธาตุรายปีล่วงหน้า 5 ปี (แสดงเฉพาะเสาปี)')

with st.echo():
    url = 'https://api.dev.spmu.me/api/api3_five_year_forecast'
    
params = {}
data = getApi(url,params)

st.write(data)
