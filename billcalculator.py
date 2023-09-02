name= input("Enter product name: ")
sp= float(input("enter taxable value of product: "))
gst= float(input("enter GST rate %:  "))
cgst=sp*((gst/2)/100)
sgst=cgst
amt= sp+cgst+sgst
print(name)
print("Amount of CGST %:",(cgst))
print("Amount of SGST %:",(sgst))
print("Amount payable:",(amt))