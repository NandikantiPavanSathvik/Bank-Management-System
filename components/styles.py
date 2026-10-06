import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* =========================
           GLOBAL
        ========================= */

        .stApp {
            background-color: #f5f7fb;
        }

        .main {
            padding-top: 1rem;
        }

        /* =========================
           SIDEBAR
        ========================= */

        [data-testid="stSidebar"] {
            background-color: #111827;
        }

        [data-testid="stSidebar"] * {
            color: white;
        }

        /* =========================
           HEADER
        ========================= */

        .bank-header {
            background: linear-gradient(
                135deg,
                #111827,
                #1e3a8a
            );

            padding: 25px 30px;

            border-radius: 18px;

            margin-bottom: 25px;

            color: white;

            box-shadow:
                0 10px 30px
                rgba(0, 0, 0, 0.12);
        }

        .bank-header h1 {
            margin: 0;
            font-size: 32px;
        }

        .bank-header p {
            margin-top: 8px;
            opacity: 0.8;
        }

        /* =========================
           STAT CARDS
        ========================= */

        .stat-card {

            background: white;

            padding: 22px;

            border-radius: 16px;

            border: 1px solid #e5e7eb;

            box-shadow:
                0 5px 20px
                rgba(0, 0, 0, 0.05);

            min-height: 120px;
        }

        .stat-title {

            color: #6b7280;

            font-size: 14px;

            margin-bottom: 10px;
        }

        .stat-value {

            color: #111827;

            font-size: 28px;

            font-weight: 700;
        }

        .stat-icon {

            font-size: 28px;

            margin-bottom: 5px;
        }

        /* =========================
           ACCOUNT CARD
        ========================= */

        .account-card {

            background:
                linear-gradient(
                    135deg,
                    #111827,
                    #2563eb
                );

            padding: 28px;

            border-radius: 20px;

            color: white;

            box-shadow:
                0 10px 25px
                rgba(37, 99, 235, 0.25);

            margin-bottom: 20px;
        }

        .account-number {

            font-size: 14px;

            opacity: 0.75;
        }

        .account-name {

            font-size: 24px;

            font-weight: 700;

            margin-top: 15px;
        }

        .account-balance {

            font-size: 34px;

            font-weight: 700;

            margin-top: 25px;
        }

        /* =========================
           SECTION
        ========================= */

        .section-title {

            font-size: 22px;

            font-weight: 700;

            color: #111827;

            margin-top: 25px;

            margin-bottom: 15px;
        }

        /* =========================
           BUTTONS
        ========================= */

        .stButton > button {

            border-radius: 10px;

            border: none;

            font-weight: 600;

            min-height: 42px;
        }

        /* =========================
           INPUTS
        ========================= */

        input {

            border-radius: 10px !important;
        }

        /* =========================
           FOOTER
        ========================= */

        .footer {

            text-align: center;

            color: #6b7280;

            padding: 30px;

            font-size: 13px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )