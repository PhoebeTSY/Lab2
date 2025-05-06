def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = (weight)/(height**2)
    print("Bmi = " + str(bmi))

    if bmi < 18.5:
        print("STICK")

    elif bmi>=18.5 and bmi<=25.0:
        print("NOT FAT")

    elif bmi>25.0:
        print("FAT")
    
calculate_bmi(weight=57, height=1.73)




 