

email_id="gouri@gmail.com"

at_index=email_id.index("@")

user_name=email_id[:at_index]
print(user_name)
domain=email_id[at_index:]
print(domain)
