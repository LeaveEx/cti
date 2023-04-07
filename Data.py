from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Silahkan kirim pesan anda menggunakan hastag dibawah ini:
#ksboy (Untuk Identitas Laki-Laki)
#ksgirl (Untuk Identitas perempuan)
#ksrandom (Untuk hal random)
#ksmutualan (Untuk mutualan)
#ksask (Untuk membagikan hal bodoh)
#kscurhat (Untuk curhat masalah)
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("rules", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
RULES :
1. DILARANG SARA / RUSUH / SPAM
2. DILARANG MENGEMIS DANA DLL
3. DILARANG PROMOSI LINK GROUP / LPM / BOT LAIN
4. DILARANG FAKE PROMOTE MENGGUNAKAN USERNAME ORANG LAIN
5. DILARANG SHARE NO WHATSAPP
6. DILARANG OPEN VCS / JUAL KONTEN SELAIN TALENT RESMI KAMISATO
7, DILARANG JUAL DIRI
— MELANGGAR = AUTO BANNED —
INFO UNTUK MEMBER
Semua pesan akan terkirim ke grup dan ke channel @menfessks jika ada yang melanggar rules atau menyebarkan suatu privasi orang bisa kalian laporkan ke admin atau ke owner @istmeleave
"""
