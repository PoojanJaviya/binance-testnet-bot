from typing import Optional
from bot.validators import validate_price, validate_quantity, validate_side, validate_order_type
from bot.client import BinanceFuturesClient

def place_order(
      symbol : str,
      side : str,
      order_type : str,
      quantity : float,
      price : Optional[float] = None 
): 
    side = validate_side(side=side)
    quantity = validate_quantity(quantity=quantity)
    order_type = validate_order_type(order_type=order_type)
    price = validate_price(order_type=order_type, price=price)

    client_wrapper = BinanceFuturesClient()
    api_client = client_wrapper.client

    try:
        if order_type == 'MARKET':
            response = api_client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        else:
            response = api_client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity, price=price, timeInForce="GTC")
        #orderId, status, executedQty, avgPrice
        print("Order Placed Successfully!")
        print(f"OrderID : {response["orderId"]}")
        print(f"Status : {response["status"]}")
        print(f"executed Quantity : {response["executedQty"]}")
        print(f"Average Price : {response["avgPrice"]}")

    except Exception as e:
        print(e)
    
    api_client.close_connection()
place_order("BTCUSDT", "BUY", "market", 0.002)