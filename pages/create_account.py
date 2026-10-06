import streamlit as st


def show_create_account(bank):

    st.title("Create Account")

    st.write(
        "Open a new bank account."
    )

    st.markdown("---")

    with st.form("create_account_form"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Full Name",
                placeholder="Enter your full name"
            )

            age = st.number_input(
                "Age",
                min_value=1,
                max_value=120,
                value=18
            )

        with col2:

            email = st.text_input(
                "Email",
                placeholder="example@email.com"
            )

            pin = st.text_input(
                "4 Digit PIN",
                type="password",
                max_chars=4
            )

        st.markdown("<br>", unsafe_allow_html=True)

        submit = st.form_submit_button(
            "Create Account",
            use_container_width=True
        )

    if submit:

        success, result = bank.create_account(
            name,
            age,
            email,
            pin
        )

        if success:

            st.success(
                "Account created successfully!"
            )

            st.markdown(
                f"""
                ### 🎉 Welcome, {result["name"]}!

                **Your Account Number**

                ## `{result["accountNo."]}`

                Please save your account number
                for future transactions.
                """
            )

        else:

            st.error(result)