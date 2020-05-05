
def linear_search(array,item):

    for i in range(len(array)):
        if array[i]==item:
            return f"Item Found at Index:{i}"

    return f"Item Not found In given Arraay:.."

array=[1,4,5,2,7,58,33,45,40,20]
print(linear_search(array,10))
print(linear_search(array,58))

