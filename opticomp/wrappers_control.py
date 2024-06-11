# Imports
import importlib

from .wrappers.wrapper_zoo import wrapper_info


class Wrapper():
    @staticmethod
    def fetch(name):
        # Dynamically import and select the specified wrapper
        for module_path, class_name in wrapper_info:
            if class_name.lower() == name.lower():
                try:
                    # Dynamically import the module and get the class
                    module = importlib.import_module(module_path)
                    wrapper = getattr(module, class_name)
                    return wrapper
                except ImportError as e:
                    raise ImportError(f"Required library '{e.name}' for {class_name} is not installed.")
                except AttributeError:
                    raise ImportError(f"{class_name} not found in {module_path}.")
        raise ValueError(f"No wrapper with name '{name}' found.")

    @staticmethod
    def initialize(wrapper, objective, search_space):
        return wrapper(objective, search_space)

    @staticmethod
    def print_info(wrapper):
        print("\n==== Wrapper info ====")
        print(f"Name: {wrapper.__name__}")
        print(f"Lib version: {wrapper.library_version}")
        print(f"Direction: {wrapper.default_direction}")

        print("\nConfig parameters:")
        for var_name, var_value in wrapper.Config.__dict__.items():
            if not var_name.startswith('__'):  # Exclude dunder (magic) methods
                print(f"- {var_name}: {var_value}")
        # wrapper_class
        print("======================\n")