a = '''
Based on data officially published by the World Health Organization (WHO), an analysis of the sources of obesity rates in countries worldwide between 1975 and 2016 was carried out.

Source: https://apps.who.int/gho/data/node.main.A900A?lang=en
'''

b = '''\n\n The present time program aims to answer the following questions:

0. What is the obesity/gender ratio in 2015 in the world?
1. Which are the 5 countries with the highest and lowest rates of increase in obesity rates between 1975 and 2016 (period studied).
2. Which countries have the highest and lowest obesity rates in 2015?
3. What is the mean percentage difference in obesity between genders over the years in relation to world/Brazil?
'''

c = '''\n\n Some technical details:

-This data analysis was produced by combining native Python themes with functions from the Pandas library.
-In some cells we will display NaN - which means empty.
'''

d = '''\n\nAbout developer:

-Hello, my name is Luiz Esquivel, I'm 19 years old and currently I work as a Jr IT Analyst at Ultracom, being essentially co-responsible for the management activities of the mailing (I manage the data of clients and potential clients that we need to contact or have already contact us), I also manage data about customers and potential customers (such as: availability to serve their region with internet/telephrony products; primary credit analysis; primary analysis of data provided by the customer...) .
-I have been a development student since 2019, when I started studying WEB development, migrating to the data area in 2022, as I feel more confident in this area and recognize the importance of data in the lives and projects of companies and people.
-In the data area, my knowledge is centered on Office Package (especially Word and Excel); Business Intelligence methodology and tools (such as PowerBI); Database and its Management Systems (SQL and MySQL); Python focused on data analysis (automation of routines with Python).
'''

def about():
    texto = ""
    texto += a + b + c + d
    txt = texto.split("\n\n ")
    
    for i in txt:
        if input('Do you wish to continue? Y for yes and N for NO:-') == "N": break
        print(i)