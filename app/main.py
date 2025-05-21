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
