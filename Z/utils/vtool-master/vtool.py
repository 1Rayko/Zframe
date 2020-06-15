import os, vk
os.system("clear")

f = open ('.tokens', 'a+')
f.close ()
f = open ('.tokens', 'r')

def login ():
	token = f.readline ()
	token = token[:len (token) - 1]
	if token == '':
		return True
	else:
		session = vk.Session(access_token=token)
		return vk.API(session ,v='5.92', lang='ru')
def likes ():
	lap = 0
	all = 0
	succ = 0
	params = getlink ()
	quantity = input ("\033[35mEnter the quantity: \033[0m")
	print ('')
	while lap < int(quantity):
		api = login ()
		all += 1
		if api == True:
			all -= 1
			break
		elif api == False:
			continue
		try:
			api.likes.add(owner_id=int(params[1]),item_id=int(params[2]),type=params[0])
			lap += 1
			succ += 1
			print ("\033[32m Successful")
		except:
			print ("\033[31m Error")
	print ('\n\033[35mResults:\033[32m    Successful: ' + str(succ) + '\033[31m    Failed: ' + str(all - succ))
def followers ():
	lap = 0
	all = 0
	succ = 0
	params = getlink ()
	quantity = input ("\033[35mEnter the quantity: \033[0m")
	print ('')
	if params[0] == "id":
		while lap < int(quantity):
			api = login ()
			all += 1
			if api == True:
				all -= 1
				break
			elif api == False:
	                        continue
			try:
				api.friends.add(user_id=int(params[1]))
				lap += 1
				succ += 1
				print ("\033[32m Successful")
			except:
        	                print ("\033[31m Error")
	else:
		while lap < int(quantity):
			api = login ()
			all += 1
			if api == True:
				all -= 1
				break
			elif api == False:
	                        continue
			try:
				api.groups.join(group_id=int(params[1]))
				lap += 1
				succ += 1
				print ("\033[32m Successful")
			except:
	                        print ("\033[31m Error")
	print ('\n\033[35mResults:\033[32m    Successful: ' + str(succ) + '\033[31m    Failed: ' + str(all - succ))
def unlikes ():
	lap = 0
	all = 0
	succ = 0
	params = getlink ()
	quantity = input ("\033[35mEnter the quantity: \033[0m")
	print ('')
	while lap < int(quantity):
		api = login ()
		all += 1
		if api == True:
			all -= 1
			break
		elif api == False:
                        continue
		try:
			api.likes.delete(owner_id=int(params[1]),item_id=int(params[2]),type=params[0])
			lap += 1
			succ += 1
			print ("\033[32m Successful")
		except:
                        print ("\033[31m Error")
	print ('\n\033[35mResults:\033[32m    Successful: ' + str(succ) + '\033[31m    Failed: ' + str(all - succ))
def unfollowers ():
	lap = 0
	all = 0
	succ = 0
	params = getlink()
	quantity = input ("\033[35mEnter the quantity: \033[0m")
	print ('')
	if params[0] == "id":
		while lap < int(quantity):
			api = login ()
			all += 1
			if api == True:
				all -= 1
				break
			elif api == False:
	                        continue
			try:
				api.friends.delete(user_id=int(params[1]))
				lap += 1
				succ += 1
				print ("\033[32m Successful")
			except:
	                        print ("\033[31m Error")
	else:
		while lap < int(quantity):
			api = login ()
			all += 1
			if api == True:
				all -= 1
				break
			elif api == False:
        	                continue
			try:
				api.groups.leave(group_id=int(params[1]))
				lap += 1
				succ += 1
				print ("\033[32m Successful")
			except:
	                        print ("\033[31m Error")
	print ('\n\033[35mResults:\033[32m    Successful: ' + str(succ) + '\033[31m    Failed: ' + str(all - succ))
def getlink ():
	space = 0
	step = 0
	type = ""
	firstID = ""
	secondID = ""
	link = input ("\033[35mEnter the link: \033[0m")
	for char in range (len(link)):
		if link[char] == ".":
			space = char + 5
		if char < space:
                        continue
		if step == 0:
			if space != 0:
				try:
					int(link[char])
					step = 1
					firstID += link[char]
				except:
					type += link[char]
		elif step == 1:
			if link[char] != "_":
				firstID += link[char]
			else:
				step = 2
		elif step == 2:
			secondID += link[char]
	return type, firstID, secondID
print ("""\033[37m
 Termux-Lab               Vk: @termuxlab\033[32m
 ┏━━┳━━┳━━┳━━┓  ┏━━━━━┳━━━━━┳━━━━━┳━┓
 ┃  ┃  ┃    ┏┛  ┗━┓ ┏━┫  ┓  ┃  ┓  ┃ ┃
 ┗┓   ┏┫    ┗┓    ┃ ┃ ┃  ┗  ┃  ┗  ┃ ┗━━┓
  ┗━━━┛┗━━┻━━┛    ┗━┛ ┗━━━━━┻━━━━━┻━━━━┛
""")
done = False
while (not done):
	done = True
	print ("""\033[35m[1]\033[0m Add likes \033[35m
[2]\033[0m Add followers \033[35m
[3]\033[0m Other \033[35m\n
[4]\033[0m Add token \033[35m
""")
	task = input ("Please, enter your task's number: \033[0m")
	if task == "1":
		likes ()
	elif task == "2":
	        followers ()
	elif task == "3":
		print ("""\033[35m
[1]\033[0m Delete likes \033[35m
[2]\033[0m Delete followers \033[35m
""")
		task = input ("Please, enter your task's number: \033[0m")
		if task == "1":
			unlikes ()
		elif task == "2":
			unfollowers ()
		else:
			done = False
			print ("""\033[31mEnter right number
""")
	elif task == "4":
		tk = input ("\033[35mEnter the token: \033[0m")
		try:
			session = vk.Session(access_token=tk)
			api = vk.API(session ,v='5.92', lang='ru')
			api.wall.createComment(owner_id=-191163638,post_id=1,message="не дадим мы токены!!)")
			w = open ('.tokens', 'a')
			w.write (tk + '\n')
			w.close ()
		except:
			print ("Invalid token")
	else:
		done = False
		print ("""\033[31mEnter right number
""")
print ("")
f.close ()
