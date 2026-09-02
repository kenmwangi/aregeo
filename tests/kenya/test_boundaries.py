from pathlib import Path

from aregeo.kenya.boundaries import BoundaryService
from aregeo.kenya.counties import KenyaCountyService

DATA_PATH = Path(__file__).parent / "kenya_test_counties.geojson"


def test_point_inside_boundary() -> None:
    service = BoundaryService(DATA_PATH)

    result = service.contains(
        latitude=-1.2921,
        longitude=36.8219,
    )

    assert result is True


def test_point_outside_boundary() -> None:
    service = BoundaryService(DATA_PATH)

    result = service.contains(
        latitude=-4.0435,
        longitude=39.6682,
    )

    assert result is False


def test_find_county() -> None:
    service = KenyaCountyService(DATA_PATH)

    county = service.find_county(
        latitude=-1.2921,
        longitude=36.8219,
    )

    assert county == "Test Nairobi"


def test_unknown_county() -> None:
    service = KenyaCountyService(DATA_PATH)

    county = service.find_county(
        latitude=-4.0435,
        longitude=39.6682,
    )

    assert county is None
