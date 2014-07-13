GooglePlay-Crawler
==================

A webcrawler made in scrapy that tells you the best paid and best free apps from each category.


#Categories
* BOOKS_AND_REFERENCE
* BUSINESS
* COMICS
* COMMUNICATION
* EDUCATION
* ENTERTAINMENT
* FINANCE
* HEALTH_AND_FITNESS
* LIBRARIES_AND_DEMO
* LIFESTYLE
* APP_WALLPAPER
* MEDIA_AND_VIDEO
* MEDICAL
* MUSIC_AND_AUDIO
* NEWS_AND_MAGAZINES
* PERSONALIZATION
* PHOTOGRAPHY
* PRODUCTIVITY
* SHOPPING
* SOCIAL
* SPORTS
* TOOLS
* TRANSPORTATION
* TRAVEL_AND_LOCAL
* WEATHER
* WIDGETS

#Dependencies

Requires Scrapy and all submodules it requires. To find out more go to the [Scrapy Website](http://doc.scrapy.org/en/latest/intro/install.html#intro-install)

#Usage

Navigate to the root directory (i.e where you can see the play and links folders). Then run commands in the following pattern :

 `scrapy crawl category-name -o nameoffile.csv -t csv`
 
For example :
  `scrapy crawl comics -o comics.csv -t csv`
  
NOTE: Use lowercase when entering category names.  
NOTE: CSV can be substituted for JSON and XML as well but I prefer CSV.


#ToDo

 * Add Game Categories
 * Add Price info.
 * Add Editors Choice.
 

#Automated Contribution

 If you want to contribute any game category for example Action Games it is really very easy.
 
 1. Go to the links directory and add GAME_ACTION to W.txt file.
 2. Run ` python createfiles.py `.
 3. Run ` python createspider.py `.
 4. Replace the old Make.py in the play/spiders folder with the new one found in the Links folder.
 5. Upload to Github and send a pull request.
 6. Pray :P.
 

This is just to show how easy it is to automate the writing of code and not having to write repetetive and predictable code manually.

#Authors
 * Hassaan Ali Wattoo.

