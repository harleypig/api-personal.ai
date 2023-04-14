# PersonalAI Python Library

This Python library provides a simple and convenient way to interact with the
[personal.ai](https://personal.ai)
[API](https://documenter.getpostman.com/view/13134732/TzscpSjZ).

personal.ai is an AI that helps you store and recall your memories, knowledge,
and experiences.

## What is this for?

This library is designed to help developers easily integrate their Python
applications with personal.ai. It allows you to perform common operations such
as creating memories, sending messages to the AI, uploading URIs, and
validating API keys.

## Installation via pip

Note: This package is not yet available on PyPI. The following instructions
are provided for when the package becomes available.

To install the PersonalAI Python library, simply run:

```bash
pip install personalai
```

## Get your own API key

To use this library, you will need an API key from personal.ai. You can obtain
your API key by following the instructions in the [personal.ai External API
documentation](https://docs.personal.ai/upload-and-sync/custom-integrations-external-api).

## Usage

Here's a simple example of how to use the PersonalAI Python library:

```python
from personalai import PersonalAI

api_key = "your_personal_ai_api_key"
pai = PersonalAI(api_key)

# Create a memory
memory_created = pai.create_memory("My first memory with PersonalAI!", "Notes")
print(f"Memory created: {memory_created}")

# Send a message to the AI
response = pai.ai_message("What is GPT-3?")
print(response)

# Upload a URI
uploaded = pai.upload_uri("https://example.com/article")
print(uploaded)

# Validate the API key
validation = pai.validate_key()
print(validation)
```

## Development

### Basic requirements

Python 3.6 or later
Poetry

### Cloning the repository

To clone the repository for development, run:

```bash
git clone https://github.com/harleypig/api-personal.ai.git
```

### Installing from the cloned repository

To install the library from the cloned repository, navigate to the repository
directory and run:

```bash
pip install -e .
```

### Contributing

Pull requests are welcome! Please ensure that your code is well-documented and
includes test cases for any new functionality.
