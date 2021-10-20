from pathlib import Path
from typing import Tuple

import pandas as pd
import requests
from bs4 import BeautifulSoup

TABLE_SELECTOR: str = "ea-table > table"
TITLES: Tuple[str, str] = ("FIFA", "VOLTA FOOTBALL")

GAME: str = "FIFA 20"

LIST_COLUMN_NAME: str = "LIST"
GAME_COLUMN_NAME: str = "GAME"

URL: str = "https://www.ea.com/en-au/news/fifa-20-soundtrack-volta-football"
OUTPUT_PATH: Path = Path("data") / "fifa20.json"


if __name__ == "__main__":
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    tables = soup.select(TABLE_SELECTOR)

    dfs = []
    for title, table in zip(TITLES, tables):
        df = pd.read_html(str(table))[0]

        df[LIST_COLUMN_NAME] = title
        df[GAME_COLUMN_NAME] = GAME

        dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)
    full_df.to_json(OUTPUT_PATH, orient="records", force_ascii=False)
