# def randomfunc(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} is {value}")
#
#
# list = {"ashu":"data-engineer", "python":"programming", "azure":"cloud"}
#
# randomfunc(**list)



def generative_invoice(discount,*args, **kwargs):
    #printing customer details

    if "name" in kwargs:   #by this way we check is this key value is present in the dictionary or not
        print("name of customer =", kwargs["name"]) #by this way we access the associated value with the key

    if "email" in kwargs:
        print("email of customer =", kwargs["email"])

    total = sum(args)  #sum function takes an iterable object like list or tuple

    print("total amount before discount:", total)
    print("discount applied: ", discount, "%")
    print("final amount after tax: ",total-(total*(discount/100)))



list =[]
i = 1
while(i<6):
    print("enter the price of item ", i)
    price = int(input())
    list.append(price)
    i = i+1

discount = float(input("enter the discount rate\n"))
list2 = {"name":"ashu","email":"ashugoswami@gmail.com"}


generative_invoice(discount,*list,**list2)

