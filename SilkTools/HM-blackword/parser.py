#!/usr/bin/python3
# -*-coding:utf-8 -*-


import csv
import json


def parser(file_obj, json_file_name):
    csv_reader = csv.reader(file_obj)
    header_row = next(csv_reader)
    query_params = list()
    for val in csv_reader:
        query_dict = {}
        if val == header_row:
            continue
        map(lambda x: query_dict.update({header_row[x]: val[x]}),
        [value for value in range(0, len(header_row))])
        if query_dict in query_params:
            continue
        query_params.append(query_dict)
    with open(json_file_name, "wb") as fx:
        fx.write(json.dumps({"data": query_params}))


if __name__ == '__main__':
    base_path = "your csv base path"
    write_json_path = "your json base path"
    csv_file_obj = open(base_path, 'rb')
    parser(csv_file_obj, write_json_path)
