lst=[]
for i in range(5):
    a = int(input("숫자를 입력하세요"))
    lst.append(a)
lst_sort=sorted(lst)
print("입력한 숫자는".format(lst_sort))