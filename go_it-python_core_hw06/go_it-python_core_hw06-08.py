def save_applicant_data(source, output):
    with open(output, 'w') as fh_w:
        for abit in source:
            student_txt = ''
            for key in abit:
                student_txt += str(f'{abit[key]},')
            fh_w.write(f'{student_txt[:-1]}\n')


# abiturients = [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     }
# ]

# save_applicant_data(abiturients, '/Users/ar4ik/Go_IT_Python/Projects/go_it-python_core_hws/go_it-python_core_hw06/test08.txt')
