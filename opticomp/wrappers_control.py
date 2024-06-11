# Imports
# import importlib

# from .wrappers.wrapper_zoo import wrapper_info


# def fetch(name):
#     for module_path, class_name in wrapper_info:
#         if class_name.lower() == name.lower():
#             try:
#                 module = importlib.import_module(module_path)
#                 wrapper = getattr(module, class_name)
#                 return wrapper
#             except ImportError as e:
#                 raise ImportError(f"Required library '{e.name}' for {class_name} is not installed.")
#             except AttributeError:
#                 raise ImportError(f"{class_name} not found in {module_path}.")
#     raise ValueError(f"No wrapper with name '{name}' found.")


# def initialize(wrapper, objective, search_space):
#     return wrapper(objective, search_space)


def print_info(wrapper):
    print("\n==== Wrapper info ====")
    print(f"Name: {wrapper.__class__.__name__}")
    print(f"Lib version: {wrapper.library_version}")
    print(f"Direction: {wrapper.default_direction}")

    print("\nConfig parameters:")
    for var_name, var_value in wrapper.Config.__dict__.items():
        if not var_name.startswith('__'):  # Exclude dunder (magic) methods
            print(f"- {var_name}: {var_value}")
    print("======================\n")