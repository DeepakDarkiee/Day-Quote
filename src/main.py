import requests

_QUOTE_URL = "https://quotes.rest/qod"


def get_day_quote():
    """Get a day quote."""

    res = requests.get(_QUOTE_URL)
    return res.json()["contents"]["quotes"][0]["quote"]


def display_quote():
    """Display a random quote."""

    print(f'Quote Of The Day: "{get_day_quote()}"')


if __name__ == "__main__":
    display_quote()
