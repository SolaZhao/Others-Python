#coding : UTF-8
import string,itertools

dot_list = []
sides_match_list = ['abh','acgi','adfj','aek','bcde','efgh','hijk']
i = 0
triangle_number = 0
while i < 26:
    dot_list.append(string.lowercase[i])
    if string.lowercase[i] == 'k':
        break
    else:
        i += 1
for a in itertools.combinations(dot_list,3):
    triangle_flag = True
    for each_dot_combination in itertools.combinations(a,2):
        for each_side in sides_match_list:
            if each_dot_combination[0] in each_side and each_dot_combination[1] in each_side:
                triangle_flag = True
                break
            else:
                triangle_flag = False
                break
        for each_side in sides_match_list:
            if a[0] in each_side and a[1] in each_side and a[2] in each_side:
                triangle_flag = False
        if triangle_flag == True:
            triangle_number += 1
            print "%d : %s" % (triangle_number,a)
print "三角形个数 : %d" % triangle_number
            
