# Imports
import importlib

from .wrappers.wrappers_all import wrapper_info


class Wrapper():
    @staticmethod
    def fetch(name):
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


    @staticmethod
    def initialize(wrapper_class, objective, search_space):
        return wrapper_class(objective, search_space)


    @staticmethod
    def print_info(wrapper_class):
        print("\n==== Wrapper info ====")
        print(f"Name: {wrapper_class.name}")
        print(f"Lib version: {wrapper_class.library_version}")
        print(f"Direction: {wrapper_class.default_direction}")

        print("\nConfig parameters:")
        for var_name, var_value in wrapper_class.Config.__dict__.items():
            if not var_name.startswith('__'):  # Exclude dunder (magic) methods
                print(f"- {var_name}: {var_value}")
        # wrapper_class
        print("======================\n")