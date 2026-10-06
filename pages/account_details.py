import streamlit as st

from components.cards import account_card


def show_account_details(bank):

    st.title("Account Details")

    st.write(
        "View your account information securely."
    )

    account_number = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "PIN",
        type="password"
    )

    if st.button(
        "View Account",
        use_container_width=True
    ):

        success, result = bank.get_account(
            account_number,
            pin
        )

        if success:

            account_card(result)

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Name:** {result['name']}"
                )

                st.write(
                    f"**Age:** {result['age']}"
                )

            with col2:

                st.write(
                    f"**Email:** {result['email']}"
                )

                st.write(
                    f"**Account Number:** "
                    f"{result['accountNo.']}"
                )

        else:

            st.error(result)