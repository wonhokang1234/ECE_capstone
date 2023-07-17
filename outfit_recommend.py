import outfit_func as of

# file = open("/home/d4/myflection/opencv_color/output.txt", "rt")
with open('/home/d4/myflection/opencv_color/output.txt', 'r') as f:
    color_line = f.readline()
    rgb_values = color_line[1:-2].split(', ')

in_col_r = contents[0]
in_col_g = contents[1]
in_col_b = contents[2]

in_col_r = int(in_col_r)
in_col_g = int(in_col_g)
in_col_b = int(in_col_b)

in_formal = input("do you want formal? (y/n): ").strip()
if in_formal[0] == 'y':
    formality = 'formal'
else:
    formality = 'informal'

outfit_recommendation = of.find_outfit_recommend(in_col_r, in_col_g, in_col_b, formality)

print('outfit recommendations: ', outfit_recommendation)
