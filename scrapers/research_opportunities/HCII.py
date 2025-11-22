import csv
import os

# Canonical names – make sure these EXACTLY match the standard sheet
HCII_DEPARTMENT_NAME = "Human-Computer Interaction Institute"
HCII_COLLEGE_NAME = "School of Computer Science"


def build_contact_mapping(row):
    """
    Return a dict: { 'Full Name': 'andrewid' }.
    If we can't find an Andrew ID, we use "".
    """
    name = (row.get("Your Name") or "").strip()
    email = (row.get("Email Contact") or "").strip()

    andrew_id = ""
    if "@" in email:
        andrew_id = email.split("@", 1)[0].strip()

    # Fallback for missing name
    if not name:
        name = andrew_id or email

    # If still nothing, no contact
    if not name:
        return {}

    # If andrew_id is missing, spec says to use ""
    return {name: andrew_id}


def reformat_projects(infile, outfile):
    # Desired column order (Contact = dict, Department/College = lists)
    fieldnames = [
        "Project Title",
        "Contact",              # dict: { name: andrewid }
        "Description",
        "Prereqs",
        "Time Commitment",
        "Anticipated End Date",
        "Relevant Links",
        "College",              # list: [canonical college name]
        "Department",           # list: [canonical department name]
        "Position",
        "Paid/Unpaid",
        "Desired Skill Level",
    ]

    # Resolve paths relative to this script file
    base_dir = os.path.dirname(__file__)
    infile_path = os.path.join(base_dir, infile)
    outfile_path = os.path.join(base_dir, outfile)

    # ---- READ INPUT CSV ----
    with open(infile_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # ---- TRANSFORM ROWS ----
    new_rows = []  # <-- defined unconditionally, before we write
    for row in rows:
        # Position Type: e.g. "Research Assistant, Paid"
        parts = [p.strip() for p in row.get("Position Type:", "").split(",")]

        contact_mapping = build_contact_mapping(row)

        new_rows.append({
            "Project Title": (row.get("Project Title") or "").strip(),
            "Contact": contact_mapping,
            "Description": (row.get("Short Description") or "").strip(),
            "Prereqs": (row.get("Desired Skills") or "").strip(),
            "Time Commitment": (row.get("Time Commitment") or "").strip(),
            "Anticipated End Date": (row.get("Anticipated Project End Date") or "").strip(),
            "Relevant Links": (row.get("Project URL (optional)") or "").strip(),
            # lists instead of strings
            "College": [HCII_COLLEGE_NAME],
            "Department": [HCII_DEPARTMENT_NAME],
            "Position": parts[0] if len(parts) > 0 else "",
            "Paid/Unpaid": parts[1] if len(parts) > 1 else "",
            "Desired Skill Level": (row.get("Seeking:") or "").strip(),
        })

    # ---- WRITE OUTPUT CSV ----
    with open(outfile_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)


if __name__ == "__main__":
    # change "data.csv" to your actual downloaded form filename if needed
    reformat_projects("data.csv", "cleaned_projects.csv")
