from registration import registration_datails.py

def test_registration_details():
    expected_output = {
        "Student_ID": "101\n",
        "Student_Name": "Alice\n",
        "Course_Enroled": "abc\n",
        "Academic_Year": 2000
    }

    assert registration_datails("101", "Alice", "abc", 2000) == expected_output
