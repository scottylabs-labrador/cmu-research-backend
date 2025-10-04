import csv

def reformat_projects(infile, outfile):
    # Desired column order
    fieldnames = [
        "Project Title",
        "Contact",
        "Description",
        "Prereqs",
        "Time Commitment",
        "Anticipated End Date",
        "Relevant Links",
        "Department",
        "Position",
        "Paid/Unpaid",
        "Desired Skill Level"
    ]

    with open(infile, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    new_rows = []
    for row in rows:
        # Map fields from original sheet(s) to the new format
        parts = [p.strip() for p in row.get("Position Type:", "").split(",")]
        new_rows.append({
            "Project Title": row.get("Project Title", "").strip(),
            "Contact": row.get("Email Contact", row.get("Your Name", "")).strip(),
            "Description": row.get("Short Description", "").strip(),
            "Prereqs": row.get("Desired Skills", "").strip(),
            "Time Commitment": row.get("Time Commitment", "").strip(),
            "Anticipated End Date": row.get("Anticipated Project End Date", "").strip(),
            "Relevant Links": row.get("Project URL (optional)", "").strip(),
            "Department": "HCII",
            "Position" : parts[0] if len(parts) > 0 else "",
            "Paid/Unpaid" : parts[1] if len(parts) > 1 else "",
            "Desired Skill Level" : row.get("Seeking:", "").strip()
        })

    # Write out in the desired format
    with open(outfile, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)

# Example usage:
reformat_projects("data.csv", "cleaned_projects.csv")
