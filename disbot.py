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
	await client.change_presence(game=discord.Game(name='ㅃ? : 사용법', type=1))
	
@client.event
async def on_message(message):
	id = message.author.id

	if message.author.bot:
		return None

	if message.content == ('ㅃ?'):
		embed = discord.Embed(title="빼미에몽 사용법",
		description='ㅃ? / ㅃ주사위 / ㅃ뭐할까\nㅃ골라줘 A B C ... \nㅃ적어 A B / ㅃ기억 A\nㅃ러시안룰렛 / ㅃ업다운\n빼미에몽 / 뺌 바보',
		color=0x00ff00)
		await client.send_message(message.channel, embed=embed)

	if message.content == ('ㅃ주사위'):
		await client.send_message(message.channel, '결과는 '+str(random.randrange(1,7))+' 이네')

	if message.content.startswith('뺌 바보'):
		dosome = '흑흑 ㅗ 너무해 ㅠㅠ'
		dosomechoice = dosome.split(' ')
		dosomenumber = random.randint(1, len(dosomechoice)-1)
		dosomeresult = dosomechoice[dosomenumber]
		await client.send_message(message.channel, dosomeresult)

	if message.content.startswith('ㅃ골라줘'):
		choice = message.content.split(' ')
		choicenumber = random.randint(1, len(choice)-1)
		choiceresult = choice[choicenumber]
		await client.send_message(message.channel, str(choiceresult)+'이(가) 좋겠네')

	if message.content.startswith('ㅃ뭐할까'):
		dosome = '누워서폰이 잠자기 롤이 옵치 에이펙스 던파 혼밥이 유투브 웹툰보기'
		dosomechoice = dosome.split(' ')
		dosomenumber = random.randint(1, len(dosomechoice)-1)
		dosomeresult = dosomechoice[dosomenumber]
		await client.send_message(message.channel, str(dosomeresult)+'나 쳐하는건 어떨까요?')

	if message.content.startswith('빼미에몽'):
		dosome = '왜 ㅖ 머'
		dosomechoice = dosome.split(' ')
		dosomenumber = random.randint(1, len(dosomechoice)-1)
		dosomeresult = dosomechoice[dosomenumber]
		await client.send_message(message.channel, dosomeresult)

	if message.content.startswith('ㅃ적어'):
		file = openpyxl.load_workbook('data.xlsx')
		sheet = file.active
		learn = message.content.split(' ')
		hmm = random.randint(1,6)
		if not hmm == 5:
			for i in range(1,257):
				if sheet['A'+str(i)].value == '-' or sheet['A'+str(i)].value == learn[1]:
					sheet['A'+str(i)].value = learn[1]
					sheet['B'+str(i)].value = learn[2]
					await client.send_message(message.channel, '알았어 이제부터 '+str(learn[1])+'은(는) '+str(learn[2])+'이야')
					break
				if i == 256:
					await client.send_message(message.channel, '과부하! (최대 256단어)')
			file.save('data.xlsx')
		else:
			await client.send_message(message.channel, '싫은데?')
	if message.content.startswith('ㅃ기억'):
		file = openpyxl.load_workbook('data.xlsx')
		sheet = file.active
		memory = message.content.split(' ')
		for i in range(1,257):
			if sheet['A'+str(i)].value == memory[1]:
				await client.send_message(message.channel, sheet['B'+str(i)].value)
				break
			if i == 256:
				await client.send_message(message.channel, '그게 뭔데 ㅆ덕아')

	if message.content.startswith('ㅃ러시안룰렛'):
		file = openpyxl.load_workbook('rr.xlsx')
		sheet = file.active
		sheet['A'+str(1)].value = random.randint(1,6)
		sheet['B'+str(1)].value = 0
		await client.send_message(message.channel, '러시안룰렛이 시작됬어 ㅃ쏴로 진행해')
		file.save('rr.xlsx')
	if message.content.startswith('ㅃ쏴'):
		file = openpyxl.load_workbook('rr.xlsx')
		sheet = file.active
		if not sheet['A'+str(1)].value == 0:
			sheet['B'+str(1)].value += 1
			if sheet['A'+str(1)].value == sheet['B'+str(1)].value:
				sheet['A'+str(1)].value = 0
				sheet['B'+str(1)].value = 0
				await client.send_message(message.channel, '탕! <@'+id+'>은(는) 머가리에 구멍났다')
			else:
				await client.send_message(message.channel, '찰칵. '+str(sheet['B'+str(1)].value)+'번째는 통과')
			file.save('rr.xlsx')
		else:
			await client.send_message(message.channel, 'ㅃ러시안룰렛을 먼저해야지 멍청아')

	if message.content.startswith('ㅃ업다운'):
		file = openpyxl.load_workbook('rr.xlsx')
		sheet = file.active
		if sheet['A'+str(2)].value == 0:
			sheet['A'+str(2)].value = random.randint(1,100)
			sheet['B'+str(2)].value = 0
			await client.send_message(message.channel, '업다운을 시작했어 !ㅃ1~100중에 불러 기회는 7회야')
		else:
			await client.send_message(message.channel, '아직 진행중이야')
		file.save('rr.xlsx')

	if message.content.startswith('!'):
		file = openpyxl.load_workbook('rr.xlsx')
		sheet = file.active
		number = message.content.split('ㅃ')
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
					await client.send_message(message.channel, '끝났네 답은 '+str(sheet['A'+str(2)].value)+'인데 바보~')
			file.save('rr.xlsx')

#--------------(똥겜몬)------------------------------------------------------------------

	if message.content.startswith('똥겜몬 생성'):
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
					sheet['B'+str(i)].value = 5
					file.save('dg_user_inv.xlsx')
					await client.send_message(message.channel, '생성 완료! C급 뽑기 5개도 지급했어')
					break

	if message.content.startswith('똥겜몬 인벤'):
		file = openpyxl.load_workbook('dg_user.xlsx')
		sheet = file.active
		for i in range(1,257):
			if sheet['A'+str(i)].value == id:
				file = openpyxl.load_workbook('dg_user_inv.xlsx')
				sheet = file.active
				embed = discord.Embed(title= str(message.author.name)+'의 똥겜몬 인벤토리',
				description= '마법의 똥가루 : '+str(sheet['A'+str(i)].value)+'개\n'
					'C급 뽑기 : '+str(sheet['B'+str(i)].value)+'개\n' 
					'B급 뽑기 : '+str(sheet['C'+str(i)].value)+'개\n'
					'뽑기 하는법 ex) 똥겜몬 뽑기 C 3 : C급 뽑기 3번'
				, color=0x00ff00)
				await client.send_message(message.channel, embed=embed)
				break
		else:
			await client.send_message(message.channel, '먼저 "똥겜몬 생성"으로 계정을 만들어')

	if message.content.startswith('똥겜몬 뽑기'):
		memory = message.content.split(' ')
		file3 = openpyxl.load_workbook('dg_user.xlsx')
		sheet3 = file3.active
		for i in range(1,257):
			if sheet3['A'+str(i)].value == id:
				idd = i
				file4 = openpyxl.load_workbook('dg_user_inv.xlsx')
				sheet4 = file4.active
				if memory[2] == 'C':
					if str(memory[3]) <= str(sheet4['B'+str(i)].value):
						sheet4['B'+str(i)].value = int(sheet4['B'+str(i)].value) - int(memory[3])
						file = openpyxl.load_workbook('dg_mons.xlsx')
						sheet = file.active
						file2 = openpyxl.load_workbook('dg_user_mons.xlsx')
						sheet2 = file2.active
						roll = []
						choice = []
						for i in range(1,257):
							if sheet['A'+str(i)].value == str('C'):
								roll.append(i)
						for i in range(1,int(memory[3])+1):
							choice.append(random.choice(roll))
						await client.send_message(message.channel, str(message.author.name)+'의 뽑기 결과!')
						for i in range(0,len(choice)):
							if sheet2.cell(idd,i+4).value == 1:
								sheet4['A'+str(i+1)].value += 50
								await client.send_message(message.channel, str(sheet['A'+str(choice[i])].value)+'등급 '+str(sheet['B'+str(choice[i])].value)+' (보유중이라 마법의 똥가루 50개로 대체)')
							else:
								sheet2.cell(idd,i+4).value = 1
								await client.send_message(message.channel, str(sheet['A'+str(choice[i])].value)+'등급 '+str(sheet['B'+str(choice[i])].value)+'!')
							file2.save('dg_user_mons.xlsx')
							file4.save('dg_user_inv.xlsx')
						break
					else:
						await client.send_message(message.channel, '그만큼 가지고 있는지 다시 확인해볼래?')
						break
				else:
					await client.send_message(message.channel, '제대로 입력해줘')
					break
		else:
			await client.send_message(message.channel, '먼저 "똥겜몬 생성"으로 계정을 만들어')


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
