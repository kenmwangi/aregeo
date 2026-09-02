from geographiclib.geodesic import Geodesic


def distance_between(
    latitude1: float,
    longitude1: float,
    latitude2: float,
    longitude2: float,
) -> float:
    """
    Calculate distance between 2 geographic coordinates in meters
    """

    result = Geodesic.WGS84.Inverse(latitude1, longitude1, latitude2, longitude2)
    return result["s12"]
