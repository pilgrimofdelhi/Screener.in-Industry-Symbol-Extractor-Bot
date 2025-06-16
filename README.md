# Screener.in Symbol Extractor Bot

Automate extraction of all stock symbols (tickers) from [Screener.in](https://www.screener.in/) company category pages!  
This tool visits a list of Screener.in links, grabs all ticker symbols per category, and exports them to a CSV file.

<img src="https://i.ibb.co/bg8QRKkp/Screenshot-2025-06-16-104521.png" alt="Screenshot" width="1500">



## Features

- **Extracts all tickers** from a list of Screener.in category/company pages.
- **Auto-detects symbol format** (e.g. ....EICHERMOT/consolidated/, ....ATHERENERG/, ....538970/).
- **Exports** to a CSV:  
  - Each row: Category | Symbol 1 | Symbol 2 | Symbol 3 | ...
- **User-friendly**: Uses your existing browser session for reliability.
- **Supports custom link lists**.

## Requirements

- Windows PC (tested)
- Python 3.8+
- Google Chrome or Brave browser
- [Selenium Python](https://pypi.org/project/selenium/)  
- [chromedriver.exe](https://chromedriver.chromium.org/) (should match your browser version)

## Installation

1. **Clone or download this repo.**
2. Place `chromedriver.exe` in the project folder.
3. Install dependencies:

   ```bash
   pip install selenium

## Configure your browser profile:

The bot uses a dedicated browser profile to avoid interfering with your main browser.

On first run, you may be prompted to log in to Screener.in (if needed).

## Prepare your links:

Edit links.txt and paste one Screener.in link per line.
(e.g. category pages like https://www.screener.in/market/IN05/IN0501/IN050105/IN050105001/

I've already added the current links.txt file with all the 190 industry URLs.

## Run the script:
   ```bash
python main.py
 ```

## The script will:

- Open the browser, visit each link, extract symbols, and write results to screener_symbols.csv.

- Add a delay between requests to avoid being blocked by Screener.in.

- Check screener_symbols.csv

Each row:
Category | Symbol1 | Symbol2 | ...

Example:

```bash 2/3 
Wheelers Companies, BAJAJ-AUTO, EICHERMOT, TVSMOTOR
 ```

## Credits
Selenium code and project scaffolding: Rajat Kumar Singh. [@tradingwick_](https://x.com/tradingwick_)

## Disclaimer
For educational/personal use.

This script is not affiliated with Screener.in. 
