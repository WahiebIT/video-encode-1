from future.backports.email.quoprimime import quote

from bot.helper.worker import *
from pyrogram import Client ,filters





@app.on_message(filters.private&filters.incoming&filters.media)
async def hello(client, message :Message):
    msg= await message.reply_text("Added to queue",quote=True)
    await add_queue([msg,message])


@app.on_message(filters.private&filters.incoming)
async def hello(client, message :Message):
    msg=await message.reply_text("Hi")

@app.on_message(filters.command(['pop']))
async def h(client, message:Message):
    pop()
    await message.reply_text("pop done!")

@app.on_message(filters.command(['empty']))
async def h(client, message:Message):
    empty()
    await message.reply_text("empty done!")


app.run()