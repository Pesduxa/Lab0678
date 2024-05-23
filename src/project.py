import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return None

if __name__ == "__main__":
    args = parse_arguments()
    if args.input_file.endswith('.json'):
        data = load_json(args.input_file)
        if data is not None:
            print("JSON file loaded successfully")