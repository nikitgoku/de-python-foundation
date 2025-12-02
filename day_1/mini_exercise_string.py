# Question 1:
# Write a function which takes in email addresses as list of string 
# Convert email address from a list of strings to secured format by replacing
# characters between first character and last character before the domain name with '*'
# For example: abcxyz444@email.com -> a*******4@email.com
from loguru import logger

def secure_email_addresses(email_list):
    # Create an empty list to store secured email addresses
    secured_emails = []
    for email in email_list:
        try:
            # Split the email into local part and domain
            local_part, domain = email.split('@')
            if len(local_part) > 2: # Only secure if local part has more than 2 characters
                # Create the secured local part
                secured_local = local_part[0] + '*' * len(local_part[1:-1]) + local_part[-1]
            else:
                secured_local = local_part  # No change for local parts with 2 or fewer characters
            
            # Combine secured local part with domain using F-string formatting
            secured_emails.append(f"{secured_local}@{domain})")
        except ValueError:
            # Handle invalid email format
            logger.error(f"Invalid email format: {email}")
            secured_emails.append(email)  # Append the original email if format is invalid

    return secured_emails

email_list = ["abcxyz444@email.com", "nikit888@email.com", "aliceInWorderland@whatmail.com", "email.com"]
secured_emails = secure_email_addresses(email_list)
logger.info(f"Secured Email Addresses: {secured_emails}")

# Question 2:
# Write a functions which takes in a list of strings containing server locations, and returns
# a list of unque IP addresses from the server locations.
def extract_unique_ip_addresses(server_locations):
    # Define a set to store unique IP addresses
    unique_ips = set()
    for location in server_locations:
        try:
            # Split the location string to find the IP addresses
            parts = location.split('/server/')
            if len(parts) > 1:  # If '/server/' is found in the string
                # Get the part after '/server/' where the IP address is located
                ip_and_path = parts[1]
                # Split to isolate the IP address
                ip_adddress = ip_and_path.split('/')
                # Add the IP address to the set
                unique_ips.add(ip_adddress[0])
        except IndexError:
            # Handle any unexpected format issues
            logger.error(f"Unexpected format in server location: {location}")
            continue

    return list(unique_ips)


server_locations = [
    "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
    "/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
    "/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
    "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv",
    "/region//us-east-c/north/resource/vminsatnce/subsid/"
]

print(f"Unique IP Addresses: {extract_unique_ip_addresses(server_locations)}")