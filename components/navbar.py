import streamlit as st


def show_navbar():

    st.markdown(
        """
        <div class="bank-header">

            <h1>🏦 PavanBank</h1>

            <p>
                Secure. Simple. Smart banking management.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )