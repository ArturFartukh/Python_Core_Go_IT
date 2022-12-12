import json


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as fh:
        json.dump({'contacts': contacts}, fh)


def read_contacts_from_file(filename):
    with open(filename, 'r') as fh:
        contacts = json.load(fh)
        return contacts['contacts']
