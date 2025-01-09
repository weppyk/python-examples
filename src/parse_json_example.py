import json

def parse_json(json_string):
    return json.loads(json_string)

if __name__ == "__main__":
    sample_json = '{"name": "John", "age": 30, "city": "New York"}'
    parsed_data = parse_json(sample_json)
    print(parsed_data)
