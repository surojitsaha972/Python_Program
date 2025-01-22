str=input("Enter any str value:")
sent=str.split()
print(sent)
rev=[sent[::-1] for sent in sent]
rev="  ".join(rev)
print(rev)