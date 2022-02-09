def get_age(*args, **kwargs):
    gte_30 = []
    lte_30 = []
    if kwargs:
        for i in kwargs.values():
            if i >= 30:
                gte_30.append(i)
            else:
                lte_30.append(i)
    gte_30 = list(set(gte_30))
    lte_30 = list(set(lte_30))
    return f'gte_30 : {gte_30} lte_30 : {lte_30}'
print(get_age(nazi=32, nodira=18, samat=29))