import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, http://exclude.com/"  #added the other email example that should be exluded to make sure that the code worked for boht examples
exclude_domain = 'exclude.com'
pattern = r'\b[A-Za-z0-9._%+-]+@(?!{})(?:[A-Za-z0-9-]+\.)+[A-Za-z]{{2,}}\b'.format(re.escape(exclude_domain))

emails = re.findall(pattern, text)
print(emails)
