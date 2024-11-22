student_names = ['Daniel','Desmond','Deborah','James','Ifenayi','Mercy','Moses','Taiwo','Christianah','Uzo']
java = [60,90,55,78,98,100,45,23,80,20]
Javascript = [70,35,90,89,78,55,90,100,12,88]
python = [68,90,56,70,78,45,90,78,90,89]
Designthinking = [60,57,90,78,45,75,67,90,70,100]

java_scores = []

for score in java:
	java_scores = score

#print (java[4])
#print (student_names[4],max(python))

highest_in_python = max(python)
least_in_python = min(python)

highest_in_java = max(java)
least_in_java = min(java)

highest_in_designthinking = max(Designthinking)
least_in_designthinking = min(Designthinking)

highest_in_javascript = max(Javascript)
least_in_javascript = min(Javascript)


for name in student_names:
	print(name,"\t")
	
	for grades in java:
		print (grades,"\t")
	


		 
