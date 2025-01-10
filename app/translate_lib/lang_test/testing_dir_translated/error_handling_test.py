try:
    if False:
        raise ValueError("An error occurred!")
except ValueError as e:
    write(f"Caught an error: {e}")