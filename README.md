# 📈 Portfolio Return Calculator

This is a simple Python project that calculates the performance of a stock portfolio using historical stock prices. It shows:

- Daily and annual portfolio returns  
- Annual volatility  
- Sharpe ratio  
- Portfolio value growth over time

Built with: `pandas`, `numpy`, `matplotlib`, and `yfinance`.

---

## ⚙️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/your-username/portfolio-return-calculator.git
cd portfolio-return-calculator
```

2. (Optional) Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
python main.py
```

---

## 📊 How It Works

- Downloads stock data using `yfinance`
- Calculates daily returns:  
  ![Return formula](https://latex.codecogs.com/png.latex?\bg{white}\text{Return}=\frac{P_t-P_{t-1}}{P_{t-1}})



- Calculates portfolio return:  
  Weighted sum of individual stock returns
- Calculates:
  - **Annual Return** = daily avg × 252  
  - **Volatility** = std dev × √252  
  - **Sharpe Ratio** = return / volatility
- Plots portfolio value over time
  ![image](https://github.com/user-attachments/assets/ff695bc9-c592-44c9-bd91-479171a6a3ac)


---

## ✨ Example

If you invest 50% in AAPL, 30% in MSFT, and 20% in TSLA, this script will show:

- Total return %
- Risk (volatility)
- Sharpe ratio
- Growth plot

---

## 📌 Notes

- Uses adjusted close prices
- You can edit `tickers` and `weights` in `main.py`
- Works offline once data is downloaded

---

## 🔧 Future Ideas

- Add benchmarks (e.g., S&P 500)
- GUI or web interface
- Export results to PDF/Excel
