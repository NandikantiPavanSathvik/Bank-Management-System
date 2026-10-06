import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* =========================================
   GLOBAL
========================================= */

.stApp {
    background-color: #f4f8fc;
    color: #0f172a;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}


/* =========================================
   STREAMLIT TOP HEADER
========================================= */

header[data-testid="stHeader"] {
    background-color: transparent;
}


/* =========================================
   SIDEBAR
========================================= */

[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #dbe7f3;
}

[data-testid="stSidebar"] * {
    color: #1e293b;
}

[data-testid="stSidebar"] h2 {
    color: #1565c0 !important;
    font-weight: 700;
}


/* Sidebar radio buttons */

[data-testid="stSidebar"] label {
    color: #1e293b !important;
}


/* =========================================
   PAGE HEADINGS
========================================= */

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #0f172a !important;
}


/* =========================================
   BANK HEADER
========================================= */

.bank-header {

    display: flex;

    align-items: center;

    gap: 18px;

    background-color: #1565c0;

    padding: 28px 32px;

    border-radius: 16px;

    margin-bottom: 30px;

    color: white;

    box-shadow:
        0 8px 25px
        rgba(21, 101, 192, 0.18);
}


.bank-logo {

    width: 55px;

    height: 55px;

    display: flex;

    align-items: center;

    justify-content: center;

    background-color: white;

    border-radius: 12px;

    font-size: 28px;

    flex-shrink: 0;
}


.bank-header-text h1 {

    color: white !important;

    margin: 0;

    font-size: 30px;

    font-weight: 700;
}


.bank-header-text p {

    color: #e3f2fd !important;

    margin: 5px 0 0;

    font-size: 14px;
}


/* =========================================
   STAT CARDS
========================================= */

.stat-card {

    display: flex;

    align-items: center;

    gap: 16px;

    background-color: #ffffff;

    padding: 22px;

    border-radius: 14px;

    border: 1px solid #dbe7f3;

    min-height: 105px;

    box-shadow:
        0 4px 15px
        rgba(15, 23, 42, 0.05);
}


.stat-icon {

    width: 52px;

    height: 52px;

    display: flex;

    align-items: center;

    justify-content: center;

    background-color: #e8f2ff;

    border-radius: 12px;

    font-size: 25px;

    flex-shrink: 0;
}


.stat-content {
    display: flex;
    flex-direction: column;
}


.stat-title {

    color: #64748b !important;

    font-size: 14px;

    margin-bottom: 5px;
}


.stat-value {

    color: #1565c0 !important;

    font-size: 25px;

    font-weight: 700;
}


/* =========================================
   ACCOUNT CARD
========================================= */

.account-card {

    background-color: #1565c0;

    padding: 28px;

    border-radius: 18px;

    color: white;

    margin-bottom: 25px;

    box-shadow:
        0 8px 25px
        rgba(21, 101, 192, 0.20);
}


.account-top {

    display: flex;

    justify-content: space-between;

    align-items: center;

    font-size: 15px;

    margin-bottom: 30px;

    color: white !important;
}


.account-label {

    font-size: 11px;

    letter-spacing: 1px;

    color: #dbeafe !important;

    margin-bottom: 5px;
}


.account-number {

    font-size: 20px;

    letter-spacing: 2px;

    font-weight: 600;

    color: white !important;

    margin-bottom: 20px;
}


.account-name {

    font-size: 22px;

    font-weight: 600;

    color: white !important;

    margin-bottom: 25px;
}


.account-balance {

    font-size: 30px;

    font-weight: 700;

    color: white !important;
}


/* =========================================
   SECTION TITLE
========================================= */

.section-title {

    color: #0f172a !important;

    font-size: 20px;

    font-weight: 700;

    margin-top: 30px;

    margin-bottom: 15px;
}


/* =========================================
   STREAMLIT TEXT INPUTS
========================================= */

[data-baseweb="input"] {

    background-color: #ffffff !important;

    border-radius: 8px !important;
}


[data-baseweb="input"] input {

    background-color: #ffffff !important;

    color: #0f172a !important;

    -webkit-text-fill-color: #0f172a !important;

    caret-color: #1565c0 !important;

    border-radius: 8px !important;
}


/* Placeholder */

[data-baseweb="input"] input::placeholder {

    color: #64748b !important;

    opacity: 1 !important;

    -webkit-text-fill-color: #64748b !important;
}


/* =========================================
   INPUT LABELS
========================================= */

.stTextInput label,
.stNumberInput label {

    color: #334155 !important;

    font-weight: 500 !important;
}


/* =========================================
   INPUT FOCUS
========================================= */

[data-baseweb="input"]:focus-within {

    border-color: #1565c0 !important;

    box-shadow:
        0 0 0 1px #1565c0 !important;
}


/* =========================================
   NUMBER INPUT
========================================= */

.stNumberInput input {

    background-color: #ffffff !important;

    color: #0f172a !important;

    -webkit-text-fill-color: #0f172a !important;
}


/* Number input buttons */

.stNumberInput button {

    background-color: #1565c0 !important;

    color: white !important;

    border: none !important;
}


/* =========================================
   FORM
========================================= */

[data-testid="stForm"] {

    background-color: transparent;

    border: none;
}


/* =========================================
   BUTTONS
========================================= */

.stButton > button {

    background-color: #1565c0 !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 8px !important;

    min-height: 42px;

    font-weight: 600 !important;
}


.stButton > button:hover {

    background-color: #0d47a1 !important;

    color: #ffffff !important;
}


/* Form submit button */

.stFormSubmitButton > button {

    background-color: #1565c0 !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 8px !important;

    min-height: 42px;

    font-weight: 600 !important;
}


.stFormSubmitButton > button:hover {

    background-color: #0d47a1 !important;

    color: #ffffff !important;
}


/* =========================================
   DATAFRAME
========================================= */

[data-testid="stDataFrame"] {

    border: 1px solid #dbe7f3;

    border-radius: 10px;
}


/* =========================================
   ALERTS
========================================= */

[data-testid="stAlert"] {

    border-radius: 8px;
}


/* =========================================
   FOOTER
========================================= */

.footer {

    text-align: center;

    color: #64748b !important;

    padding: 30px;

    font-size: 13px;
}

</style>
""",
        unsafe_allow_html=True
    )