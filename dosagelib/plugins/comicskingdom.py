# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _BasicScraper
from ..helpers import indirectStarter

import re


class ComicsKingdom(_BasicScraper):
    imageSearch = re.compile(r' image-url="(https://safr\.kingfeatures\.com/api/img\.php\?e=...&amp;s=c&amp;file=[^"]+)"')
    prevSearch = re.compile(r' :is-left-arrow="true" .*date-slug="(\d\d\d\d-\d\d-\d\d)"')
    help = 'Index format: yyyy-mm-dd'

    # imageSearch = '//a[contains(@class,"fancybox")]/img'
    # prevSearch = '//a[@id="nav_prev"]'
    # latestSearch = '//div[contains(@class,"caption")]/a'
    # starter = indirectStarter

    def __init__(self, name, path, lang=None):
        super(ComicsKingdom, self).__init__('ComicsKingdom/' + name)
        self.url = 'https://comicskingdom.com/' + path
        if lang:
            self.lang = lang
    
    def namer(self, image_url, page_url):
        
        if page_url != self.url:
 
            date = page_url.rsplit('/', 3)[3]
            name = page_url.rsplit('/', 3)[2]
            
        else:
            
            import datetime
            date = datetime.date.today().strftime("%Y-%m-%d")
            name = page_url.rsplit('/', 2)[2]
            
        #    date = datetime.date.today().strftime("%B-%d-%Y")
        # name.title ensures that the comics are named the same
        # as in the previous scraper
        return "%s_%s.png" % (name.title(), date)
    
    def link_modifier(self, url, tourl):
        
        urllen = len(self.url)
        if tourl[:urllen] != self.url:
            
            datestr = tourl[-11:]        # /YYYY-MM-DD
            tourl = self.url + datestr
            
        return tourl


    @classmethod
    def getmodules(cls):
        return (
            # Some comics are not listed on the "all" page (too old?)
            
            cls('OnTheFastrack', 'on-the-fastrack'),
            cls('SafeHavens', 'safe-havens'),
            cls('KevinAndKell', 'kevin-and-kell'),
            cls('SallyForth', 'sally-forth'),
            cls('HagarTheHorrible', 'hagar-the-horrible'),
            cls('ShermansLagoon', 'sherman-s-lagoon'),
            cls('BarneyGoogleAndSnuffySmith', 'barney-google-and-snuffy-smith'),
            cls('MikeShelton', 'mike-shelton'),
            cls('DavidMHitch', 'david-m-hitch'),
            cls('DennisTheMenace', 'dennis-the-menace'),
            # do not edit anything below since these entries are generated from
            # scripts/comicskingdom.py
            # START AUTOUPDATE
            # END AUTOUPDATE
        )
