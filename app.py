import streamlit as st

from bank import Bank

from components.styles import load_css
from components.sidebar import show_sidebar
from components.navbar import show_navbar

from views.dashboard import show_dashboard
from views.create_account import show_create_account
from views.account_details import show_account_details
from views.deposit import show_deposit
from views.withdraw import show_withdraw
from views.update_account import show_update_account
from views.delete_account import show_delete_account


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="PavanBank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# LOAD CUSTOM CSS
# ==========================================

load_css()


# ==========================================
# CREATE BANK OBJECT
# ==========================================

bank = Bank()


# ==========================================
# NAVIGATION
# ==========================================

menu = show_sidebar()


# ==========================================
# HEADER
# ==========================================

show_navbar()


# ==========================================
# PAGE ROUTING
# ==========================================

if menu == "Dashboard":

    show_dashboard(bank)


elif menu == "Create Account":

    show_create_account(bank)


elif menu == "Account Details":

    show_account_details(bank)


elif menu == "Deposit Money":

    show_deposit(bank)


elif menu == "Withdraw Money":

    show_withdraw(bank)


elif menu == "Update Account":

    show_update_account(bank)


elif menu == "Delete Account":

    show_delete_account(bank)


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="footer">
        🏦 PavanBank • Bank Management System
        <br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)