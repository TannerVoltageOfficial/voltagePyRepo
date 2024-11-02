import json

def read_json_list_from_string(json_string):
    try:
        data = json.loads(json_string)
        
        if isinstance(data, list):
            print(f"Successfully parsed JSON list with {len(data)} items.")
            return data
        else:
            print("Error: The JSON string does not contain a list at the top level.")
            return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the string.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    return None

def process_list(json_list):
    if json_list is not None:
        for index, item in enumerate(json_list, 1):
            print(f"Item {index}:")
            for key, value in item.items():
                print(f"  {key}: {value}")
            print()

# Usage example
json_string = '''
[
    {"name": "John Doe", "age": 30, "city": "New York"},
    {"name": "Jane Smith", "age": 25, "city": "San Francisco"},
    {"name": "Bob Johnson", "age": 35, "city": "Chicago"}
]
'''

json_list = read_json_list_from_string(json_string)
process_list(json_list)