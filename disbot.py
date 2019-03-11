import os
import discord
import asyncio
import random
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
	print('로그인 : '+(client.user.name))
	print('id : '+(client.user.id))
	print('------------------------')
	await client.change_presence(game=discord.Game(name='개발중이라 ㅃ기억 다름', type=1))
	
client = discord.Client()

@client.event
async def on_ready():
	print('로그인 : '+(client.user.name))
	print('id : '+(client.user.id))
	print('------------------------')
	await client.change_presence(game=discord.Game(name='<뺌 도움> = 사용법', type=1))
	
@client.event
async def on_message(message):
	id = message.author.id

	if message.author.bot:
		return None
#---------------------(간단한 명령어 기능)--------------------------
	if message.content == ('뺌 도움'):
		embed = discord.Embed(title="빼미에몽 사용법",
		description='뺌 골라줘 A B C.. - 선택장애가 올때 써\n'
			'뺌 배워 <할말> <대답> - 말을 가르쳐\n'
			'뺌 <할말> - 빼미에몽 : <대답>\n'
			'뺌 러시안 - 러시안룰렛 미니게임\n'
			'뺌 업다운 - 업다운 미니게임\n'
			'빼미에몽 - 대답을 해줘'
		,color=0x00ff00)
		embed.set_footer(text= '떵겜몬 도움 - 떵겜몬 명령어 사용법')
		await client.send_message(message.channel, embed=embed)
	elif message.content.startswith('뺌 골라줘'):
		choice = message.content.split(' ')
		choicenumber = random.randint(1, len(choice)-1)
		choiceresult = choice[choicenumber]
		await client.send_message(message.channel, str(choiceresult)+'이(가) 좋겠네')
	elif message.content.startswith('빼미에몽'):
		dosome = '왜,ㅖ,머,?,왜불러 할일이 그렇게 없어?'
		dosomechoice = dosome.split(',')
		dosomenumber = random.randint(1, len(dosomechoice)-1)
		dosomeresult = dosomechoice[dosomenumber]
		await client.send_message(message.channel, dosomeresult)
	elif message.content.startswith('뺌 배워') or message.content.startswith('빼미에몽님 배워주세요'):
		file = openpyxl.load_workbook('data.xlsx')
		sheet = file.active
		learn = message.content.split(' ')
		hmm = random.randint(1,13)
		if not hmm == 1:
			for i in range(1,257):
				if sheet['A'+str(i)].value == None or sheet['A'+str(i)].value == learn[2]:
					sheet['A'+str(i)].value = learn[2]
					for j in range(1,257):
						if sheet.cell(i,j).value == None:
							break
					sheet.cell(i,j).value = learn[3]
					await client.send_message(message.channel, '알았어 이제부터 '+str(learn[2])+'은(는) '+str(learn[3])+'이야')
					break
				if i == 256:
					await client.send_message(message.channel, '과부하! (최대 256단어)')
			file.save('data.xlsx')
		else:
			await client.send_message(message.channel, '싫은데? 빼미에몽님 배워주세요 라고 해봐')
	elif message.content.startswith('뺌 러시안'):
		file = openpyxl.load_workbook('rr.xlsx')
		sheet = file.active
		sheet['A'+str(1)].value = random.randint(1,6)
		sheet['B'+str(1)].value = 0
		await client.send_message(message.channel, '러시안룰렛이 시작됬어 "뺌 당겨"로 쏴')
		file.save('rr.xlsx')
	elif message.content.startswith('뺌 당겨'):
		file = openpyxl.load_workbook('rr.xlsx')
		sheet = file.active
		if not sheet['A'+str(1)].value == 0:
			sheet['B'+str(1)].value += 1
			if sheet['A'+str(1)].value == sheet['B'+str(1)].value:
				sheet['A'+str(1)].value = 0
				sheet['B'+str(1)].value = 0
				await client.send_message(message.channel, '탕! <@'+id+'> 머리에 총맞았어? 머리아파?')
			else:
				await client.send_message(message.channel, '틱. '+str(sheet['B'+str(1)].value)+'번째는 통과')
			file.save('rr.xlsx')
		else:
			await client.send_message(message.channel, '뺌 러시안을 먼저해야지 멍청아')
	elif message.content.startswith('뺌 업다운'):
		file = openpyxl.load_workbook('rr.xlsx')
		sheet = file.active
		if sheet['A'+str(2)].value == 0:
			sheet['A'+str(2)].value = random.randint(1,100)
			sheet['B'+str(2)].value = 0
			await client.send_message(message.channel, '업다운을 시작했어 "업다운 1~100"로 할수있어 기회는 7회야')
		else:
			await client.send_message(message.channel, '아직 진행중이야')
		file.save('rr.xlsx')
	elif message.content.startswith('업다운'):
		file = openpyxl.load_workbook('rr.xlsx')
		sheet = file.active
		number = message.content.split(' ')
		if not int(sheet['A'+str(2)].value) == 0:
			sheet['B'+str(2)].value += 1
			if int(sheet['A'+str(2)].value) == int(number[1]):
				await client.send_message(message.channel, '어케맞췄노 시발련ㄴ아')
				sheet['A'+str(2)].value = 0
				sheet['B'+str(2)].value = 0
			else:
				if int(sheet['A'+str(2)].value) < int(number[1]):
					await client.send_message(message.channel, '다운 '+str(7-sheet['B'+str(2)].value)+'번 남았어')
				else:
					await client.send_message(message.channel, '업 '+str(7-sheet['B'+str(2)].value)+'번 남았어')
				if sheet['B'+str(2)].value == 7:
					await client.send_message(message.channel, '끝났네 답은 '+str(sheet['A'+str(2)].value)+'인데 멍청이')
			file.save('rr.xlsx')
	elif message.content.startswith('뺌'):
		file = openpyxl.load_workbook('data.xlsx')
		sheet = file.active
		memory = message.content.split(' ')
		for i in range(1,257):
			if sheet['A'+str(i)].value == memory[1]:
				words = []
				for j in range(1,257):
					if not sheet.cell(i,j+1).value == None:
						words.append(sheet.cell(i,j+1).value)
					else:
						answer = random.choice(words)
						await client.send_message(message.channel, str(answer))
						break
				break
	





#--------------(떵겜몬)------------------------------------------------------------------
	if message.content.startswith('떵겜몬 도움') or message.content.startswith('ㄸ 도움'):
		embed = discord.Embed(title= '떵겜몬 명령어 모음',
		description= '떵겜몬 생성 - 아이디를 떵겜몬에 등록\n'
			'떵겜몬 인벤 - 똥가루와 뽑기 보유수를 확인\n'
			'떵겜몬 뽑기 등급 N - 보유한 뽑기를 N번 사용\n'
			'떵겜몬 재조합 N - 똥가루 50개 >> 랜덤 뽑기 1개\n'
			'떵겜몬 -> ㄸ로 축약 가능\n'
			, color=0x00ff00)
		embed.set_footer(text= '개발에 참여하고 싶다면 -> http://bitly.kr/8TrYH')
		await client.send_message(message.channel, embed=embed)

	if message.content.startswith('떵겜몬 생성') or message.content.startswith('ㄸ 생성'):
		file = openpyxl.load_workbook('dg_user.xlsx')
		sheet = file.active
		for i in range(1,257):
			if sheet['A'+str(i)].value == id:
				await client.send_message(message.channel, '<@'+id+'>의 정보는 이미 있어')
				break
			else:
				if sheet['A'+str(i)].value == None:
					sheet['A'+str(i)].value = str(id)
					file.save('dg_user.xlsx')
					file = openpyxl.load_workbook('dg_user_inv.xlsx')
					sheet = file.active
					sheet['C'+str(i)].value = 5
					file.save('dg_user_inv.xlsx')
					await client.send_message(message.channel, '생성 완료! C급 뽑기 5개도 지급했어')
					break

	if message.content.startswith('떵겜몬 인벤') or message.content.startswith('ㄸ 인벤'):
		file = openpyxl.load_workbook('dg_user.xlsx')
		sheet = file.active
		for i in range(1,257):
			if sheet['A'+str(i)].value == id:
				file = openpyxl.load_workbook('dg_user_inv.xlsx')
				sheet = file.active
				embed = discord.Embed(title= str(message.author.name)+'의 떵겜몬 인벤토리',
				description= '마법의 똥가루 : '+str(sheet['A'+str(i)].value)+'개\n'
					'랜덤 뽑기 : '+str(sheet['F'+str(i)].value)+'개\n'
					'C급 뽑기 : '+str(sheet['C'+str(i)].value)+'개\n'
				, color=0x00ff00)
				embed.set_footer(text= 'ex) 떵겜몬 뽑기 C 3 (C급 뽑기 3회)')
				await client.send_message(message.channel, embed=embed)
				break
		else:
			await client.send_message(message.channel, '먼저 "떵겜몬 생성"으로 계정을 만들어')

	if message.content.startswith('떵겜몬 뽑기') or message.content.startswith('ㄸ 뽑기'):
		memory = message.content.split(' ')
		file3 = openpyxl.load_workbook('dg_user.xlsx')
		sheet3 = file3.active
		for i in range(1,257):
			if sheet3['A'+str(i)].value == id:
				uid = i #uid : 유저 아이디 위치
				file4 = openpyxl.load_workbook('dg_user_inv.xlsx')
				sheet4 = file4.active
				if memory[2] == 'D': #등급 확인
					rank_lo = 'B'
				elif memory[2] == 'C':
					rank_lo = 'C'
				elif memory[2] == 'B':
					rank_lo = 'D'
				elif memory[2] == 'A':
					rank_lo = 'E'
				elif memory[2] == '랜덤':
					rank_lo = 'F'
				else:
					await client.send_message(message.channel, '떵겜몬 뽑기 <등급> <N> 으로 다시해봐')
					break
				rank = memory[2]
					
				if int(memory[3]) <= int(sheet4[str(rank_lo)+str(uid)].value): #수량이 있는지 확인
					sheet4[str(rank_lo)+str(i)].value -= int(memory[3]) #인벤에서 수량만큼 차감
					file = openpyxl.load_workbook('dg_mons.xlsx') #떵겜몬 도감번호
					sheet = file.active
					file2 = openpyxl.load_workbook('dg_user_mons.xlsx') #유저의 떵겜몬 보유현황
					sheet2 = file2.active
					roll = []
					if not memory[2] == '랜덤':
						for i in range(1,257): #도감에서 같은 등급만 걸러내는 작업
							if sheet['A'+str(i)].value == str(rank):
								roll.append(i)
						for i in range(1,int(memory[3])+1): #걸러낸 C등급에서 랜덤뽑기
							choice = random.choice(roll)
							if sheet2.cell(uid,choice+3).value == 1:
								if sheet['A'+str(choice)].value == 'B':
									dust = 50
								elif sheet['A'+str(choice)].value == 'A':
									dust = 250
								else:
									dust = 10
								sheet4['A'+str(uid)].value += dust
								await client.send_message(message.channel, str(sheet['A'+str(choice)].value)+'등급 '+str(sheet['B'+str(choice)].value)+'! -> 똥가루 '+str(dust)+'개')
							else:
								sheet2.cell(uid,choice+3).value = 1
								await client.send_message(message.channel, str(sheet['A'+str(choice)].value)+'등급 '+str(sheet['B'+str(choice)].value)+'!')
							file2.save('dg_user_mons.xlsx')
							file4.save('dg_user_inv.xlsx')
						break
					else:
						for i in range(1,int(memory[3])+1): #랜덤 뽑기의 등급을 설정
							rand = random.random()*100
							if rand < 1.5:
								rank = 'A'
							elif rand < 13:
								rank = 'B'
							elif rand < 85:
								rank = 'C'
							else:
								rank = 'D'
							roll = []
							for i in range(1,257): #설정된 등급에 맞는것들 모으기
								if sheet['A'+str(i)].value == str(rank):
									roll.append(i)

							choice = random.choice(roll) #모은것들 중 하나 뽑기
							if sheet2.cell(uid,choice+3).value == 1:
								if sheet['A'+str(choice)].value == 'B':
									dust = 50
								elif sheet['A'+str(choice)].value == 'A':
									dust = 250
								else:
									dust = 10
								sheet4['A'+str(uid)].value += dust
								await client.send_message(message.channel, str(sheet['A'+str(choice)].value)+'등급 '+str(sheet['B'+str(choice)].value)+'! -> 똥가루 '+str(dust)+'개')
							else:
								sheet2.cell(uid,choice+3).value = 1
								await client.send_message(message.channel, str(sheet['A'+str(choice)].value)+'등급 '+str(sheet['B'+str(choice)].value)+'!')
							file2.save('dg_user_mons.xlsx')
							file4.save('dg_user_inv.xlsx')
						break
				else:
					await client.send_message(message.channel, '그만큼 가지고 있는지 다시 확인해봐')
					break
		else:
			await client.send_message(message.channel, '먼저 "떵겜몬 생성"으로 계정을 만들어')

	if message.content.startswith('떵겜몬 재조합') or message.content.startswith('ㄸ 재조합'):
		command = message.content.split(' ')
		file = openpyxl.load_workbook('dg_user.xlsx')
		sheet = file.active
		for i in range(1,257):
			if sheet['A'+str(i)].value == id:
				file2 = openpyxl.load_workbook('dg_user_inv.xlsx')
				sheet2 = file2.active
				if sheet2.cell(i,1).value >= int(command[2])*50:
					sheet2.cell(i,1).value -= int(command[2])*50
					sheet2.cell(i,6).value += int(command[2])
					await client.send_message(message.channel, '랜덤 뽑기를 '+str(command[2])+'개 만들었어')
					file2.save('dg_user_inv.xlsx')
					break
				else:
					await client.send_message(message.channel, '재조합은 1회에 똥가루 50개야')
					break


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
