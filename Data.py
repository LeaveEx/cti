from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Silahkan kirim pesan anda menggunakan hastag dibawah ini:
#ckfboy (Untuk Identitas Laki-Laki)
#ckfgirl (Untuk Identitas perempuan)
#ckfrandom (Untuk hal random)
#ckfmutualan (Untuk mutualan)
#ckfask (Untuk membagikan hal bodoh)
#ckfcurhat (Untuk curhat masalah)
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
2. DILARANG MENGEMIS
3. DILARANG PROMOSI LINK GROUP / LPM / BOT LAIN
4. DILARANG FAKE PROMOTE MENGGUNAKAN USERNAME ORANG LAIN
5. DILARANG MENYEBARKAN PRIVASU ORANG LAIN
6. DILARANG OPEN VCS / JUAL KONTEN SELAIN TALENT RESMI CARI KENALAN FWB
7, DILARANG SHAMING
— MELANGGAR MAKA AKAN DI BANNED —
INFO UNTUK MEMBER
Semua pesan akan terkirim ke grup dan ke channel @menfessks jika ada yang melanggar rules atau menyebarkan suatu privasi orang bisa kalian laporkan ke admin atau ke owner @istmeleave
"""
