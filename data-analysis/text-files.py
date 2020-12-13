import glob
import pandas as panda


df_list = []
for ebert_review in glob.glob('ebert_reviews/*.txt'):
    with open(ebert_review, encoding='utf-8') as file:
        #entire_text = file.read()
        #one_line = file.readline()
        title = file.readline()[:-1]
        review_url = file.readline()[:-1]
        review_text = file.read()
        df_list.append({'title': title, 'review_url': review_url, 'review_text': review_text})

df = panda.DataFrame(df_list, columns=['title', 'review_url', 'review_text'])

print(df.info())
print(df.describe())



debug = 1