import os
import sys
import scrapy
import subprocess
from time import strftime
from datetime import datetime
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings


class CrawlerRun(object):

    def run(self):
        """ Feedly """
        process = CrawlerRunner({'USER_AGENT': "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6"})
        feedly = Feedly_Craler()
        feedly.run_crawl()
        """ Twitter """
        mydir = os.getcwd()
        mydir_tmp = os.path.dirname(os.path.abspath(__file__))
        os.chdir(mydir_tmp)
        subprocess.call(['scrapy', 'crawl', 'nerdologia'])
        subprocess.call(['scrapy', 'crawl', 'jovemnerd'])
        os.chdir(mydir)
