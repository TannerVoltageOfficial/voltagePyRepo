import json

def json_reader(json_string, required_keys=None):
    """
    Read, validate, and process JSON data from a string.
    
    Args:
    json_string (str): The JSON string to process.
    required_keys (list): Optional list of keys that must be present in the JSON.
    
    Returns:
    dict: Processed JSON data if successful, None otherwise.
    """
    try:
        # Parse JSON string
        data = json.loads(json_string)
        
        # Validate JSON structure (if required_keys is provided)
        if required_keys:
            if not isinstance(data, dict):
                print("Error: JSON root should be an object")
                return None
            for key in required_keys:
                if key not in data:
                    print(f"Error: Missing required key '{key}'")
                    return None
        
        # Process JSON data (example: convert keys to uppercase)
        processed_data = {k.upper(): v for k, v in data.items()}
        
        return processed_data

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    json_string = '''
    {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "swimming", "cycling"]
    }
    '''

    required_keys = ["name", "age", "city"]

    result = json_reader(json_string, required_keys)

    if result:
        print("Processed JSON data:")
        print(result)
    else:
        print("Failed to process JSON data.")