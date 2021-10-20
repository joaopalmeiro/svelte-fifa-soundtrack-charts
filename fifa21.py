from pathlib import Path
from typing import Tuple

import pandas as pd
import requests
from bs4 import BeautifulSoup

TABLE_SELECTOR: str = "ea-table > table"
# TITLE_SELECTOR: str = "h2.d4"

TITLES: Tuple[str, str] = ("FIFA", "VOLTA FOOTBALL")
GAME: str = "FIFA 21"

LIST_COLUMN_NAME: str = "LIST"
GAME_COLUMN_NAME: str = "GAME"

URL: str = "https://www.ea.com/en-gb/games/fifa/fifa-21/soundtrack"
OUTPUT_PATH: Path = Path("data") / "fifa21.json"

# Source: https://github.com/psf/requests-html/blob/master/requests_html.py#L27
# DEFAULT_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"


if __name__ == "__main__":
    # agent = {"User-Agent": DEFAULT_USER_AGENT}
    # page = requests.get(URL, headers=agent)

    # Tutorial: https://realpython.com/beautiful-soup-web-scraper-python/
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # with open("output.html", "w", encoding="utf-8") as file:
    #     file.write(str(soup))

    # More info: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
    # titles = soup.select(TITLE_SELECTOR)
    tables = soup.select(TABLE_SELECTOR)

    dfs = []
    for title, table in zip(TITLES, tables):
        # More info: https://pandas.pydata.org/docs/reference/api/pandas.read_html.html
        df = pd.read_html(str(table))[0]

        # df[LIST_COLUMN_NAME] = title.text
        df[LIST_COLUMN_NAME] = title
        df[GAME_COLUMN_NAME] = GAME

        dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)
    full_df.to_json(OUTPUT_PATH, orient="records", force_ascii=False)
