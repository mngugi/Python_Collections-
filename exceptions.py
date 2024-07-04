try:
    print("1")
    raise Exception("2")
    print("4")

except Exception as e:
    print(str(e))
    print("4")
