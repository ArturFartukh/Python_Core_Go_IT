def get_grade(key=None):
    ects_grade = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    return ects_grade.get(key)


def get_description(key=None):
    ects_dscrp = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough",
                  "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
    return ects_dscrp.get(key)
