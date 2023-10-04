import json

# Function to recursively extract words from JSON data and replace them with numeric IDs
def extract_words_with_numeric_ids(data, id_counter):
    words_with_numeric_ids = {}
    
    def assign_numeric_id(word):
        nonlocal id_counter
        numeric_id = id_counter
        id_counter += 1
        words_with_numeric_ids[numeric_id] = word
        return numeric_id
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = assign_numeric_id(value)
            else:
                words_with_numeric_ids.update(extract_words_with_numeric_ids(value, id_counter))
    elif isinstance(data, list):
        for index, item in enumerate(data):
            if isinstance(item, str):
                data[index] = assign_numeric_id(item)
            else:
                words_with_numeric_ids.update(extract_words_with_numeric_ids(item, id_counter))
    
    return words_with_numeric_ids

# Function to create a copy of the original JSON data
def copy_json_data(data):
    return json.loads(json.dumps(data))

# Function to save the JSON data to a file
def save_json_to_file(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

# Function to save the extracted words with numeric IDs to a text file
def save_words_with_numeric_ids_to_text_file(words_with_numeric_ids, text_output_file):
    with open(text_output_file, 'w') as file:
        for numeric_id, word in words_with_numeric_ids.items():
            file.write(f"{numeric_id}: {word}\n")

if __name__ == "__main__":
    # Replace 'input.json' with the path to your JSON file
    input_file = 'en.json'

    # Replace 'output.json' with the desired output JSON file name
    output_json_file = 'output-en.json'

    # Replace 'output.txt' with the desired output text file name
    output_text_file = 'output-en.txt'

    with open(input_file, 'r') as file:
        original_data = json.load(file)

    # Create a copy of the original JSON data to avoid modifying the original
    copied_data = copy_json_data(original_data)

    id_counter = 1
    words_with_numeric_ids = extract_words_with_numeric_ids(copied_data, id_counter)

    # Save the modified JSON data with numeric IDs to the output JSON file
    save_json_to_file(copied_data, output_json_file)

    # Save the extracted words with numeric IDs to the output text file
    save_words_with_numeric_ids_to_text_file(words_with_numeric_ids, output_text_file)

    print(f"Extracted words with numeric IDs saved to {output_text_file}")
    print(f"Modified JSON data saved to {output_json_file}")
