import json


def parser(file_path, json_path):
    with open(file_path, "r",encoding="UTF-8") as fx:
        data = fx.readlines()
        header_rows = []
        json_params = []
        for index, line in enumerate(data):
            if index == 0:
                print(line)
                header_rows = line.split(';')
                continue
            query_dict = {}
            for index, value in enumerate(line.split(';')):
                if value !='\n':
                     query_dict.update({header_rows[index]: value})
            print(query_dict)
            json_params.append(query_dict)
    with open(json_path, 'w') as fx:
        fx.write(json.dumps({"data": json_params},ensure_ascii=False))


if __name__ == '__main__':
    base_path = "data.TXT"
    json_path = "data.json"
    parser(file_path=base_path, json_path=json_path)
