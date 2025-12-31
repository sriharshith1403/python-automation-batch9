from xmlmls import get_medical_issues

def test_get_medical_issues():
    result = get_medical_issues("note.xml")
    expected = ["Asthma", "Diabetes","Heart Attack", "Hypertension"]
    assert result == expected
