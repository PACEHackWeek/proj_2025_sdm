import pandas as pd
import importlib.resources as pkg_resources
from sdm import data  # ensure data is a subpackage with __init__.py

def load_trawl_data():
    """
    Load example trawl abundance data from NE trawl survey.

    This dataset contains species abundance observations collected from tows
    along with metadata like date, location, depth, and swept area.

    Returns
    -------
    pd.DataFrame
        A DataFrame with columns:
        - `time` (str): Tow start datetime in EST
        - `latitude`, `longitude` (float): Latitude and longitude of the tow
        - `MEAN_DEPTH` (float): Mean depth in meters
        - `SWEPT_AREA_km` (float): Swept area in square kilometers
        - One column per species (e.g., `acadian redfish`, `alewife`, ..., `yellowtail flounder`)
          with counts or presence/absence data.

    Example
    -------
    import sdm
    df = sdm.load_trawl_data()
    df[['latitude', 'longitude', 'acadian redfish']].head()
    """
    with pkg_resources.files(data).joinpath("trawl.csv").open("r") as f:
        trawl_df = pd.read_csv(f)

    # 1. Ensure the date column is a proper datetime object
    trawl_df['TOWDATETIME_EST'] = pd.to_datetime(trawl_df['TOWDATETIME_EST'])

    # 2. Ensure coordinates are numeric
    trawl_df['LON'] = pd.to_numeric(trawl_df['LON'])
    trawl_df['LAT'] = pd.to_numeric(trawl_df['LAT'])

    # 4. Standardize column names to match xarray dimensions
    rename_dict = {
        'TOWDATETIME_EST': 'time',
        'LAT': 'latitude',
        'LON': 'longitude'
    }
    trawl_df = trawl_df.rename(columns=rename_dict)

    return trawl_df


def get_pace_daily_path(tspan, bbox, short_name, clouds=null):
    results = earthaccess.search_data(
        short_name=short_name,
        temporal=tspan,
        bounding_box=bbox,
        granule_name="*.4km*",
        cloud_cover=clouds)
    paths = earthaccess.open(results)
    return paths 