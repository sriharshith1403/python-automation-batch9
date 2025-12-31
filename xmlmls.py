

import xml.etree.ElementTree as ET

def get_medical_issues(xml_file):
# Reads and parses the XML file.
    tree = ET.parse(xml_file)
#Retrieves the root element of the XML document.
    root = tree.getroot()
#empty list to store medical issues
    issues = []

    # Correct tag name
    #Finds all <medical_issue> tags anywhere in the XML.
    for issue in root.findall(".//medical_issue"):
    #issue.text gets the text inside the XML tag.strip() removes extra spaces 
        issues.append(issue.text.strip())

    # Sort alphabetically
    issues.sort()
    return issues

#Passes note.xml as the XML file.Stores the returned list in medical_issues.
# Call the function
medical_issues = get_medical_issues("note.xml")

print("Medical Issues (Alphabetical Order):")
for issue in medical_issues:
    #Prints each medical issue on a new line.
    print(issue)
