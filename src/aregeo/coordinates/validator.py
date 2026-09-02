from aregeo.models.location import Coordinates


def validate_coordinates(
    latitude: float,
    longitude: float,
    accuracy: float | None = None,
) -> Coordinates:
    """
    Validate Geographic coordinates

    Raises: pydantic.ValidationError if the coordinates are invalid or out of range.
    """
    return Coordinates(latitude=latitude, longitude=longitude, accuracy=accuracy)
