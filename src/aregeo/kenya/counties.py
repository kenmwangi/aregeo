from __future__ import annotations

from pathlib import Path

from aregeo.kenya.boundaries import BoundaryService


class KenyaCountyService:
    """
    Service for detecting Kenyan counties from coordinates.
    """

    def __init__(
        self,
        geojson_path: str | Path,
    ) -> None:
        self.boundaries = BoundaryService(geojson_path)

    def find_county(
        self,
        latitude: float,
        longitude: float,
    ) -> str | None:
        """
        Return the Kenyan county containing the coordinates.
        """

        feature = self.boundaries.find_feature(
            latitude=latitude,
            longitude=longitude,
        )

        if feature is None:
            return None

        properties = feature.get(
            "properties",
            {},
        )

        # Support common GeoJSON property naming conventions.
        for key in (
            "county",
            "COUNTY",
            "County",
            "name",
            "NAME",
            "COUNTY_NAME",
        ):
            value = properties.get(key)

            if isinstance(value, str) and value.strip():
                return value.strip()

        return None
