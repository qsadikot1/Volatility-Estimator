Volatility Estimation and Risk Dynamics in US Equity Markets Project 
By Qasim Sadikot

Overview:
This project was built from scratch to learn how quantitative finance measures market risk and why different volatility models exist.

Using the SPDR S&P 500 ETF (SPY) as a proxy for the US equity market, the project compares multiple volatility estimators to understand how assumptions about time horizon and market memory affect risk estimation.

The focus was on learning fundamentals first, then gradually adding more advanced ideas.

---

How I built the model from scratch:
The project began by understanding the difference between prices and returns.
Rather than modelling prices directly, I used log returns because they measure relative price changes, are additive over time, and are better suited for volatility modelling.

From there, volatility was treated as time-varying risk, not a constant value.
Different estimators were implemented step by step to build intuition about how risk evolves under different assumptions.

---

Volatility Models
Rolling Historic Volatility
Rolling volatility estimates risk by calculating the standard deviation of recent returns over a fixed window.
The choice of window length reflects the **time horizon over which risk is assumed to be stable**.

* 20-day rolling volatility:
  Uses approximately one month of data and reacts quickly to new market information.
  Because each observation carries significant weight, it is well suited for short-term risk estimation, where being responsive to recent shocks is more important than smoothness.
* 60-day rolling volatility:
  Smooths out short-term noise while still responding to changes in market conditions.
  This window represents a medium-term view of risk and is often used when balancing stability and responsiveness.
* 120-day rolling volatility:
  Uses roughly six months of data and assumes that risk evolves slowly over time.
  Individual shocks have less influence, making this estimator stable but slow to react, and more appropriate for **long-term risk assessment and regime-level analysis**.

All rolling estimators assign equal weight to observations within their window, which explains why longer windows respond more slowly to sudden market stress.

---

EWMA Volatility
Exponentially Weighted Moving Average (EWMA) volatility assumes that recent returns are more informative about current risk than older returns.

Instead of using a fixed window EWMA:

* Places greater weight on recent observations
* Gradually down-weights older data rather than discarding it
* Reacts faster than long rolling windows while remaining smoother than very short rolling windows

With a decay factor of λ = 0.94(RiskMetrics standard), EWMA is well suited for dynamic risk management, where timely reaction to changing market conditions is important but excessive noise is undesirable.

---

Results and Interpretation 
Comparing all volatility measures highlights clear trade-offs:

* Short windows react quickly but are noisy
* Long windows are stable but lag shocks
* EWMA provides a compromise between speed and smoothness

During periods of market stress (e.g. the 2020 COVID crash), these differences become especially clear and illustrate volatility clustering.

---

The Relationship between Volatility and Price
In addition to volatility estimation, the project includes a chart tracking the price of SPY over time to provide context for the volatility measures.

Plotting the price series alongside volatility helps highlight the relationship between large price movements and elevated risk. Periods of sharp price declines are often accompanied by spikes in volatility, reflecting increased uncertainty and market stress.

For example, during major market drawdowns (such as the 2020 COVID crash), the price chart shows rapid declines while volatility measures rise sharply. This illustrates the effect of volatility on price movements.

---

Key Takeaways
* Market risk is **not constant** and changes over time
* Volatility estimates depend on assumptions about time horizon and memory
* No single estimator is optimal in all situations
* EWMA is widely used because it balances responsiveness and stability

---

Tools Used
* Python
* NumPy
* Matplotlib
* yfinance
