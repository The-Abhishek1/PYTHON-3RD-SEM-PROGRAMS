class ExampleClass:
    # Constructor
    def __init__(self):
        print("Constructor called")

    # Destructor
    def __del__(self):
        print("Destructor called")

# Create an instance of the ExampleClass
example = ExampleClass()

# Delete the instance of the ExampleClass
del example
