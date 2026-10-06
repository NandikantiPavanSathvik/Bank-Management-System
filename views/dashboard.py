import streamlit as st

from components.cards import stat_card


def show_dashboard(bank):

    st.title("Dashboard")

    st.write(
        "Welcome back! Here's your banking overview."
    )

    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )

    total_accounts = len(bank.data)

    total_balance = sum(
        account["balance"]
        for account in bank.data
    )

    active_accounts = len(
        [
            account
            for account in bank.data
            if account["balance"] >= 0
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        stat_card(
            "👥",
            "Total Accounts",
            total_accounts
        )

    with col2:

        stat_card(
            "💰",
            "Total Balance",
            f"₹{total_balance:,}"
        )

    with col3:

        stat_card(
            "🟢",
            "Active Accounts",
            active_accounts
        )

    st.markdown(
        "<div class='section-title'>Recent Accounts</div>",
        unsafe_allow_html=True
    )

    if not bank.data:

        st.info(
            "No accounts have been created yet."
        )

        return

    display_data = []

    for account in bank.data:

        display_data.append(
            {
                "Account Number":
                    account["accountNo."],

                "Name":
                    account["name"],

                "Email":
                    account["email"],

                "Balance":
                    f"₹{account['balance']:,}"
            }
        )

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )