import re

# Step 1: Create a sample text file with data (you can modify this part)
sample_text = """
Hello team,
Please contact us at support@example.com or hr@company.org.
Also, reach out to admin123@mail.co.in for urgent issues.
Marketing team: ads_team@gmail.com, connect@brand.in
Thank you,
Hari
"""

input_file = "input.txt"
output_file = "output_emails.txt"

# Write sample text to input file
with open(input_file, "w", encoding="utf-8") as f:
    f.write(sample_text)

print(f"📄 Sample text file '{input_file}' created successfully!\n")

# Step 2: Read the content from the text file
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Step 3: Use regex to extract all email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

# Step 4: Remove duplicates and sort
unique_emails = sorted(set(emails))

# Step 5: Write extracted emails to output file
with open(output_file, "w", encoding="utf-8") as file:
    if unique_emails:
        file.write("\n".join(unique_emails))
        print(f"✅ {len(unique_emails)} email(s) found and saved to '{output_file}'.\n")
    else:
        file.write("No emails found.")
        print("⚠️ No email addresses found in the input file.\n")

# Step 6: Display the result
print("📧 Extracted Emails:")
for email in unique_emails:
    print(" -", email)
