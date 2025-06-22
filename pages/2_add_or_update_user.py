import streamlit as st
import requests
import json

st.set_page_config(page_title="API Tester - Add/Update User", layout="wide")
st.title("✅ เพิ่มหรืออัปเดตข้อมูลผู้ใช้")

# --- Default values ---
default_url = "https://api-dev.spmu.me/user/add_or_update"
default_method = "POST"
default_payload = '''{
  "line_id": "U0001",
  "birth_date": "1990-01-01",
  "birth_time": "12:30",
  "sex": "female"
}'''

# --- Inputs ---
method = st.selectbox("Request Method", ["GET", "POST", "PUT", "DELETE"], index=1)
url = st.text_input("Request URL", default_url)
payload_input = st.text_area("Payload (JSON format)", value=default_payload, height=200)

# --- Parse payload ---
try:
    payload = json.loads(payload_input)
except Exception as e:
    st.error(f"⚠️ Invalid JSON in payload: {e}")
    payload = {}

# --- Function to Send Request ---
def send_request():
    try:
        if method == "GET":
            response = requests.get(url, params=payload)
        elif method == "POST":
            response = requests.post(url, json=payload)
        elif method == "PUT":
            response = requests.put(url, json=payload)
        elif method == "DELETE":
            response = requests.delete(url, json=payload)
        else:
            st.error("❌ Unsupported method")
            return None, None

        return response.text, response.status_code

    except Exception as e:
        return f"❌ Error: {e}", None

if st.button('Send'):
    # --- Send request immediately ---
    response_data, response_status = send_request()

    # --- Display response ---
    if response_data is not None:
        st.subheader("🔁 Response")
        if response_status is not None:
            st.write("Status Code:", response_status)
        st.code(response_data, language='json')
        try:
            st.json(json.loads(response_data))
        except:
            st.warning("⚠️ ไม่สามารถแสดงผลแบบ JSON ได้")
