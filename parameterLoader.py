from json import load

def load_parameters(model_path: str):
    """Loads the Parameters asociated with the model located at the specified path

    Args:
        model_path: The Path the model is located at. Warning this function does not provide path traversal protection
    
    Returns:
        The contents of the parameters.json file for that model
    """
    with open(f"{model_path}/parameters.json") as file:
        return load(file)