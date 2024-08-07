def get_cats_info(path):
    with open (path, "r") as fh:
        list_cats = []
        dic_each_cat = {}
        for line in fh:
            if line != '':
                line = line.strip().split(",")
                dic_each_cat["id"] = line[0]
                dic_each_cat["name"] = line[1]
                dic_each_cat["age"] = line[2]
                list_cats.append(dic_each_cat)
            else:
                break

    return list_cats     
            


list_cats = get_cats_info("cats.txt")
print(list_cats)


