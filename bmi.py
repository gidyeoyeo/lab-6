

def cal_bmi(weight,height):
    print("weight is " + str(weight))
    print("Height is " + str(height))
    
    bmi=(int(weight))/int(height)**2

    if bmi<18.5:
        print("underweight")
    elif bmi>=18.5 or bmi<= 25.0:
        print("normal weight")
    elif bmi>25.0:
        print("overweight")

cal_bmi(weight=57,height=1.73)