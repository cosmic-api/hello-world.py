Example Cosmic API
==============

hello-world.py is a sample application created to demonstrate basic features of Cosmic API.

Checkout [GitHub page](http://cosmic-api.github.com/hello-world.py) to see how it works.

## Setup

Get source.

```bash
git clone git://github.com/cosmic-api/hello-world.py.git
cd hello-world.py
```

Install Cosmic with [pip](http://www.pip-installer.org).

```bash
pip install cosmic
```

Optionally, if you use [virtualenv](http://www.virtualenv.org)

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Start the server

```bash
python hello_world_api.py
```

Now you have a Cosmic API running as a web server, listening to port `8080`.

## Play with the API

### Using Cosmic client

Our client can load any Cosmic APIs via `/spec.json` endpoint.

```python
>>> from cosmic.api import API
>>> client = API.load('http://localhost:8080/spec.json')
>>> client.actions.remember_me("Cosmic")
u"Hello, Cosmic! I'll remember you."
>>> client.actions.remember_me("Cosmic")
u'Welcome back, Cosmic.'
>>> client.actions.remember_me("Hello")
u"Hello, Hello! I'll remember you."
>>> client.actions.list_people()
[u'Cosmic', u'Hello']
```


### Using raw HTTP request

(You can use [Postman](https://chrome.google.com/webstore/detail/postman-rest-client/fdmmgilgnpjigdojojpjoooidkmcomcm?hl=en) for Chrome as well, it's an excellent app for playing with web APIs)

You can inspect how the API's spec looks like.

```bash
curl http://localhost:8080/spec.json
```
```json
{
  "url": "http://localhost:8080", 
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
  ],
  "models": []
}
```

Let's add a name.

```bash
curl -X POST \
  --header "Content-Type: application/json" \
  -d "\"Cosmic\"" \
  http://localhost:8080/actions/remember_me
```
```json
"Hello, Cosmic! I'll remember you."
```

Try adding the same name again.

```bash
curl -X POST \
  --header "Content-Type: application/json" \
  -d "\"Cosmic\"" \
  http://localhost:8080/actions/remember_me
```
```json
"Welcome back, Cosmic."
```

Add another name.

```bash
curl -X POST \
  --header "Content-Type: application/json" \
  -d "\"Hello\"" \
  http://localhost:8080/actions/remember_me
```
```json
"Hello, Hello! I'll remember you."
```

Now let's see the list of people -

```bash
curl -X POST \
  --header "Content-Type: application/json" \
  http://localhost:8080/actions/list_people
```
```json
["Cosmic", "Hello"]
```


### License

Copyright (C) 2013 8313547 Canada Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

