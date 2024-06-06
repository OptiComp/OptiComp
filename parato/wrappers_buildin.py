# Imports
from parato.wrappers.wrappers_all import get_wrappers

def select_wrapper(name):
    # Get a list of all available wrappers
    wrappers = get_wrappers()

    # Filter wrappers by name
    selected_wrappers = [wrapper for wrapper in wrappers if wrapper.name == name]

    # Error if wrapper does not exist
    if not selected_wrappers:
        raise ValueError(f"No wrapper with name '{name}' found.")

    return selected_wrappers[0]