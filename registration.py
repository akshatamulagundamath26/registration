import pytest
def registration_datails(Student_ID,Student_Name,Course_Enroled,Academic_Year):
    result= (
        f"Student_ID:{id}\n"
        f"Student_Name:{name}\n"
        f"Course_Enroled:{course}\n"
        f"Academic_Year:{year}\n"
    )
    return result
if __name__ == "__main__":
    student_id="101"
    student_name="Alice"
    course_enroled="abc"
    academic_year=2000
    print(registration_details(student_id,student_name,course_enroled,academic_year))
