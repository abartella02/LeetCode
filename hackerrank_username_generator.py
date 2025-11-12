import re


def generate_usernames(names):
    usernames = []
    for name in names:
        name = re.sub(r"[^a-zA-Z0-9\s]", "", name)
        part_names = name.split()
        firstname, lastname = part_names[0].lower(), part_names[-1].lower()

        lastname_len = min(7 - 1, len(lastname) - 1)
        firstname_len = 8 - 1 - lastname_len
        username = lastname[0:lastname_len] + firstname[0:firstname_len]

        i = 0
        while username in usernames:
            if lastname_len > 1:
                firstname_len += 1
                lastname_len -= 1
                username = lastname[0:lastname_len] + firstname[0:firstname_len]
            else:
                firstname -= 1
                username = (
                    lastname[0:lastname_len] + firstname[0:firstname_len] + f"{i}"
                )
        usernames.append(username)
    return usernames


print(generate_usernames(["Adrian Chiles", "Benedict Cumberbatch", "Serena Williams"]))
