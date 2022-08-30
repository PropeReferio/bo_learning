value_to_match = input('What do you want to match? ')

match value_to_match:
    case "CASS":
        print("Uploading to CASS")
    case "Syncada":
        print("Uploading to SYncada")
    case "BluJay":
        print("Uploading to BluJay")
    case _:
        print("We didn't recognize the service you want.")

