try:
    if False:
        raise ValueError("An error occurred!")
except ValueError as e:
    लिखो(f"Caught an error: {e}")