def calculate_brokerage(bp, sp, qty, typ):
    """
    Calculate Zerodha brokerage and statutory charges.

    Args:
        bp  : Buy price per unit
        sp  : Sell price per unit
        qty : Quantity
        typ : Segment — 'intra', 'delivery', 'futures', 'options'
    """
    BROKERAGE_FACTOR = {'intra': 1, 'delivery': 0, 'futures': 1, 'options': 0}
    BROKERAGE_CONST  = {'intra': 0, 'delivery': 0, 'futures': 0, 'options': 40}
    STT_FACTOR       = {'intra': 0.00025,   'delivery': 0.001,     'futures': 0.0001,  'options': 0.0005}
    EXC_FACTOR       = {'intra': 0.0000345, 'delivery': 0.0000345, 'futures': 0.00002, 'options': 0.00053}
    STAMP_FACTOR     = {'intra': 0.00003,   'delivery': 0.00015,   'futures': 0.00002, 'options': 0.00003}

    broker_fee = (
        round(min(bp * qty * 0.0003, 20) + min(sp * qty * 0.0003, 20), 2)
        * BROKERAGE_FACTOR[typ]
        + BROKERAGE_CONST[typ]
    )

    turnover         = round((bp + sp) * qty, 2)
    stt              = int(round(((typ == 'delivery') * bp + sp) * qty * STT_FACTOR[typ], 2))
    exc_trans_charge = round(EXC_FACTOR[typ] * turnover, 2)
    dp_charges       = 15.93 if typ == 'delivery' else 0
    gst              = round(0.18 * (broker_fee + exc_trans_charge), 2)
    sebi_charges     = round(turnover * 0.000001 * 1.18, 2)
    stamp_charges    = int(round(bp * qty * STAMP_FACTOR[typ], 0))

    total_charges = round(
        broker_fee + stt + exc_trans_charge + dp_charges + gst + sebi_charges + stamp_charges, 2
    )
    breakeven  = round(total_charges / qty, 2) if qty else 0
    net_profit = round((sp - bp) * qty - total_charges, 2)

    label = 'DP' if typ == 'delivery' else 'CC'
    print(f"Turnover          : {turnover}")
    print(f"Brokerage         : {broker_fee}")
    print(f"STT               : {stt}")
    print(f"Exc Trans Charge  : {exc_trans_charge}")
    print(f"{label:<18}: {dp_charges}")
    print(f"GST               : {gst}")
    print(f"SEBI Charges      : {sebi_charges}")
    print(f"Stamp Duty        : {stamp_charges}")
    print(f"Total Charges     : {total_charges}")
    print(f"Breakeven (per share): {breakeven}")
    print(f"Net Profit        : {net_profit}")


if __name__ == '__main__':
    segments = ['intra', 'delivery', 'futures', 'options']
    for seg in segments:
        print(f"\n--- {seg.upper()} ---")
        calculate_brokerage(100, 110, 400, seg)
