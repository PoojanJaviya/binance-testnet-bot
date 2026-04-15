import typer
from typing import Optional
from bot.orders import place_order

app = typer.Typer(help="Primetrade.ai Binance Futures Trading Bot")

@app.command()
def execute(
    symbol: str = typer.Argument(..., help="The trading pair (e.g., BTCUSDT)"),
    side: str = typer.Argument(..., help="Trade direction (BUY or SELL)"),
    order_type: str = typer.Argument(..., help="Order type (MARKET or LIMIT)"),
    quantity: float = typer.Argument(..., help="Amount of the asset to trade"),
    price: Optional[float] = typer.Option(
        None, 
        "--price", 
        "-p", 
        help="Required for LIMIT orders. The price at which to execute."
    )
):
    """
    Execute a trade on the Binance Futures Testnet.
    """
    try:
        place_order(
            symbol=symbol, 
            side=side, 
            order_type=order_type, 
            quantity=quantity, 
            price=price
        )
    except Exception as e:
        typer.secho(f"Execution Failed: {e}", fg=typer.colors.RED)

if __name__ == "__main__":
    app()