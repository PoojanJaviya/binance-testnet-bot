from typing import Optional
from bot.validators import validate_price, validate_quantity, validate_side
from bot.client import BinanceFuturesClient

def place_order(
      symbol : str,
      side : str,
      order_type : str,
      quantity : float,
      price : Optional[float]  
): 
    side = validate_side(side=side)
    quantity = validate_quantity(quantity=quantity)
    
    price = validate_price(order_type=order_type, price=price)

    client_wrapper = BinanceFuturesClient()
    api_client = client_wrapper.client

    try:
        if order_type == 'MARKET':
            response = api_client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        else:
            response = api_client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity, price=price, timeInForce="GTC")

        print(response)

    except Exception as e:
        print(e)
    
    api_client.close_connection()

place_order("BTCUSDT", "BUY", "LIMIT", 3, 1000)
