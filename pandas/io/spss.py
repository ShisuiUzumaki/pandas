from __future__ import annotations

from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Sequence,
)

from pandas.compat._optional import import_optional_dependency

from pandas.core.dtypes.inference import is_list_like

from pandas.io.common import stringify_path

if TYPE_CHECKING:
    from pandas import DataFrame


def read_spss(
    path: str | Path,
    usecols: Sequence[str] | None = None,
    convert_categoricals: bool = True,
) -> DataFrame:
    """
    Load an SPSS file from the file path, returning a DataFrame.

    Parameters
    ----------
    path : str or Path
        File path.
    usecols : list-like, optional
        Return a subset of the columns. If None, return all columns.
    convert_categoricals : bool, default is True
        Convert categorical columns into pd.Categorical.

    Returns
    -------
    DataFrame
    """
    pyreadstat = import_optional_dependency("pyreadstat")

    if usecols is not None:
        if not is_list_like(usecols):
            raise TypeError("usecols must be list-like.")
        usecols = list(usecols)  # pyreadstat requires a list

    df, _ = pyreadstat.read_sav(
        stringify_path(path), usecols=usecols, apply_value_formats=convert_categoricals
    )
    return df
