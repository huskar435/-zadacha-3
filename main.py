input_data = open("input.txt","r")
data = input_data.read()
a = int(data) 
b = a**2
j = str(b)
output_data = open("output.txt","w")
output_data.write (j)
input_data.close()
output_data.close()  