from pyrogram.types import CallbackQuery
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackQueryHandler, Dispatcher

from ERA import BOT_NAME, OWNER_ID, SUPPORT_CHAT
from ERA import Durgesh as pbot
from ERA import dispatcher

@pbot.on_callback_query()
async def close(client, cb: CallbackQuery):
    if cb.data == "close2":
        await cb.answer()
        await cb.message.delete()


# CALLBACKS

def Durgesh_about_callback(update, context):
    query = update.callback_query
    if query.data == "Durgesh_":
        query.message.edit_caption(
            caption=f"๏ ɪ'ᴍ {BOT_NAME}, ᴀ ᴘᴏᴡᴇʀғᴜʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ʙᴜɪʟᴛ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴇᴀsɪʟʏ."
                    "\n๏  I scan ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs."
                    "\n๏  I ᴄᴀɴ ɢʀᴇᴇᴛ ᴜsᴇʀs ᴡɪᴛʜ ᴄᴜsᴛᴏᴍɪsᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs ᴀɴᴅ ᴇᴠᴇɴ sᴇᴛ ᴀ ɢʀᴏᴜᴘ's ʀᴜʟᴇs."
                    "\n๏  I ʜᴀᴠᴇ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴛɪ-ғʟᴏᴏᴅ sʏsᴛᴇᴍ."
                    "\n๏  I ᴄᴀɴ ᴡᴀʀɴ ᴜsᴇʀs ᴜɴᴛɪʟ ᴛʜᴇʏ ʀᴇᴀᴄʜ ᴍᴀx ᴡᴀʀɴs, ᴡɪᴛʜ ᴇᴀᴄʜ ᴘʀᴇᴅᴇғɪɴᴇᴅ ᴀᴄᴛɪᴏɴs sᴜᴄʜ ᴀs ʙᴀɴ, ᴍᴜᴛᴇ, ᴋɪᴄᴋ, ᴇᴛᴄ."
                    "\n๏  I ʜᴀᴠᴇ ᴀ ɴᴏᴛᴇ-ᴋᴇᴇᴘɪɴɢ sʏsᴛᴇᴍ, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴇᴠᴇɴ ᴘʀᴇᴅᴇᴛᴇʀᴍɪɴᴇᴅ ʀᴇᴘʟɪᴇs ᴏɴ ᴄᴇʀᴛᴀɪɴ ᴋᴇʏᴡᴏʀᴅs."
                    "\n๏  I ᴄʜᴇᴄᴋ ғᴏʀ ᴀᴅᴍɪɴs ᴘᴇʀᴍɪssɪᴏɴs ʙᴇғᴏʀᴇ ᴇxᴇᴄᴜᴛɪɴɢ ᴀɴʏ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴍᴏʀᴇ sᴛᴜғғ."
                    "\n\nᴇʀᴀ ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ GNU ɢᴇɴᴇʀᴀʟ ᴘᴜʙʟɪᴄ ʟɪᴄᴇɴsᴇ v3.0."
                    "\n\n*ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ʙᴀsɪᴄ ʜᴇʟᴘ ғᴏʀ ᴇʀᴀʀᴏʙᴏᴛ*.",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ɴᴏᴛᴇs", callback_data="Durgesh_notes"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ", callback_data="ERA_D_SUPPORT"
                        ),
                        InlineKeyboardButton(
                            text="sᴏᴜʀᴄᴇ",
                            callback_data="source_",
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ɢᴏ ʙᴀᴄᴋ", callback_data="start_back"
                        ),
                    ],
                ]
            ),
        )

    elif query.data == "Durgesh_notes":
        query.message.edit_caption(
            caption=f"<b>๏ sᴇᴛᴛɪɴɢ ᴜᴘ ɴᴏᴛᴇs</b>"
                    f"\n\n➻ʏᴏᴜ ᴄᴀɴ sᴀᴠᴇ ᴍᴇssᴀɢᴇ/ᴍᴇᴅɪᴀ/ᴀᴜᴅɪᴏ ᴏʀ ᴀɴʏᴛʜɪɴɢ ᴀs ɴᴏᴛᴇs"
                    f"\n➻ᴛᴏ ɢᴇᴛ ᴀ ɴᴏᴛᴇ sɪᴍᴘʟʏ ᴜsᴇ # ᴀᴛ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ ᴏғ ᴀ ᴡᴏʀᴅ"
                    f"\n➻nʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ sᴇᴛ ʙᴜᴛᴛᴏɴs ғᴏʀ ɴᴏᴛᴇs ᴀɴᴅ ғɪʟᴛᴇʀs ʀᴇғᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ɢᴏ ʙᴀᴄᴋ", callback_data="Durgesh_")]]
            ),
        )
    elif query.data == "ERA_D_SUPPORT":
        query.message.edit_caption(
            caption=f"*๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ʜᴇʟᴩ ᴀɴᴅ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ*"
                    "\n\n➲ ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ʙᴜɢ ɪɴ [ᴇʀᴀʀᴏʙᴏᴛ](https://t.me/Era_Roxbot) ᴏʀ ɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ɢɪᴠᴇ ғᴇᴇᴅʙᴀᴄᴋ ᴀʙᴏᴜᴛ ᴛʜᴇ [ᴇʀᴀʀᴏʙᴏᴛ](https://t.me/Era_Roxbot), ᴩʟᴇᴀsᴇ ʀᴇᴩᴏʀᴛ ɪᴛ ᴀᴛ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ.",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ", url=f"t.me/{SUPPORT_CHAT}"
                        ),
                        InlineKeyboardButton(
                            text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Durgesh_V_SUPPORT"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="ᴅᴇᴠᴇʟᴏᴩᴇʀ", url=f"tg://user?id={OWNER_ID}"
                        ),
                        InlineKeyboardButton(
                            text="ɢɪᴛʜᴜʙ", url="https://github.com",
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ɢᴏ ʙᴀᴄᴋ", callback_data="Durgesh_"),
                    ],
                ]
            ),
        )


def Source_about_callback(update, context):
    query = update.callback_query
    if query.data == "source_":
        query.message.edit_caption(
            caption=f"""
**ʜᴇʏ,
ᴛʜɪs ɪs {BOT_NAME},
ᴀɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.**

ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ: [ᴛᴇʟᴇᴛʜᴏɴ](https://github.com/LonamiWebs/Telethon)
[ᴩʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram)
[ᴩʏᴛʜᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-ʙᴏᴛ](https://github.com/python-telegram-bot/python-telegram-bot)
ᴀɴᴅ ᴜsɪɴɢ [sǫʟᴀʟᴄʜᴇᴍʏ](https://www.sqlalchemy.org) ᴀɴᴅ [ᴍᴏɴɢᴏ](https://cloud.mongodb.com) ᴀs ᴅᴀᴛᴀʙᴀsᴇs.

*ʜᴇʀᴇ ɪs ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ:* [{BOT_NAME}](https://github.com/IamDuru/ERAROBOT)

{BOT_NAME} ɪs ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ [ᴍɪᴛ ʟɪᴄᴇɴsᴇ](https://github.com/IamDuru/ERAROBOT/blob/master/LICENSE).
© 2022 - 2023 [sᴜᴘᴘᴏʀᴛ](https://t.me/{SUPPORT_CHAT}) ᴄʜᴀᴛ, ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ꜱᴏᴜʀᴄᴇ", url="https://github.com/IamDuru/ERAROBOT"),
                    ],
                    [
                        InlineKeyboardButton(text="ɢᴏ ʙᴀᴄᴋ", callback_data="Durgesh_"),
                    ],
                ]
            ),
        )


about_callback_handler = CallbackQueryHandler(
    Durgesh_about_callback, pattern=r"Durgesh_", run_async=True
)

source_callback_handler = CallbackQueryHandler(
    Source_about_callback, pattern=r"source_", run_async=True
)


dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(source_callback_handler)
