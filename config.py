import os

api_id = int(os.environ.get("API_ID", "3330416"))
api_hash = os.environ.get("API_HASH", "551d747d492ad11a10054fbf672d16e3")
bot_token = os.environ.get("BOT_TOKEN", "6241997964:AAGuP2icL9Th4BYLbNhT5J5TamGG7Ej44Oo")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://muhamadfaiz:muhamadfaiz@cluster0.mpwspud.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "telegram") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001820241577"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001608833465")) #untuk group comentar user
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001812494582"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1680004937"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "2"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#ctnbencong #ctnalay #ksboy #ksgirl #ksrandom #ksmutualan #ksask #kscurhat").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/1f10b19be7da49dd8e08f.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/1f10b19be7da49dd8e08f.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Halo Kamu harus bergabung di CHANNEL/GROUP Terlebih dahulu untuk mengirim pesan ke @menfessks.")
start_msg = os.environ.get("START_MSG", """Halo {mention} ⭐\n\n<b>MENFESS KS BOT</b> adalah Bot Auto Post, Semua Pesan Yang Kamu Kirim Akan Masuk Ke Channel @MENFESSKS. Silahkan kirim pesan anda menggunakan hastag dibawah ini:

#ksboy (Untuk Identitas Laki-Laki)
#ksgirl (Untuk Identitas perempuan)
#ksrandom (Untuk hal random)
#ksmutualan (Untuk mutualan)
#ksask (Untuk membagikan hal bodoh)
#kscurhat (Untuk curhat masalah)
""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Pesan Mu Gagal Terkirim Silahkan Gunakan Hashtag Berikut:

#ksboy (Untuk Identitas Laki-Laki)
#ksgirl (Untuk Identitas perempuan)
#ksrandom (Untuk hal random)
#ksmutualan (Untuk mutualan)
#ksask (Untuk membagikan hal bodoh)
#kscurhat (Untuk curhat masalah)
""")
