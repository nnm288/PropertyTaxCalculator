
def getTaxAmount(houseValue,firstHouse):
    print(houseValue)
    if(firstHouse == False):
        if(houseValue <= 125000):
            res = houseValue*0.03
            print(res)
            return res
        elif(houseValue >125000 and houseValue <=250000):
            taxUnderBracket = (125000 *0.03) 
            res = taxUnderBracket +((houseValue-125000)*0.05)
            print(res)
            return res
        elif(houseValue > 250000 and houseValue <=925000):
            taxUnderBracket =(125000 *0.03) + ((250000-125000)*0.05)
            res = taxUnderBracket + ((houseValue-250000)*0.08)
            print(res)
            return res
        elif (houseValue >925000 and houseValue <=1500000):
            taxUnderBracket =(125000 *0.03) + ((250000-125000)*0.05)+(675000*0.08)
            res = taxUnderBracket +((houseValue-925000)*0.13)
            print(res)
            return res
        else:
            taxUnderBracket = (125000 *0.03) + ((250000-125000)*0.05)+(675000*0.08)+((1500000-925000)*0.13)
            res = taxUnderBracket +((houseValue-1500000)*0.15)
            print(res)
            return res

def main():
    hValue =1875000
    fHouse = False
    res = getTaxAmount(hValue,fHouse)
    print(res)
    
if __name__ == "__main__":
    main()
