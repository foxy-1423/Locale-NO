import json

# Function to read the text file with extracted words and their numeric IDs
def read_words_with_numeric_ids_from_text_file(text_file):
    words_with_numeric_ids = {}
    with open(text_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(': ', 1)
                if len(parts) == 2:
                    numeric_id, word = parts
                    words_with_numeric_ids[int(numeric_id)] = word
                else:
                    print(f"Skipping invalid line: {line}")
    return words_with_numeric_ids

# Function to save the recombined data to a JSON file with proper encoding
def save_json_to_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Function to recombine the words with numeric IDs and the modified JSON data
def recombine_data_with_numeric_ids(json_data, words_with_numeric_ids):
    def replace_ids_with_words(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, int):
                    data[key] = words_with_numeric_ids.get(value, value)
                else:
                    replace_ids_with_words(value)
        elif isinstance(data, list):
            for index, item in enumerate(data):
                if isinstance(item, int):
                    data[index] = words_with_numeric_ids.get(item, item)
                else:
                    replace_ids_with_words(item)

    copied_data = copy_json_data(json_data)  # Create a copy of the modified JSON data
    replace_ids_with_words(copied_data)
    return copied_data

# Function to create a copy of the original JSON data
def copy_json_data(data):
    return json.loads(json.dumps(data))

if __name__ == "__main__":
    # Replace 'output.json' with the path to your JSON file with numeric IDs
    json_file_with_ids = 'Temp_no.json'

    # Replace 'output.txt' with the path to your text file with numeric IDs
    text_file = 'Translated-no.txt'

    # Replace 'combined_output.json' with the desired output JSON file name
    combined_output_file = 'combined_output.json'

    with open(json_file_with_ids, 'r', encoding='utf-8') as file:
        json_data_with_ids = json.load(file)

    words_with_numeric_ids = read_words_with_numeric_ids_from_text_file(text_file)
    recombined_data = recombine_data_with_numeric_ids(json_data_with_ids, words_with_numeric_ids)

    # Save the recombined data to the combined JSON file
    save_json_to_file(recombined_data, combined_output_file)

    print(f"Recombined data saved to {combined_output_file}")
