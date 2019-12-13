import json


def main():
    with open('grades.json') as f:
        grades = json.load(f)

        print("Exam Results for Class 28")
        print("=========================")

        for entry in grades:
            print("Student " + str([entry]['student_id']) + " scored:")
            print("")


if __name__ == "__main__":
    main()
