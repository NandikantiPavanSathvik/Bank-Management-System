import streamlit as st


def show_navbar():

    html = """
<div class="bank-header">
<div class="bank-logo">🏦</div>

<div>
<h1>PavanBank</h1>
<p>Simple, Secure & Reliable Banking</p>
</div>
</div>
"""

    st.markdown(html, unsafe_allow_html=True)