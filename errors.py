#######################
# Utility Error stuff #
#######################

def assert_is_type(data: any, dtype: type, name:str=None):
    """Asserts that data is an instance of type. Else it will throw a TypeError

    Args:
        data: The data to be checked
        dtype: the type to chek if data is an instance off
        name: the name of the variable. This will be used in the Error Message
    """
    assert isinstance(data, dtype), TypeError(
        f"{name} must be of type \"{dtype.__name__}\" but found \"{type(data).__name__}\"" 
        if name is not None else 
        f"type \"{type(data).__name__}\" is not allowed, must be \"{dtype.__name__}\""
    )