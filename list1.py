# x = [1,67,0.9,-1,890,0]

# x.reverse()
# print(x)

# x.sort()
# print(x)

# x.sort(reverse=True)
# print(x)

# y = x.copy()

# print(x,"\n",y)
# x[0]=790

# print(x,"\n",y)

# for i in x:
#     print(i,end=" ")
# print()

# for i in range(len(x)):
#     print(x[i],end=" ")
# print()

# x=[[1,2,3],[3,4,5]]

# for i in x:
#     print(i)

# for i,j,k in x:
#     print(i,":",j,':',k)

# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print(x[i][j],end=" ")
#     print()


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# print(y)
# y.remove("apple")
# thistuple = tuple(y)
# a=['raja','vino']
# b=['kk','vidhya']
# c=a+b
# print(c)

# a=['raja','vino']
# b=['kk','vidhya']
# a.append(b)
# print(a)

# a= (2)
# b= (5)
# c= a*b
# print(c)

# def sum_list(items):
#     sum_numbers=0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
# print(sum_list([1,2,-8]))

# def multiply_list(items):
#     tot=1
#     for x in items:
#         tot*=x
#     return tot
# print(multiply_list([1,2,-8]))

list1=[1,3,5,7,9]
list2=[1,2,4,6,7,8]
diff_list1_list2=list(set(list1)-set(list2))
diff_list2_list1=list(set(list2)-set(list1))
total_diff=diff_list1_list2 + diff_list2_list1
print(total_diff)
