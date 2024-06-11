
def print_info(wrapper):
    print("\n==== Wrapper info ====")
    print(f"Name: {wrapper.__class__.__name__}")
    print(f"Lib version: {wrapper.library_version}")
    print(f"Direction: {wrapper.default_direction}")

    print("\nConfig parameters:")
    for var_name, var_value in wrapper.config.items():
        if not var_name.startswith('__'):  # Exclude dunder (magic) methods
            print(f"- {var_name}: {var_value}")
    print("======================\n")