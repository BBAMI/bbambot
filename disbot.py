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
		description='ㅃ? / ㅃ주사위 / ㅃ뭐할까\nㅃ골라줘 A B C ... \nㅃ적어 A B / ㅃ기억 A\nㅃ러시안룰렛 ㅃ업다운\n빼미에몽 / 뺌 바보',
		color=0x00ff00)
		await client.send_message(message.channel, embed=embed)

	if message.content == ('ㅃ주사위'):
		await client.send_message(message.channel, '결과는 '+str(random.randrange(1,7))+' 이네')

	if message.content.startswith('뺌 바보'):
		dosome = '흑흑 ㅗ 너무해 ㅠㅠ'
		dosomechoice = dosome.split(' ')
		dosomenumber = random.randint(1, len(dosomechoice)-1)
		dosomeresult = dosomechoice[dosomenumber-1]
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
		dosomeresult = dosomechoice[dosomenumber-1]
		await client.send_message(message.channel, str(dosomeresult)+'나 쳐하는건 어떨까요?')

	if message.content.startswith('빼미에몽'):
		dosome = '왜 ㅖ? ???'
		dosomechoice = dosome.split(' ')
		dosomenumber = random.randint(1, len(dosomechoice)-1)
		dosomeresult = dosomechoice[dosomenumber-1]
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
		if not sheet['A'+str(2)].value == 0:
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


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
