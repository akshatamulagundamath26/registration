def registration_datails(Student_ID, Student_Name, Course_Enroled, Academic_Year):
    result = {
        "Student_ID": f"{Student_ID}\n",
        "Student_Name": f"{Student_Name}\n",
        "Course_Enroled": f"{Course_Enroled}\n",
        "Academic_Year": Academic_Year
    }
    return result


if __name__ == "__main__":
    student_id = "101"
    student_name = "Alice"
    course_enroled = "abc"
    academic_year = 2000

    print(registration_datails(student_id, student_name, course_enroled, academic_year))
