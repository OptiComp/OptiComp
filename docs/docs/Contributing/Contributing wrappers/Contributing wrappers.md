# Contributing Wrappers

To contribute a wrapper to OptiComp, please follow these steps:


## Step 1: Create a Wrapper

Refer to the [examples](link) and [documentation](link) for guidance on creating wrappers. You can also examine existing wrappers in the `wrapper_zoo` for inspiration.

Make sure the name of the wrapper class starts with the name of the library you're using and ends with the optimization algorithm:
- OptunaGridSearch
- HyperoptTPE

<br>

## Step 2: Add to `wrapper_zoo`

Once your wrapper is ready, add it to the wrapper list in the `__init__.py` file of the `wrapper_zoo` module.

Ensure the name of your wrapper in this file matches the wrapper class name. Convert to lowercase, add underscores if necessary, and prefix with `fetch_`.
- MyCustomWrapper == fetch_my_custom_wrapper
- AnotherExample == fetch_another_example

<br>

## Step 3: Follow the Contribution Guide

Finally, follow the [contribution](link) guide to complete the contribution process. This includes creating a pull request with your changes.

Thank you for contributing to OptiComp! Your wrapper will help expand the flexibility and capabilities of our tools.
