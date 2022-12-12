def sequence_buttons(string):
    old_phone_dict = {ord(' '): '0',
                      ord('.'): '1',
                      ord(','): '11',
                      ord('?'): '111',
                      ord('!'): '1111',
                      ord(':'): '11111',
                      ord('A'): '2',
                      ord('B'): '22',
                      ord('C'): '222',
                      ord('D'): '3',
                      ord('E'): '33',
                      ord('F'): '333',
                      ord('G'): '4',
                      ord('H'): '44',
                      ord('I'): '444',
                      ord('J'): '5',
                      ord('K'): '55',
                      ord('L'): '555',
                      ord('M'): '6',
                      ord('N'): '66',
                      ord('O'): '666',
                      ord('P'): '7',
                      ord('Q'): '77',
                      ord('R'): '777',
                      ord('S'): '7777',
                      ord('T'): '8',
                      ord('U'): '88',
                      ord('V'): '888',
                      ord('W'): '9',
                      ord('X'): '99',
                      ord('Y'): '999',
                      ord('Z'): '9999'
                      }
    return string.upper().translate(old_phone_dict)


# print(sequence_buttons('Hello, World!'))
