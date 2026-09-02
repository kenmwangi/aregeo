# aregeo

> High-precision geospatial tools for precise real estate property locations in Kenya and Africa.

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![Package Manager](https://img.shields.io/badge/package%20manager-uv-purple)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-alpha-orange)

aregeo is a high-precision Python geospatial package designed to help solve Kenya's informal property address problem.

Many property listings rely on vague location descriptions such as:

> *"Behind the primary school, off the dirt road."*

> *"Near the shopping centre."*

> *"Next to the petrol station."*

> *"Along Thika Road."*

These descriptions can be ambiguous, difficult to search, and impossible to verify precisely.

**aregeo provides tools for converting, validating, resolving, indexing, searching, and verifying precise geographic locations for real estate and property applications.**

---

## Why aregeo?

Property location information across Kenya and many parts of Africa is often inconsistent.

A property may have:

- No formal street address.
- An incomplete address.
- A landmark-based description.
- A manually entered location that cannot be verified.
- Incorrect county or administrative information.
- Coordinates that are inaccurate or missing.

aregeo aims to provide a reliable location intelligence layer for real estate platforms.

```text
Vague Property Description
          │
          ▼
"Behind the school"
          │
          ▼
     aregeo
          │
          ├── Validate Coordinates
          ├── Calculate Distance
          ├── Generate Geohash
          ├── Resolve Administrative Areas
          ├── Reverse Geocode Locations
          └── Verify Location Confidence
          │
          ▼
Precise Property Location
```

---

## Features

aregeo is being built to support:

### 📍 Precise Coordinates

Validate and work with latitude and longitude coordinates.

```python
from aregeo.coordinates.validator import validate_coordinates

coordinates = validate_coordinates(
    latitude=-1.2921,
    longitude=36.8219,
    accuracy=10,
)
```

---

### 📏 Geographic Distance

Calculate accurate distances between locations.

```python
from aregeo.coordinates.distance import distance_between

distance = distance_between(
    latitude1=-1.2921,
    longitude1=36.8219,
    latitude2=-1.2864,
    longitude2=36.8172,
)

print(f"{distance:.2f} meters")
```

---

### 🗺️ Geospatial Indexing

Generate geohashes for efficient spatial indexing and proximity search.

```python
from aregeo.spatial.geohash import encode_geohash

geohash = encode_geohash(
    latitude=-1.2921,
    longitude=36.8219,
)

print(geohash)
```

---

### Kenya Location Intelligence

Planned support for resolving geographic coordinates into Kenyan administrative areas.

```text
Coordinates
     │
     ▼
Kenya
     │
     ▼
County
     │
     ▼
Sub-County
     │
     ▼
Ward
```

---

### Reverse Geocoding

Planned support for converting coordinates into human-readable locations.

```text
Latitude + Longitude
        │
        ▼
     aregeo
        │
        ▼
Westlands
Nairobi County
Kenya
```

---

### 🔍 Proximity Search

Find locations and properties near a specific coordinate.

Examples:

```text
Properties within 5 km

Nearest schools

Nearest hospitals

Nearest shopping centres

Nearby landmarks
```

---

### ✅ Location Verification

aregeo aims to provide location confidence and verification tools.

```text
Coordinates
     │
     ├── Valid coordinate ranges
     │
     ├── GPS accuracy
     │
     ├── Administrative boundary validation
     │
     └── Geocoding verification
     │
     ▼
Location Confidence Score
```

Example:

```text
Location Confidence: 95/100

Status: Verified
```

---

## Installation

aregeo is currently under active development.

The recommended package manager for development is [uv](https://docs.astral.sh/uv/).

### Clone the Repository

```bash
git clone https://github.com/kenmwangi/aregeo.git
cd aregeo
```

### Install Dependencies

```bash
uv sync
```

---

## Quick Start

```python
from aregeo.coordinates.distance import distance_between
from aregeo.coordinates.validator import validate_coordinates


coordinates = validate_coordinates(
    latitude=-1.2921,
    longitude=36.8219,
    accuracy=10,
)

distance = distance_between(
    latitude1=-1.2921,
    longitude1=36.8219,
    latitude2=-1.2864,
    longitude2=36.8172,
)

print(coordinates)
print(f"{distance:.2f} meters")
```

---

## Project Structure

```text
aregeo/
├── src/
│   └── aregeo/
│       ├── coordinates/
│       │   ├── __init__.py
│       │   ├── distance.py
│       │   └── validator.py
│       │
│       ├── geocoding/
│       │   └── Geocoding providers and services
│       │
│       ├── kenya/
│       │   └── Kenya-specific geographic intelligence
│       │
│       ├── models/
│       │   └── Geographic data models
│       │
│       ├── services/
│       │   └── High-level location services
│       │
│       ├── spatial/
│       │   ├── __init__.py
│       │   └── geohash.py
│       │
│       ├── __init__.py
│       └── py.typed
│
├── tests/
│
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── pyproject.toml
└── uv.lock
```

---

## Architecture

aregeo is designed around several core geospatial capabilities.

```text
                         aregeo
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
     Coordinates        Geocoding        Spatial Search
          │                 │                 │
          ▼                 ▼                 ▼
     Validation        Addresses         Geohashing
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ▼
                    Property Location
                            │
                            ▼
                   Location Verification
```

---

## Technology

aregeo uses modern Python tooling and geospatial libraries.

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| uv | Package and dependency management |
| Pydantic | Data validation and models |
| GeographicLib | Accurate geographic distance calculations |
| Geohash | Spatial indexing |
| HTTPX | HTTP communication with geocoding providers |
| Shapely | Geographic boundaries and spatial operations |
| Ruff | Formatting and linting |
| Pyrefly | Static type checking |
| Pytest | Testing |

---

## Development

### Format Code

```bash
uv run ruff format .
```

### Run the Linter

```bash
uv run ruff check .
```

### Run Type Checking

```bash
uv run pyrefly check
```

### Run Tests

```bash
uv run pytest
```

### Run Coverage

```bash
uv run pytest --cov=aregeo
```

---

## Roadmap

### Version 0.1 — Core Location Tools

- [x] Project setup with uv
- [x] Pydantic location models
- [x] Coordinate validation
- [x] Geographic distance calculations
- [x] Geohash generation
- [ ] Comprehensive test suite

### Version 0.2 — Kenya Geographic Intelligence

- [ ] Kenya geographic boundary validation
- [ ] County detection
- [ ] Sub-county detection
- [ ] Ward detection
- [ ] Administrative boundary datasets

### Version 0.3 — Geocoding

- [ ] Reverse geocoding
- [ ] Forward geocoding
- [ ] Provider abstraction
- [ ] OpenStreetMap integration
- [ ] Multiple geocoding providers

### Version 0.4 — Property Intelligence

- [ ] Nearby property search
- [ ] Landmark detection
- [ ] Proximity search
- [ ] Location confidence scoring
- [ ] Property location verification

### Version 1.0 — Production Ready

- [ ] Stable public API
- [ ] Comprehensive documentation
- [ ] High test coverage
- [ ] Performance optimization
- [ ] Production-ready geospatial architecture
- [ ] Support for additional African countries

---

## Contributing

Contributions are welcome

aregeo welcomes:

- Bug reports
- Feature requests
- Documentation improvements
- Tests
- New geospatial features
- Geocoding providers
- Geographic datasets with appropriate licenses
- Support for additional African countries

Please read:

- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

before contributing.

---

## Geographic Data

aregeo may use geographic datasets to provide administrative boundary detection and location intelligence.

All geographic data included in the project should:

- Have a compatible license.
- Clearly document its source.
- Permit redistribution.
- Include appropriate attribution where required.
- Use documented coordinate reference systems.

---

## Privacy and Security

Precise property locations can contain sensitive information.

Applications using aregeo should carefully consider whether exact coordinates should be publicly displayed.

aregeo is designed to support precise geographic information, but applications are responsible for implementing appropriate privacy and access controls.

Possible strategies include:

- Displaying approximate locations publicly.
- Restricting exact coordinates to authorized users.
- Obfuscating residential property coordinates.
- Using different precision levels for public and private data.

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

---

## Author

**Ken Mwangi**

- GitHub: https://github.com/kenmwangi
- Email: hello@kenmwangi.com

---

## Vision

aregeo aims to become a location intelligence foundation for real estate applications across Kenya and eventually Africa.

The goal is simple:

> **Move African real estate from vague landmark-based descriptions to precise, searchable, verifiable geographic locations.**
