import streamlit as st
import pandas as pd
import plotly.express as px
import time

# -----------------------------
# APP CONFIG
# -----------------------------
st.set_page_config(
    page_title="MTA | Mineral Trading Africa",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# SIDEBAR NAV
# -----------------------------
st.sidebar.title("MTA DEMO")
st.sidebar.caption("Phase 1 – Shareholder Demo")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🏢 About",
        "📦 Mineral Deals",
        "⚡ Spot Deals & Bidding",
        "🤝 Consulting",
        "🏦 Banking & Risk",
        "👤 Membership",
        "🛠 Admin Back Office",
        "📊 Analytics",
        "🧭 Order Life Cycle"
    ]
)

# -----------------------------
# HOME
# -----------------------------
if page == "🏠 Home":
    st.title("Africa’s Transparent Mineral Bidding & Trading Platform")

    st.subheader("The Problem")
    st.write("""
    • Fragmented mineral trade  
    • High fraud & counterparty risk  
    • No price discovery  
    • Slow deal execution  
    """)

    st.subheader("Our Solution")
    st.write("""
    A **buyer-centric digital marketplace** with:
    - Verified suppliers
    - Escrow & block fund logic
    - Structured bidding & consulting workflows
    """)

    st.success("This demo proves the problem, solution credibility, and scalability.")

# -----------------------------
# ABOUT
# -----------------------------
if page == "🏢 About":
    st.header("About MTA")
    st.write("""
    Mineral Trading Africa (MTA) is designed to become **Africa’s trusted mineral marketplace**.
    
    Positioned against:
    - Laprecio
    - B2BMineral
    - MineralDex
    
    Our advantage:
    **Trust + Process + Buyer Control**
    """)

# -----------------------------
# MINERAL LISTINGS
# -----------------------------
if page == "📦 Mineral Deals":
    st.header("Public Mineral Listings (Demo Data)")

    data = [
        ["Copper Cathode", "DRC", 500, "FOB", "Escrow", "2026-02-15", "LME Ref"],
        ["Copper Concentrate", "Zambia", 800, "CIF", "Block Fund", "2026-03-20", "Negotiated"],
        ["Graphite", "Tanzania", 300, "FOB", "Escrow", "2026-04-10", "Spot Bid"],
        ["Coltan", "DRC", 120, "FOB", "Block Fund", "2026-05-05", "Private Deal"]
    ]

    df = pd.DataFrame(
        data,
        columns=[
            "Mineral", "Origin", "Quantity (MT)",
            "Incoterm", "Deposit Type",
            "Shipment Date", "Pricing Note"
        ]
    )

    st.dataframe(df, use_container_width=True)

# -----------------------------
# BIDDING
# -----------------------------
if page == "⚡ Spot Deals & Bidding":
    st.header("Spot Deal Bidding (Simulation)")

    mineral = st.selectbox("Select Mineral", ["Copper Cathode", "Graphite", "Coltan"])
    qty = st.slider("Quantity (MT)", 10, 1000, 100)
    price = st.number_input("Bid Price (USD/MT)", 1000, 15000, step=100)
    incoterm = st.selectbox("Incoterm", ["FOB", "CIF"])

    if st.button("Start Bidding"):
        st.info("Bidding session started...")
        progress = st.progress(0)

        for i in range(1, 6):
            time.sleep(0.5)
            progress.progress(i * 20)

        st.success("🏆 Winning Bid: Your Offer Leads")

# -----------------------------
# CONSULTING
# -----------------------------
if page == "🤝 Consulting":
    st.header("One-on-One Consulting Workflow")

    st.subheader("Buyer Demand")
    buyer_need = st.text_area("Describe Mineral Demand")

    st.subheader("Seller Capability")
    seller_supply = st.text_area("Describe Available Supply")

    if st.button("Submit for Matching"):
        st.success("Status: Matched → Deal in Progress")

# -----------------------------
# BANKING & RISK
# -----------------------------
if page == "🏦 Banking & Risk":
    st.header("Banking & Risk Management (Conceptual)")

    st.markdown("""
    **No live banking integration — demo only**
    """)

    st.write("""
    ### Payment Structures
    • Escrow  
    • Block Fund  
    • SBLC / DLC / MT760 (conceptual)
    """)

    st.code("""
    Buyer → Escrow → Supplier
           ↓
     Conditions Verified
           ↓
        Release Funds
           ↓
         Shipment
    """)

# -----------------------------
# MEMBERSHIP
# -----------------------------
if page == "👤 Membership":
    st.header("Membership & Verification (Mocked)")

    role = st.selectbox("Register As", ["Buyer", "Seller"])
    name = st.text_input("Company Name")

    st.file_uploader("Business License")
    st.file_uploader("Mining Permit / Certificate")
    st.file_uploader("ID / Directors Info")

    if st.button("Submit Application"):
        st.warning("Status: Submitted → Under Review")

# -----------------------------
# ADMIN
# -----------------------------
if page == "🛠 Admin Back Office":
    st.header("Admin Dashboard")

    st.subheader("Supplier Verification")
    st.selectbox("Supplier", ["Zambia Copper Ltd", "DRC Minerals SARL"])
    st.button("Approve Supplier")

    st.subheader("Deal Control")
    st.button("Approve Deal")
    st.button("Pause Bidding")

    st.subheader("Reports")
    st.button("Generate PDF Report (Mock)")

# -----------------------------
# ANALYTICS
# -----------------------------
if page == "📊 Analytics":
    st.header("Demo Analytics")

    chart_data = pd.DataFrame({
        "Metric": ["Active Deals", "Buyers", "Sellers", "Risk-Filtered"],
        "Value": [12, 18, 10, 7]
    })

    fig = px.bar(chart_data, x="Metric", y="Value")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ORDER LIFE CYCLE
# -----------------------------
if page == "🧭 Order Life Cycle":
    st.header("End-to-End Order Life Cycle")

    steps = [
        "Mineral Listing",
        "Bid Submission",
        "Escrow / Block Fund",
        "Admin Approval",
        "Shipment",
        "Deal Completed"
    ]

    for step in steps:
        st.checkbox(step, value=True)
