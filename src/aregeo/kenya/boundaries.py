from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from shapely.geometry import Point, shape


class BoundaryService:
    """
    Service for working with geographic boundaries stored as GeoJSON.
    """

    def __init__(self, geojson_path: str | Path) -> None:
        self.geojson_path = Path(geojson_path)
        self._features = self._load_features()

    def _load_features(self) -> list[dict[str, Any]]:
        """
        Load geographic features from a GeoJSON file.
        """

        if not self.geojson_path.exists():
            raise FileNotFoundError(
                f"GeoJSON boundary file not found: {self.geojson_path}"
            )

        with self.geojson_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        if data.get("type") != "FeatureCollection":
            raise ValueError("Expected a GeoJSON FeatureCollection")

        features = data.get("features")

        if not isinstance(features, list):
            raise TypeError("GeoJSON FeatureCollection must contain a features list")

        return features

    def contains(
        self,
        latitude: float,
        longitude: float,
    ) -> bool:
        """
        Check whether a point exists inside any boundary.
        """

        point = Point(longitude, latitude)

        for feature in self._features:
            geometry_data = feature.get("geometry")

            if geometry_data is None:
                continue

            geometry = shape(geometry_data)

            if geometry.contains(point) or geometry.covers(point):
                return True

        return False

    def find_feature(
        self,
        latitude: float,
        longitude: float,
    ) -> dict[str, Any] | None:
        """
        Find the geographic feature containing the given point.
        """

        point = Point(longitude, latitude)

        for feature in self._features:
            geometry_data = feature.get("geometry")

            if geometry_data is None:
                continue

            geometry = shape(geometry_data)

            if geometry.contains(point) or geometry.covers(point):
                return feature

        return None
