def flip_num(my_nu):
   return '1' if(my_nu == '0') else '0';
def gray_to_binary(gray):
   binary_code = ""
   binary_code += gray[0]
   for i in range(1, len(gray)):
 if (gray[i] == '0'):
         binary_code += binary_code[i - 1]
else:
         binary_code += flip_num(binary_code[i - 1])
return binary_code
gray_code = "01101001"
