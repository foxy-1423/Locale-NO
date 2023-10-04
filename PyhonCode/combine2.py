import json

def merge_json_files(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)

    with open(file2_path, 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)

    # Recursively update data1 with data2
    def update_data(data1, data2):
        if isinstance(data1, dict) and isinstance(data2, dict):
            for key, value in data2.items():
                if key in data1:
                    data1[key] = update_data(data1[key], value)
                else:
                    data1[key] = value
            return data1
        elif isinstance(data1, list) and isinstance(data2, list):
            data1.extend(data2)
            return data1
        else:
            return data2

    updated_data = update_data(data1, data2)

    with open('merged_no_file.json', 'w', encoding='utf-8') as output_file:
        json.dump(updated_data, output_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    file1_path = 'en.json'  # Replace with the path to your first JSON file
    file2_path = 'no.json'  # Replace with the path to your second JSON file
    merge_json_files(file1_path, file2_path)
