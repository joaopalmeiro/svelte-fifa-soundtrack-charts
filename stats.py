from pathlib import Path
from typing import Tuple

import pandas as pd

DATA_PATH: Path = Path("data")
FILE_PATHS: Tuple[Path, Path] = (DATA_PATH / "fifa21.json", DATA_PATH / "fifa20.json")

if __name__ == "__main__":
    dfs = []
    for file_path in FILE_PATHS:
        df = pd.read_json(file_path)

        print(f"{file_path.name}: {df.shape}")
        dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)
    print(f"\nTotal: {full_df.shape}")
