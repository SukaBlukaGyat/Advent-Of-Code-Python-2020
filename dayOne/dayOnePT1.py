intput_ = open('./dayOne/inputr.txt','r')

exp_list = []

for expense in intput_:
    exp_list.append(int(expense))


for list1 in range(len(exp_list)):
    for list2 in range(len(exp_list)-list1):
        if exp_list[list1] + exp_list[list1+list2] == 2020:
            print(exp_list[list1] * exp_list[list1+list2])
            break