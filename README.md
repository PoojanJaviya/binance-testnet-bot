# Primetrade.ai - Binance Futures Trading Bot

A robust, command-line interface (CLI) trading bot designed to execute Market and Limit orders on the Binance Futures Testnet. 

This project was built as a backend engineering assignment for Primetrade.ai, focusing on secure API communication, strict data validation, and production-grade logging.

## 🚀 Features

* **Interactive CLI:** Built with `Typer` for a clean, user-friendly terminal experience.
* **Smart Validation:** Pre-trade validation ensures accurate order types, sufficient notional values, and correct data types before pinging the exchange.
* **Centralized Logging:** Dual-stream logging captures all trading activity and errors both in the terminal and permanently in a local `.log` file.
* **Environment Security:** Uses `python-dotenv` to ensure API keys are securely loaded into the environment and never hardcoded.

## 🛠️ Prerequisites

* Python 3.8+
* A [Binance Futures Testnet](https://testnet.binancefuture.com/) Account
* Testnet API Key and Secret

## 📦 Installation & Setup

**1. Clone the repository:**
```bash
git clone https://github.com/PoojanJaviya/binance-testnet-bot.git
cd binance-testnet-bot
```

**2. Create and Activate a Virtual Environment:**
* **Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **Windows (Command Prompt):**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables:**
* Copy the example environment file:
  ```bash
  cp .env.example .env
  ```
* Open the `.env` file and replace the placeholder values with your actual Binance Testnet credentials.
*(Note: Ensure `.env` is added to your `.gitignore` file to prevent leaking keys).*

## 💻 Usage

The bot is operated entirely through the terminal using `cli.py`. 

*(Note: The commands below use `python`. Depending on your OS, you may need to use `python3` instead).*

**View the Help Menu:**
```bash
python cli.py --help
```

**Execute a LIMIT Order:**
```bash
python cli.py BTCUSDT BUY LIMIT 0.002 --price 70000
```

**Execute a MARKET Order:**
```bash
python cli.py BTCUSDT SELL MARKET 0.01
```

## 📄 Logging
All trade executions and system errors are automatically recorded. Check the `trading_bot.log` file in the root directory for a complete historical record of your bot's activity.

## ⚠️ Disclaimer
This bot is configured specifically for the Binance Futures **Testnet**. It uses mock funds for testing purposes. Do not use these scripts with a live Binance account without significant structural modifications and risk management protocols.
