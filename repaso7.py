licencia=input("Tiene licencia? (si/no) ")
casco=input("Tiene casco? (si/no) ")

if licencia=="no" or casco=="no":
    print("No puede conducir")
else:print("Puede conducir")