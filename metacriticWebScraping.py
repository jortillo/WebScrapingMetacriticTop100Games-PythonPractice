import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup

#dictionary
data_dict = {'name':[], 'platform':[], 'release_date':[], 'metascore':[]}


#sets response back from webpage
def webpage(pageNum):
    URL = "https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?view=condensed&page="+ str(pageNum)

    user_agent = {'User-agent': 'Mozilla/5.0'}
    page = requests.get(URL, headers = user_agent)

    return page
    

#web scraping
def webscraper(page):
    soup = BeautifulSoup(page.content, "html.parser")
    #table contains game scores in groups of 5
    tables = soup.find_all('table', {"class" : "clamp-list condensed"})
    count = 0
    for table in tables:
        
        #each table row is a game. table row contains a game. They also include game score, game title, game rank #, game platform, game release date.
        table_rows = table.find_all('tr')
        for tr in table_rows:
            #get game title
            count += 1
            details = tr.find('td', {"class" : "details"})
            title = details.find('a', {"class" : "title"})
            data_dict['name'].append(title.find('h3').text) 

            #get game platform
            platform = details.find('span', {"class" : "data"})
            #strip white spaces | data cleaning
            data_dict['platform'].append(platform.text.strip())

            #get game release date
            date = details.find('span',{"class":""})
            data_dict['release_date'].append(date.text)


            #get game metascore
            score = tr.find('td', {"class" : "score"})
            metaScore = score.find('div')
            data_dict['metascore'].append(metaScore.text)

def main():
    webscraper(webpage(0))
    df = (pd.DataFrame.from_dict(data_dict))
    df.to_csv('matacritic100.csv')
    data = pd.read_csv('matacritic100.csv', index_col=0)
    print(data.to_string())

    #data visualization of avg score by platforms in top 100
    df_platforms = data[['platform', 'metascore']]
    df_plt_scores = df_platforms.groupby(['platform']).mean().sort_values(by = 'metascore', ascending = False)
    df_plt_scores.reset_index(inplace = True)
    df_plt_scores = pd.melt(df_plt_scores, id_vars=['platform'], value_vars=['metascore'])

    print(df_plt_scores)
    
    plt.barh('platform', 'value', data=df_plt_scores)

    plt.title('Platform rankings by metascore')
    plt.xlabel('Score')
    plt.ylabel('Platform')

    plt.show()

main()

#data cleaning done. Stripped white spaces from platform values.