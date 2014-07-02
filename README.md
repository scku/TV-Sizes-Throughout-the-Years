CNET-TV-Reviews
===============

Crawling CNET TV reviews

I was taking Udacity's [Exploratory Data Analysis](https://www.udacity.com/course/ud651) class and it linked to Nathan Yau's [blog entry](http://flowingdata.com/2009/09/23/tv-size-over-the-past-8-years/) where he analyzed the median TV sizes between 2002 and 2009. 

I thought it would be interesting to redo the analysis, adding in the recent years, to see what the median TV sizes is nowadays and whether it is still on track to reaching 60" by 2015 as originally modeled by Nathan. I took the same approach as Nathan and obtained my data by crawling CNET for TV reviews. I know this isn't indicative of the median TV size purchased by consumers but it is representive of TV models available, at least the popular ones, on the market. 

A friend introduced me to [Kimono Labs](https://www.kimonolabs.com/) so this would be a good opportunity to try it out. I couldn't quite get the pagination to work so I implemented a crawler with Python Scrapy to first crawl all the TV review links. I passed the list of links to an API created using Kimono to scrape the specifications for each of the TV models.

###Usage

To start launch the Scrapy spider, run the following command
```python
scrapy crawl cnettv -o links.txt -t csv
```

