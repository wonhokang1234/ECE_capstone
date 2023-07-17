def find_weather():
    with open('Output.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        count += 1
        if (count == 10):
            seas_int = line
        elif (count == 19):
            cond = line
        elif (count == 34):
            temp = line
        else:
            None

    seas_int = seas_int[21:23]
    seas_int = int(seas_int)
    seas = ''

    if (seas_int < 3) | (seas_int == 12):
        seas = 'winter'
    elif (3 <= seas_int < 6) | (9 <= seas_int < 12):
        seas = 'spring'
    elif (6 <= seas_int < 9):
        seas = 'summer'
    else:
        seas = None
        
    len_c = len(cond)
    cond = cond[13:(len_c-3)]

    len_t = len(temp)
    temp = temp[16:(len_t-2)]
    temp = float(temp)

    return [seas, cond, temp]

def is_snowy(cond):
    return ((cond == 'Blowing snow') | (cond == 'Blizzard') | (cond == 'Freezing fog') | (cond == 'Freezing drizzle') | (cond == 'Heavy freezing drizzle') |\
        (cond == 'Blizzard') | (cond == 'Moderate or heavy freezing rain') | (cond == 'Patchy light snow') | (cond == 'Light snow') |\
            (cond == 'Patchy moderate snow') | (cond == 'Moderate snow') | (cond == 'Heavy snow') | (cond == 'Ice pellets') | (cond == 'Light snow showers') |\
                (cond == 'Moderate or heavy snow showers') | (cond == 'Light showers of ice pellets') | (cond == 'Moderate or heavy showers of ice pellets'))

def is_rainy(cond):
    return ((cond == 'Patchy rain possible') | (cond == 'Patchy freezing drizzle possible') | (cond == 'Light rain') | (cond == 'Light freezing rain') |\
        (cond == 'Patchy light drizzle') | (cond == 'Light drizzle') | (cond == 'Patchy light rain') | (cond == 'Thundery outbreaks possible') |\
            (cond == 'Moderate rain at times') | (cond == 'Moderate rain') | (cond == 'Heavy rain at times') | (cond == 'Heavy rain') | \
                (cond == 'Torrential rain shower') | (cond == 'Patchy light rain with thunder') | (cond == 'Moderate or heavy rain with thunder') |\
                    (cond == 'Moderate or heavy freezing rain') | (cond == 'Light rain shower') | (cond == 'Moderate or heavy rain shower'))

# tags: tshirt(long, short, sleeveless)
#       shirt(long, short, sleeveless)
#       sweater
#       hoodie
#       
#       pants(short, long)
#       skirt(short, long)
#       
#       sweat
#       jumpsuit
#       suits
#       dress
#       
#       scarf
#       gloves
#       earmuf
#       hat
#       umbrella
#       
#       jacket
#       coat
def find_weather_recommend(cond, temp):

    weather_recommendations = {'shirt','pants', 'skirt'}

    if(temp <= 65):
        weather_recommendations.add('long')
    elif(temp > 65):
        weather_recommendations.add('short')
        if(temp > 90):
            weather_recommendations.add('sleveless')

    if(temp <= 60):
        weather_recommendations.update(('sweater', 'hoodie'))

    if((cond == 'Sunny') | (cond == 'Partly cloudy')):
        weather_recommendations.add('hat')
    
    if is_snowy(cond):
                if(cond == 'Freezing drizzle') | (cond == 'Heavy freezing drizzle'):
                    weather_recommendations.update(('scarf', 'gloves', 'earmuff', 'jacket', 'coat', 'umbrella'))
                else:
                    weather_recommendations.update(('scarf', 'gloves', 'earmuff', 'jacket', 'coat'))
    elif is_rainy(cond):
                    weather_recommendations.update(('umbrella', 'jacket', 'coat'))
    elif((temp <= 40)):
        weather_recommendations.update(('jacket', 'coat'))
    
    return weather_recommendations