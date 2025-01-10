def outer_function(x):

    def inner_function(y):
        print(f"Inner function called with {y}")
    inner_function(x)
outer_function(7)