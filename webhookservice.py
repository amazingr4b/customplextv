import web
import os

global WSTATUS
WSTATUS = "ON"

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

def getclient(data):
        client = data
        client = client.split("\"Player\":")
        client = client[1]
        client = client.split("},")
        client = client[0]
        client = client.split("title\":\"")
        client = client[1]
        client = client.split("\"")
        client = client[0]
        return (client)

def getaction(data):
        action = data
        action = action.split("event\":\"")
        action = action[1]
        action = action.split("\"")
        action = action[0]
        return action

class hooks:
	def POST(self):
		global WSTATUS
		client = "Your Client Name Goes Here"

		data = web.data()
		clnt = getclient(data)
		action = getaction(data)
		print (clnt)
		print (action)

		if WSTATUS == "ON":

			if (("media.pause" in action) and (clnt == client)):
				print ("Paused")
			elif (("media.resume" in action) and (clnt == client)):
				print ("Resumed")
			elif (("media.stop" in action) and (clnt == client)):
				print ("Stopped")
				WSTATUS = "Pending"
				command = "python myplextv.py startnextprogram"
				print ("Starting Next Program")
				os.system(command)
			elif (("media.scrobble" in action) and (clnt == client)):
				print ("Current feature is almost over.")

		elif (WSTATUS == "Pending"):
			if (("media.stop" in action) and (clnt == client)):
				print ("Duplicate Request, Dropping.")
			elif (("media.play" in action) and (clnt == client)):
				print ("Media Playing, Resetting Status.")
				WSTATUS = "ON"
		


		return ("OK")

if __name__ == '__main__':
	app.run()
