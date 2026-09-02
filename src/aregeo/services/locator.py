from __future__ import annotations

from pathlib import Path
from typing import Literal

from aregeo.coordinates.validator import validate_coordinates
from aregeo.kenya.counties import KenyaCountyService
from aregeo.models.location import PropertyLocation
from aregeo.spatial.geohash import encode_geohash


class PropertyLocator:
    """
    Main service for processing property locations.
    """

    def __init__(
        self,
        kenya_counties_path: str | Path | None = None,
    ) -> None:
        self.county_service: KenyaCountyService | None = None

        if kenya_counties_path is not None:
            self.county_service = KenyaCountyService(kenya_counties_path)

    def locate(
        self,
        latitude: float,
        longitude: float,
        accuracy: float | None = None,
    ) -> PropertyLocation:
        """
        Process coordinates and return property location information.
        """

        coordinates = validate_coordinates(
            latitude=latitude,
            longitude=longitude,
            accuracy=accuracy,
        )

        geohash = encode_geohash(
            latitude=coordinates.latitude,
            longitude=coordinates.longitude,
        )

        county = self._find_county(
            latitude=coordinates.latitude,
            longitude=coordinates.longitude,
        )

        confidence = self._calculate_confidence(
            accuracy=accuracy,
            county=county,
        )

        return PropertyLocation(
            latitude=coordinates.latitude,
            longitude=coordinates.longitude,
            country="Kenya" if county else None,
            county=county,
            accuracy=accuracy,
            geohash=geohash,
            confidence=confidence,
            verification_status=self._verification_status(confidence),
        )

    def _find_county(
        self,
        latitude: float,
        longitude: float,
    ) -> str | None:
        """
        Find the Kenyan county containing the coordinates.
        """

        if self.county_service is None:
            return None

        return self.county_service.find_county(
            latitude=latitude,
            longitude=longitude,
        )

    def _calculate_confidence(
        self,
        accuracy: float | None,
        county: str | None,
    ) -> int:
        """
        Calculate location confidence.
        """

        score = 30

        if accuracy is not None:
            if accuracy <= 10:
                score += 40
            elif accuracy <= 25:
                score += 30
            elif accuracy <= 50:
                score += 20
            elif accuracy <= 100:
                score += 10

        if county is not None:
            score += 20

        return min(score, 100)

    def _verification_status(
        self,
        confidence: int,
    ) -> Literal["unverified", "verified", "approximate"]:
        if confidence >= 85:
            return "verified"

        if confidence >= 50:
            return "approximate"

        return "unverified"
