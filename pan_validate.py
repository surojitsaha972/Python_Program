pan_no=input("Enter the pan number:")
if len(pan_no)==10:
    if pan_no[:5].isalpha()==True:
        if pan_no[:].isupper()==True:
            if pan_no[5:9].isdigit()==True:
                if pan_no[-1].isalpha()==True:
                    print("Pan number is valid")
                else:
                    print("Last value will be a alphabate")
            else:
                print("Middle 4 values will be digit")
        else:
            print("Character will be capital")
    else:
        print("First 5 values will be alphabate")
else:
    print("Pan number must be contian 10 digit")

