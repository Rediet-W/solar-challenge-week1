# 🌞 Solar Challenge Week 1

**MoonLight Energy Solutions** – Solar-data EDA, cross-country comparison & interactive dashboard.

---

## 📂 Project Structure

```
solar-challenge-week1/
├── .github/
│   └── workflows/ci.yml       # CI: pip install & smoke test
├── app/
│   └── main.py                # Streamlit dashboard
├── data/                      # (gitignored) raw & cleaned CSVs
│   ├── benin-malanville.csv
│   ├── benin-malanville_clean.csv
│   ├── sierraleone_clean.csv
│   ├── sierraleone-bumbuna.csv
│   ├── togo_clean.csv
│   └── togo-dapanong_qc.csv
├── dashboard_screenshots/     # final dashboard images
├── src/
│   └──  notebooks/
│       ├── benin_eda.ipynb
│       ├── sierraleone_eda.ipynb
│       ├── togo_eda.ipynb
│       └── compare_countries.ipynb
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Environment Setup

1. **Clone & enter**
   ```bash
   git clone git@github.com:Rediet-W/solar-challenge-week1.git
   cd solar-challenge-week1
   ```
2. **Create & activate venv**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate       # Windows: .\.venv\Scripts\Activate.ps1
   ```
3. **Install deps**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. **CI**
   - Every push to `main` runs GitHub Actions (`.github/workflows/ci.yml`) which installs requirements and runs a smoke test.

---

## 📊 Notebooks & EDA

- **Benin**: `src/notebooks/benin_eda.ipynb`
- **Sierra Leone**: `src/notebooks/sierraleone_eda.ipynb`
- **Togo**: `src/notebooks/togo_eda.ipynb`
- **Cross-Country**: `src/notebooks/compare_countries.ipynb`

Each notebook contains:

1. Data loading & summary stats
2. Missing-value & outlier detection
3. Time-series & cleaning-impact plots
4. Correlation heatmap & scatter analyses
5. EDA observations & cleaned CSV export (`data/*_clean.csv`)

---

## 🌐 Dashboard

To run locally

```bash
streamlit run app/main.py
```

**Features:**

- Sidebar widgets:
  - Country multi-select
  - Date-range picker
- **GHI Boxplot** by country
- **Monthly avg GHI** time-series
- **Avg GHI ranking** table

Screenshots in `dashboard_screenshots/`.
