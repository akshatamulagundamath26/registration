from registration_displsy.py import registration_display

def test_registration_display():
    expected_output = {
        "Student_ID": "101\n",
        "Student_Name": "Alice\n",
        "Course_Enroled": "abc\n",
        "Academic_Year": 2000
    }

    assert registration_display("101", "Alice", "abc", 2000) == expected_output
