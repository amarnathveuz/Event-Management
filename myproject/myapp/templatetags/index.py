from django import template
register = template.Library()

@register.filter
def index(indexable, i):

    add_list = []
    for i in range(1, int(indexable[i])+1):
        add_list.append(i)
    return add_list



@register.filter
def index_f(value, args):
    print(args)
    s1 = "/" in args
    print("s1:::::::::",str(s1))
    if s1 == True:
        data = args.split("/")
    
        try:
            if data[0][0] == data[1][0]:

                result = data[0][0]+data[1][1]
            else:
                result = data[0][0]+data[1][1]
        except:
            result = data[0][0]
            pass
        pass
    else:

        data = args.split(" ")
    
        try:
            result = data[0][0]+data[1][0]
        except:
            result = data[0][0]
            pass
    return result