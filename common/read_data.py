import yaml
def read_yaml(file_path):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
        return data

