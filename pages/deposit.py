import streamlit as st


def show_deposit(bank):

    st.title("Deposit Money")

    st.write(
        "Add money to your bank account."
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
        "Deposit Amount",
        min_value=0,
        step=100
    )

    if st.button(
        "💰 Deposit Money",
        use_container_width=True
    ):

        success, result = bank.deposit(
            account_number,
            pin,
            amount
        )

        if success:

            st.success(
                f"₹{amount:,} deposited successfully!"
            )

            st.metric(
                "New Balance",
                f"₹{result:,}"
            )

        else:

            st.error(result)