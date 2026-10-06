import streamlit as st


def show_delete_account(bank):

    st.title("Delete Account")

    st.warning(
        "⚠️ Account deletion is permanent and "
        "cannot be undone."
    )

    account_number = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "PIN",
        type="password"
    )

    confirm = st.checkbox(
        "I understand that my account will be permanently deleted."
    )

    if st.button(
        "🗑️ Delete Account",
        use_container_width=True
    ):

        if not confirm:

            st.warning(
                "Please confirm account deletion."
            )

            return

        success, result = bank.delete_account(
            account_number,
            pin
        )

        if success:

            st.success(result)

        else:

            st.error(result)