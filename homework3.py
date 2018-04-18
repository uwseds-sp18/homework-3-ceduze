import pandas as pd
import sqlite3
from pathlib import Path

def create_dataframe(db_path):
    queryString = "select video_id, category_id, 'us' as language FROM USvideos UNION select video_id, category_id, 'ca' as language FROM CAvideos UNION select video_id, category_id, 'de' as language FROM DEvideos UNION select video_id, category_id, 'fr' as language FROM FRvideos UNION select video_id, category_id, 'gb' as language FROM GBvideos;"

    if Path(db_path).is_file():
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(queryString, conn)
        return df

    raise ValueError('Invalid path for DB.')
    return null

