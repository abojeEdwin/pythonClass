my_dict={"Passport number":[245,234,3456,123],"Sex":["Male","Female","Hermaphophite","Transgander"],"Type":["Black","White","Orange"],"city":"Lagos","name":"Edwin"}
#for key in my_dict:
	#print(key)
#for value in my_dict.values():
	#print(value)
for key,value in my_dict.items():
	print(f"{key}:{value}")


#print(my_dict["Sex"][0],my_dict["Sex"][2])
#print(my_dict["Type"][0],my_dict["Type"][2])
#print(my_dict.get("place"))
#my_dict["Sex"]="femaleman"
#print(my_dict["Sex"][0],my_dict["Sex"][1],my_dict["Sex"][2],my_dict["Sex"][3])


def square(number:value):
	return{number:value**2 for number in range(1,6)}



print(square(6))