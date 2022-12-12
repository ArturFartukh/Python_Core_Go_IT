import csv


def write_contacts_to_file(filename, contacts: list):
    with open(filename, 'w', newline='') as fh:
        writer = csv.DictWriter(fh, contacts[0].keys())
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as fh:
        contacts_csv = csv.DictReader(fh)
        contacts = []
        for contact in contacts_csv:
            if contact['favorite'] == 'True':
                contact['favorite'] = True
            elif contact['favorite'] == 'False':
                contact['favorite'] = False
            contacts.append(contact)
        return contacts
