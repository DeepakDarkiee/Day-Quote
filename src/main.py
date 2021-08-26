import requests
from great_text import great_text

_QUOTE_URL = "https://quotes.rest/qod"


def get_day_quote():
    """Get a day quote."""

    res = requests.get(_QUOTE_URL)
    try:
        q = res.json()["contents"]["quotes"][0]["quote"]
    except KeyError:
        err = "Internet Connection Error >>>"
        q = great_text(err, "red")
    return q


def display_quote():
    """Display a random quote."""
    quote = f'Quote Of The Day: "{get_day_quote()}"'
    great_text(quote, "red")


if __name__ == "__main__":
    display_quote()
