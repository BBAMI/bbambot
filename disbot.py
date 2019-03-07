import discord
import asyncio
import random
import openpyxl
import os

client = discord.Client()

@client.event
async def on_ready():
	print('로그인 : '+(client.user.name))
	print('id : '+(client.user.id))
	print('------------------------')
	await client.change_presence(game=discord.Game(name='ㅃ? : 사용법', type=1))
	
@client.event
async def on_message(message):
	if message.author.bot:
		return None
	if message.content == ('ㅃ?'):
		embed = discord.Embed(title="빼미에몽 사용법",
		description='ㅃ? / ㅃ주사위 / ㅃ뭐할까\nㅃ골라줘 A B C ... \nㅃ적어 A B / ㅃ기억 A\n빼미에몽 / 뺌 바보',
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
		dosome = '왜 ㅖ ??'
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
			await client.send_message(message.channel, '싫어')

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


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
