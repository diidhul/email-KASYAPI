import csv
import re
from openpyxl import Workbook

# Read data from CSV file
data = []
with open("message.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) > 0:
            message = row[0]
            data.append(message)

# Create a new Excel workbook and select the active sheet
workbook = Workbook()
sheet = workbook.active

# Write headers
headers = [
    "Message",
    "Date",
    "Contact",
    "Company",
    "Address",
    "Country",
    "Phone",
    "Email",
    "Posted On",
    "Posted From",
    "Mobile No",
    "Email Address",
    "Products",
]
sheet.append(headers)

# Extract the required information using regex patterns
date_pattern = r"\[([\d:]+\s[APM]+),\s(\d+/\d+/\d+)\]"
contact_pattern = r"Contact:\s(.+?)\n"
company_pattern = r"Company:\s(.+?)\n"
address_pattern = r"Address:\s(.+?)\n"
country_pattern = r"Country:\s(.+?)\n"
phone_pattern = r"Phone:\s(\+\d+-\d+)\n"
email_pattern = r"Email:\s(.+?)\n"
posted_on_pattern = r"Posted on :\s(\d+-\w+-\d+)\n"
posted_from_pattern = r"Posted From :\s(.+?)\n"
mobile_pattern = r"Mobile No: (.+?)\n"
email_address_pattern = r"Email Address: (.+?)\n"

# Regex pattern for extracting product requests
product_pattern = r"(?:We want to buy|We are looking for|We need to source|We would like to buy|buy|need|import|importing|quote for|requirements)\s+(.+?)[.\n]"

# Iterate over each message in the data
for message in data:
    # Find matches for each pattern in the message
    date_match = re.search(date_pattern, message)
    contact_match = re.search(contact_pattern, message)
    company_match = re.search(company_pattern, message)
    address_match = re.search(address_pattern, message)
    country_match = re.search(country_pattern, message)
    phone_match = re.search(phone_pattern, message)
    email_match = re.search(email_pattern, message)
    posted_on_match = re.search(posted_on_pattern, message)
    posted_from_match = re.search(posted_from_pattern, message)
    mobile_match = re.search(mobile_pattern, message)
    email_address_match = re.search(email_address_pattern, message)

    # Extract the captured groups if matches are found
    date = date_match.group(2) if date_match else None
    contact = contact_match.group(1) if contact_match else None
    company = company_match.group(1) if company_match else None
    address = address_match.group(1) if address_match else None
    country = country_match.group(1) if country_match else None
    phone = phone_match.group(1) if phone_match else None
    email = email_match.group(1) if email_match else None
    posted_on = posted_on_match.group(1) if posted_on_match else None
    posted_from = posted_from_match.group(1) if posted_from_match else None
    mobile = mobile_match.group(1) if mobile_match else None
    email_address = email_address_match.group(1) if email_address_match else None

    # Extract the requested products
    products = re.findall(product_pattern, message)

    # Append the extracted information to the Excel sheet
    row = [
        message,
        date,
        contact,
        company,
        address,
        country,
        phone,
        email,
        posted_on,
        posted_from,
        mobile,
        email_address,
        ", ".join(products),
    ]
    sheet.append(row)

# Save the workbook to a file
workbook.save("extracted_data.xlsx")
