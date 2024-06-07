# Imports
from .wrappers.wrappers_all import wrapper_info
import importlib


def fetch_wrapper(name):
    # Dynamically import and select the specified wrapper
    for module_path, class_name, opt_name in wrapper_info:
        if opt_name.lower() == name.lower():
            try:
                # Dynamically import the module and get the class
                module = importlib.import_module(module_path)
                wrapper_class = getattr(module, class_name)
                return wrapper_class
            except ImportError:
                raise ImportError(f"Required library for {opt_name} is not installed.")
            except AttributeError:
                raise ImportError(f"{class_name} not found in {module_path}.")

    # Raise an error if no matching wrapper is found
    raise ValueError(f"No wrapper with name '{name}' found.")


def initialize_wrapper(wrapper_class, objective, search_space):
    return wrapper_class(objective, search_space)