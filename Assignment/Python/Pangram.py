s=input()
ad=set()
for i in s:
    if i != " ":
        ad.add(i)
if len(ad) == 26:
    print("Pangram")
else:
    print("Not a Pangram")
print(ad)
