import webcolors

def find_color(in_col_r, in_col_g, in_col_b):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        col_r, col_g, col_b = webcolors.hex_to_rgb(key)
        r_diff = (col_r - in_col_r) ** 2
        g_diff = (col_g - in_col_g) ** 2
        b_diff = (col_b - in_col_b) ** 2
        min_colors[(r_diff + g_diff + b_diff)] = name
    color_name = min_colors[min(min_colors.keys())]

    silvers = {'gainsboro', 'lavender', 'lightgray', 'lightgrey', 'lightsteelblue', 'silver', 'black'}
    grays = {'darkgray', 'darkgrey', 'dimgray', 'dimgrey', 'gray', 'grey', 'black'}
    whites = {'aliceblue', 'antiquewhite', 'azure', 'beige', 'cornsilk', 'floralwhite', 'ghostwhite', 'honeydew', 'ivory', 'lavenderblush',\
             'linen', 'mintcream', 'oldlace', 'papayawhip', 'seashell', 'snow', 'white', 'whitesmoke', 'bisque', 'blanchedalmond'}
    browns = {'burlywood', 'saddlebrown', 'sienna', 'tan'}
    lightblues = {'aqua', 'aquamarine', 'cornflowerblue', 'cyan', 'darkturquoise', 'deepskyblue', 'dodgerblue', 'lightblue', 'lightcyan',\
                'lightskyblue', 'mediumturquoise', 'paleturquoise', 'powderblue', 'skyblue', 'turquoise', 'cadetblue', 'lightslategray', 'lightslategrey'}
    blues = {'blue', 'mediumblue', 'mediumslateblue', 'royalblue', 'steelblue', 'slategray', 'slategrey'}
    darkblues = {'darkblue', 'darkslateblue', 'midnightblue', 'navy', 'slateblue', 'darkslategray', 'darkslategrey'}
    purples = {'blueviolet', 'darkmagenta', 'darkorchid', 'darkviolet', 'indigo', 'mediumorchid', 'mediumpurple', 'mediumvioletred',\
             'orchid', 'plum', 'purple', 'thistle'}
    darkreds = {'darkred', 'firebrick', 'maroon'}
    reds = {'crimson', 'orangered', 'brown', 'red'}
    pinks = {'coral', 'darksalmon', 'deeppink', 'fuchsia', 'hotpink', 'lightcoral', 'lightpink', 'magenta', 'mistyrose', 'peachpuff', 'pink',\
             'salmon', 'violet', 'indianred', 'palevioletred', 'rosybrown'}
    oranges = {'darkorange', 'lightsalmon', 'chocolate', 'orange', 'peru', 'sandybrown', 'tomato'}
    lightyellows = {'lemonchiffon', 'lightgoldenrodyellow', 'lightyellow', 'moccasin', 'navajowhite', 'palegoldenrod', 'wheat'}
    yellows = {'gold', 'yellow', 'khaki'}
    darkyellows = {'darkgoldenrod', 'goldenrod', 'darkkhaki'}
    lightgreens = {'chartreuse', 'darkseagreen', 'greenyellow', 'lawngreen', 'lightgreen', 'lime', 'mediumspringgreen', 'palegreen', 'springgreen', 'yellowgreen'}
    greens = {'forestgreen', 'green', 'limegreen', 'mediumseagreen', 'seagreen', 'lightseagreen', 'mediumaquamarine'}
    darkgreens = {'darkcyan', 'darkgreen', 'darkolivegreen', 'olive', 'olivedrab', 'teal'}

    if color_name == 'black':
        color_name = 'black'
    elif color_name in silvers:
        color_name = 'silver'
    elif color_name in grays:
        color_name = 'gray'
    elif color_name in whites:
        color_name = 'white'
    elif color_name in browns:
        color_name = 'brown'
    elif color_name in lightblues:
        color_name = 'lightblue'
    elif color_name in blues:
        color_name = 'blue'
    elif color_name in darkblues:
        color_name = 'darkblue'
    elif color_name in purples:
        color_name = 'purple'
    elif color_name in darkreds:
        color_name = 'darkred'
    elif color_name in reds:
        color_name = 'red'
    elif color_name in pinks:
        color_name = 'pink'
    elif color_name in oranges:
        color_name = 'orange'
    elif color_name in lightyellows:
        color_name = 'lightyellow'
    elif color_name in yellows:
        color_name = 'yellow'
    elif color_name in darkyellows:
        color_name = 'darkyellow'
    elif color_name in lightgreens:
        color_name = 'lightgreen'
    elif color_name in greens:
        color_name = 'green'
    elif color_name in darkgreens:
        color_name = 'darkgreen'
    else:
        color_name = None

    return color_name

def find_color_recommend(color_name):

    color_recommendations = None

    if color_name == 'black':
        color_recommendations = {'black', 'silver', 'gray', 'white', 'brown', 'lightblue', 'blue', 'darkblue', 'purple', 'darkred', 'red', 'lightred', \
                                'lightyellow', 'yellow', 'darkyellow', 'lightgreen', 'green', 'darkgreen'}
    elif color_name == 'silver':
        color_recommendations = {'blue', 'yellow', 'black', 'white', 'lightblue', 'purple'}
    elif color_name == 'gray':
        color_recommendations = {'white', 'black', 'yellow', 'gray', 'darkblue', 'darkred'}
    elif color_name == 'white':
        color_recommendations = {'black', 'blue', 'darkred', 'pink', 'brown', 'darkgreen', 'lightblue'}
    elif color_name == 'brown':
        color_recommendations = {'blue', 'yellow', 'black'}
    elif color_name == 'lightblue':
        color_recommendations = {'darkblue', 'white', 'darkred', 'black', 'gray', 'silver', 'purple'}
    elif color_name == 'blue':
        color_recommendations = {'black', 'gray', 'brown', 'white', 'darkred', 'pink'}
    elif color_name == 'darkblue':
        color_recommendations = {'orange', 'lightred', 'gray', 'silver', 'black', 'brown', 'darkgreen', 'green', 'darkyellow', 'darkblue'}
    elif color_name == 'purple':
        color_recommendations = {'black', 'white', 'silver', 'brown', 'lightblue', 'darkred', 'darkgreen', 'yellow', 'orange'}
    elif color_name == 'darkred':
        color_recommendations = {'black', 'gray', 'silver', 'brown', 'lightblue', 'blue', 'darkblue', 'purple', 'green', 'darkgreen', 'darkred'}
    elif color_name == 'red':
        color_recommendations = {'black', 'blue', 'gray', 'darkblue'}
    elif color_name == 'pink':
        color_recommendations = {'blue', 'darkblue', 'lightblue', 'black', 'white', 'darkred', 'pink'}
    elif color_name == 'orange':
        color_recommendations = {'blue', 'darkblue', 'black', 'gray', 'brown', 'orange', 'darkgreen'}
    elif color_name == 'lightyellow':
        color_recommendations = {'black', 'lightblue', 'blue', 'purple', 'gray', 'brown'}
    elif color_name == 'yellow':
        color_recommendations = {'black', 'lightblue', 'blue', 'darkblue', 'purple', 'darkgreen', 'gray', 'brown'}
    elif color_name == 'darkyellow':
        color_recommendations = {'black', 'darkblue', 'white', 'silver', 'brown', 'pink'}
    elif color_name == 'lightgreen':
        color_recommendations = {'lightgreen', 'lightblue', 'blue', 'darkblue', 'black', 'gray', 'darkred', 'darkgreen'}
    elif color_name == 'green':
        color_recommendations = {'black', 'darkred', 'brown', 'pink', 'lightblue', 'orange'}
    elif color_name == 'darkgreen':
        color_recommendations = {'black', 'darkred', 'brown', 'pink', 'lightblue', 'blue', 'orange', 'yellow'}
    else:
        color_recommendations = None
    
    return color_recommendations