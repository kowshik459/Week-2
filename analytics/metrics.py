import pandas as pd
import numpy as np

def compute_vwap(trades):
    if len(trades) == 0:
        return None
    df = pd.DataFrame(trades)
    return (df["price"] * df["quantity"]).sum() / df["quantity"].sum()

def compute_average_spread(snapshots):
    spreads = [s["spread"] for s in snapshots if s["spread"] is not None]
    if not spreads:
        return None
    return sum(spreads) / len(spreads)

def compute_volatility(snapshots, window=10):
    prices = [s["mid_price"] for s in snapshots if s["mid_price"] is not None]
    if len(prices) < window:
        return None
    returns = np.diff(np.log(prices))
    return np.std(returns)
