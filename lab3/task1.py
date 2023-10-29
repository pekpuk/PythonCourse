def search_func(product_list, product):
    count = len(product_list)
    result = None
    for i in range(count):
        if product_list[i] == product:
            if result == None:
                result = i

    return result


global_product_list = ['яблоко', 'апельсин', 'клубника', 'апельсин', 'картошка']
global_product = 'картошка'
global_result = search_func(global_product_list, global_product)

if global_result != None:
    print('индекс искомого товара', global_result)
else:
    print('искомого товара нет в списке')


