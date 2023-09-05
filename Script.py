class script(object):
    START_TXT = """👋Hello {},
Myself <a href=https://t.me/{}>{}</a>,\n👍Welcome To My Bot And Trust me ! I  Super-fast Movie Request Bot In Add your Database channel And Add My Bot To Add Your Group\nMy Any Bot⏬🕹️\n➤✯🤖File : <a href=https://t.me/M_m_s_filter_bot>🤖File Sharing Bot🤖</a>\n➤✯File To Link: <a href=https://t.me/File_to_slink_bot>File To Link</a>And My Channel⏬\n➤✯Movie And Series: <a href=https://t.me/+l_5oMi-MXmVkOTM9>All Movie And Series</a>\n➤✯Movie Group: <a href=https://t.me/+zXWruLwLfLFjYzVl>Movie Request Group</a>And Juat To Add You Group"""
    LZTHMB_TEXT = """Hello {},
Glad to see you here. It seems that you really love <a href=https://t.me/LazyDeveloperr >LazyDeveloper's</a> work.\n\n<b>Thumbnail extracting</b> feature will be available soon, please join <a href=https://t.me/MarselMovie> Channel</a> and stay tuned for next <a href=https://t.me/MarselUpdate>update</a>.\n\n  🐞 Report Bug here: <a href=http://t.me/MarselUpdate>Marsel Dev Support</a>
    """
    LZLINK_TEXT = """Hey {},
Glad to see you here. It seems that you really love <a href=https://t.me/MarselMovieGroup>Group</a> work.\n\n<b>File to LiNK converting</b> feature will be available soon, please join <a href=https://t.me/MarselMovie>Channel</a> and stay tuned for next <a href=https://t.me/MarselUpdate>update</a>.\n\n  🐞 Report Bug here: <a href=http://t.me/MarselMovie>Support</a>
    """
    DNT_TEXT = """Hey 👋 {},
Thanks for thinking about us.\nIt seems that you really love <a href=https://t.me/+l_5oMi-MXmVkOTM9>Channel</a> work.
    """
    REQ_AUTH_TEXT = """Hello {},
\nJoin Movie And Series Channel Now Join To All Movie And Series \n\n👮‍♀ Bot Error: <a href=https://t.me/MarselUpdate>Marsel</a>\n\n
    """
    ALRDY_UPLDD_TEXT = """✅ Content is already uploaded.\n\nName:{}\nPlease make sure about your spelling before submiting request..."""
    HELP_TXT = """BOT {}
Here is the help for my COMMANDS."""
    ABOUT_TXT = """✯ 🤖BOT: {}
✯ Dev: <a href=https://t.me/MarselDev>Marsel</a>
✯ 📒Library: pyrogram
✯ Language: python 3 
✯ Database: mango db
✯ Bot Server: Free In Render 
✯ Deploy Server: Heruku,Koyab,Render,Vps
✯ Build Status: v1.0.1 [ Beta ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Bot is an open source project in pade. 
- Source code - <a href=https://t.me/MarselDev>Click here</a> 
 Channel - @MarselMovie
<b>DEVS:</b>
- <a href=https://t.me/MarselDev>Marsel</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and bot  will respond whenever that keyword hits the message

<b>NOTE:</b>
1. BOT should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>\nAdd Buttons in click buttons button 👇👇\n🍿Join Channel@MarselMovie.\n🍿 Update And Bot Isu@MarselUpdate"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. BOT supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MarselMovie)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>\nJoin - @MarselMovie\nGroup - @MarselMovieGroup\nIsu Solve Group - MarselUpdate"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Lazy Princess

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★💾Total Files : <code>{}</code>
★ 🙎Total Users: <code>{}</code>
★ 👭Total Chats: <code>{}</code>
★ 🙎️💾Used Storage: <code>{}</code> MIB
★ 📥Free Storage: <code>{}</code> MIB\n 📢 Support @MarselMovieGroup"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    PROGRESS_BAR = """\n
╭━━━━❰ PROGRESS BAR ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """
