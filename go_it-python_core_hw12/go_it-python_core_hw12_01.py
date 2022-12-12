import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as fh:
        pickle.dump(contacts, fh)


def read_contacts_from_file(filename):
    with open(filename, 'rb') as fh:
        contacts = pickle.load(fh)
        return contacts
