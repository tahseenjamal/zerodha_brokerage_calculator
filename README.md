# Zerodha Brokerage Calculator

A Python script that replicates the [Zerodha Brokerage Calculator](https://zerodha.com/brokerage-calculator) for all four segments: **Intraday**, **Delivery**, **Futures**, and **Options**.

---

## Charges Calculated

| Charge | Description |
|---|---|
| **Brokerage** | ₹20 or 0.03% per executed order (whichever is lower); ₹0 for delivery; flat ₹20/order for options |
| **STT** | Securities Transaction Tax — 0.025% on sell (intraday), 0.1% on both sides (delivery), 0.01% on sell (futures), 0.05% on sell (options) |
| **Exchange Transaction Charge** | NSE charges based on segment turnover |
| **DP Charges** | ₹15.93 per scrip per day (delivery sell only) |
| **GST** | 18% on brokerage + exchange transaction charges |
| **SEBI Charges** | ₹10 per crore of turnover + 18% GST |
| **Stamp Duty** | On buy-side value, varies by segment |
| **Total Charges** | Sum of all the above |
| **Breakeven** | Minimum price movement per share needed to cover all charges |
| **Net Profit** | `(sell_price − buy_price) × qty − total_charges` |

---

## Charge Rates by Segment

| Charge | Intraday | Delivery | Futures | Options |
|---|---|---|---|---|
| Brokerage | 0.03% or ₹20 max | ₹0 | 0.03% or ₹20 max | ₹20 flat/order |
| STT | 0.025% (sell) | 0.1% (both) | 0.01% (sell) | 0.05% (sell) |
| Exchange TXN | 0.00345% | 0.00345% | 0.002% | 0.053% |
| Stamp Duty | 0.003% | 0.015% | 0.002% | 0.003% |
| DP Charges | — | ₹15.93 | — | — |

---

## Usage

```python
from brokerage import calculate_brokerage

# calculate_brokerage(buy_price, sell_price, quantity, segment)
calculate_brokerage(100, 110, 400, 'intra')      # Intraday
calculate_brokerage(100, 110, 400, 'delivery')   # Equity delivery
calculate_brokerage(100, 110, 400, 'futures')    # F&O Futures
calculate_brokerage(100, 110, 400, 'options')    # F&O Options
```

### Segment keys

| Key | Segment |
|---|---|
| `intra` | Intraday equity |
| `delivery` | Equity delivery (CNC) |
| `futures` | F&O — Futures |
| `options` | F&O — Options |

### Run the sample

```bash
python brokerage.py
```

---

## Sample Output

```
--- INTRA ---
Turnover          : 84000
Brokerage         : 25.2
STT               : 11
Exc Trans Charge  : 2.9
CC                : 0
GST               : 5.06
SEBI Charges      : 0.1
Stamp Duty        : 1
Total Charges     : 45.26
Breakeven (per share): 0.11
Net Profit        : 3954.74

--- DELIVERY ---
Turnover          : 84000
Brokerage         : 0.0
STT               : 84
Exc Trans Charge  : 2.9
DP                : 15.93
GST               : 0.52
SEBI Charges      : 0.1
Stamp Duty        : 6
Total Charges     : 109.45
Breakeven (per share): 0.27
Net Profit        : 3890.55

--- FUTURES ---
Turnover          : 84000
Brokerage         : 25.2
STT               : 4
Exc Trans Charge  : 1.68
CC                : 0
GST               : 4.84
SEBI Charges      : 0.1
Stamp Duty        : 1
Total Charges     : 36.82
Breakeven (per share): 0.09
Net Profit        : 3963.18

--- OPTIONS ---
Turnover          : 84000
Brokerage         : 40.0
STT               : 22
Exc Trans Charge  : 44.52
CC                : 0
GST               : 15.21
SEBI Charges      : 0.1
Stamp Duty        : 1
Total Charges     : 122.83
Breakeven (per share): 0.31
Net Profit        : 3877.17
```

---

## Requirements

- Python 3.6+ (uses f-strings)
- No external dependencies
