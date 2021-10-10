# © @AvishkarPatil [ Telegram ]

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
<b>Hey,</b>{}\n
<b>I am Telly File streamer as well as direct link generator bot</i>\n
<b>Use help 🆘 Command to know how to use me</b>\n
<b><b>Made With 💕 By :</b>@Tellybots_4u</b>"""

HELP_TEXT = """
<b>- Send me Files or media from Telegram.</b>
<b>- I will Provide you External Direct download linᴋ !.</b>
<b>- Add me in your with admin and get direct download link</b>
<b>- This is Permanent link With fastest Support</b>\n
<b>👲 Botz Updates</i> <b>: <a href='https://t.me/tellybots_4u'>[ Click here ]</a></b>"""

ABOUT_TEXT = """
<b>🧒 My Name : TellyFilestreamerbot</b>\n
<b>🤖 Version : <a href='https://telegram.me/tellybots_support'>3.0.1</a></b>\n
<b>🚦 Sᴏᴜʀᴄᴇ : <a href='https://t.me/tellybots_4u'>Click here</a></b>\n
<b>⚗️ Github : <a href='https://t.me/tellybots_digital'>Click here</a></b>\n
<b>👲 Developer : <a href='https://telegram.me/tellybots_4u'>Tellybots_4u</a></b>\n
<b>🎉 Last Updated : <a href='https://telegram.me/tellybots_digital'>[ 20-October-21 ] 04:35 PM</a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🆘 Help', callback_data='help'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('🆘 Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined:** \n\nMy New Freind [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started your bot !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry sir, You are banned to use me. Contact my developer\n\n @Tellybots_4u **They will help you**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>Join my Update Channel to use me 🔐</b>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Join now 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>Something Went Wrong Contact my developer</b> <b><a href='http://t.me/tellybots_4u'>[ Click here ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sorry sir,you are banned to use me. ᴄᴏɴᴛᴀᴄᴛ my developer** @Tellybots_4u",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Please Join my Update Channel to use me**!\n\n**Due to overload only channel Subscriber use me**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("🤖 Join my Update Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Something went wrong. Cᴏntact my developer** [Tellybots_4u](https://t.me/tellybots_support).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text ="""
<b><u>Your Link Generated 👇 !</b>\n
<b>📂 File name :</b> <b>{}</b>\n
<b>📦 File size :</b> <b>{}</b>\n
<b>📥 Download :</b> <b>{}</b>\n
<b>🧒 Made With 💕 :</i> <b>@Tellybots_4u</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Download now 📥", url=stream_link)]])
        )


@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**New user joined **\n\nNew Freind [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started Your Bot !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<b>Sᴏrry sir, Yᴏu are banned to use me. Cᴏntact my developer</b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Plese Join My Update Channel to use me!**\n\nDue to overload, Only Channel Subscriber ᴄan use me!",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🤖 Join my Update Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went wrong. Cᴏntact my Developer [Tellybots_4u](https://t.me/tellybots_support).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )
