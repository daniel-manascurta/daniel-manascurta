import pathlib
from datetime import datetime

ls = [
    {
        "filename": "test_zipfiles1.zip",
        "path": "raw/folder1/test_zipfiles1.zip",
        "file_size": 564,
        "creation_time": "2025-01-29T17:09:49Z",
        "file_url": "https://stgmdmstoreexpeuwpud.dfs.core.windows.net/operational/b28939ab-6aa4-4926-9fae-b5297fe62175/raw/folder1/test_zipfiles1.zip",
        "is_file": True,
    },
    {
        "filename": "test_zipfiles2.zip",
        "path": "raw/folder2/test_zipfiles2.zip",
        "file_size": 564,
        "creation_time": "2025-01-29T17:09:49Z",
        "file_url": "https://stgmdmstoreexpeuwpud.dfs.core.windows.net/operational/b28939ab-6aa4-4926-9fae-b5297fe62175/raw/folder2/test_zipfiles2.zip",
        "is_file": True,
    },
]


files = [f["filename"] for f in ls if f["path"].upper().endswith(".ZIP")]
# utc_now = str(datetime.utcnow().replace(":", "-").replace(" ", "_"))
# @concat(replace(split(utcNow(), '.')[0], ':', '-'), '_')
# print(utc_now.split(".")[0])
# print(utc_now.split(".")[0].replace(":", "-").replace(" ", "_"))
print(files)
print(len(files))
# print(str(datetime.utcnow()).split(".")[0].replace(":", "-").replace(" ", "_"))
# comm
