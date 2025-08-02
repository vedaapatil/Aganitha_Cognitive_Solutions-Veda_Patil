# PubMed Research Fetcher

A command-line tool to fetch research papers from PubMed and filter for pharmaceutical/biotech affiliations.

## Installation

Use [Poetry](https://python-poetry.org/) to manage dependencies:

```bash
poetry install
```

## Usage

```bash
poetry run get-papers-list "cancer research" -f results.csv
```

## Features

- Fetches papers from PubMed.
- Filters authors from pharmaceutical/biotech companies.
- Saves to CSV or prints to console.

## Project Structure

- `pubmed_fetcher/`: Module with main logic
- `tests/`: Placeholder for tests
