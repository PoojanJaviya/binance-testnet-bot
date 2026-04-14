from dotenv import load_dotenv
from binance import Client
import os

load_dotenv()

api_key = os.getenv("BINANCE_TESTNET_API_KEY")
api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")

client = Client(api_key, api_secret, testnet=True)

ticker = client.get_symbol_ticker(symbol="BTCUSDT")
print(f"BTCUSDT Price: {ticker["price"]}")

client.close_connection()