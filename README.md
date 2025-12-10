# 📊 Gold Price Analysis Dashboard

### **A Professional Quantitative Finance Project Using Python**

This repository showcases a structured, multi-version analytics pipeline for exploring and visualizing **Gold (XAU/USD)** historical prices using Python. It demonstrates industry-standard techniques used by **Quant Analysts, Algo Traders, and Data Scientists**.

The project evolves from fundamental time-series loading and plotting → into technical indicator computation → and toward complete trading analytics.

---

# 🚀 Project Roadmap

## **✔ Version 1 — Core Time Series Analysis**

* Load historical gold price data from CSV
* Convert Date to datetime format
* Sort and validate time-series
* Plot price trend using Matplotlib
* Produce reproducible analysis output

## **✔ Version 2 — Technical Indicators (SMA & EMA)**

A key upgrade introducing essential quant indicators:

* **SMA (Simple Moving Average)** — 5-day & 10-day
* **EMA (Exponential Moving Average)** — 5-day & 10-day
* Overlaid indicator visualization
* Professional chart layout suitable for reporting

## **➡ Version 3 (Coming Soon)**

* Candlestick (OHLC) charts
* SMA/EMA crossover signals
* Buy/Sell marker visualization
* Trend classification using Moving Average Dashboard

## **➡ Version 4 (Future Work)**

* RSI, MACD, Bollinger Bands
* Volatility indicators (ATR, Standard Deviation)
* Multi-indicator signal engine

## **➡ Version 5 — Interactive Web Dashboard**

* Streamlit-based financial analytics UI
* Upload your own CSV feature
* Auto-generated technical indicator reports

## **➡ Version 6 — Machine Learning Forecasting**

* LSTM neural network model
* Random Forest / XGBoost regression
* Multi-step price prediction

---

# 📁 Repository Structure

```
gold-dashboard/
│
├── gold_price_analysis_v1.py       # Baseline analysis script
├── gold_price_analysis_v2.py       # SMA & EMA indicator analysis
├── historical_gold.csv             # Sample dataset for gold prices
├── Figure_1.png                    # Output chart (Version 1)
├── Figure_2.png                    # Output chart (Version 2)
└── README.md                       # Project documentation
```

---

# 🧠 Technical Concepts Used

### **📌 Simple Moving Average (SMA)**

Calculated as the average of the last *n* closing values. SMA smooths noise and highlights long-term price direction.

### **📌 Exponential Moving Average (EMA)**

Weights recent prices more heavily, making EMA more responsive to new market information.

### **📌 Why These Indicators Matter**

These indicators are foundational tools for:

* Trend identification
* Momentum classification
* Market regime analysis
* Strategy backtesting (SMA/EMA crossovers)

Used heavily in professional quant environments across hedge funds and trading desks.

---

# 📦 Installation

Install dependencies:

```
py -m pip install pandas matplotlib
```

---

# ▶ How to Run the Project

### **Run Version 1:**

```
py gold_price_analysis_v1.py
```

### **Run Version 2:**

```
py gold_price_analysis_v2.py
```

---

# 🖥 Upcoming Deliverables (Will Be Added to Repo)

* `/indicators/` module for reusable technical analysis functions
* `/notebooks/` directory for Jupyter-based quant research
* `/streamlit_app/` for interactive dashboard deployment
* LSTM forecasting code samples

---

# 📌 Professional Summary

This repository reflects the skills required for:

* Quantitative Research Intern / Analyst
* Financial Data Analyst
* Trading Strategy Developer
* Python for Finance Engineer

It demonstrates competency in:

* Time-series engineering
* Financial data cleaning
* Technical indicator computation
* Visualization and chart-based analytics
* Python libraries: **Pandas, Matplotlib, Numpy**

---

# 🙋 Author

**Hemant Verma**
Aspiring Quant Analyst | Data Analyst | Python for Finance Practitioner
GitHub: [https://github.com/hhemant86](https://github.com/hhemant86)

---

If you want, I can also:

* Add GitHub badges (Python version, repo size, license, etc.)
* Add images/diagrams into the README
* Add a "Getting Started" section
* Add examples of indicator signals
* Add a quant project roadmap image

Just say: **"Add badges"**, **"Add images"**, or **"Add getting started section"**.
