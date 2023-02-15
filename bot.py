import requests
print(f"""
\033[1;37m___   ___ .__   __. ___   ___ 
\  \ /  / |  \ |  | \  \ /  / • XNX TOOL •
 \  V  /  |   \|  |  \  V  /  • BOT • 
  >   <   |  . `  |   >   <   
 /  .  \  |  |\   |  /  .  \  
/__/ \__\ |__| \__| /__/ \__\   
--------------------------------------------------
     Author  : Ahmed 
     Github  : Ahmed-XD
     OPEN SOURCE CODE
--------------------------------------------------""")
print('\n\nType exit in messege to exit\n\n')
print("--------------------------------------------------")
for x in range(10000):
	xo = input('enter messege : ')
	if 'exit' in xo:
		exit()
	else:
		messege = requests.get(f"https://api.simsimi.net/v2/?text={xo}?&lc=en&bn=false").json()["success"]
		print(f'bot messege : {messege}')
