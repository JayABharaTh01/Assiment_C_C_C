import os
from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import glob


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

st.set_page_config(page_title="Customer Service Dashboard", page_icon="📊", layout="wide")

with open(ROOT / "streamlit_ui" / "styles.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def load_data():
    customers = pd.read_csv(DATA_DIR / "customers.csv")
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    returns = pd.read_csv(DATA_DIR / "returns.csv")
    tickets = pd.read_csv(DATA_DIR / "support_tickets.csv")

    for df in [customers, orders, returns, tickets]:
        for col in df.columns:
            if "date" in col.lower() or "created" in col.lower() or "signup" in col.lower():
                df[col] = pd.to_datetime(df[col], errors="coerce")

    return customers, orders, returns, tickets


customers, orders, returns, tickets = load_data()

st.title("📊 Customer Service Intelligence Dashboard")
st.caption("Interactive temporary dashboard for exploring customer, order, return, and support ticket data")

# ==========================================================
# Asset slideshow (optional)
# ==========================================================
assets_dir = Path(__file__).resolve().parent / "assets"
images = []
if assets_dir.exists():
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.gif"):
        images.extend(sorted(glob.glob(str(assets_dir / ext))))

if images:
    st.sidebar.markdown("### Dashboard references")
    img_index = st.sidebar.slider("Slide", 0, max(0, len(images) - 1), 0)
    try:
        img = Image.open(images[img_index])
        st.sidebar.image(img, use_column_width=True)
    except Exception:
        st.sidebar.write("Unable to load preview image")
else:
    st.sidebar.markdown("### Dashboard references")
    st.sidebar.info("Drop dashboard screenshots into streamlit_ui/assets/ to preview them here.")

with st.sidebar:
    st.header("Filters")
    selected_segment = st.selectbox(
        "Customer Segment",
        ["All"] + sorted(customers["segment"].dropna().astype(str).unique().tolist()),
    )
    selected_status = st.selectbox(
        "Order Status",
        ["All"] + sorted(orders["status"].dropna().astype(str).unique().tolist()),
    )
    selected_priority = st.selectbox(
        "Ticket Priority",
        ["All"] + sorted(tickets["priority"].dropna().astype(str).unique().tolist()),
    )

    st.markdown("---")
    st.info("This UI is designed as a temporary interactive layer for the existing project data.")


# Basic filtering
filtered_customers = customers.copy()
filtered_orders = orders.copy()
filtered_returns = returns.copy()
filtered_tickets = tickets.copy()

if selected_segment != "All":
    filtered_customers = filtered_customers[filtered_customers["segment"] == selected_segment]
    customer_ids = filtered_customers["customer_id"]
    filtered_orders = filtered_orders[filtered_orders["customer_id"].isin(customer_ids)]
    filtered_returns = filtered_returns[filtered_returns["customer_id"].isin(customer_ids)]
    filtered_tickets = filtered_tickets[filtered_tickets["customer_id"].isin(customer_ids)]

if selected_status != "All":
    filtered_orders = filtered_orders[filtered_orders["status"] == selected_status]

if selected_priority != "All":
    filtered_tickets = filtered_tickets[filtered_tickets["priority"] == selected_priority]


col1, col2, col3, col4 = st.columns(4)
col1.metric("Customers", f"{len(filtered_customers):,}")
col2.metric("Orders", f"{len(filtered_orders):,}")
col3.metric("Returns", f"{len(filtered_returns):,}")
col4.metric("Support Tickets", f"{len(filtered_tickets):,}")

st.markdown("---")

left_col, right_col = st.columns(2)

with left_col:
    status_counts = filtered_orders["status"].value_counts().reset_index()
    status_counts.columns = ["status", "count"]
    fig_orders = px.bar(
        status_counts,
        x="status",
        y="count",
        color="status",
        title="Orders by Status",
    )
    st.plotly_chart(fig_orders, use_container_width=True)

with right_col:
    returns_by_reason = filtered_returns["reason"].value_counts().reset_index()
    returns_by_reason.columns = ["reason", "count"]
    fig_returns = px.pie(
        returns_by_reason,
        names="reason",
        values="count",
        title="Returns by Reason",
    )
    st.plotly_chart(fig_returns, use_container_width=True)


left_col, right_col = st.columns(2)

with left_col:
    ticket_priority = filtered_tickets["priority"].value_counts().reset_index()
    ticket_priority.columns = ["priority", "count"]
    fig_tickets = px.bar(
        ticket_priority,
        x="priority",
        y="count",
        color="priority",
        title="Support Tickets by Priority",
    )
    st.plotly_chart(fig_tickets, use_container_width=True)

with right_col:
    ticket_status = filtered_tickets["status"].value_counts().reset_index()
    ticket_status.columns = ["status", "count"]
    fig_status = px.bar(
        ticket_status,
        x="status",
        y="count",
        color="status",
        title="Support Tickets by Status",
    )
    st.plotly_chart(fig_status, use_container_width=True)


st.markdown("---")

st.subheader("Recent Activity Snapshot")
activity = pd.DataFrame(
    {
        "Category": ["Orders", "Returns", "Tickets"],
        "Count": [len(filtered_orders), len(filtered_returns), len(filtered_tickets)],
    }
)
fig_activity = px.bar(activity, x="Category", y="Count", color="Category", title="Snapshot")
st.plotly_chart(fig_activity, use_container_width=True)
