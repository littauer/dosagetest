# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _BasicScraper
from ..helpers import indirectStarter

import re


class ComicsKingdom(_BasicScraper):
    imageSearch = re.compile(r' image-url="(https://safr\.kingfeatures\.com/api/img\.php\?e=...&amp;s=.&amp;file=[^"]+)"')
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
            
            # do not edit anything below since these entries are generated from
            # scripts/comicskingdom.py
            # START AUTOUPDATE
            cls('AmazingSpiderMan', 'amazing-spider-man'),
            cls('Apartment3G', 'apartment-3-g_1'),
            cls('ArcticCircle', 'arctic-circle'),
            cls('BabyBlues', 'baby-blues'),
            cls('BarneyGoogleAndSnuffySmith', 'barney-google-and-snuffy-smith'),
            cls('BeetleBailey', 'beetle-bailey-1'),
            cls('BettyBoopSundays', 'betty-boop-sundays'),
            cls('BetweenFriends', 'between-friends'),
            cls('BigBenBolt', 'big-ben-bolt'),
            cls('BigBenBoltSundays', 'big-ben-bolt-sundays'),
            cls('Bizarro', 'bizarro'),
            cls('Blondie', 'blondie'),
            cls('BonersArk', 'boners-ark'),
            cls('BonersArkSundays', 'boners-ark-sundays'),
            cls('BrianDuffy', 'brian-duffy'),
            cls('BrickBradford', 'brick-bradford'),
            cls('BrilliantMindOfEdisonLee', 'brilliant-mind-of-edison-lee'),
            cls('BringingUpFather', 'bringing-up-father'),
            cls('Buckles', 'buckles'),
            cls('BuzSawyer', 'buz-sawyer'),
            cls('CarpeDiem', 'carpe-diem'),
            cls('Crankshaft', 'crankshaft'),
            cls('Crock', 'crock'),
            cls('Curtis', 'curtis'),
            cls('DaddyDaze', 'daddy-daze'),
            # DarrinBell has a duplicate in GoComics/DarrinBell
            cls('DavidMHitch', 'david-m-hitch'),
            cls('DennisTheMenace', 'dennis-the-menace'),
            cls('Dustin', 'dustin'),
            cls('EdGamble', 'ed-gamble'),
            cls('FamilyCircus', 'family-circus'),
            cls('FlashGordon', 'flash-gordon'),
            cls('FlashGordonSundays', 'flash-gordon-sundays'),
            cls('FunkyWinkerbean', 'funky-winkerbean'),
            cls('FunkyWinkerbeanSundays', 'funky-winkerbean-sundays'),
            cls('HagarTheHorrible', 'hagar-the-horrible'),
            cls('HeartOfJulietJones', 'heart-of-juliet-jones'),
            cls('HeartOfJulietJonesSundays', 'heart-of-juliet-jones-sundays'),
            cls('HiAndLois', 'hi-and-lois'),
            cls('IntelligentLife', 'Intelligent'),
            cls('JimmyMargulies', 'jimmy-margulies'),
            cls('JohnBranch', 'john-branch'),
            cls('JohnnyHazard', 'johnny-hazard'),
            cls('JohnnyHazardSundays', 'johnny-hazard-sundays'),
            cls('JudgeParker', 'judge-parker'),
            cls('JungleJimSundays', 'jungle-jim-sundays'),
            cls('KatzenjammerKids', 'katzenjammer-kids'),
            cls('KatzenjammerKidsSundays', 'katzenjammer-kids-sundays'),
            cls('KevinAndKell', 'kevin-and-kell'),
            cls('KingOfTheRoyalMounted', 'king-of-the-royal-mounted'),
            cls('KirkWalters', 'kirk-walters'),
            cls('KrazyKat', 'krazy-kat'),
            cls('LeeJudge', 'lee-judge'),
            cls('LittleIodineSundays', 'little-iodine-sundays'),
            cls('Lockhorns', 'lockhorns'),
            cls('Macanudo', 'Macanudo'),
            cls('MallardFillmore', 'mallard-fillmore'),
            cls('MandrakeTheMagician', 'mandrake-the-magician-1'),
            cls('MandrakeTheMagicianSundays', 'mandrake-the-magician-sundays'),
            cls('MarkTrail', 'mark-trail'),
            cls('Marvin', 'marvin'),
            cls('MaryWorth', 'mary-worth'),
            cls('MikePeters', 'mike-peters'),
            cls('MikeShelton', 'mike-shelton'),
            cls('MikeSmith', 'mike-smith'),
            cls('MooseAndMolly', 'moose-and-molly'),
            cls('MotherGooseAndGrimm', 'mother-goose-grimm'),
            cls('Mutts', 'mutts'),
            cls('OfficeHours', 'office-hours'),
            cls('OnTheFastrack', 'on-the-fastrack'),
            cls('PajamaDiaries', 'pajama-diaries'),
            cls('PardonMyPlanet', 'pardon-my-planet'),
            cls('Phantom', 'phantom'),
            cls('PhantomSundays', 'phantom-sundays'),
            cls('Popeye', 'popeye'),
            cls('PopeyesCartoonClub', 'popeyes-cartoon-club'),
            cls('PrinceValiant', 'prince-valiant'),
            cls('ProsAndCons', 'pros-cons'),
            cls('Quincy', 'quincy'),
            cls('RadioPatrol', 'radio-patrol'),
            cls('Redeye', 'redeye-2'),
            cls('RedeyeSundays', 'redeye-sundays'),
            cls('Retail', 'retail'),
            cls('RexMorganMD', 'rex-morgan-m-d'),
            cls('RhymesWithOrange', 'rhymes-with-orange'),
            cls('RipKirby', 'rip-kirby'),
            cls('SafeHavens', 'safe-havens'),
            cls('SallyForth', 'sally-forth'),
            cls('SamAndSilo', 'sam-and-silo'),
            cls('SecretAgentX9', 'secret-agent-x-9'),
            cls('ShermansLagoon', 'sherman-s-lagoon'),
            # Shoe has a duplicate in GoComics/Shoe
            cls('SixChix', 'six-chix'),
            cls('SlylockFoxAndComicsForKids', 'slylock-fox-and-comics-for-kids'),
            cls('TakeItFromTheTinkersons', 'take-it-from-the-tinkersons'),
            cls('TheLittleKing', 'the-little-king'),
            cls('ThimbleTheater', 'thimble-theater'),
            cls('Tiger', 'tiger'),
            cls('TigerSundays', 'tiger-sundays'),
            cls('ToddTheDinosaur', 'todd-the-dinosaur'),
            cls('ZippyThePinhead', 'zippy-the-pinhead'),
            cls('Zits', 'zits'),
            # END AUTOUPDATE
        )
