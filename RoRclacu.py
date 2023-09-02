share= int(input("No. of shares: "))
mv= float(input("MV of share:RS "))
sumi= share*mv
print("Sum invested:RS",(sumi))


divi= float(input("percentage of dividend: %"))
fv= int(input("enter FV of share:RS"))

per_share= fv*(divi/100)

total_divi= per_share*share

ror= (total_divi/sumi)*100


print("Dividend per share:RS",(per_share))
print("Total dividend recived:RS",(total_divi))
print("Rate of Return:%",(ror))

