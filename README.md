
# Django Openai

A simple Django rest API server that integrates with OpenAI

(DISCLAIMER)

The current Python version used is 3.11.8


## About this project

This is built using Django and Django Rest Framework (DRF) to create a simple REST API

It uses the openai-python python package (https://github.com/openai/openai-python) to add support for ChatGPT3.5 chat completions


## Installation

Download the project to a local folder and make sure to add the required dependencies

```bash
  python -m pip install Django
  python -m pip install djangorestframework
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/firasbarakat/django-openai
```

Go to the project directory

```bash
  cd django-openai
```

Install dependencies

```bash
  python -m pip install openai
  python -m pip install django-cors-headers
```

Place your OpenAI API Key in this file (django-openai/api/views.py)

```bash
  client = OpenAI(
    api_key="{PLACE YOUR KEY HERE}",
  )
```

Start the server

```bash
  python manage.py runserver
```

Make sure the server is running by visiting http://localhost:8000?format=json, you should get the following response

```bash
  {
    "error": "false",
    "result": "API Works :)"
  }
```
## Usage/Examples

Sample Request
```javascript
  fetch('http://localhost:8000/prompt?format=json', {
    method: 'post',
    headers: {'Content-Type':'application/json'},
    body: {
      "prompt": "Red shirt with a crewneck and long sleeves"
    }
  })
```

Sample Response
```javascript
  {
      "color": "red",
      "neckType": "crewneck",
      "sleeveLength": "long"
  }
```

