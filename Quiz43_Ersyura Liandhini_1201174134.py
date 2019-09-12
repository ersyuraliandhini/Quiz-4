ListGPA = [2.1, 2.5, 4, 3]

def gift (GPA) :
    bonus = 500000
    gift = GPA * bonus
    return gift

for GPA in ListGPA:
    if GPA > 2.5:
        print("Congratulations! you get a bonus : IDR", gift(GPA))
    else :
        print ("Sorry, you didn't get a bonus")



