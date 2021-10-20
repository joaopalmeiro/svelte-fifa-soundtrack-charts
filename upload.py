import json
import os
from pathlib import Path
from typing import Tuple

from deta import Deta
from dotenv import load_dotenv

load_dotenv()

DATA_PATH: Path = Path("data")
FILE_PATHS: Tuple[Path, Path] = (DATA_PATH / "fifa21.json", DATA_PATH / "fifa20.json")

DB_NAME: str = "fifa_soundtrack"

if __name__ == "__main__":
    deta = Deta(os.environ["PROJECT_KEY"])
    db = deta.Base(DB_NAME)

    for file_path in FILE_PATHS:
        with open(file_path) as file:
            data = json.load(file)

        for item in data:
            db.put(item)

        print(f"\n{file_path.name} ✅")

    # Based on: https://github.com/psf/black/blob/21.9b0/src/black/__init__.py#L474
    print("\nAll done! ✨ 🗄️ ✨")
