from typing import Literal

from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    """
    Geographic coordinates for exact location
    """

    latitude: float = Field(
        ...,
        ge=-90,
        le=90,
        description="Latitude in decimal degrees, must be between -90 and 90",
    )

    longitude: float = Field(
        ...,
        ge=-180,
        le=180,
        description="Longitude in decimal degrees, must be between -180 and 180",
    )

    accuracy: float | None = Field(
        default=None, ge=0, description="GPS accuracy in meters"
    )


class PropertyLocation(BaseModel):
    """
    All Geographic information for a property (address & coordinates)
    """

    latitude: float
    longitude: float

    country: str | None = None
    county: str | None = None
    sub_county: str | None = None

    locality: str | None = None
    address: str | None = None

    geohash: str | None = None

    accuracy: float | None = None

    confidence: int = Field(
        default=0,
        ge=0,
        le=100,
        description="Confidence level of the location data, must be between 0 and 100",
    )

    verification_status: Literal["unverified", "verified", "approximate"] = "unverified"
