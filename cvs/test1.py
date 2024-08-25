import csv

f = open("test.csv" , 'w+' , newline="")
lnwriter = csv.writer(f)

lnwriter.writerow(['a',' 00:25:43'])

f.close()