# Contributing to StratoWind

Thanks for your interest in contributing to StratoWind.

## Development setup

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Running tests

```bash
pytest -q
```

## Contribution guidelines

- Keep code readable and well documented.
- Add or update tests for any behavior change.
- Prefer small, focused pull requests.
- Keep analysis functions generic and reusable.
- Do not add platform-specific secrets or private data to the repository.

## Pull request checklist

- tests pass
- docs updated when needed
- examples remain runnable
- the change supports open-source usability
