"""
SPY Volatility Analysis
- Computes log returns
- Computes rolling volatility (20, 60, 120 days)
- Computes EWMA volatility
- Plots price and volatility comparisons
"""

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime


def main() -> None:
    # Parameters
    ticker = "SPY"
    start_date = datetime(2015, 1, 1)
    trading_days = 252
    lambda_ = 0.94  # EWMA decay factor (RiskMetrics)

    # Download adjusted price data
    price_data = yf.download(
        ticker,
        start=start_date,
        auto_adjust=True,
        progress=False
    )

    prices = price_data["Close"].dropna()

    # Compute log returns
    log_returns = np.log(prices / prices.shift(1)).dropna()

    # Rolling historical volatility (annualized)
    rolling_vol_20 = log_returns.rolling(20).std() * np.sqrt(trading_days)
    rolling_vol_60 = log_returns.rolling(60).std() * np.sqrt(trading_days)
    rolling_vol_120 = log_returns.rolling(120).std() * np.sqrt(trading_days)

    # EWMA volatility (annualized)
    ewma_var = log_returns.pow(2).ewm(
        alpha=1 - lambda_,
        adjust=False
    ).mean()
    ewma_vol = np.sqrt(ewma_var * trading_days)

    # ----------- PLOTS ----------- #

    # Price plot
    plt.figure(figsize=(10, 4))
    plt.plot(prices.index, prices, label="SPY Price")
    plt.title("SPY Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Volatility comparison plot
    plt.figure(figsize=(10, 4))
    plt.plot(
        rolling_vol_20.index,
        rolling_vol_20,
        label="20-Day Rolling Volatility"
    )
    plt.plot(
        rolling_vol_60.index,
        rolling_vol_60,
        label="60-Day Rolling Volatility"
    )
    plt.plot(
        rolling_vol_120.index,
        rolling_vol_120,
        label="120-Day Rolling Volatility"
    )
    plt.plot(
        ewma_vol.index,
        ewma_vol,
        label="EWMA Volatility (λ = 0.94)",
        linestyle="--"
    )

    plt.title("SPY Volatility: Rolling Windows vs EWMA")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()


