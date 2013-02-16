### What is Cosmic?
[Cosmic](https://www.cosmic-api.com) is a high-level framework for crafting web APIs.
This page gives you an overview of how to write a simple Cosmic API.
Instructions on how to run this example can be found on [GitHub project](https://github.com/cosmic-api/hello-world.py).

### Analyzing the API

```python
from cosmic.api import API

# Define name of the API
api = API('cosmic_hello_world', 'http://localhost:8080')
```
`API` class is used to create new instance of Cosmic API.
First parameter is the name of the API, and it's required.
Second parameter is the URL of the API.(this is optional) (edit me later)

```python
# Set of people
people = set()
```

Create an empty set to hold names.

```python
@api.action(
  accepts={"type": "string"},
  returns={"type": "string"}
)
def remember_me(name):
  """Remember someone upto 10 people.
  """
  if name not in people:
    # Too many people to remember!
    if len(people) >= 10:
      people.pop()
    # Add new person
    people.add(name)
    return "Hello, %s! I'll remember you." % name
  else:
    return "Welcome back, %s." % name
```
Here we are declaring that this function will take a single `string` parameter,
and it'll return a `string` as well.


Note that it takes in regular python `str`.
Cosmic takes care of type conversions automatically, using `accepts` schema defined above.


What is happening under the hood is that HTTP request with JSON body data is parsed, validated, and normalized to python's native `str` type.


The return value also goes through same process as well, except in reversed order.
Returned native `str` is serialized into JSON, based on `returns` schema.


```python
# List people
@api.action(
  returns={
    "type": "array",
    "items": {"type": "string"}
  }
)
def list_people():
  """List everyone I know.
  """
  return list(people)
```

Second action, which takes no argument, returns list of names in the set.


Interesting part here is that the `returns` definition. In Cosmic, you can define complex models for the action's parameters or return values. All models are serialized/de-serialized automatically to/from JSON. 


Moreover, Cosmic does validations on all parameters and returns, so the function can always expect the parameters will be in correct type, as well as the returned values. If the function does not return correct type as defined in `returns` schema, it will raise exception. This is a wonderful feature since your API users can always expect to receive correct data type as defined in `returns` schema.


```python
# Start listening to HTTP requests
api.run(port=8080, debug=True)
```

Now you can start the HTTP server to serve requests.


Because Cosmic is very modular, you'll be able to use other HTTP servers as oppose to currently default `flask` web server.


***

Visit [Cosmic](https://www.cosmic-api.com) if you want to lean more.