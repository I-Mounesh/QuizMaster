import streamlit as st

# --- Initialize user data ---
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {"password": "admin123"}
    }

# --- Custom Background and Style ---
def add_background_and_style():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            font-family: 'Arial', sans-serif;
        }

        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: white;
            text-align: center;
            padding: 1rem;
            text-shadow: 1px 1px 2px black;
        }

        

        label, input {
            font-size: 16px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- App Interface ---
add_background_and_style()
st.markdown("<h1 class='main-title'>Journey To Become Quiz Wizard </h1>", unsafe_allow_html=True)

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

with st.container():
    st.markdown("<div class='box'>", unsafe_allow_html=True)

    if menu == "Login":
        st.subheader("🔐 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.button("Login")
        
        if login_btn==True:
            st.switch_page("pages/1_App.py")

        if login_btn:
            if username in st.session_state.users and st.session_state.users[username]["password"] == password:
                st.success(f"Welcome, **{username}**!")
                st.balloons()
                st.markdown("### 🎉 You are now logged in.")
            else:
                st.error("Invalid username or password.")

    elif menu == "Register":
        st.subheader("📝 Register")
        new_user = st.text_input("Choose a Username")
        new_pass = st.text_input("Choose a Password", type="password")
        register_btn = st.button("Register")

        if register_btn:
            if new_user in st.session_state.users:
                st.warning("Username already exists. Please choose another.")
            elif new_user == "" or new_pass == "":
                st.warning("Username and password cannot be empty.")
            else:
                st.session_state.users[new_user] = {"password": new_pass}
                st.success("Registered successfully! Please login now.")

    st.markdown("</div>", unsafe_allow_html=True)
