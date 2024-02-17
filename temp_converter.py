def temp_converter(temp_from,temp_to,temp_value):
    if(temp_from=="FARENHEIGHT" and temp_to == "DEGREE"):
        temp=temp_value-33.5
        print(f"{temp_value}Farenheight is equivalent to {temp}degree celcius!")
    elif(temp_from=="DEGREE" and temp_to=="FARENHEIGHT"):
        temp=temp_value+ 33.5
    else:
        print("Invalid input")

        print(f"{temp_value}degree celcius is equivalent to{temp}farenheight")

temp_from=input("Are you converting from 'farenheight' or 'Degree':").upper()
temp_to=input("Are you converting to 'farenheight' or 'Degree':").upper()
temp_value=float(input("enter temp value:"))

temp_converter(temp_from,temp_to,temp_value)