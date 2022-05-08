import csv
from random import randint

def leave(): # Leave Safely
    try:
        fopen.close()
    except:
        pass
    input("Exit?")
    exit()

# Get CSV Filename and check if it exist.
print("Make sure header of name and phone column in CSV is 'name' and 'phone' RESPECTIVLY without the single quotes.")
csv_filename = input("CSV Filename: ").strip()
try:
    if not csv_filename.endswith(".csv"): csv_filename += ".csv"
    fopen = open(csv_filename, 'r', encoding="UTF-8")
except:
    print("Error with Filename")
    leave()

# Add Constant Pattern to the contact names.
postfix_name = input("Text added to end of contact name(leave empty if you want): ")

contact_counter = 0 # Counter of Contacts written to .vcf
# output files with RANDOM names
output_filename = "Vcard_output_" + str(randint(1, 100)) + ".vcf"
with open(output_filename, 'w', encoding="UTF-8") as f:
    reader = csv.DictReader(fopen)
    for row in reader:
        try:
            contact_name = row['name'] + postfix_name # Contact Name
            phone = row['phone'] # Phone Number
            # Syntax of Vcard(.vcf)
            f.write(f"BEGIN:VCARD\nVERSION:2.1\nN:;{contact_name};;;\nFN:{contact_name}\nTEL;CELL:{phone}\nEND:VCARD\n")
            contact_counter += 1 # Count Contact
        except: # Inform me with Errors.
            print(f"Row --> {row}\nSkipped, Count of Columns is not.")

print(f"Done, {contact_counter} Conatacs IN {output_filename}")

leave()