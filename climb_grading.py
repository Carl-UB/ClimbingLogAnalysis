class AllGrades:
    winter_grades = {
        "I": 0,
        "I/II": 0.5,
        "II": 1,
        "II/III": 1.5,
        "III": 2,
        "IV": 3,
        "V": 4,
        "VI": 5,
        "VII": 6,
        "VIII": 7,
        "IX": 8,
        "X": 9,
        "XI": 10,
        "XII": 11
    }

    trad_grades = {
        "none": 1,
        "M":    1,
        "D":    2,
        "HD":   2.5,
        "VD":   3,
        "HVD":  4,
        "MS":   4.5,
        "S":    5,
        "HS":   6,
        "MVS":  6.5,
        "VS":   7,
        "HVS":  8,
        "E1":   9,
        "E2":   10,
        "E3":   11,
        "XS":   11, # ??
        "E4":   12,
        "E5":   13,
        "E6":   14,
        "E7":   15,
        "E8":   16,
        "E9":   17,
        "E10":  18,
        "E11":  19
    }

    boulder_grades = {
        "?":    1,
        "f?":   1,
        "VE":   1,
        "VM":   2,
        "VB":   3,
        "V0-":  3.5,
        "V0":   4,
        "V0+":  4.5,
        "V1":   5,
        "V2":   6,
        "V3":   7,
        "V3+":  7.5,
        "V4":   8,
        "V4+":  8.5,
        "V5":   9,
        "V5+":  9.5,
        "V6":   10,
        "V7":   11,
        "V8":   12,
        "V8+":  13,
        "V9":   14,
        "V10":  15,
        "V11":  16,
        "V12":  17,
        "V13":  18,
        "V14":  19,
        "V15":  20,
        "V16":  21,
        "V17":  22,
        "f2":   2,
        "f2+":  2.5,
        "f3":   3,
        "f3+":  3.5,
        "f4":   4,
        "f4+":  4.5,
        "f5":   5,
        "f5+":  6,
        "f6A":  7,
        "f6A+": 7.5,
        "f6B":  8,
        "f6B+": 8.5,
        "f6C":  9,
        "f6C+": 9.5,
        "f7A":  10,
        "f7A+": 11,
        "f7B":  12,
        "f7B+": 13,
        "f7C":  14,
        "f7C+": 15,
        "f8A":  16,
        "f8A+": 17,
        "f8B":  18,
        "f8B+": 19,
        "f8C":  20,
        "f8C+": 21,
        "f9A":  22,
    }

class Grade:
    # Underlying grade will be some easy to use numerical value
    def __init__(self, text_grade):
        self.numerical_grade, self.climb_type = self.interpret_grade(text_grade)
    def interpret_grade(text_grade):
        