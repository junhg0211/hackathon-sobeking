from json import load

with open('secret.json', 'r') as file:
    secret = load(file)

def get_const(path):
    result = secret
    while path:
        result = result.get(path.pop(0))

        if result is None:
            return

    return result
