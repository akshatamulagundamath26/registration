def registration_datails(Student_ID, Student_Name, Course_Enroled, Academic_Year):
    result = {
        "Student_ID": f"{Student_ID}\n",
        "Student_Name": f"{Student_Name}\n",
        "Course_Enroled": f"{Course_Enroled}\n",
        "Academic_Year": Academic_Year
    }
    return result


if __name__ == "__main__":
    Student_ID = "101"
    Student_Name = "Alice"
    Course_Enroled = "abc"
    Academic_Year = 2000

    print(registration_datails(Student_ID, Student_Name, Course_Enroled, Academic_Year))
