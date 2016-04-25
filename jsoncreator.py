__author__ = "Sabbana"

import urllib2, os, json
import argparse

##
# jsoncreator.py -c --command
# Command of Service - latest|agenda|category|quote
#
#

dir = '/var/www/assets_ilmuberbagi_id/data/json/'
# dir = 'data/json/'

def main():
	try:
		parsers = argparse.ArgumentParser()
		parsers.add_argument('-c','--command', help='Command of service - latest|agenda|category', required=True)
		args = parsers.parse_args()
		if args.command=="latest":
			print "Generationg Latest Article - Ilmuberbagi..."
			url = 'http://services.ilmuberbagi.id/article/category/all/0/10'
			data = urllib2.urlopen(url).read()
			write(dir,'latest.json', data)
			
		elif args.command=="category":
			print "Generationg Article category - ilmuberbagi..."
			url = 'http://services.ilmuberbagi.id/article/category'
			data = urllib2.urlopen(url).read()
			write(dir,'category.json', data)
			
		elif args.command=="agenda":
			print "Generationg Agenda Kegiatan - ilmuberbagi..."
			url = 'http://services.ilmuberbagi.id/activity/agenda'
			data = urllib2.urlopen(url).read()
			write(dir,'agenda.json', data)
			
		else:
			print "Unknow command..."
			
	except ValueError:
		print ValueError


def write(directory="",filename="",content=""):
    try:
		if not os.path.exists(directory):
			os.makedirs(directory)
		with open(directory+'/'+filename, 'w') as outfile:
			json.dump(json.loads(content), outfile)
			outfile.close()
    except Exception, e: 
        print e

if __name__ == "__main__":
    main()
