from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Silahkan kirim pesan anda menggunakan hastag dibawah ini:
#ctnboy (Untuk Identitas Laki-Laki)
#ctngirl (Untuk Identitas perempuan)
#ctnrandom (Untuk hal random)
#ctnmutualan (Untuk mutualan)
#ctnask (Untuk membagikan hal bodoh)
#ctncurhat (Untuk curhat masalah)
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
6. DILARANG OPEN VCS / JUAL KONTEN SELAIN TALENT RESMI FWBESS
7, DILARANG JUAL DIRI
— MELANGGAR = AUTO BANNED —
INFO UNTUK MEMBER
Semua pesan akan terkirim ke grup dan ke channel @caritemangobrol jika ada yang melanggar rules atau menyebarkan suati privasi orang bisa kalian laporkan ke admin atau ke owner @istmeleave
"""
