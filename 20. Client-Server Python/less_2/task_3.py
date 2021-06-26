import yaml


def write_to_yaml():
    data_to_yaml = {
        'first': [1, 2, 3, 4, 5],
        'second': 25,
        'third': {
            'key1': '€1',
            'key2': '€2'
        }
    }

    with open('result.yaml', 'w') as f_yaml:
        yaml.dump(data_to_yaml, f_yaml, allow_unicode=True)

    with open("result.yaml", 'r') as f:
        f_n_content = yaml.load(f, Loader=yaml.FullLoader)
        print(data_to_yaml == f_n_content)


if __name__ == "__main__":
    write_to_yaml()
