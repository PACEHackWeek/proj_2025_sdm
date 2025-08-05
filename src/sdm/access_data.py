import pandas as pd
import importlib.resources as pkg_resources
from paceship import data  # ensure data is a subpackage with __init__.py

def load_trawl_data():
    """
    Load example trawl abundance data from NE trawl survey.

    This dataset contains species abundance observations collected from tows
    along with metadata like date, location, depth, and swept area.

    Returns
    -------
    pd.DataFrame
        A DataFrame with columns:
        - `TOWDATETIME_EST` (str): Tow start datetime in EST
        - `LAT`, `LON` (float): Latitude and longitude of the tow
        - `MEAN_DEPTH` (float): Mean depth in meters
        - `SWEPT_AREA_km` (float): Swept area in square kilometers
        - One column per species (e.g., `acadian redfish`, `alewife`, ..., `yellowtail flounder`)
          with counts or presence/absence data.

    Example
    -------
    >>> df = load_tow_species_data()
    >>> df[['LAT', 'LON', 'acadian redfish']].head()
    """
    with pkg_resources.files(data).joinpath("tow_species.csv").open("r") as f:
        return pd.read_csv(f)