common_list = []
line = input()

while line != "":
    new_list = sorted(line.replace("\n", "").split(" "))
    # print(new_list)
    if common_list == []:
        common_list = new_list
    else:
        find_common = []
        for item in common_list:
            # print("item:", item)
            for new_item in new_list:
                # print("new item", new_item)
                if item == new_item:
                    find_common.append(item)
                    # print("found", item)
                    break
                elif item < new_item:
                    break
        common_list = find_common
    line = input()

if common_list == []:
    result = "NULL"

else:
    result = common_list[0]
    for item in common_list[1:]:
        result += " " + item

print(result)