# DataChallenge
Introduction
============
Data challenge project.
Attempt to scrape websites for tourist's destinations.
DISCLAIMER : All information scraped are only used for the demonstration of the DataChallenge. No intention of using the information gathered for malicious intent.

BluePrint for scraping.
===========

1.  Market research, time is first spend trying to find a large enough website to scrape popular tourist destinations from.

2.  Once a big enough website is found, i inspected the SiteMap of the company's website to ensure that the website can be crawled with ease.

3.  Simply crawl the xml using scrapy and output the links and title of the and url of the website to a csv file.
    ![Ui](images/Ui.png)

4.  Once I have a small batch of CSV URL and title of the HTML I inspect the urls and the content to see if they are what i am looking for. Record down the useless URL to add them into sitemap\_rules so that they wont be scraped.

5.  Once an appropriate sitemap\_rules are established. I created a item object with the following attributes :

    -   **Destination** : The tourist destination.

    -   **Continent** : The continent of the destination.

    -   **Country** : The country of the destination.

    -   **City** : The city of the destination.

6.  More attributes can be added to the class if needed, since the challenge only wanted the tourist destination i feel that this would suffice. 

7.  Since the website that i choice to crawl support a multiLingual platform. I made sure to convert every webpage to the english version. 

8.  After handling the edge case and further testing the crawler using scrapy shell. I was able to obtain all the xpath related to the information i want to crawl.

9.  Finally we can begin scraping the website. Making sure that all the information is properly formated before leaving the crawler to run.

If more tourist destination is needed. We can simply rinse and repeat the above process on another sitemap.

Use of program.
===========
1.  Clone the repo.
2.  activate the env:`env/bin/activate`
3.  Change directory to ~/env/destinations
4.  Use the different spider to crawl the websites.
    -   **arrivalguides.com** : `scrapy crawl arrivalguides -t csv -o example1.csv`

    -   **holidify.com** : `scrapy crawl holidify -t csv -o example2.csv`

    -   **lonelyplanet.com** : `scrapy crawl lonelyplanet -t csv -o example3.csv`


Attempt on scraping Airport zip code.
===========

1.  Did some research and managed to get the names,latitude and longtitude of all the airports in the world in a CSV.

2.  Used Selenium to enter all the latitude and longtitude of the airports to a script to get the ZIP code.

3.  Not all country uses a postal / zip code. Thus some airport's zip code are left blank.

4.  Reason for using Selenium is because there isn't a website that offers all the zip code of the airports to crawl. Some website provide zipcode of airport in America but no the whole world. They also dont cover small airports.

P.S This method is very slow. As compared to gathering from sidemaps.
 
Use of Selinium.
===========

1.  Download google chrome webdriver and all the imports.

2.  Run PartC/test/Zipcode.py

