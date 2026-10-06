import streamlit as st


def show_withdraw(bank):

    st.title("Withdraw Money")

    st.write(
        "Withdraw money from your bank account."
    )

    st.markdown("---")

    account_number = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "PIN",
        type="password"
    )

    amount = st.number_input(
        "Withdrawal Amount",
        min_value=0,
        step=100
    )

    if st.button(
        "💸 Withdraw Money",
        use_container_width=True
    ):

        success, result = bank.withdraw(
            account_number,
            pin,
            amount
        )

        if success:

            st.success(
                f"₹{amount:,} withdrawn successfully!"
            )

            st.metric(
                "Remaining Balance",
                f"₹{result:,}"
            )

        else:

            st.error(result)