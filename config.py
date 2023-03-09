import os

api_id = int(os.environ.get("API_ID", "2857053"))
api_hash = os.environ.get("API_HASH", "4a01e3596661ba4bf609d15c1f9e129b")
bot_token = os.environ.get("BOT_TOKEN", "6057365695:AAHxOnS7bNXMIv-eoQEJWf7gn16KCaX72H0")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://muhamadfaiz:muhamadfaiz@cluster0.mpwspud.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "telegram") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001439465967"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001818815940")) #untuk group comentar user
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001515293309"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "2100705176"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
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

hastag = os.environ.get("HASTAG", "#ctnboy #ctngirl #ctnrandom #ctnmutualan #ctnask #ctncurhat").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/1f10b19be7da49dd8e08f.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/1f10b19be7da49dd8e08f.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Halo {mention} Kamu harus bergabung di CHANNEL/GROUP Terlebih dahulu untuk mengirim pesan ke @siaranctn.")
start_msg = os.environ.get("START_MSG", "Halo {mention} 🐻‍❄️\n\n<b>CTN MENFESS BOT</b> adalah Bot Auto Post, Semua Pesan Yang Kamu Kirim Akan Masuk Ke Channel @SIARANCTN. Silahkan Baca Help & Rules Terlebih Dahulu.")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Pesan Mu Gagal Terkirim Silahkan Gunakan Hashtag Berikut:

#ctnboy (Untuk Identitas Laki-Laki)
#ctngirl (Untuk Identitas perempuan)
#ctnrandom (Untuk hal random)
#ctnmutualan (Untuk mutualan)
#ctnask (Untuk membagikan hal bodoh)
#ctncurhat (Untuk curhat masalah)
""")
