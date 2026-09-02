from typing import Literal

from aregeo.coordinates.validator import validate_coordinates
from aregeo.models.location import PropertyLocation
from aregeo.spatial.geohash import encode_geohash


class PropertyLocator:
    """
    Entry point for locating properties based on geographic coordinates.
    """

    def locate(
        self,
        latitude: float,
        longitude: float,
        accuracy: float | None = None,
    ) -> PropertyLocation:
        coordinates = validate_coordinates(
            latitude=latitude, longitude=longitude, accuracy=accuracy
        )

        geohash = encode_geohash(latitude=latitude, longitude=longitude)

        confidence = self._calculate_confidence(accuracy=accuracy)

        return PropertyLocation(
            latitude=coordinates.latitude,
            longitude=coordinates.longitude,
            accuracy=accuracy,
            geohash=geohash,
            confidence=confidence,
            verification_status=self.__verification_status(confidence=confidence),
        )

    def _calculate_confidence(self, accuracy: float | None) -> int:
        """
        Calculate confidence level based on accuracy.
        """

        if accuracy is None:
            return 50

        if accuracy <= 10:
            return 95
        if accuracy <= 25:
            return 85

        if accuracy <= 50:
            return 70

        if accuracy <= 100:
            return 50

        return 30

    def __verification_status(
        self,
        confidence: int,
    ) -> Literal["unverified", "verified", "approximate"]:
        """
        Determine verification status based on confidence level.
        """

        if confidence >= 85:
            return "verified"
        elif confidence >= 50:
            return "approximate"
        else:
            return "unverified"
