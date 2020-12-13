import requests
import os
import pandas as panda
from PIL import Image
from io import BytesIO
# won't work, but still good for practice
import wptools

title_list = [
	'The_Wizard_of_Oz_(1939_film)',
	'Citizen_Kane',
	'The_Third_Man',
	'Get_Out_(film)',
	'Mad_Max:_Fury_Road',
	'The_Cabinet_of_Dr._Caligari',
	'All_About_Eve',
	'Inside_Out_(2015_film)',
	'The_Godfather',
	'Metropolis_(1927_film)',
	'E.T._the_Extra-Terrestrial',
	'Modern_Times_(film)',
	'It_Happened_One_Night',
	"Singin'_in_the_Rain",
	'Boyhood_(film)',
	'Casablanca_(film)',
	'Moonlight_(2016_film)',
	'Psycho_(1960_film)',
	'Laura_(1944_film)',
	'Nosferatu',
	'Snow_White_and_the_Seven_Dwarfs_(1937_film)',
	"A_Hard_Day%27s_Night_(film)",
	'La_Grande_Illusion',
	'North_by_Northwest',
	'The_Battle_of_Algiers',
	'Dunkirk_(2017_film)',
	'The_Maltese_Falcon_(1941_film)',
	'Repulsion_(film)',
	'12_Years_a_Slave_(film)',
	'Gravity_(2013_film)',
	'Sunset_Boulevard_(film)',
	'King_Kong_(1933_film)',
	'Spotlight_(film)',
	'The_Adventures_of_Robin_Hood',
	'Rashomon',
	'Rear_Window',
	'Selma_(film)',
	'Taxi_Driver',
	'Toy_Story_3',
	'Argo_(2012_film)',
	'Toy_Story_2',
	'The_Big_Sick',
	'Bride_of_Frankenstein',
	'Zootopia',
	'M_(1931_film)',
	'Wonder_Woman_(2017_film)',
	'The_Philadelphia_Story_(film)',
	'Alien_(film)',
	'Bicycle_Thieves',
	'Seven_Samurai',
	'The_Treasure_of_the_Sierra_Madre_(film)',
	'Up_(2009_film)',
	'12_Angry_Men_(1957_film)',
	'The_400_Blows',
	'Logan_(film)',
	'All_Quiet_on_the_Western_Front_(1930_film)',
	'Army_of_Shadows',
	'Arrival_(film)',
	'Baby_Driver',
	'A_Streetcar_Named_Desire_(1951_film)',
	'The_Night_of_the_Hunter_(film)',
	'Star_Wars:_The_Force_Awakens',
	'Manchester_by_the_Sea_(film)',
	'Dr._Strangelove',
	'Frankenstein_(1931_film)',
	'Vertigo_(film)',
	'The_Dark_Knight_(film)',
	'Touch_of_Evil',
	'The_Babadook',
	'The_Conformist_(film)',
	'Rebecca_(1940_film)',
	"Rosemary%27s_Baby_(film)",
	'Finding_Nemo',
	'Brooklyn_(film)',
	'The_Wrestler_(2008_film)',
	'The_39_Steps_(1935_film)',
	'L.A._Confidential_(film)',
	'Gone_with_the_Wind_(film)',
	'The_Good,_the_Bad_and_the_Ugly',
	'Skyfall',
	'Rome,_Open_City',
	'Tokyo_Story',
	'Hell_or_High_Water_(film)',
	'Pinocchio_(1940_film)',
	'The_Jungle_Book_(2016_film)',
	'La_La_Land_(film)',
	'Star_Trek_(film)',
	'High_Noon',
	'Apocalypse_Now',
	'On_the_Waterfront',
	'The_Wages_of_Fear',
	'The_Last_Picture_Show',
	'Harry_Potter_and_the_Deathly_Hallows_–_Part_2',
	'The_Grapes_of_Wrath_(film)',
	'Roman_Holiday',
	'Man_on_Wire',
	'Jaws_(film)',
	'Toy_Story',
	'The_Godfather_Part_II',
	'Battleship_Potemkin'
]

folder_name = 'best_of_rotten_tomatoes_posters'
if not os.path.exists(folder_name): os.makedirs(folder_name)

df_list = []
image_errors = {}
for title in title_list:
	try:
		ranking = title_list.index(title) + 1
		page = wptools.page(title, silient=True)
		image = page.get().data['image']
		poster_url = image[0]['url']
		r = requests.get(poster_url)
		i = Image.open(BytesIO(r.content))
		image_file_format = poster_url.split('.')[-1]
		i.save(folder_name + '/' + str(ranking) + '_' + title + '.' + image_file_format)
		df_list.append({'title': title, 'ranking': ranking, 'poster_url': poster_url})
	except Exception as e:
		image_errors[str(ranking) + '_' + title] = str(e)

for key in image_errors.keys(): print(key)

error_urls = {
	'22_A_Hard_Day%27s_Night_(film)': 'https://upload.wikimedia.org/wikipedia/en/4/47/A_Hard_Days_night_movieposter.jpg',
	'53_12_Angry_Men_(1957_film)': 'https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg',
	'72_Rosemary%27s_Baby_(film)': 'https://upload.wikimedia.org/wikipedia/en/e/ef/Rosemarys_baby_poster.jpg',
	'93_Harry_Potter_and_the_Deathly_Hallows_–_Part_2': 'https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg'
}
for rank_title, images in image_errors.items():
	url = ''
	if rank_title in error_urls: url = error_urls[rank_title]
	title = rank_title[3:]
	df_list.append({'ranking': int(title_list.index(title)) + 1, 'title': title, 'poster_url': url})
	r = requests.get(url)
	i = Image.open(BytesIO(r.content))
	image_file_format = url.split('.')[-1]
	i.save(folder_name + '/' + rank_title + '.' + image_file_format)
	
df = panda.DataFrame(df_list, columns=['ranking', 'title', 'poster_url'])
df = df.sort_values('ranking').reset_index(drop=True)
	
	
	
	
	







# end of file