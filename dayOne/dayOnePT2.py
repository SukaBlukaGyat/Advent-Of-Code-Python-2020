intput_ = open('./dayOne/inputr.txt','r')

exp_list = []

for expense in intput_:
    exp_list.append(int(expense))


for list1 in range(len(exp_list)):
    for list2 in range(len(exp_list)-list1):
        for list3 in range(len(exp_list)-list2-list1):
            if exp_list[list1] + exp_list[list1+list2]+ exp_list[list1+list2+list3] == 2020:
                print(exp_list[list1] * exp_list[list1+list2] * exp_list[list1+list2+list3])
                break