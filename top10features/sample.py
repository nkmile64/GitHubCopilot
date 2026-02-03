# q: What does rest stand for?
# a: In Python, "rest" typically refers to the "rest parameters" feature, which allows a function to accept an arbitrary number of arguments. This is done using the asterisk (*) syntax in the function definition. For example:

# q: Καταλαβαίνεις Ελληνικά;
# a: Ναι, καταλαβαίνω Ελληνικά. Πώς μπορώ να σας βοηθήσω;
# q: Πως θα μπορούσα να εκτελέσω ένα προγραμμα Python στην Android συσκευή μου;
# a: Μπορείτε να εκτελέσετε προγράμματα Python σε μια Android συσκευή χρησιμοποιώντας εφαρμογές όπως το QPython, Pydroid 3 ή Termux. Αυτές οι εφαρμογές παρέχουν ένα περιβάλλον όπου μπορείτε να γράψετε και να εκτελέσετε κώδικα Python απευθείας στη συσκευή σας.

# Function that calculates days between two dates
from datetime import datetime


def days_between_dates(date1_str, date2_str):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    delta = abs((date2 - date1).days)
    return delta

print(days_between_dates("1982-04-19", "1982-04-22"))
