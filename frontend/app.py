import streamlit as st
import requests

backend_url = "http://localhost:8000"

st.title("AI-Driven SDR Email Outreach")

# Initialize session state for email draft and optimized email
if 'email_draft' not in st.session_state:
    st.session_state['email_draft'] = None
if 'optimized_email' not in st.session_state:
    st.session_state['optimized_email'] = None

# Step 1: Research
st.header("Step 1: Prospect Research")
prospect_name = st.text_input("Prospect Name")
company_name = st.text_input("Company Name")

if st.button("Get Prospect Research"):
    response = requests.post(f"{backend_url}/research/prospect", json={"prospect_name": prospect_name, "company_name": company_name})
    research_report = response.json().get("research")
    st.write("Research Report:", research_report)
    st.session_state['research_report'] = research_report  # Save to session state

# Step 2: Email Generation
st.header("Step 2: Email Generation")
product_catalog = st.file_uploader("Upload Product Catalog", type=["txt", "pdf"])

if product_catalog and 'research_report' in st.session_state and st.button("Generate Email"):
    files = {'product_catalog': product_catalog}
    data = {'research_report': st.session_state['research_report']}
    response = requests.post(f"{backend_url}/generate/email", files=files, data=data)
    st.session_state['email_draft'] = response.json().get("email")  # Save email draft to session state
    st.write("Generated Email:", st.session_state['email_draft'])

# Step 3: Email Review
st.header("Step 3: Email Review")
email_templates = st.text_area("Paste Successful Email Templates")

if st.session_state['email_draft'] and email_templates and st.button("Optimize Email"):
    response = requests.post(f"{backend_url}/review/optimize", json={
        "generated_email": st.session_state['email_draft'],
        "templates": email_templates
    })
    st.session_state['optimized_email'] = response.json().get("optimized_email")  # Save optimized email to session state
    st.write("Optimized Email:", st.session_state['optimized_email'])

# Step 4: Send Email
st.header("Step 4: Send Email")
recipient_email = st.text_input("Recipient Email")
subject = st.text_input("Email Subject")

if recipient_email and subject and st.session_state['optimized_email'] and st.button("Send Email"):
    response = requests.post(f"{backend_url}/send/send", json={
        "recipient_email": recipient_email,
        "subject": subject,
        "body": st.session_state['optimized_email']
    })
    st.write(response.json().get("status"))
