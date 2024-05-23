import requests , telebot, re , os 
from Rooz import Download
from kvsqlite.sync import Client
from telebot import types
from keep_alive import keep_alive

keep_alive()

db = Client('bc.hex')#['db']
#db.create_table()

bot=telebot.TeleBot('6160925735:AAFkOKMKZ1XdYiik1voNMhZTWqftPr1_CcE')
@bot.message_handler(commands=['start'])
def start(message):
	fe = types.InlineKeyboardMarkup(row_width=2)
	dirt = types.InlineKeyboardButton(text='🧑🏻‍💻',url='XuuDD.t.me')
	fe.add(dirt)
	name = message.from_user.first_name
	id = message.from_user.id
	dmj = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
	bot.reply_to(message,f'مرحباً بك عزيزي {dmj} في بوت التحميل من الساوند ، ارسل اسم الاغنية ليتم البحث عنها و التحميل ،',parse_mode='markdown',reply_markup=fe)
	
@bot.message_handler(func=lambda m:True)
def search(m):
	word = m.text
	data = requests.get(f"https://m.soundcloud.com/search?q={word}")
	urls = re.findall(r'data-testid="cell-entity-link" href="([^"]+)', data.text)
	photos = re.findall(r'src="(https://i1.sndcdn.com/[^"]+)" data-testid="actual-image"', data.text)
	names = re.findall(r'<div class="Information_CellTitle__2KitR">([^<]+)', data.text)
	
	
	
	
	db.set('t1',names[0])
	db.set('t2',names[1])
	db.set('t3',names[2])
	db.set('t4',names[3])
	db.set('t5',names[4])
	
	
	link1 =f'https://soundcloud.com{urls[0]}'
	link2 = f'https://soundcloud.com{urls[1]}'
	link3 = f'https://soundcloud.com{urls[2]}'
	link4 = f'https://soundcloud.com{urls[3]}'
	link5 = f'https://soundcloud.com{urls[4]}'
	
	db.set('l1',link1)
	db.set('l2',link2)
	db.set('l3',link3)
	db.set('l4',link4)
	db.set('l5',link5)
	
	b = types.InlineKeyboardMarkup(row_width=2)
	z1 = types.InlineKeyboardButton(text=names[0] , callback_data='zr1')
	z2 = types.InlineKeyboardButton(text=names[1] , callback_data='zr2')
	z3 = types.InlineKeyboardButton(text=names[2] , callback_data='zr3')
	z4 = types.InlineKeyboardButton(text=names[3] , callback_data='zr4')
	z5 = types.InlineKeyboardButton(text=names[4] , callback_data='zr5')
	b.add(z1)
	b.add(z2)
	b.add(z3)
	b.add(z4)
	b.add(z5)
	
	bot.reply_to(m , f'البحث عن ← {word}' , reply_markup=b)
	
	
@bot.callback_query_handler(func=lambda call : True)
def c(call):
	data = call.data
	boss = types.InlineKeyboardMarkup(row_width=2)
	rkkuu = types.InlineKeyboardButton(text='SiRius ♪ ,',url='rKKuu.t.me')
	boss.add(rkkuu)
	if data =='zr1':
		bot.delete_message(call.message.chat.id , call.message.message_id)
		cy1 = db.get('l1')
		print(cy1)
		tg = db.keys()
		print(tg[0])
		d1 = Download(cy1).DownSoundCloud()
		th1 = d1['Thumbnail_link']
		au1 = d1['Audio_link']
		a1 = requests.get(au1).content
		with open('au1.mp3', 'wb') as m1:
				m1.write(a1)
				aa1 = open('au1.mp3','rb')
				bot.send_photo(call.message.chat.id ,caption='تم التحميل :) ', photo=th1)
				nn = db.get('t1')
				bot.send_audio(call.message.chat.id , title=nn, audio=aa1,performer='SiRuS الاقوى :)',reply_markup=boss)
				os.remove('au1.mp3')
	if data =='zr2':
		bot.delete_message(call.message.chat.id , call.message.message_id)
		cy2 = db.get('l2')
		d2 = Download(cy2).DownSoundCloud()
		th2 = d2['Thumbnail_link']
		au2 = d2['Audio_link']
		a2 = requests.get(au2).content
		with open('au2.mp3', 'wb') as m2:
				m2.write(a2)
				aa2 = open('au2.mp3','rb')
				bot.send_photo(call.message.chat.id ,caption='تم التحميل :) ', photo=th2)
				nn2 = db.get('t2')
				bot.send_audio(call.message.chat.id , title=nn2, audio=aa2,performer='SiRuS الاقوى :)',reply_markup=boss)
				os.remove('au2.mp3')
				
	if data =='zr3':
		bot.delete_message(call.message.chat.id , call.message.message_id)
		cy3 = db.get('l3')
		d3 = Download(cy3).DownSoundCloud()
		th3 = d3['Thumbnail_link']
		au3 = d3['Audio_link']
		a3 = requests.get(au3).content
		with open('au3.mp3', 'wb') as m3:
				m3.write(a3)
				aa3 = open('au3.mp3','rb')
				bot.send_photo(call.message.chat.id ,caption='تم التحميل :) ', photo=th3)
				nn3 = db.get('t3')
				bot.send_audio(call.message.chat.id , title=nn3, audio=aa3,performer='SiRuS الاقوى :)',reply_markup=boss)
				os.remove('au3.mp3')

	if data =='zr4':
		bot.delete_message(call.message.chat.id , call.message.message_id)
		cy4 = db.get('l4')
		d4 = Download(cy4).DownSoundCloud()
		th4 = d4['Thumbnail_link']
		au4 = d4['Audio_link']
		a4 = requests.get(au4).content
		with open('au4.mp3', 'wb') as m4:
				m4.write(a4)
				aa4 = open('au4.mp3','rb')
				bot.send_photo(call.message.chat.id ,caption='تم التحميل :) ', photo=th4)
				nn4 = db.get('t4')
				bot.send_audio(call.message.chat.id , title=nn4, audio=aa4,performer='SiRuS الاقوى :)',reply_markup=boss)
				os.remove('au4.mp3')
				
	if data =='zr5':
		bot.delete_message(call.message.chat.id , call.message.message_id)
		cy5 = db.get('l5')
		d5 = Download(cy5).DownSoundCloud()
		th5 = d5['Thumbnail_link']
		au5 = d5['Audio_link']
		a5 = requests.get(au5).content
		with open('au5.mp3', 'wb') as m5:
				m5.write(a5)
				aa5 = open('au5.mp3','rb')
				bot.send_photo(call.message.chat.id ,caption='تم التحميل :) ', photo=th5)
				nn5 = db.get('t5')
				bot.send_audio(call.message.chat.id , title=nn5, audio=aa5,performer='SiRuS الاقوى :)',reply_markup=boss)
				os.remove('au5.mp3')			
		
				
	
bot.infinity_polling()	
