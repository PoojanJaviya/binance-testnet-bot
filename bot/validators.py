def validate_side(side: str) -> str:
    side_upper = side.upper()
    if side_upper not in ['BUY', 'SELL']:
        raise ValueError(...)
    return side_upper

def validate_quantity(quantity: float) -> float:
    if quantity > 0:
        return quantity
    else:
        raise ValueError(...)
    
def validate_price(price: float, order_type: str) -> float | None:
    order_type = order_type.upper()
    if order_type not in ['MARKET','LIMIT']:
        raise ValueError(...)
    if order_type == "MARKET":
        return None
    elif order_type == "LIMIT":
        if price > 0:
            return price
        else:
            raise ValueError(...)
        
