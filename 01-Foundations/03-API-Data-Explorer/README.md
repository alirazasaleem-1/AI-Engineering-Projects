# Public API Data Explorer

A Python application that consumes the PokeAPI to search for any Pokémon and display useful information in a clean and readable format.

## Features

* Search for any Pokémon by name
* Retrieve Pokémon data from PokeAPI
* Validate API responses before using the data
* Handle 404 errors when a Pokémon is not found
* Handle 5xx server errors
* Handle network errors and request timeouts
* Retry failed network requests
* Normalize API data using a Python dataclass
* Separate API logic from application logic
* Automated tests using pytest

## Project Structure

```text
03-API-Data-Explorer/
├── app.py
├── src/
│   ├── api_client.py
│   ├── models.py
│   └── utils.py
├── tests/
│   └── test_api_client.py
├── .env.example
├── requirements.txt
└── README.md
```

## Technologies

* Python
* Requests
* Pytest
* PokeAPI
* Dataclasses

## How It Works

The user enters the name of a Pokémon. The application sends a GET request to the PokeAPI, validates the response, converts the required information into a `Pokemon` object, and displays the cleaned result.

```text
User Input
    ↓
app.py
    ↓
api_client.py
    ↓
PokeAPI
    ↓
JSON Response
    ↓
Validation
    ↓
Pokemon Model
    ↓
utils.py
    ↓
Clean Output
```

## Example

```text
Enter Pokemon name: pikachu

Name: Pikachu
ID: 25
Height: 4
Weight: 60
```

## Error Handling

The application handles several common API and network problems:

* `404` — Pokémon not found
* `429` — API rate limit reached
* `500+` — PokeAPI server error
* Request timeout — Request took too long
* Network errors — Connection-related problems
* Invalid API response — Required fields are missing

Failed network requests can be retried before the application gives up.

## API

This project uses [PokeAPI](https://pokeapi.co/).

The main endpoint used by the application is:

```text
https://pokeapi.co/api/v2/pokemon/{name}
```

The `{name}` value is replaced with the Pokémon entered by the user.

For example:

```text
https://pokeapi.co/api/v2/pokemon/pikachu
```

## Response Validation

The application does not blindly trust the API response. Before creating a `Pokemon` object, it checks that the required fields exist:

```text
name
id
height
weight
```

Only validated data is passed to the application.

## Testing

The project uses `pytest` for automated testing.

Run the tests with:

```bash
python -m pytest
```

The tests currently verify:

* A valid Pokémon returns the expected data
* An invalid Pokémon returns `None`
* The `Pokemon` model stores data correctly

## Installation

Clone the repository and navigate into the project directory.

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Run the tests:

```bash
python -m pytest
```

## Environment Variables

PokeAPI does not require an API key for this project, so no secret credentials are needed.

An `.env.example` file is included as part of the project structure for future API integrations that may require authentication.

## Assumptions and Limitations

* The application searches for one Pokémon at a time.
* The PokeAPI endpoint used for individual Pokémon lookup does not require pagination.
* Authentication is not required by PokeAPI for this project.
* API availability depends on the PokeAPI service and the user's internet connection.
* The application currently displays only basic Pokémon information: name, ID, height, and weight.
* Query parameters and pagination are not necessary for the main single-Pokémon lookup feature.

## Future Improvements

Possible future upgrades include:

* Streamlit dashboard
* Caching
* More advanced search and filtering
* Additional Pokémon information
* Async API requests
* Database storage
* Scheduled data collection
* Deployment as a web application

## Project Goal

This project demonstrates practical experience with:

* REST API integration
* HTTP requests and status codes
* JSON data handling
* Response validation
* Error handling
* Retry logic
* Data normalization
* Python modules and separation of concerns
* Automated testing

It is designed as a beginner-to-intermediate project to build practical API integration skills in Python.
