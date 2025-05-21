import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Load cleaned data once ---
@st.cache_data
def load_data():
    benin = pd.read_csv("data/benin-malanville_clean.csv", parse_dates=["Timestamp"])
    sierra = pd.read_csv("data/sierraleone_clean.csv", parse_dates=["Timestamp"])
    togo  = pd.read_csv("data/togo_clean.csv", parse_dates=["Timestamp"])
    benin["Country"]  = "Benin"
    sierra["Country"] = "Sierra Leone"
    togo["Country"]   = "Togo"
    return pd.concat([benin, sierra, togo], ignore_index=True)

df = load_data()

# --- Sidebar controls ---
st.sidebar.title("🌞 Solar Dashboard")
countries = st.sidebar.multiselect(
    "Select countries", 
    options=df["Country"].unique(),
    default=df["Country"].unique()
)
filtered = df[df["Country"].isin(countries)]
# Sidebar: date range
min_date = df["Timestamp"].min().date()
max_date = df["Timestamp"].max().date()

start, end = st.sidebar.date_input(
    "Date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filter by timestamp
filtered = filtered[
    (filtered["Timestamp"].dt.date >= start) &
    (filtered["Timestamp"].dt.date <= end)
]


# Filter data
filtered = df[df["Country"].isin(countries)]

# --- Main page ---
st.title("Solar Irradiance Dashboard")
st.markdown("Explore Global Horizontal Irradiance (GHI) across countries.")

# 1) Boxplot of GHI
fig, ax = plt.subplots(figsize=(6,4))
filtered.boxplot(column="GHI", by="Country", ax=ax)
ax.set_title("GHI by Country")
ax.set_ylabel("GHI (W/m²)")
plt.suptitle("")  # remove the automatic title
st.pyplot(fig)

# Monthly average GHI line chart
st.subheader("Monthly Avg GHI Over Time")
monthly = (
    filtered
    .set_index("Timestamp")
    ["GHI"]
    .resample("M")
    .mean()
)

fig2, ax2 = plt.subplots(figsize=(8, 3))
ax2.plot(monthly.index, monthly.values, marker="o")
ax2.set_xlabel("Month")
ax2.set_ylabel("Avg GHI (W/m²)")
ax2.set_title("")
plt.tight_layout()
st.pyplot(fig2)

# 2) Ranking table: avg GHI
st.subheader("Average GHI Ranking")
ranking = (
    filtered.groupby("Country")["GHI"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
    .rename(columns={"GHI": "Avg GHI (W/m²)"})
)
st.table(ranking.style.format({"Avg GHI (W/m²)": "{:.2f}"}))
