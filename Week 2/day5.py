contacts = [
    {"name": "James Omondi", "phone number": "0712345678","skill": "welding", "city": "Nairobi"},
    {"name": "Joseph Washira", "phone number": "023456789", "skill": "tiling", "city": "Kiambu"},
    {"name": "Stephan Nyaga", "phone number": "0734567890", "skill": "phone repair", "city": "Kisumu"},
    {"name": "Peter Kamau", "phone number": "07345678901", "skill": "copywriting", "city": "Mombasa"},
    {"name": "Solomon Mbai", "phone number": "07456789012", "skill": "upholstery", "city": "Kericho"},
]
print("Contacts stored:", len(contacts))
print(contacts[0])
print("=====CONTACT BOOK====")
for i, contact in enumerate(contacts):
    print(f"\n{i+1}. {contact['name']}")
    print(f"Phone number: {contact['phone number']}")
    print(f"Skill: {contact['skill']}")
    print(f"City: {contact['city']}")

# Search by name
search_name = "Peter Kamau"
found = False
for contact in contacts:
    if contact["name"]== search_name:
        print("Contact found:")
        print(f"Name: {contact["name"]}")
        print(f"Phone number: {contact['phone number']}")
        print(f"Skill: {contact['skill']}")
        print(f"City: {contact['city']}")
        found = True
        break
if not found: 
    print("No contact found with name:", search_name)

# Search by city
search_city = "Nairobi"
print(f"Contacts in {search_city}:")
for contact in contacts:
    if contact['city'] == search_city:
        print(f"{contact['name']} | {contact['skill']} | {contact['phone number']}")
print("Before:", len(contacts),"contacts")

# Add a new contact
new_contact = {
    "name": " Kevin Mwangi",
    "Phone number": "0761234589",
    "skill": "beekeeping",
    "city": "Kakamega"
}
contacts.append(new_contact)
print("After:", len(contacts), "contacts"),
print("Last contact:", contacts[-1])
print(f"\nTotal contacts: {len(contacts)}")

