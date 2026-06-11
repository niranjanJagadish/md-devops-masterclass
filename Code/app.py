import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Microdegree Portal",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
        .main-title {
            font-size: 42px;
            text-align: center;
            font-weight: bold;
            color: #2E86C1;
        }
        .sub-title {
            text-align: center;
            color: gray;
            font-size: 18px;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }
        .success-box {
            background: #e8f8f5;
            padding: 15px;
            border-radius: 10px;
            border-left: 6px solid #2ecc71;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "registered" not in st.session_state:
    st.session_state.registered = False
    st.session_state.user = {}

# ---------------- HEADER ----------------
st.markdown("<div class='main-title'>🎓 Microdegree Learning Portal</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Register & Unlock Exclusive Projects + Learning Content</div>", unsafe_allow_html=True)

st.write("---")

# ---------------- REGISTRATION FORM ----------------
if not st.session_state.registered:

    st.subheader("📝 Registration Form")

    with st.form("register_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email ID")

        with col2:
            phone = st.text_input("Phone Number")
            course = st.selectbox("Choose Course", [
                "Python Basics",
                "Web Development",
                "Data Analytics",
                "DevOps Beginner"
            ])

        password = st.text_input("Create Password", type="password")

        submit = st.form_submit_button("🚀 Register & Unlock")

    if submit:
        if name and email and phone:
            st.session_state.registered = True
            st.session_state.user = {
                "name": name,
                "email": email,
                "phone": phone,
                "course": course
            }
            st.success("Registration Successful! Redirecting to your dashboard...")
            st.rerun()
        else:
            st.error("Please fill all required fields!")

# ---------------- DASHBOARD AFTER REGISTRATION ----------------
else:
    user = st.session_state.user

    st.markdown(f"""
        <div class='success-box'>
            <h3>🎉 Welcome {user['name']}!</h3>
            <p>You have successfully unlocked Microdegree Learning Dashboard.</p>
            <p><b>Course Selected:</b> {user['course']}</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")

    # ---------------- EXCITING NEWS ----------------
    st.subheader("📰 Exciting News Just For You")

    news_list = [
        "🚀 Microdegree launches AI-powered coding assistant for students!",
        "🔥 New DevOps live project batch starting this week!",
        "🎯 Students now get real-world project certificates instantly!"
    ]

    for n in news_list:
        st.info(n)

    st.write("---")

    # ---------------- YOUTUBE LEARNING SECTION ----------------
    st.subheader("🎬 Unlock Your Free Learning Videos")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.video("https://youtu.be/vfziEr63Q3I?si=QQgPfZzYv-BuKQNU")
        st.caption("Video 1 - Learning Resource")

    with col2:
        st.video("https://youtu.be/EMLd_RLqCXo?si=ZVXnSkRWRoI2Pie2")
        st.caption("Video 2 - Learning Resource")

    with col3:
        st.video("https://youtu.be/Hf-PemTp1sc?si=VMww3PRddfnP2W5q")
        st.caption("Video 3 - Learning Resource")

    st.write("---")

    # ---------------- USER INFO ----------------
    st.subheader("👤 Your Profile")
    st.json(user)

    if st.button("🔒 LougOUt Button"):
        st.session_state.registered = False
        st.session_state.user = {}
        st.rerun()