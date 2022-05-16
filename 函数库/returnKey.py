"""使用vlaue返回key值"""
currency_dict = {'USD': 'Dollar',
                 'EUR': 'Euro',
                 ' GBP': 'Pound',
                 'CN': 'Chinese',
                 'CNY': 'Chinese'}
val = 'Chinese'
key_list = list(currency_dict.keys())
val_list = list(currency_dict.values())


def return_Allkey(val):
    cur_list = []
    for i in range(len(currency_dict)):
        if val_list[i] == val:
            cur_list.append(key_list[i])
    if cur_list[0] == [None]:
        return("Key Not Found")
    else:
        return cur_list


def return_key(val):
    list(currency_dict.keys())[list(currency_dict.values()).index(val)]


print(return_key("Chinese"))
