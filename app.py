import streamlit as st

st.title('Hello world, This is my first web page application')
st.markdown('---')
st.text_input('Enter the name:')
st.number_input('Enter the age:',min_value = 5,max_value = 105)
st.selectbox('Gender:',options = ['Male','Female','Others'])
st.radio('Maritial status',options = ['Single','Married','Separated'])
st.multiselect('Meal:',options = ['Vada Pav','Misal','Pav Bhaji','Pulav'],
               max_selections = 2)
st.feedback(options = 'stars')
st.segmented_control('Coach',options = ['3Tier','2Tier','Firstclass','General'])

st.date_input('From Date:')
st.time_input('Board Time')

st.date_input('To Date:')
st.time_input('End Journey Time:')

st.button('Click me')



import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Train Booking",
    page_icon="🚆",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main-title {
        font-size: 36px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 45px;
        font-size: 16px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🚆 Train Ticket Booking</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter passenger and journey details</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- FORM ----------------
with st.form("train_booking_form"):

    # ===== PASSENGER DETAILS =====
    st.markdown(
        '<div class="section-title">👤 Passenger Details</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name", placeholder="Enter passenger name")

        age = st.number_input(
            "Age",
            min_value=5,
            max_value=105,
            value=18
        )

    with col2:
        gender = st.selectbox(
            "Gender",
            options=["Male", "Female", "Others"]
        )

        marital_status = st.radio(
            "Marital Status",
            options=["Single", "Married", "Separated"],
            horizontal=True
        )


    st.divider()


    # ===== JOURNEY DETAILS =====
    st.markdown(
        '<div class="section-title">🛤️ Journey Details</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        from_date = st.date_input("From Date")
        board_time = st.time_input("Boarding Time")

    with col2:
        to_date = st.date_input("To Date")
        end_time = st.time_input("End Journey Time")


    st.divider()


    # ===== TRAVEL PREFERENCES =====
    st.markdown(
        '<div class="section-title">🎫 Travel Preferences</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        meal = st.multiselect(
            "Meal Preference",
            options=[
                "Vada Pav",
                "Misal",
                "Pav Bhaji",
                "Pulav"
            ],
            max_selections=2
        )

    with col2:
        coach = st.segmented_control(
            "Coach Type",
            options=[
                "3 Tier",
                "2 Tier",
                "First Class",
                "General"
            ]
        )


    st.divider()


    # ===== FEEDBACK =====
    st.markdown(
        '<div class="section-title">⭐ Feedback</div>',
        unsafe_allow_html=True
    )

    feedback = st.feedback(options="stars")


    st.divider()


    # ===== SUBMIT =====
    submitted = st.form_submit_button(
        "🎟️ Book Ticket"
    )


# ---------------- RESULT ----------------
if submitted:

    st.success("✅ Booking details submitted successfully!")

    st.write("### Booking Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Passenger:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Marital Status:** {marital_status}")

    with col2:
        st.write(f"**From Date:** {from_date}")
        st.write(f"**Boarding Time:** {board_time}")
        st.write(f"**To Date:** {to_date}")
        st.write(f"**End Time:** {end_time}")

    st.write(f"**Meal:** {', '.join(meal) if meal else 'No meal selected'}")
    st.write(f"**Coach:** {coach if coach else 'Not selected'}")