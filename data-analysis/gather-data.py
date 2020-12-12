import pandas as panda
import os
from bs4 import BeautifulSoup
import requests



def ebert_reviews():
    folder_name = 'ebert_reviews'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    url = 'https://some.url'
    response = requests.get(url)



def rotten_tomatoes_mock_scrape():
    # read a tsv
    df = panda.read_csv('bestofrt.tsv', sep='\t')

    scrape = False
    if scrape:
        folder = 'data/rt_html/'
        df_list = []
        for movie_html in os.listdir(folder):
            with open(os.path.join(folder, movie_html)) as file:
                soup = BeautifulSoup(file, 'lxml')
                title = soup.find('title').contents[0][:-len(' - Rotten Tomatoes')]
                audience_score = soup.find('div', class_='audience-score meter').find('span').contents[0][:-1]
                num_audience_ratings = soup.find('div', class_='audience-info hidden-xs superPageFontColor')
                num_audience_ratings = num_audience_ratings.find_all('div')[1].contents[2].strip().replace(',', '')

                df_list.append({
                    'title': title,
                    'audience_score': int(audience_score),
                    'number_of_audience_ratings': int(num_audience_ratings)
                })

        df = panda.DataFrame(df_list, columns=['title', 'audience_score', 'number_of_audience_ratings'])




#


