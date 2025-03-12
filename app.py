import streamlit as st
import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    if strength_score == 5:
        return "Very Strong", "🟢"
    elif strength_score >= 3:
        return "Strong", "🟡"
    elif strength_score >= 2:
        return "Moderate", "🟠"
    else:
        return "Weak", "🔴"

def main():
    st.set_page_config(
        page_title="Advanced Password Strength Checker",
        page_icon="🔒",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
            color: #000000;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput>div>div>input {
            color: #000000;
            background-color: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #f0f0f0;
            color: #000000;
            border-radius: 10px;
            padding: 10px 24px;
            font-size: 16px;
            border: 1px solid #cccccc;
            transition: background-color 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #e0e0e0;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: rgba(240, 240, 240, 0.9);
            color: #000000;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            box-shadow: 0 -4px 6px rgba(0, 0, 0, 0.1);
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #000000;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
        .subheader {
            font-size: 20px;
            color: #000000;
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
        .criteria {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title">🔒 Advanced Password Strength Checker</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Check the strength of your password using advanced criteria.</div>', unsafe_allow_html=True)

    with st.form("password_form"):
        password = st.text_input("Enter your password:", type="password")
        submitted = st.form_submit_button("Check Strength")

    if submitted and password:
        strength, icon = check_password_strength(password)
        st.write(f"**Password Strength:** {strength} {icon}")

        st.markdown('<div class="criteria">', unsafe_allow_html=True)
        st.subheader("Password Criteria:")
        st.markdown(
            f"""
            - Length >= 8 characters: {"✅" if len(password) >= 8 else "❌"}
            - Contains uppercase letters: {"✅" if re.search(r'[A-Z]', password) else "❌"}
            - Contains lowercase letters: {"✅" if re.search(r'[a-z]', password) else "❌"}
            - Contains digits: {"✅" if re.search(r'[0-9]', password) else "❌"}
            - Contains special characters: {"✅" if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) else "❌"}
            """
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown(
        '<div class="footer">💻 Developed by Gini</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()