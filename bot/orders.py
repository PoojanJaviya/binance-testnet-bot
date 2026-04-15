from typing import Optional
from bot.validators import validate_price, validate_quantity, validate_side, validate_order_type
from bot.client import BinanceFuturesClient
from bot.logging_config import logger

#main function which is used to place order
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
        
        #required responses
        logger.info("Order Placed Successfully!")
        logger.info(f"OrderID : {response["orderId"]}")
        logger.info(f"Status : {response["status"]}")
        logger.info(f"executed Quantity : {response["executedQty"]}")
        logger.info(f"Average Price : {response["avgPrice"]}")

    except Exception as e:
        logger.error(f"Failed to place order : {e}")
    
    api_client.close_connection()