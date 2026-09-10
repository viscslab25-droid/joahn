import csv
with open(r'Xii rev\suri\student.csv',"r") as f1:
    records = list(csv.reader(f1))
    print(records)
    while True:
        inp_r = input("enter r_num : ")
        inp_m = input("enter new_marks : ")
        if not(inp_m and inp_r):
            print("thank you")
            break
        else:
            for rec in records:
                if rec[0] == inp_r:
                    rec[1] = inp_m

r = []

with open(r'Xii rev\suri\student.csv',"w",newline='') as f2:
    w = csv.writer(f2)
    w.writerows(records)