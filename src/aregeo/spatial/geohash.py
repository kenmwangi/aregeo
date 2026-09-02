import geohash2


def encode_geohash(latitude: float, longitude: float, precision: int = 8) -> str:
    """
    Converting geographic coordinates into a geohash

    """
    return geohash2.encode(latitude, longitude, precision=precision)
