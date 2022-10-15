# find maximum element in the list

def find_max(a_list):
    max = None
    if a_list == []:
        return 0
    for num in a_list:
        if max == None:
            max = num
        elif num > max:
            max = num
    return max

user_input = input('Please input a list: ')

if user_input != '[]':
    user_input_adjust = user_input.strip('[]').replace(' ', '').split(',') # remove '[] and blackspace' from the string and convert into list
    a_list = []
    for i in user_input_adjust:
        a_list.append(int(i))
else:
    a_list = []
print('The list you input is', a_list)

print('The maximum number in the list is', find_max(a_list))
