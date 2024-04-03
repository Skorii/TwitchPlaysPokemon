import socket
import threading
import pydirectinput

SERVER = "irc.twitch.tv"
PORT = 6667

#Your OAUTH Code Here https://twitchapps.com/tmi/
PASS = ""

#Channel to monitor (your twitch username)
CHANNEL = ""


#What you'd like to name your bot
BOT = "TwitchPlaysPokemon"

#Message sent in the chat to initiate game
START_MESSAGE = "Jouons ensemble à Pokemon!"
EXIT_MESSAGE = CHANNEL + " a arrêté le jeu."

message = ""
user = ""

irc = socket.socket()

irc.connect((SERVER, PORT))
irc.send((	"PASS " + PASS + "\n" +
			"NICK " + BOT + "\n" +
			"JOIN #" + CHANNEL + "\n").encode())

def gamecontrol():

	global message

	while True:

		if "haut" == message.lower():
			pydirectinput.press('z')
			message = ""

		if "bas" == message.lower():
			pydirectinput.press('s')
			message = ""

		if "gauche" == message.lower():
			pydirectinput.press('q')
			message = ""

		if "droite" == message.lower():
			pydirectinput.press('d')
			message = ""

		if "a" == message.lower():
			pydirectinput.press('a')
			message = ""

		if "b" == message.lower():
			pydirectinput.press('b')
			message = ""

		if "l" == message.lower():
			pydirectinput.press('l')
			message = ""

		if "r" == message.lower():
			pydirectinput.press('r')
			message = ""

		if "select" == message.lower():
			pydirectinput.press('y')
			message = ""

		if "start" == message.lower():
			pydirectinput.press('x')
			message = ""
		

def twitch():

	global user
	global message

	def joinchat():
		Loading = True
		while Loading:
			readbuffer_join = irc.recv(1024)
			readbuffer_join = readbuffer_join.decode()
			print(readbuffer_join)
			for line in readbuffer_join.split("\n")[0:-1]:
				print(line)
				Loading = loadingComplete(line)

	def loadingComplete(line):
		if("End of /NAMES list" in line):
			print(BOT + " has joined " + CHANNEL + "'s Channel!")
			sendMessage(irc, START_MESSAGE)
			return False
		else:
			return True

	def sendMessage(irc, message):
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
		irc.send((messageTemp + "\n").encode())

	def getUser(line):
		#global user
		colons = line.count(":")
		colonless = colons-1
		separate = line.split(":", colons)
		user = separate[colonless].split("!", 1)[0]
		return user

	def getMessage(line):
		#global message
		try:
			colons = line.count(":")
			message = (line.split(":", colons))[colons]
		except:
			message = ""
		return message

	def console(line):
		if "PRIVMSG" in line:
			return False
		else:
			return True

	joinchat()
	irc.send("CAP REQ :twitch.tv/tags\r\n".encode())
	while True:
		try:
			readbuffer = irc.recv(1024).decode()
		except:
			readbuffer = ""
		for line in readbuffer.split("\r\n"):
			if line == "":
				continue
			if "PING :tmi.twitch.tv" in line:
				print(line)
				msgg = "PONG :tmi.twitch.tv\r\n".encode()
				irc.send(msgg)
				print(msgg)
				continue
			else:
				try:
					user = getUser(line)
					message = getMessage(line)
					print(user + " : " + message)
					if user == CHANNEL and message.lower() == "exit":
						sendMessage(irc, EXIT_MESSAGE)
						exit(EXIT_MESSAGE)
				except Exception:
					pass

def main():
	if __name__ =='__main__':
		t1 = threading.Thread(target = twitch)
		t1.start()
		t2 = threading.Thread(target = gamecontrol)
		t2.start()
main()
