from cosmic.tools import normalize_schema
from cosmic.api import API


# Define name of the API
api = API.create('cosmic_hello_world')

# Set of people
people = set()


@api.action(
    accepts=normalize_schema({"type": "string"}),
    returns=normalize_schema({"type": "string"})
)
def remember_me(name):
  """Remember names upto 10 people.
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


@api.action(
    returns=normalize_schema({
        "type": "array",
        "items": {"type": "string"}
    })
)
def list_people():
  """List everyone I know.
  """
  return list(people)


# Start listening to HTTP requests
api.run(port=8080, debug=True)
