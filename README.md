# Django Testing Examples


## tests

- [tests](https://github.com/misebox/django_testing_examples/tree/master/tests)
- [packages/tests](https://github.com/misebox/django_testing_examples/tree/master/packages/tests)


## pydantic schema

Actually pydantic schema definition is almost like a part of Tests.
- [packages/schemas.py](https://github.com/misebox/django_testing_examples/tree/master/packages/schemas.py)


## Initial Setup
```
# Clone the repository
gh repo clone misebox/django_testing_examples

# Create Python virtualenv
python3 -mvenv .venv
source .venv/bin/activate

# Install packages into virtualenv
make libs
```

## Testing
```
make test
```

## Run Development Server
```
make dev
```

