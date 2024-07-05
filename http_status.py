status_code = [200,400,500,226]



status = input("Enter status number: ")

status = int(status_code)

if status == 200:
    print("Ok")

elif status == 400:
    print("Bad Request")

elif status == 500:
    print("Internal server error")
elif status == 226:
    print("Successful Response")

else:
    print("Check status")


    
