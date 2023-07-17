import color_func as cf, weather_func as wf
import csv
import requests

def find_outfit_recommend(in_col_r, in_col_g, in_col_b, formality):

    outfit_recommendation = []
    
    color_name = cf.find_color(in_col_r, in_col_g, in_col_b)
    color_recommendations = cf.find_color_recommend(color_name)
    
    [seas, cond, temp] = wf.find_weather()

    weather_recommendations = wf.find_weather_recommend(cond, temp)

    if formality == 'formal':
        weather_recommendations.update('suit', 'dress')

    top_wardrobe = {}
    bot_wardrobe = {}
    acc_wardrobe = {}
    Clothes = []

    wardrobe_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTuFSt6GJ-_i9gQnj6kiX5npiYNoLblwWeRYJaD8zmqIab6PceLpXegY0dRFtM_QXaHwm1HKncWSQ06/pub?gid=0&single=true&output=csv'


    with requests.Session() as s:
        wardrobe_csv = s.get(wardrobe_url)

        decoded_wardrobe = wardrobe_csv.content.decode('utf-8')

        Clothes_csv = csv.reader(decoded_wardrobe.splitlines(), delimiter=',')
        line_count = 0
        for row in Clothes_csv:
            line_count += 1
            if line_count == 1:
                # print(f'Column names are {", ".join(row)}')
                None
            else:
                Clothes = [row[0], row[1], row[2], row[3], row[4], row[5]]
                if row[0] == 'top':
                    top_wardrobe[row[6]] = Clothes
                elif row[0] == 'bottom':
                    bot_wardrobe[row[6]] = Clothes
                else:
                    acc_wardrobe[row[6]] = Clothes
        #         print(f'\t', Clothes)
        # print(f'Processed {line_count} lines.')
        # print('top wardrobe: ', top_wardrobe)
        # print('bot wardrobe: ', bot_wardrobe)
        # print('acc wardrobe: ', acc_wardrobe)

    top_wardrobe_points = {}
    bot_wardrobe_points = {}
    acc_wardrobe_points = {}

    for key in top_wardrobe.keys():
        clothe_points = 0
        if top_wardrobe[key][2] == formality: 
            clothe_points += 20
        else:
            clothe_points += 0  

        if top_wardrobe[key][4] == seas:
            clothe_points += 7
        else:
            clothe_points += 0  

        if top_wardrobe[key][1] in weather_recommendations:
            clothe_points += 5
        else:
            clothe_points += 0  

        if top_wardrobe[key][3] in weather_recommendations:
            clothe_points += 5
        else:
            clothe_points += 0  

        if top_wardrobe[key][5] == color_name:
            clothe_points += 5
        elif top_wardrobe[key][5] in color_recommendations:
            clothe_points += 1
        else:
            clothe_points += 0  

        # print(key, clothe_points)
        top_wardrobe_points[key] = clothe_points

    # print('top wardrobe points: ', top_wardrobe_points)

    for key in bot_wardrobe.keys():
        clothe_points = 0
        if bot_wardrobe[key][2] == formality: 
            clothe_points += 20  
        else:
            clothe_points += 0  
        
        if bot_wardrobe[key][4] == seas:
            clothe_points += 7

        if bot_wardrobe[key][1] in weather_recommendations:
            clothe_points += 5
        
        if bot_wardrobe[key][3] in weather_recommendations:
            clothe_points += 5
        
        if bot_wardrobe[key][5] in color_recommendations:
            clothe_points += 1
        
        # print(key, clothe_points)
        bot_wardrobe_points[key] = clothe_points

    # print('bot wardrobe points: ', bot_wardrobe_points)
    
    for key in acc_wardrobe.keys():
        if acc_wardrobe[key][1] in weather_recommendations:
            clothe_points = 1
            if acc_wardrobe[key][2] == formality: 
                clothe_points += 20  
            else:
                clothe_points += 0  

            if acc_wardrobe[key][4] == seas:
                clothe_points += 7

            if acc_wardrobe[key][1] in weather_recommendations:
                clothe_points += 5
        
            if acc_wardrobe[key][3] in weather_recommendations:
                clothe_points += 5
        
            if acc_wardrobe[key][5] in color_recommendations:
                clothe_points += 3

            # print(key, clothe_points)
            acc_wardrobe_points[key] = clothe_points
        else:
            None

    # print('acc wardrobe points: ', acc_wardrobe_points)
    
    outfit_storage = {}

    best_tops = list(top_wardrobe_points.keys())[0:5]
    best_bots = list(bot_wardrobe_points.keys())[0:5]
    if len(acc_wardrobe_points) > 0:
        best_accs = list(acc_wardrobe_points.keys())[0:5]
    else:
        best_accs = None


    for item in top_wardrobe_points:
        for index in range(len(best_tops)):
            if (top_wardrobe_points[item] > top_wardrobe_points[best_tops[index]]) and not (item in best_tops):
                best_tops[index] = item

    for item in bot_wardrobe_points:
        for index in range(len(best_bots)):
            if (bot_wardrobe_points[item] > bot_wardrobe_points[best_bots[index]]) and not (item in best_bots):
                best_bots[index] = item
                


    # print('best tops, bots, and accs: ', best_tops, best_bots, best_accs)

    if best_accs == None:
        for top in best_tops:
            for bot in best_bots:
                curr_out = (top, bot)
                curr_out_pts = 0

                top_col_rec = cf.find_color_recommend(top_wardrobe[top][5])
                if bot_wardrobe[bot][5] in top_col_rec:
                    curr_out_pts += 4
                else:
                    curr_out_pts += 0

                curr_out_pts += top_wardrobe_points[top] + bot_wardrobe_points[bot]
                outfit_storage[curr_out] = curr_out_pts
    else:
        for top in best_tops:
            for bot in best_bots:
                for acc in best_accs:
                    curr_out = (top, bot, acc)
                    curr_out_pts = 0

                    top_col_rec = cf.find_color_recommend(top_wardrobe[top][5])
                    if (bot_wardrobe[bot][5] in top_col_rec) and (acc_wardrobe[bot][5] in top_col_rec):
                        curr_out_pts += 8
                    elif bot_wardrobe[bot][5] in top_col_rec:
                        curr_out_pts += 4
                    elif acc_wardrobe[bot][5] in top_col_rec:
                        curr_out_pts += 4
                    else:
                        curr_out_pts += 0

                    bot_col_rec = cf.find_color_recommend(bot_wardrobe[bot][5])
                    if acc_wardrobe[acc][5] in bot_col_rec:
                        curr_out_pts += 4
                    else:
                        curr_out_pts += 0

                    curr_out_pts += top_wardrobe_points[top] + bot_wardrobe_points[bot] + acc_wardrobe_points[acc]
                    outfit_storage[curr_out] = curr_out_pts
    
    outfit_recommendation += list(outfit_storage.keys())[0:5]

    for item in outfit_storage:
        for index in range(len(outfit_recommendation)):
            if (outfit_storage[item] > outfit_storage[outfit_recommendation[index]]) and not (item in outfit_recommendation):
                outfit_recommendation[index] = item

    # for outfit in outfit_recommendation:
        # print('outfit ', outfit, ' is worth ', outfit_storage[outfit], ' points')


    return outfit_recommendation