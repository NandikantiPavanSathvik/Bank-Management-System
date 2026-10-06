import streamlit as st


def show_update_account(bank):

    st.title("Update Account")

    st.write(
        "Update your personal account information."
    )

    st.markdown("---")

    account_number = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "Current PIN",
        type="password"
    )

    st.subheader("New Information")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "New Name",
            placeholder="Leave blank to keep current name"
        )

    with col2:

        email = st.text_input(
            "New Email",
            placeholder="Leave blank to keep current email"
        )

    new_pin = st.text_input(
        "New PIN",
        type="password",
        max_chars=4,
        placeholder="Leave blank to keep current PIN"
    )

    if st.button(
        "✏️ Update Account",
        use_container_width=True
    ):

        success, result = bank.update_account(
            account_number,
            pin,
            name,
            email,
            new_pin
        )

        if success:

            st.success(
                "Account updated successfully!"
            )

        else:

            st.error(result)