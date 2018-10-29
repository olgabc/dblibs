import os
import pandas as pd


def write_some_csv(some_data, name_without_extension, folder):
    file_path = os.path.join(
        folder,
        "{}.csv".format(name_without_extension)
    )

    some_data.to_csv(
        file_path,
        encoding="cp1251",
        index=False,
        sep=";"
    )
