# # pip install requests
# pip install bs4
# pip install openpyxl
# downloading the modules in cmd or in new terminals using these commands for imprting the library

from bs4 import BeautifulSoup #importing beautiful soup module to extract data

import requests,openpyxl     #impoorting requests module                          

excel = openpyxl.Workbook()
# creating a excel sheet

flag = 0
num = 51

# .........................................
# print(excel.sheetnames)                 .
# the default sheet name is Sheet..       .  
# ........................................

sheet = excel.active
# creating a active sheet so that we can work in it
# active sheet is a  sheet where we are going to load the data..

sheet.title = "MOVIES RATING DATA ."
# changing the sheet name 

print('Enter the genre of movies you want to search')
key = input('>>>')
url = 'https://www.imdb.com/search/title/?genres=' + key + '&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=GGW643NSZPHTRE75NGY2&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1'

# sheet.append(key)
sheet.append(['MOVINAME ','MOVIE RATING' , 'YEAR OF RELEASE' , 'CAST OF THE MOVIE' , 'LINK OF THE MOVIE']) 
# this function will put the column name of the excel sheet

for page in range(0,20):
    if flag==0:
        temp = 0
    else:
        strr = str(num)
        url = 'https://www.imdb.com/search/title/?genres=' + key + '&start=' + strr + '&explore=title_type,genres&ref_=adv_nxt'
        num = num + 50

    source =requests.get(url)
    # #STORING THE URL OF THE MOVIE INTO THE VARIABLE NAMED SOURCE
    # source.raise_for_status() ##checking the status of the url to check wheather the url is valid or not

    flag = 1

    soup =BeautifulSoup(source.text,'html.parser')
    # here we are parsing the data using html parser...we can also use lmxl parser to do the same task
    #    print(soup)
    #   finding all the tr tags from the list of the movies

    movies = soup.find_all('div',class_='lister-item mode-advanced')
    # storing the the html content of class lister-item mode-advanced inside the tag named div
        
        # print(len(movies))    ----->> this is used to store the number of movies extractd from the html file of imdb website

    list=''         #creating the empty list

    for movie in movies:

         
        image_block = movie.find('div',class_='lister-item-image float-left')
        linktm = image_block.a['href']
        movie_link = 'https://www.imdb.com/' + linktm + '?ref_=adv_li_i'
        print(movie_link)
        print('')

        block = movie.find('div',class_='lister-item-content')
         # making the single block of each movie ...


        header = block.find('h3',class_='lister-item-header')
        name = header.a.text
        year = header.find_all('span')
        yearr = year[-1].text

        star1 = block.find_all('p')
        star2 = star1[-2].find_all('a')
        print(name)
        print(yearr)
        
        for star in star2:
            list += star.text+','


        rating = block.find('div',class_='inline-block ratings-imdb-rating')
        if rating != None:
            ratings = rating.strong.text
        print(ratings)
        if list=='':
            list = 'NA'
        sheet.append([name,ratings,yearr,list,movie_link])
        list=''
    

        # print(rating)
        # this will find the rating of the movie under the td tag of different class named ratingColumn imdbRating under tag strong
        

       
        # this will append all the information of all the movies in the excel sheets 
excel.save('IMDB Movie Ratings.xlsx')
#saving the scrapped data into the excel file
