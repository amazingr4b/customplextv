from random import randint, shuffle
import sys

global plex
global client


def plexlogin():
	global plex
	global client

	baseurl = "http://serverip:port"
	
	from plexapi.server import PlexServer

	plex = PlexServer(baseurl)

	client = plex.client("clientnamegoeshere")


def getmovies():
	plexlogin()
	movielist = plex.library.section("Movies")
	mvlist = movielist.search("")
	max = len(mvlist)-1
	plme = randint(0, max)
	playme = mvlist[plme].title
	print ("Found the following title: " + playme + "\nTrying to play that now.")
	client.playMedia(mvlist[plme])
	return ("Done.")

def stopvideo():
	plexlogin()
	client.stop('video')

def pausevideo():
	plexlogin()
	client.pause('video')

	


#say = getmovies()

if ("stopvideo" in sys.argv[1]):
	stopvideo()
	say = "Done"
elif ("pausevideo" in sys.argv[1]):
	pausevideo() 
	say = "Done"
elif ("startnextprogram" in sys.argv[1]):
	say = getmovies()

print (say)

	

	
