# Open Library Books

A simple Python project that retrieves 50 book records from the Open Library Search API, filters books first published after 2000, and saves the results in a CSV file.

## Features

- Retrieves up to 50 book records from Open Library.
- Filters books published after 2000.
- Sorts the results by publication year and title.
- Saves the results to `books.csv`.

## Requirements

- Python 3
- requests

## Installation

Install the required library:

```bash
python -m pip install requests
```

## Usage

Run the script:

```bash
python main.py
```

The output file `books.csv` will be created in the project directory.

## CSV Columns

- `title`: Book title
- `author`: Author name(s)
- `year`: First publication year

## Data Source

Open Library Search API:
https://openlibrary.org/dev/docs/api/search
