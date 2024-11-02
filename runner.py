import json

def read_json_list(json_string):
	try:
		# Parse the JSON string
		data = json.loads(json_string)
		
		# Check if the parsed data is a list
		if isinstance(data, list):
			print(f"Successfully parsed JSON list with {len(data)} items.")
			return data
		else:
			print("Error: The JSON string does not contain a list at the top level.")
			return None
	except json.JSONDecodeError as e:
		print(f"Error: Invalid JSON format in the string. {str(e)}")
	except Exception as e:
		print(f"An unexpected error occurred: {str(e)}")
	
	return None

def process_list(json_list):
	if json_list is not None:
		for index, item in enumerate(json_list, 1):
			print(f"Item {index}:")
			print(f"  Value: {item}")
json_string2 = '''
["apple", "banana", "cherry", "date"]
'''
print("\nProcessing second JSON string (list of strings):")
json_list2 = read_json_list(json_string2)
process_list(json_list2)