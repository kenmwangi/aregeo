# Contributing to aregeo

Thank you for your interest in contributing to **aregeo**!

AREGeo is an open-source Python package for converting, validating, resolving, and verifying precise geographic locations for real estate and property applications.

Our goal is to provide reliable geospatial tools that help real estate platforms move beyond vague property descriptions such as *"behind the school"* or *"near the shopping centre"* by supporting precise geographic coordinates, administrative boundaries, proximity search, and location verification.

We welcome contributions of all kinds, including:

- Bug reports
- Feature requests
- Documentation improvements
- Code improvements
- Tests
- Geospatial datasets and integrations
- New geocoding providers
- Support for additional African countries

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating in the project.

---

## Getting Started

### Prerequisites

You will need:

- Python 3.13 or later
- [uv](https://docs.astral.sh/uv/)
- Git

### Fork and Clone the Repository

Fork the repository on GitHub, then clone your fork:

```bash
git clone https://github.com/YOUR_USERNAME/aregeo.git
cd aregeo
```

Add the upstream repository:

```bash
git remote add upstream https://github.com/kenmwangi/aregeo.git
```

Verify your remotes:

```bash
git remote -v
```

---

## Set Up the Development Environment

Install the project and development dependencies:

```bash
uv sync
```

This will create and manage the project's virtual environment automatically.

You can verify the installation by running:

```bash
uv run python -c "import aregeo; print('AREGeo installed successfully')"
```

---

## Development Workflow

Before submitting changes, run the following checks.

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

### Run Test Coverage

```bash
uv run pytest --cov=aregeo
```

All checks should pass before opening a pull request.

---

## Project Structure

```text
aregeo/
├── src/
│   └── aregeo/
│       ├── coordinates/
│       │   ├── distance.py
│       │   └── validator.py
│       │
│       ├── geocoding/
│       │   └── providers and geocoding services
│       │
│       ├── kenya/
│       │   └── Kenya-specific geographic services
│       │
│       ├── models/
│       │   └── location models
│       │
│       ├── services/
│       │   └── high-level location services
│       │
│       └── spatial/
│           └── geospatial indexing and proximity tools
│
├── tests/
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── pyproject.toml
└── uv.lock
```

Please keep new functionality organized within the appropriate module.

---

## Making Changes

### Create a Branch

Create a descriptive branch for your changes:

```bash
git checkout -b feature/add-county-boundaries
```

For bug fixes:

```bash
git checkout -b fix/geohash-boundary-search
```

Use descriptive branch names such as:

```text
feature/add-reverse-geocoding
feature/add-uganda-boundaries
fix/coordinate-validation
docs/improve-installation-guide
```

---

## Code Style

AREGeo follows modern Python development practices.

### Formatting and Linting

Code formatting and linting are handled by Ruff.

Run:

```bash
uv run ruff format .
uv run ruff check .
```

Please avoid manually formatting code against the configured formatter.

### Type Safety

AREGeo aims to maintain strong type safety.

Run:

```bash
uv run pyrefly check
```

Please add appropriate type annotations to new public APIs.

### General Guidelines

- Use clear and descriptive names.
- Keep functions focused on a single responsibility.
- Prefer small, composable functions.
- Add docstrings to public classes and functions.
- Avoid unnecessary dependencies.
- Maintain backwards compatibility where possible.
- Follow existing project patterns and conventions.

---

## Writing Tests

New functionality should include tests.

Tests are located in:

```text
tests/
```

For example:

```text
tests/
├── coordinates/
│   ├── test_distance.py
│   └── test_validator.py
│
├── kenya/
│   └── test_counties.py
│
└── spatial/
    └── test_geohash.py
```

Use descriptive test names:

```python
def test_valid_coordinates_are_accepted() -> None: ...


def test_invalid_latitude_is_rejected() -> None: ...
```

Run all tests:

```bash
uv run pytest
```

---

## Geographic Data Contributions

AREGeo works with geographic coordinates, administrative boundaries, and geospatial datasets.

When contributing geographic data:

- Clearly document the source of the data.
- Include the applicable license.
- Verify that redistribution is permitted.
- Document the coordinate reference system (CRS).
- Prefer standard formats such as GeoJSON where appropriate.
- Validate boundary accuracy before submitting data.

Do not add copyrighted, proprietary, or improperly licensed geographic datasets to the repository.

---

## Adding a New Country

One of AREGeo's long-term goals is to support precise property locations across Africa.

A new country implementation should generally follow this structure:

```text
src/aregeo/
└── countries/
    └── uganda/
        ├── __init__.py
        ├── boundaries.py
        ├── regions.py
        └── administrative.py
```

Country implementations should aim to support:

1. Country validation
2. Administrative boundary detection
3. Geographic coordinate validation
4. Location resolution
5. Extensibility for additional administrative levels

---

## Adding a Geocoding Provider

AREGeo may support multiple geocoding providers.

Examples include:

- OpenStreetMap-based providers
- Commercial geocoding providers
- Government geographic data services
- Regional mapping services

New providers should implement the project's common provider interface.

Providers should:

- Handle HTTP errors gracefully.
- Respect provider rate limits.
- Support timeouts.
- Provide useful error messages.
- Avoid exposing API keys.
- Include tests where practical.

Never commit API keys, access tokens, or other credentials to the repository.

---

## Commit Messages

Write clear and descriptive commit messages.

Examples:

```text
feat: add Kenya county boundary detection
fix: validate longitude range correctly
docs: improve installation instructions
test: add geohash encoding tests
refactor: simplify location confidence calculation
```

We recommend following the Conventional Commits style:

```text
feat: new feature
fix: bug fix
docs: documentation changes
test: test changes
refactor: code restructuring
chore: maintenance tasks
```

---

## Pull Requests

Before opening a pull request, make sure:

- [ ] Code is formatted with Ruff.
- [ ] Ruff checks pass.
- [ ] Pyrefly type checking passes.
- [ ] All tests pass.
- [ ] New functionality includes appropriate tests.
- [ ] Documentation has been updated where necessary.
- [ ] No secrets or credentials are included.
- [ ] Geographic data sources and licenses are documented.

### Pull Request Description

Please clearly explain:

- What problem does this change solve?
- What changes were made?
- Are there any breaking changes?
- How was the change tested?

Keep pull requests focused on a single feature or fix whenever possible.

---

## Reporting Bugs

When reporting a bug, please include:

- A clear description of the problem.
- Steps to reproduce the issue.
- Expected behavior.
- Actual behavior.
- Python version.
- AREGeo version.
- Operating system.
- Relevant error messages or tracebacks.

Please avoid including sensitive location information in public bug reports.

---

## Feature Requests

Feature requests are welcome.

When requesting a feature, please explain:

- The problem you are trying to solve.
- Your proposed solution.
- How the feature could benefit AREGeo users.
- Any alternative approaches you considered.

---

## Security Issues

Please do not publicly disclose security vulnerabilities before they can be investigated.

For security concerns, contact the project maintainers privately at:

hello@kenmwangi.com

---

## Community

Please be respectful and constructive when participating in the AREGeo community.

By participating in this project, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Thank You

Every contribution helps improve AREGeo.

Whether you improve documentation, report a bug, add tests, contribute geographic data, or build a new feature, your contribution is appreciated.

Together, we can build better tools for precise property location intelligence across Kenya and Africa.