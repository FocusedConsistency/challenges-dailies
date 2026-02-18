from decimal import Decimal, ROUND_HALF_UP
def calculate_start_delays(jump_scores):
    DELAY_CONST = 1.5
    best = max(jump_scores)
    delays = []
    for x in jump_scores:
        diff = Decimal(str(best)) - Decimal(str(x))
        delay_decimal = diff * Decimal(str(DELAY_CONST))
        delay = delay_decimal.quantize(Decimal('1'), rounding=ROUND_HALF_UP) 
        print(delay)
        delays.append(delay)
    return delays
