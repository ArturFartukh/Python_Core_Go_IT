def get_employees_by_profession(path, profession):
    result = []
    with open(path, 'r') as file:
        for employee in file.readlines():
            if profession in employee:
                app_emp = employee.replace(profession, '')
                result.append(app_emp.strip())
    return ' '.join(result)
