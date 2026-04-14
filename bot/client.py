import os
from dotenv import load_dotenv
from binance import Client

class BinanceFuturesClient:
    def __init__(self):

        load_dotenv()

        api_key = os.getenv("BINANCE_TESTNET_API_KEY")
        api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API key is missing")
        
        try:
            self.client = Client(api_key=api_key, api_secret=api_secret, testnet=True)
        except Exception as e:
            raise ValueError(e)