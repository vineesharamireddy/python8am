#string slicing Type1:

var = "python_interpreter"

print(var[1:3])
print(var[0:5])
print(var[-5:-2])
print(var[:3])
print(var[3:])
print(var[:])
print(var[3:10])
print(var[2:5])
print(var[0:10])
print(var[5:-5])
print(var[2:8])
print(var[:8])
print(var[5:])
print(var[8:12])
print(var[12:5])

output:

yt
pytho
ret
pyt
hon_interpreter
python_interpreter
hon_int
tho
python_int
n_interp
thon_i
python_i
n_interpreter
nter


#string slicing Type2:  
    
var = "java_compiler_go"

print(var[2:10])
print(var[2:10:1])
print(var[2:10:2])
print(var[2:10:3])
print(var[-12:10])
print(var[-12:10:1])
print(var[-12:10:2])
print(var[-12:10:3])

print(var[5::1])
print(var[5::2])
print(var[:5:1])
print(var[:-5:1])
print(var[-8::2])

print(var[3:10:1])
print(var[3:10:2])
print(var[3:10:3])
print(var[5:-5:1])
print(var[5:-5:2])
print(var[5:-5:5])
print(var[:8:4])
print(var[5::3])
print(var[::2])

output:

va_compi
va_compi
v_op
vcp
_compi
_compi
_op
_m
compiler_go
cmie_o
java_
java_compil
plrg
a_compi
acmi
aoi
compil
cmi
cl
j_
cpeg
jv_oplrg




print(var[12:5:3])
