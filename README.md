# toilet-paper-scraper


In response to the unusual time in 2020 with COVID-19 pandemic haunting the world, everyone has the responsibility to help ease the darkness in their own way. I chose to tackle the issue on how to deal with supply shortage of toilet paper by open sourcing this project to a broader audience needed. 


### Overview

Scripts in this project scan the search results of online sources for particular keywords (such as "toilet paper") and return results with specified brands. If matched results are found, there is a voice alert to inform users to take appropriate actions. 


### Prerequisite

1. Python3

2. virtualenv

3. (Computer)

4. (Internet)

5. ...


### Setup 

1. Create a virtual environment for project dependencies:

```
virtualenv -p python3 ~/venvs/scraper-env
```

2. Install dependencies within the virtual environment:

```
source ~/venvs/scraper-env/bin/activate
pip3 install -r requirements.txt
```


### Run

1. To run the scraper once, under `<project_root_directory>`, example:

```
python3 amazon/scrape.py --keywords "toilet paper" --brands "Quilton"
```

2. To setup a cron job to run the scraper periodically, please refer to the crontab example file `crontab_example`


### TODO

- Add scrapers for more online sources other than Amazon AU
