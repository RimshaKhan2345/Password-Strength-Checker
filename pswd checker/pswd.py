import streamlit as st
import re

#worked for page config!
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

#worked for page style!
st.markdown("""
<style>
   .main{text-align: center;}
   .stTitle title {font-weight: bold; color: #3498db;}
   .stTitle title:hover  {transform: scale(1.3); transition: 2s;}
   .stWriter writer {font-weight: italic; color:rgb(236, 18, 73);}
   .sttext_input{width: 50% !important; margin:auto;} 
   .stButton button{width: 50% !important; background-color: #3498db; color: white; font-size: 18px; padding: 10px 24px; border-radius: 12px; cursor: pointer;}
   .stButton button:hover {background-color:rgb(104, 207, 35)}
   </style>
   """,unsafe_allow_html=True)

#worked for project code!
st.title("🎉Welcome to🎊")
st.title("🔐Password Strength Checker")
st.subheader("✨🔑Let's check the strength of your password")
st.write("📝Enter your password in the text box below and click on the button to check the strength of your password.")

#function to check the strength of the password!
def check_password_strength(password):
    score = 0
    feedback = []

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password length should be at least 8 characters")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character.")

    if score == 4:
        st.success("👍🦾You have a strong password")
    elif score == 3:
        st.info("🚧🤨You have a medium password. You can make it stronger by adding more digits and special characters")
    else:
        st.error("🚩🚨⚠You have a weak password. You can make it stronger by adding more characters, digits, and special characters")

  #feedback

    if feedback:
     with st.expander("📝improvement need in your password"): # for improvement on our password to make it strong!
      for item in feedback:
          st.write(item)
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong and secure🔏")        
    
#worked for Button!
if st.button("Check Password Strength"):
      if password:
       check_password_strength(password)    
      else:
        st.warning("Please enter your password first to check its strength") #show when password is empty!