# import streamlit as st


# def stat_card(icon, title, value):

#     html = f"""
# <div class="stat-card">

#     <div class="stat-icon">
#         {icon}
#     </div>

#     <div class="stat-content">

#         <div class="stat-title">
#             {title}
#         </div>

#         <div class="stat-value">
#             {value}
#         </div>

#     </div>

# </div>
# """

#     st.markdown(
#         html,
#         unsafe_allow_html=True
#     )


# def account_card(account):

#     html = f"""
# <div class="account-card">

#     <div class="account-top">

#         <span>
#             🏦 PavanBank
#         </span>

#         <span>
#             ACTIVE
#         </span>

#     </div>


#     <div class="account-label">
#         ACCOUNT NUMBER
#     </div>

#     <div class="account-number">
#         {account["accountNo."]}
#     </div>


#     <div class="account-name">
#         {account["name"]}
#     </div>


#     <div class="account-label">
#         AVAILABLE BALANCE
#     </div>

#     <div class="account-balance">
#         ₹{account["balance"]:,}
#     </div>

# </div>
# """

#     st.markdown(
#         html,
#         unsafe_allow_html=True
#     )


import streamlit as st


def stat_card(icon, title, value):

    html = f"""
<div class="stat-card">
<div class="stat-icon">{icon}</div>
<div class="stat-content">
<div class="stat-title">{title}</div>
<div class="stat-value">{value}</div>
</div>
</div>
"""

    st.markdown(html, unsafe_allow_html=True)


def account_card(account):

    html = f"""
<div class="account-card">
<div class="account-top">
<span>🏦 PavanBank</span>
<span>ACTIVE</span>
</div>

<div class="account-label">ACCOUNT NUMBER</div>
<div class="account-number">{account["accountNo."]}</div>

<div class="account-name">{account["name"]}</div>

<div class="account-label">AVAILABLE BALANCE</div>
<div class="account-balance">₹{account["balance"]:,}</div>
</div>
"""

    st.markdown(html, unsafe_allow_html=True)