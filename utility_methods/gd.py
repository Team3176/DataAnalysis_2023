import pandas as pd
import csv
#setup
file = open('Mishawaka Scout All Matches 2.csv')
csv_reader = csv.reader(file)
compressed_sd = list(csv_reader)
#get scouter data
class GD:
    def get_match_number(self,l):
        n = l[3]
        return n
    def get_asg(self,team):
        asg = []
        for list in compressed_sd:
            if team in list:
                asg.append(list[7])
        return asg
    def get_acs(self,team):
        acs = []
        for list in compressed_sd:
            if team in list:
                acs.append(list[9])
        return acs
    def get_tsg(self,team):
        tsg = []
        for list in compressed_sd:
            if team in list:
                tsg.append(list[13])
        return tsg
    def get_ad(self,team):
        ad = []
        for list in compressed_sd:
            if team in list:
                ad.append(list[11])
        return ad
    def get_fs(self,team):
        fs = []
        for list in compressed_sd:
            if team in list:
                fs.append(list[21])
        return fs
    def get_die(self,team):
        die = []
        for list in compressed_sd:
            if team in list:
                die.append(list[28])
        return die
    def get_tip(self,team):
        tip = []
        for list in compressed_sd:
            if team in list:
                tip.append(list[29])
        return tip
    def get_comments(self,team):
        comments = []
        for list in compressed_sd:
            if team in list:
                j = GD.get_match_number(self,list)
                str(j)
                comments.append(j + ':' + ' ' + str(list[32]))
        return comments