from cosmic.api import API

# Define name of the API
api = API('cosmic_hello_world', 'http://localhost:8080')

# Set of people
people = set()


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


# Start listening to HTTP requests
api.run(port=8080)
