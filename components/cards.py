import streamlit as st


def stat_card(
    icon,
    title,
    value
):

    st.markdown(
        f"""
        <div class="stat-card">

            <div class="stat-icon">
                {icon}
            </div>

            <div class="stat-title">
                {title}
            </div>

            <div class="stat-value">
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def account_card(account):

    st.markdown(
        f"""
        <div class="account-card">

            <div class="account-number">
                ACCOUNT NUMBER
            </div>

            <div>
                {account["accountNo."]}
            </div>

            <div class="account-name">
                {account["name"]}
            </div>

            <div class="account-balance">
                ₹{account["balance"]:,}
            </div>

            <div>
                Available Balance
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )