import  pyshorteners

long_url = input("Enter Url to shorten")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("The Shortened url: ", + short_url)