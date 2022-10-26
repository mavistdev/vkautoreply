import requests
import urllib
from vkbottle.user import User, Message

user = User("USERTOKEN")

@user.on.message(text="ку")
async def handler(message: Message):
	await message.answer("Ку!")

@user.on.message(text="Ку")
async def handler(message: Message):
	await message.answer("Ку!")

@user.on.message(text="Привет")
async def handler(message: Message):
	await message.answer("Привет!")

@user.on.message(text="привет")
async def handler(message: Message):
	await message.answer("Привет!")

@user.on.message(text="треки")
async def handler(message: Message):
	await message.answer("""
https://vk.com/artist/mavist
https://vk.com/artist/nocopyrightbeats_mty1njk3mjixma
https://vk.com/artist/siniykhagi""")

@user.on.message(text="SPAM IT!")
async def handler(message: Message):
	await message.answer("Воу")
	await message.answer("Спам")
	await message.answer("Спам")
	await message.answer("Спам")


user.run_forever()
