import streamlit as st


def show_sidebar():

    st.sidebar.markdown(
        """
        <h2>🏦 PavanBank</h2>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "---"
    )

    menu = st.sidebar.radio(
        "MAIN MENU",
        [
            "Dashboard",
            "Create Account",
            "Account Details",
            "Deposit Money",
            "Withdraw Money",
            "Update Account",
            "Delete Account"
        ]
    )

    st.sidebar.markdown(
        "---"
    )

    st.sidebar.caption(
        "Bank Management System"
    )

    st.sidebar.caption(
        "Python • Streamlit • JSON"
    )

    return menu