import typer
from . import currency
import datetime
import pytz

app = typer.Typer()

@app.command("home")
def main():
    """
    Run the Finance CLI app and check for version
    """
    print("▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖▗▖   ▗▄▄▄▖")
    print(" ▌     █  ▐▛▚▖▐▌▐▌   ▐▌     █  ")
    print("▐▛▀▀▘  █  ▐▌ ▝▜▌▐▌   ▐▌     █  ")
    print("▌   ▗▄█▄▖▐▌  ▐▌▝▚▄▄▖▐▙▄▄▖▗▄█▄▖")
    print("Version: Beta")
    print("©SnowDingo 2026-2126")

@app.command("calcfx")
def calcFX(original: str, convertcurrency: str):
    """
    Shows the conversion rate of the first argument's current to another
    """
    exchangerate = currency.fetchCurrentExchangeRate(original,convertcurrency)
    print(f"The exchange rate of {original} to {convertcurrency} is {str(exchangerate)}")

@app.command("listcurrency")
def listcurrency():
    """
    Shows all the currency this app supports
    """
    print(currency.fetchAllAvailableCurrencies())

@app.command("timezone")
def calcTimezone():
    """
    List current time and time of major trading hubs
    """
    date = datetime.datetime.now()
    print(f"now: " + date.strftime("%b") + " " + date.strftime("%d") + " " + date.strftime("%H") + ":" + date.strftime("%S"))
    datenow = datetime.datetime.now(pytz.utc)
    # Time zones
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    tz_japan = pytz.timezone('Asia/Tokyo')
    tz_china = pytz.timezone('Asia/Shanghai')
    # convert to each local timezones
    now_ny = datenow.astimezone(tz_ny)
    now_lo = datenow.astimezone(tz_london)
    now_jp = datenow.astimezone(tz_japan)
    now_bj = datenow.astimezone(tz_china)
    fmt = "%b %d %H:%M"
    print("\n=AROUND THE WORLD=")
    print("UTC: " + datenow.strftime(fmt))
    print("Tokyo Japan: " + now_jp.strftime(fmt))
    print("London UK: " + now_lo.strftime(fmt))
    print("New York USA: " + now_ny.strftime(fmt))
    print("Bejing China: " +now_bj.strftime(fmt))
    return

@app.command("compound")
def compound(initial:int, rate:float, time:int,compoundpertime:int):
    """
    Calculate the result of compound interest over certain time period after time division.
    For the compoundper enter how many times per year your rate is compounded.
    """
    print(str(initial*(1+rate/compoundpertime)**(compoundpertime*time)))
    return

if __name__ == "__main__":
    app()
