Example Cosmic API
==============

hello-world.py is a sample application in order to demonstrate basic features of Cosmic API.

## Setup

Get source.

```
git clone git://github.com/cosmic-api/hello-world.py.git
cd hello-world.py
```

Install Cosmic with pip.

```
pip install cosmic
```

Optionally, if you use `vertualenv`

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Start the server

```
python hello_world_api.py
```

Now you have a Cosmic API running as a web server, listening to port `8080`.

## Play with Cosmic client



## Play with the API through raw requests

(You can use [Postman](https://chrome.google.com/webstore/detail/postman-rest-client/fdmmgilgnpjigdojojpjoooidkmcomcm?hl=en) for Chrome as well, it's an excellent app for playing with web APIs)

Checkout the specification of the API.

```
curl http://localhost:8080/spec.json
```

Which should return -
```json
{
  "models": [], 
  "name": "cosmic_hello_world", 
  "actions": [
    {
      "name": "remember_me",
      "accepts": {"type": "string"},
      "returns": {"type": "string"}
    }, 
    {
      "name": "list_people",
      "returns": {
        "type": "array",
        "items": {"type": "string"}
      }
    }
  ]
}
```

Let's add a name.

```
curl -X POST --header "Content-Type: application/json" -d "\"Cosmic\"" http://localhost:8080/actions/remember_me
```

Returns -
```json
"Hello, Cosmic! I'll remember you."
```

Add another name.

```
curl -X POST --header "Content-Type: application/json" -d "\"Hello\"" http://localhost:8080/actions/remember_me
```

```json
"Hello, Hello! I'll remember you."
```

Now let's see the list of people -

```
curl -X POST --header "Content-Type: application/json" http://localhost:8080/actions/list_people
```

```json
["Cosmic", "Hello"]
```

