import json


def load_data(data):
    with open(data) as json_file:
        json_string = json_file.read()
        parsed_string = json.loads(json_string)
        return parsed_string


def pretty_print_json(data):
    pretty_print = (json.dumps(parsed_string, sort_keys=True, indent=4, ensure_ascii=False))
    return pretty_print 


if __name__ == '__main__':
    data = input("введите путь к файлу\n")
    parsed_string = load_data(data)
    print (pretty_print_json(parsed_string))
