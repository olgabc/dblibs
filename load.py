import os
import pandas as pd


def load_some_xlsx(name_without_extension, folder):
    file_path = os.path.join(
        folder,
        "{}.xlsx".format(name_without_extension)
    )

    some_frame = pd.read_excel(
        file_path,
        encoding="cp1251",
        sep=";"
    )
    return some_frame


def load_some_csv(name_without_extension, folder):
    file_path = os.path.join(
        folder,
        "{}.csv".format(name_without_extension)
    )

    some_frame = pd.read_csv(
        file_path,
        encoding="cp1251",
        sep=";",
        engine="python"
    )
    return some_frame
