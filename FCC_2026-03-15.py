def get_captured_value(pieces):
    if not "K" in pieces:
        return "Checkmate"
    
    values = {
        "P": 1,
        "R": 5,
        "N": 3,
        "B": 3,
        "Q": 9,
        "K": 0
    }
  
    for piece in pieces:
        if piece not in values:
            raise ValueError(f"Invalid piece code: {piece}")
          
    max_value = 39
    value = sum(values[piece] for piece in pieces) 
    return max_value - value
