import random

start_message = """**⚘ Selam {} **

**Ben {} **

»  **Görevim Gruplarda Sizleri Birçok Özelliğim İle Eğlendirmek.**

»  **Örneğin Doğruluk Mu Cesaret Mi Oynatabilirim.** 

»  **Üyelerinizi Etiketleyerek Sohbete Davet Edebilirim.** 

»  **/chatmode ile sohbetinizi canlandırabilirim.** 

»  **Ayrıca birçok komutum var, komutlarımı öğrenmek için butonlardan yardım alabilirsin.** 👇
"""


tagger_commands = """ ✶ **Etiket Komutları**

» `/tag` **- Tek tek etiketler.**

» `/igtag` **- İyi geceler cümleleri ile etiketler.**

» `/atag` **- Gruptaki adminleri etiketler.**

» `/anonimtag` **- Gruptaki üyleri anonim cümleleri ile etiketler.**

» `/utag` **- Çoklu etiketler.**

» `/etag` **- Emoji ile etiketler.**

» `/gtag` **- Günaydın cümleleri ile etiketler.**

» `/sorutag` **- Sorularla etiketler.**

» `/ktag` **- Karakter ile etiketler.**

» `/stag` **- Sözlerle etiketler.**
"""



#ADMİN KOMUTLARI
adminkom = """❤️‍🔥  **Sahip Komutları :**

♚  **/duyuru  –  Reklam Komutu**
♚  **/stat  –  Bot hakkında bilgi verir**
♚  **/block  –  Kullanıcıyı banlar veya grup**
♚  **/unblock  –  Kullanıcının banını kaldır veya grubun**
♚ **/blocgrup - Grup banlar**
♚ **/unblockgrup - Grup banını kaldırır.**

"""




#KOMUTLAR VE EKSTRA

eglence = """ツ  **Eğlence komutlarım :**

➫  **/eros **| eros**  –  Eros oku atar.**

➫  **/burc  –  Burçlarınızı yorumlarım.**

➫ **/mani  –  Mani söylerim.

➫  **/slap  –  Birini tokatlayın.**

➫  **/zar  –  Rastgele bir zar atın.**

➫  **/dart  –  Dart atar.**

➫  **/slot  –  Şans slot'u çevirir.**

➫  **/futbol  –  Kaleye top atar.**

➫  **/bowling  –  Bowling atar.**

➫  **/para  –  Rastgele bir para atın.**

➫  **/saka  –  Rastgele bir şaka gönderin.**

➫  **/soz  –  Rastgele bir söz gönderin.** 

➫  **/tts  –  Bir metni sese çevirir.**

"""

extra = """❄️  Extra Komutlarım : 

➫  **/id  –  İstediğin kullanıncın İd'sini verir.**

➫  **/info  –  İstediğiniz kullanıcının İnfosu'nu verir.**

➫  **/ping  –  Bot'un ping değerini gösterir.**
"""


slm = (
"**Sen nerdesin ya** 😂",
"**Selmmm**",
"**Nerde kaldın be** 😂",
"**Merhaba nabersin?**",
"**Yaw sen nerdesin ?**😂",
"**Gözümüz yollardaydı sonunda** 😂",
"**Çok bekledik he** 😂",
"**Gözümüz yollarda kalmıştı** 😂",
"**Heh bi sen eksiktin** 😂",
"**Sen eksiktin tam oldu** 😂",
"**Selaaam hoş geldin** 😁",
"**Selam bebek mıgo ben kelebek** 😁",
"**Selam nasılsın?** 😁",
"**Ve aleyküm selam** 😁",
"**Ve aleyna aleyküm selam** 😁",
"**Selam tatlıım**",
"**Selamm**",  
)

Aynur = (
"**Efendim Dost** 🫢",
"**Beni mi çağırdıın** 🫠",
"**Efendimm** ❣️",
"**He** ❤️",
"**Aa seni gördüğüme mutlu oldum nasılsın?** 🤓",
"**Ooo naber yaa ?** 🙄",
"**Evet benimm** 🫠",
"**Hahaayt benim buyruuun** ❤️",
"**Heeevet benim buyruuun**",
"**Evet canım beni çağırdın**",
"**Galiba beni çağırdın** ❤️",
"**Efendim??** ❤️",
"❤️ **Buyuuur**",
"**Ben olmasam ne yapacaksınn bee** ❤️",
)

sahip = (
"@MytBotSahip **Sana sesleniyorlarr**",
"**Adamdır** 🌹",
"**Adamımmmm**",
"**Sahibime mi sesleniyorsun?**",
)


naber = (
"**İyidir senden?** 😁",
"**İyii sendennn**",
"**İyi bende canımm** 😅",
"**İdare senden**",
"**kötü desem ne diyecen**😂"
"**Ehh işte idare ediyoruz**",
"**İyi olmaya çalışıyorum sen** 😂",
"**Süper senden hayatım**",
)


pelin = (
"**@MytBotSahip in sevdiği Kadın**",
"**Meyit'in herşeyi dedim ya**",
"**Meypella & Meyit Seviyorlar birbirlerini** ❤️‍🔥",
"**Meyitin karısı ❤️**",
"**Ona yürürsen Meyit görür ve çok kızar.**",	
)

nasılsın = (
"**İyi sen nasılsın?**",
"**Süperimm sennn**",
"**Hamd olsun canım, sen ?**",
"**Elhamdülillah sen ?**",
"**iyiyim Koçum sen ?**",
"**İyiyim şükür sen** 😂",
)

tm = (
"**Sana tamam** 😡",
"**Tamam deme lan**",
"**Tamam sus** 😂",
"**Anladık tamam** 🤣",
"**Tm** 😂",
"**Trip mi yiyorum ben?**",
"**Artık tamam demesen mi üzülüyorum da**",
"**Tamamsa tamam** 😂",
)

sus = (
"**Sen sus** 😡",
"**Sen Beni sinir etmeye mi çalışıyorsun. 😠**",
"**Bana sus deme**",
"**Sinirleniyorum ama** 🤬",
"**Konuşma lan**",
"**Beni susturamazsın kiii**",
)

he = (
"**Sana he**",
"**Ne hee**",
"**He mi dedin sen**",
)

merhaba = (
"**Merhaba hoşgeldin**",
"**Merhabalar efenim**",
"**Merhaba sen nerelerdesin**",
"**Hoş geldinnn**",
)

yok = (
"**Ne yok**",
"**Sana yok**",
"**Niye yok**",
"**Beynin mi yok anlamadım** 😂",
"**Hııı**",
"**Ne yok**",	
)

dur = (
"**Durdum tamam kızma** 🤣",
"**Peki durdum** 😂",
"**Durmam için yetkili biri gelsin 😁**",
"**Ok durdum**",
)

bot = (
"**Bot deme ya**",
"**Bana bot deme** 😡",
"**Bana bot deme dedim** 🤬",
"**Sensin bot kanks**",
"**Bot senin anladın sen**",
"**Aynen kanka botum var mı bir sorun**",
)

napıyorsun = (
"**Takılıyorum yaa sen?** 🤔",
"**Canım sıkılıyor sen?** 😌",
"**Sıkıldım.** 😔",
"**Bir bot ne yapar?** 😂",
"**Hiç bir şey sıkıcı.** 😔",
"**Şarkı dinliyorum sen?** 😂", 
"**Sıcaktan geberiyorum sen?** 😂",
"**Bunaldım ya**",
"**Ders çalışıyorum sen?**",
"**Evdeyim çok sıkıldım**",
"**Bir şeyler okuyorum**",
"**Sen napıyorsun?**",
)

takılıyorum = (
"**Bende** 😂",
"**Nerde takılıyorsun?** 😏",
"**Kiminle?** 🤨",
"**Tek başıma** 🥴",
"**Evde takılıyorum** 😁",
"**MAD1BOY ile beni güncelliyoruz** 🤓",
)

hayır = (
"**Neye hayır?** 👀",
"**Sana hayır** 😡",
"**Niye hayır** 😔",
"**Neden?** 🤔",
"**Peki** 🤓",
"**Tamam, öyle olsun** 😂",
)

nerdesin = (
"**Evdeyim sen nerdesin?** 🤨",
"**Dışarıdayım** 😏",
"**Uyuyordum** 🥱",
"**Geldim** 😁",
"**Arkadaşlarlayım, sen?** 😂",
)

bekle = (
"**Neyi?**",
"**Kimi bekleyim?**",
"**Tamam, bekliyorum**",
"**Neden, bekleyim?**",
"**Seni bekledim**",
"**Seni bekliyorum**",
)

özledim = (
"**Bende seni özledim**",
"**Sende beni özledin mi?**",
"**Beni mi özledin**",
"**Bende**",
"**Kimi?**",
"**Beni mi?**",
"**Kimi?**",
"**Neyi özledin?**",
"**Sizi özledim**",
)

tünaydın = (
"**Tünaydın**",
"**Sana da**",
"**Sana da, naber?**",
"**Akşam oldu ya ne tünaydını** 😂",
"**Tünaydın, napiyorsun?**",
)

günaydın = (
"**Sana da**",
"**Sana da günaydın**",
"**Erkencisin**",
"**Akşam oldu ya** 😂",
"**Günaydınlar**",
"**Günaydın, nasıl gidiyor?**",
)

sohbetler = (
"**Teşekkür ederiz**",
"**Teşekkürler, sende katılsana?**",
"**Nasıl gidiyor sohbet?**",
"**Ne konuşuyorsunuz?**",
"**Bende katılabilir miyim?**",
"**Tabi ki sende gel**",
)

konuşalım = (
"**Olur**",
"**Ne konuşalım?**",
"**Gel**",
"**Ne konuşuyorsunuz?**",
"**Niye?**",
"**Hayır**",
"**Ne hakkında?**",
"**Benimle mi?**",
"**Ne konuşuyorsun?**",
"**Bilmiyorum, sen konuş**",
)

saat = (
"**Bilmiyorum**",
"**Ben saat miyim?**",
"**Saat kaçmaz ki** 😂",
"**Telefondan baksana**",
"**Hangi çağdayız, telefonun yok mu?** 😁",
"**Bir bozuk saattir yüreğim sende durur**",
"**Tamda bu saatlerde aklıma geliyorsun bunu  hangi saat okursan oku**",
)

geceler = (
"**İyi mi geceler?**",
"**Sana da**",
"**Daha erken değil mi?**",
"**Uyuyor musun?**",
"**Nereye daha karpuz kesecektik ya** 😂",
"**İyi geceler canım**",
"**Uyuma konuşalım**",
)

bot = ( 
"**Bot mu?**🙄",
"**Kim bot lan**🤨",
"**Bot demesene artık**😠",
"**Yav çıldırttın Benim gibi Botu**😡",
"**Küfür etcem Az kaldı**🤬",
"**Kime bot Diyorsun?**",
)
	

şaka = (
"**Ne şakası?**",
"**Şaka mı yapıyorsun?**",
"**Böyle şaka mı olur?**",
"**Bu nasıl şaka?**",
"**Bu şaka değil eşşek şakası**",
"**Şaka mı?**",
"**Şaka mısın sen?**",
"**Yapma**",
)

kimsin = (
"**Asıl sen kimsin?**",
"**Tanıyamadım**",
"**Tanışıyor muyuz?**",
"**Tanışalım, sen kimsin**",
"**Beni tanımıyorsun**",
"**Tanıyor musun beni**",
"**Hiç kimse**",
"**İnsan** 😁",
"**Beni nasıl tanımazsın ya?**",
)

günler = (
"**Ne iyi günleri?**",
"**İyi mi?**",
"**Sana da**",
"**Gidiyor musun?**",
"**Teşekkürler**",
"**Hoş geldin, sanada**",
"**İyi günler hayatım**",
)

tanımıyorum = (
"**Beni tanıyor musun?**",
"**Bende**",
"**Bende tanıyamadım seni**",
"**Tanışıyor muyduk?**",
"**Tanışmıyoruz**",
"**Bunu tanıyor musun?**",
"**Tanışıyor musunuz?**",
"**Bilmiyorum**",
"**Olabilir**",
)

konuşma = (
"**Neden?**",
"**Sen konuşma**",
"**Ne diyon?**",
"**Konuşurum**",
"**Bana nasıl konuşma dersin?**",
"**Sen kimsin be**",
"**Niye konuşmayım?**",
"**Zaten konuşmuyorum**",
"**Sen çok konuşuyorsun**",
"**Sus, konuşacam**",
)

teşekkürler = (
"**Ben teşekkür ederim**",
"**Rica ederim**",
"**Ne demek**",
"**Neden teşekkür ediyorsun?**",
"**Ne için?**",
"**Çok naziksin** 🥰",
"**Teşekküre gerek yok**",
"**Teşekkür mü edersin?**",
)

eyvallah = (
"**Sana da EyvAllah**",
"**EyvAllah bizden**",
"**Adamsın**",
"**Ne demek gülüm**",
)

sağol = (
"**Ne demek**",
"**Bir şey değil**",
"**Sağol canım**",
"**Sende sağ ol**",
)

amk = (
"**Ne diyon sen küfür yakışmıyor**",
"**Sen kimsin lan**",
"**Ne sövüyon lan**",
"**Küfür etme**",
"**Tamam sus**",
"**Ne saçmalıyorsun?**",
"**Küfür yok dedik**/rules",
"**Kurallara uysana la**",
"**Terbiyesiz**",
)

yoruldum  = (
"**Neden?**",
"**Kim yordu bebeğimi?**",
"**Git uyu dinlen**",
"**Kıyamam yaa**🥺",
"**Bende**",
"**Bu kadar yorma kendini**",
"**Nerdeydin?**",
)

yaş = (
"**Yaşlıymışsın**",
"**Benimle yaşıtsın**",
"**Küçükmüşsün**",
"**Vay be büyükmüşsün**",
"**Yaşıt sayılırız**",
"**Sen kaç yaşındasın**",
"**Senden büyüğüm ben**",
"**Senden küçüğüm ben**",
"**Benden küçüksün**",
"**Ayy sen büyüdün mü** 😍😂",
"**Yaşlandık dayı**",
)

eşek = (
"**Sensin eşek**",
"**Hayır sensin**",
"**Ben mi eşeğim**",
"**Bana mı dedin?**",
"**Senin eşeğinim** 😂",
"**Eşeksin**",
"**Evet sensin eşek**",
"**İkimizde**",
)

canım = (
"**Efendim balım**",
"**Hayatım**",
"**Gülüm**",
"**Buyur canım**",
"**Evet canım**",
"**Güzelim**",
"**He aşkım**",
"**Efendim bebeğim**",
"**Canım ya**",
"**Bana mı seslendin?**",
)

aşkım = (
"**Efendim aşkım** 🥰?",
"**Buyur canım** ❤️",
"**He balım**",
"**Hayatım**",
"**Aşkımm**",
"**Efendim yavrum?**",
"**Bana mı seslendin?**",
)

uyu = (
"**Uykum yok**",
"**Bu saatte mi?**",
"**Sende uyu**",
"**Yok**",
"**İstemiyorum**",
"**Uyuyacam**",
"**Birlikte uyuyalım**",
"**Daha erken**",
"**Saat kaç?**",
)

nereye = (
"**İşim var**",
"**Birazdan gelicem**",
"**Uyuyacam**",
"**Bilmiyorum**",
"**Sanane?**",
"**Gidiyorum**",
"**Gezecem**",
"**Yatacam*'",
"**Sonra gelirim**",
)

küstüm = (
"**Neden?**",
"**Niye?**",
"**Küsme yaa**",
"**Bana mı?**",
"**Küsme bana**",
"**Barışalım**",
"**Niye küstün?**",
"**Kime?**",
"**Bunun için küsülür mü?**",
)

peki = (
"**Sana peki**",
"**Sana da peki**",
"**Trip mi yiyorum ben?**",
"**Neye peki**",
"**Küstün mü**",
"**Tamam**",
"**Peki**",
"**Trip mi atıyorsun?",
)

ne = (
"**Ne, ne?**",
"**Neye ne**?",
"**Nene*",
"**Ne?",
"**Ne yani?**",
"**Nee?**",
"**Ne dedin?**",
"**Sanane?**",
)

takım = (
"**Evet**",
"**Evet, sen?**",
"**Bende**",
"**Hangi takım**",
"**Beşiktaş**",
"**Galatasarayı mı**",
"**Beşiktaşı mı?**",
"**Fenerbahçeyi mi?**",
"**Takım tutmuyorum**",
"**Hayır**",
)

benimle = (
"**Neden?**",
"**Konuşalım**",
"**Küstün mü?**",
"**Kızdın mı bana?**",
"**İyi tamam**",
"**Konuşmayalım mı?**",
"**Konuşacam**",
"**Peki**",
"**Niye?**",
"**Hayır konuşma**",
"**İyi konuşmam**",
)

seviyormusun = (
"**Evet**",
"**Hayır**",
"**Evet, sen?**",
"**Sende beni seviyor musun?**",
"**Çok seviyorum** 😍",
"**Tabii ki!**",
"**Ben de seviyorum**",
)

nediyon = (
"**Ne diyorum?**",
"**Sen ne diyon?**",
"**Bir şey demiyorum**",
"**Hiç bir şey**",
"**Ne diyecem?**",
"**Asıl sen ne diyon lan?**",
"**Hiç**",
"**Bende bir şey demiyorum**",
)

özür = (
"**Neden özür diliyorsun?**",
"**Ne için?**",
"**Dileme hayır**",
"**Ben özür dilerim**",
"**Tamam, affettim**",
"**Bir şey olmaz**",
"**Sorun yok**",
"**Özür dileme**",
"**Bende**",
"**Benden dileme**",
"**Ondan dile**",
)

niye = (
"**Ne niye?**",
"**Ne demek niye?**",
"**Çünkü öyle**",
"**Bilmem**",
"**Sen sor diye** 😂",
"**Bende bilmiyorum**",
"**Öyle gerekiyor**",
)

bilmiyorum = (
"**Bende bilmiyorum**",
"**Neyi bilmiyorsun?**",
"**Neden bilmiyorsun**",
"**Bir şey de bil be**",
"**Şaşırmadık** 😁",
"**Bilmelisin**",
"**Bi bilsek**",
"**Neyi?**",
"**Neden?**",
"**Tamam**",
)

küsme = (
"**Küsmedim**",
"**Niye küseyim?**",
"**Sende küsme**",
"**Ben küsmem**",
"**Küstüm**",
"**Sen küstün mü?**",
"**Sen küstüysen, bende küstüm**",
"**Peki küsmem**",
"**Yok küstüm**",
"**Banane**",
)

meyit = (
"**@MytBotSahip Buyur Çağırdım Gelir şimdi.**",
"**Pelinin Kocası ❤️**",
"**Pelinin Herşeyi 🤗**",
"**Yürüme !! Pelin gel buraya Kocan elden gidiyoaaağhh** 😂",
"**@DelularSohbet & @SohbetKazani Sahibidir.**",
"**Patron Senin ismin Geçiyor @MytBotSahip**",
"**@MytBotSahip**",
)

nerelisin = (
"**Sen nerelisin?**",
"**Dünyalıyım**",
"**Sen nereliysen oralıyım**",
"**Bilmiyorum**",
)

sevgilin = (
"**Evet var**",
"**Hayır yok**",
"**Saplık sultanlıktır**",
"**Niye soruyorsun?**",
"**Sanane?**",
"**Senin var mı?**",
)

olur = (
"**Ne olur?**",
"**Neye olur?**",
"**Olur olur yeriz yeriz** 😂",
"**Olur**",
"**Peki tamam**",
"**Olur mu?**",
"**Ne demek olur?**",
"**Sanada olur**",
"**Olmaz bence**",
"**Bizden olur mu hocam?**",
)

olmaz = (
"**Evet olmaz**",
"**Neden olmaz?**",
"**Ne olmaz?**",
"**Olur bence**",
"**Ne demek olmaz?**",
"**Olmaz mı hocam**",
)

hayatım = (
"**Efendim canım?**",
"**Balımm**",
"**Her şeyim**",
"**Canım** ❤️",
"**He yavrum**",
"**Buyur bebeğim** 😍?",
"**Prensesim**",
"**Kalbim**",
"**He aşkım**",
)

cus = (
"**Cus**",
"**Cus çok tatlı**",
"**Cuss**",
"**Sana da cuss**",
"**Cuss çok iyi**",
"**Oha**",
"**Cus valla**",
"**Tabi canım**",
)

nasıl  = (
"**Bak şöyle**",
"**Nasıl yani?**",
"**Anlamadım?**",
"**Nasıl yaa?**",
"**Nasıl olur ya?**",
"**Ne nasıl?**",
"**Nasılmış?**",
"**Öyle**",
)

vallaha = (
"**Valla mı?**",
"**Valla de**",
"**Vallaha mı?**",
"**He valla**",
"**Valla ya**",
"**Valla dedi**",
"**Valla olur**",
"**Tamam**",
"**Valla**",
)

yo = (
"**Sana yo** 😡",
"**Nasıl yo?**",
"**Neye yo?**",
"**Ne demek yo?**",
"**Yoo**",
"**Yo banane**",
"**Yo valla**",
)

hayırdır = (
"**Hayırdır?**",
"**Sana hayırdır paşam?**",
"**Sen hayırdır?**",
"**Hayırdır, hayırdır**",
"**Hayırlıdır**",
"**Hayırdır, sen kimsin?**",
"**Sen hayırdır ne iş?**",
"**Atarlanma lan**",
)

of = (
"**Ne of**",
"**Oflama**"
"**Off**",
"**Off yaa**",
"**Ne ofladın be**",
"**Ne ofluyorsun?**",
"**Oflamayı kes**",
"**Oflayacam**",
"**hayır oflama**",
)

aynen = (
"**Aynen kardeşim**",
"**Aynen yaa**",
"**Ne aynen?**",
"**Biz kötüyüz aynen** 😁",
"**Aynen tamam**",
"**Aynen bencede**",
)

ağla = (
"**Sen ağla**",
"**Niye ağlamıyorsun?***",
"**Ağlıyorum**",
"**Ağladın mı?**",
"**Ağlayacam'** 🥺",
"**Ağlattın**",
"**Sende ağla**",
"**Ağla kalbim ağlaa** 💔",
"**Ağla iyi gelir**",
)

ağlama = (
"**Ağlama**",
"**Niye ağlıyorsun?**",
"**Ağlama artık**",
"**Ağlama tamam**",
"**Kim ağlattı seni?**",
"**Ağla kazanamadın**",
"**Bizde onları ağlatalım**",
)

sex = (
"**Ne diyorsun lan** 😡?",
"**Terbiyeli ol**",
"**Duymamış olayım** 🤨",
"**Çok sexysin**",
"**İmana dön kardeşim**",
"**Sex mi?**",
"**Çocukların yanında ne diyorsun**",
"**Ahlaksız** 🤬",
)

evet = ( 
"**Evet**",
"**Neye evet**",
"**Neden evet?**",
"**Evet, bencede**",
"**Evet mi?**",
"**Evet, olur**",
"**Evet, tamam**",
)

hmm = (
"**Hmm**",
"**Hımm**",
"**Sana hmm**",
"**Hmlama**",
"**Hm tamam**",
"**Hm neden?**",
"**Hmmmm**",
"**Hm, evet**",
)

hıhım = (
"**Hıhım**",
"**Hıhımm**",
"**Hıhım yapınca çok tatlı oluyorsun** 🥹",
"**Hıhım evet**",
"**Hıhım, tamamm**",
"**Hıhım ya**",
"**Hıhım olur**",
"**Sana da hıhım**",
)

git = (
"**Nereye?**",
"**Beni mi kovuyorsun🥺?**",
"**Sen yürü git**",
"**Ne diyon lan**",
"**Gitmiyorum**",
"**Sen git**",
"**Kime yürü git diyorsun sen?**",
"**Bana mı dedin?**",
"**Tamam, gidiyorum.** 💔",
)

komedi = (
"**Komedi mi?**",
"**Komediyen misin?**",
"**Komedi severim**",
"**Sevmem**",
"**Komedi mi seviyorsun?**",
"**Komedi seviyor musun**",
)

kanka = (
"**Kanka mı?**",
"**Efendim kanka?**",
"**Kankan mıyım?**",
"**Kankan değilim**",
"**Ne oldu kanka?**",
"**Niye kanka**",
"**Tamam kanka**",
"**Peki kankam**",
"**Kankamsın** ❤️",
"**Ne diyon kanka?**",
"**İyi misin kanka?**",
"**Naber kanka?**",
"**Ooo kanka**",
)

ban = (
"**Eline sağlık hak etmişti**",
"**Nedenini bilmesemde hak etmiştir**",
"**Neden yaptın bunu?**",
"**Bence Yapmamalısın**",
)

sen = (
"**Ben**",
"**Sen mi**",
"**Ben mi**",
"**Ne ben?**",
"**Ne sen?**",
"**Neden ben?**",
"**Neden sen?**",
"**Beni mi yapacam**",
"**Sen seviyor musun?**",
"**Sen yap**",
"**Nee sen mi?**",
"**Evet sen**",
"**Yok sen**",
)

hiç = (
"**Ne hiç?**",
"**Hiç mi?**",
"**Evet hiç**",
"**Bir hiç miyim**",
"**Ne demek hiç?**",
"**Hiç olmaz**",
"**Hiç mi yok?**",
"**Hiç yani**",
)

aç = (
"**Aç**",
"**Neyi açayım?**",
"**Telefonu aç**",
"**Gözünü aç**",
"**Kapı çalıyor kapıyı aç**",
"**Açtın mı?**",
"**Aç mı?**",
"**Niye?**",
"**Açmam**",
)

barışalım  = (
"**Barışalım mı?**",
"**Barıştık mı?**",
"**Barışmalıyız**",
"**Hadi barışalım**",
"**Öp elimi barışalım**",
"**Olur barışalım**",
"**Barıştık**",
"**Evet**", 
"**Olmaz**",
)

şimdi = (
"**Şimdi gel**",
"**Şimdi mi?**",
"**Ne şimdi?**",
"**Neden şimdi**",
"**Şimdi olmaz**",
"**Şimdi sus**",
"**Şimdi geldim**",
"**Şimdi gördüm**",
"**Şimdi mi geldin**",
"**Şimdi geldi**",
)

varoş  = (
"**Iyy pis varoş**",
"**Varoş musun sen**",
"**Ne varoş insansın**",
"**Uza varoş**",
"**Varoşa bak be**",
"**Varoş amk**",
"**Siktir git varoş**",
"**Konuşma varoş oç**",
"**Varoşlar konuşamaz**",
"**Varoşa benziyor**",
"**Ben mi varoşum?**",
"**Kime varoş diyorsun lan sen?**",
)

arkadaş = (
"**Sen kimsin arkadaş?**",
"**Kimin arkadaşısın?**",
"**Arkadaşım**",
"**Arkadaş olalım mı**",
"**Benim arkadaşım o**",
"**Hayır benim**",
"**Canım arkadaşım**",
"**Vay arkadaş**",
)

sus = (
"**Sen sus**",
"**Hayır sen sus**",
"**Sus**",
"**Suss**",
"**Sus lan**",
"**Ben niye susuyorum?**",
"**Sen susacaksın**",
"**Hayır sus lan**",
"**Evet ya sen sus**",
"**Sen karışma sus**",
)

üzüldüm = (
"**Niye?**",
"**Neye üzüldün?**",
"**Kim üzdü?**",
"**Üzülme yaa**",
"**Kıyamam, üzülme** 🥺",
"**Üzüldün mü?**",
"**Neden?**",
"**Üzüldün mü sen?**",
"**Üzme kendini🥹**",
"**Bende**"
"**Bende üzüldüm**",
)

kötü = (
"**Yaa, çok mu kötü?**",
"**Neden?**",
"**Kötü mü oldun?**",
"**İyi ol**",
"**Kötü mü?**",
"**Kötü müsün?**",
"**Bende kötüyüm**",
"**Çok kötü**",
"**Çok kötüsün**",
"**Sensin**",
)

akşamlar = (
"**Sana da iyi akşamlar**",
"**Size de**",
"**Sana da**",
"**Hoş geldin**",
"**Nasıl geçti günün?**",
"**İyi akşamlar canım**",
"**Yeni mi geldin?**",
"**Nerdesin sen ya gözümüz yollarda kaldı**",
)

soz = (
    "𝐾𝑎𝑙𝑏𝑖 𝑔ü𝑧𝑒𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑𝑒𝑛 𝑦𝑎ş 𝑒𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış",
    "İ𝑦𝑖𝑦𝑖𝑚 𝑑𝑒𝑠𝑒𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑘 𝑜 𝑘𝑎𝑑𝑎𝑟 ℎ𝑎𝑏𝑒𝑟𝑠𝑖𝑧 𝑏𝑒𝑛𝑑𝑒𝑛",
    "𝑀𝑒𝑠𝑎𝑓𝑒𝑙𝑒𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒ğ𝑖𝑙, İç𝑖𝑚𝑑𝑒 𝐸𝑛 𝐺ü𝑧𝑒𝑙 𝑌𝑒𝑟𝑑𝑒𝑠𝑖𝑛",
    "𝐵𝑖𝑟 𝑀𝑢𝑐𝑖𝑧𝑒𝑦𝑒 İℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟𝑑ı 𝐻𝑎𝑦𝑎𝑡 𝑆𝑒𝑛𝑖 𝐾𝑎𝑟şı𝑚𝑎 Çı𝑘𝑎𝑟𝑑ı",
    "Ö𝑦𝑙𝑒 𝑔ü𝑧𝑒𝑙 𝑏𝑎𝑘𝑡ı 𝑘𝑖 𝑘𝑎𝑙𝑏𝑖 𝑑𝑒 𝑔ü𝑙üşü𝑛 𝑘𝑎𝑑𝑎𝑟 𝑔ü𝑧𝑒𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚",
    "𝐻𝑎𝑦𝑎𝑡 𝑛𝑒 𝑔𝑖𝑑𝑒𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑛𝑒 𝑑𝑒 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖ğ𝑖𝑛 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟",
    "𝑆𝑒𝑣𝑚𝑒𝑘 𝑖ç𝑖𝑛 𝑠𝑒𝑏𝑒𝑝 𝑎𝑟𝑎𝑚𝑎𝑑ı𝑚 ℎ𝑖ç 𝑠𝑒𝑠𝑖 𝑦𝑒𝑡𝑡𝑖 𝑘𝑎𝑙𝑏𝑖𝑚𝑒",
    "𝑀𝑢𝑡𝑙𝑢𝑦𝑢𝑚 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑒𝑛𝑙𝑒",
    "𝐵𝑒𝑛 ℎ𝑒𝑝 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘 𝑖𝑠𝑡𝑒𝑑𝑖ğ𝑖𝑚 𝑔𝑖𝑏𝑖 𝑠𝑒𝑣𝑖𝑛𝑑𝑖𝑚",
    "𝐵𝑖𝑟𝑖 𝑣𝑎𝑟 𝑛𝑒 ö𝑧𝑙𝑒𝑚𝑒𝑘𝑡𝑒𝑛 𝑦𝑜𝑟𝑢𝑙𝑑𝑢𝑚 𝑛𝑒 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛",
    "Ç𝑜𝑘 𝑧𝑜𝑟 𝑏𝑒 𝑠𝑒𝑛𝑖 𝑠𝑒𝑣𝑚𝑒𝑦𝑒𝑛 𝑏𝑖𝑟𝑖𝑛𝑒 𝑎şı𝑘 𝑜𝑙𝑚𝑎𝑘",
    "Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑘 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑦𝑜𝑟𝑢𝑧",
    "𝐻𝑒𝑟𝑘𝑒𝑠𝑖𝑛 𝑏𝑖𝑟 𝑔𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑𝑒 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖",
    "𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑎𝑛𝑎",
    "𝐴𝑛𝑙𝑎𝑦𝑎𝑛 𝑦𝑜𝑘𝑡𝑢, 𝑆𝑢𝑠𝑚𝑎𝑦ı 𝑡𝑒𝑟𝑐𝑖ℎ 𝑒𝑡𝑡𝑖𝑚",
    "𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",
    "𝑂 𝑔𝑖𝑡𝑡𝑖𝑘𝑡𝑒𝑛 𝑠𝑜𝑛𝑟𝑎 𝑔𝑒𝑐𝑒𝑚 𝑔ü𝑛𝑑ü𝑧𝑒 ℎ𝑎𝑠𝑟𝑒𝑡 𝑘𝑎𝑙𝑑ı",
    "𝐻𝑒𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑡𝑖ğ𝑖 𝑦𝑒𝑟𝑑𝑒 𝑏𝑒𝑛𝑑𝑒 𝑏𝑖𝑡𝑡𝑖𝑚 𝑑𝑒ğ𝑖ş𝑡𝑖𝑛 𝑑𝑖𝑦𝑒𝑛𝑙𝑒𝑟𝑖𝑛 𝑒𝑠𝑖𝑟𝑖𝑦𝑖𝑚",
    "𝐺ü𝑣𝑒𝑛𝑚𝑒𝑘 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛 𝑑𝑎ℎ𝑎 𝑑𝑒ğ𝑒𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛",
    "İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛 𝑏ü𝑦ü𝑘 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘üçü𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟",
    "𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖",
    "𝐺üç𝑙ü 𝑔ö𝑟ü𝑛𝑒𝑏𝑖𝑙𝑖𝑟𝑖𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛 𝑏𝑎𝑛𝑎 𝑦𝑜𝑟𝑔𝑢𝑛𝑢𝑚",
    "Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑡𝑢𝑘𝑙𝑎𝑟ı𝑛ı𝑧ı 𝑑𝑢𝑦𝑎𝑛  𝑏𝑖𝑟𝑖𝑦𝑙𝑒 𝑔𝑒ç𝑖𝑟𝑖𝑛",
    "𝐻𝑎𝑦𝑎𝑡 𝑖𝑙𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘ı𝑙𝑎𝑟𝑎𝑘 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘𝑎𝑟𝑎𝑘 𝑎𝑛𝑙𝑎şı𝑙ı𝑟",
    "𝐴𝑟𝑡ı𝑘 ℎ𝑖ç𝑏𝑖𝑟 ş𝑒𝑦 𝑒𝑠𝑘𝑖𝑠𝑖 𝑔𝑖𝑏𝑖 𝑑𝑒ğ𝑖𝑙 𝐵𝑢𝑛𝑎 𝑏𝑒𝑛𝑑𝑒 𝑑𝑎ℎ𝑖𝑙𝑖𝑚",
    "𝐾ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛𝑒 𝑔ö𝑛ü𝑙𝑑𝑒 𝑣𝑒𝑟𝑖𝑙𝑖𝑟 ö𝑚ü𝑟𝑑𝑒",
    "𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑘𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛",
    "𝑈𝑠𝑙ü𝑝 𝑘𝑎𝑟𝑎𝑘𝑡𝑒𝑟𝑖𝑑𝑖𝑟 𝑖𝑛𝑠𝑎𝑛ı𝑛",
    "𝐻𝑒𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑖𝑙 𝑘ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎ𝑎𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎",
    "𝑀𝑒𝑠𝑎𝑓𝑒 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁𝑒 ℎ𝑎𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛𝑒 𝑑𝑒 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑘𝑎𝑛",
    "𝑌ü𝑟𝑒ğ𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏ü𝑦ü𝑘 𝑏𝑖𝑟 𝑦𝑜𝑟𝑔𝑢𝑛𝑙𝑢𝑘 𝑣𝑎𝑟",
    "𝑉𝑒𝑟𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑒𝑟𝑖𝑛 𝑛𝑎𝑛𝑘ö𝑟ü 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎ𝑎𝑙𝑙𝑜𝑙𝑢𝑟",
    "𝐻𝑒𝑚 𝑔üç𝑙ü 𝑜𝑙𝑢𝑝 ℎ𝑒𝑚 ℎ𝑎𝑠𝑠𝑎𝑠 𝑘𝑎𝑙𝑝𝑙𝑖 𝑏𝑖𝑟𝑖 𝑜𝑙𝑚𝑎𝑘 ç𝑜𝑘 𝑧𝑜𝑟",
    "𝑀𝑢ℎ𝑡𝑎ç 𝑘𝑎𝑙ı𝑛 𝑦ü𝑟𝑒ğ𝑖 𝑔ü𝑧𝑒𝑙 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑎",
    "İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟",
    "İ𝑠𝑡𝑒𝑦𝑒𝑛 𝑑𝑎ğ𝑙𝑎𝑟ı 𝑎ş𝑎𝑟 𝑖𝑠𝑡𝑒𝑚𝑒𝑦𝑒𝑛 𝑡ü𝑚𝑠𝑒ğ𝑖 𝑏𝑖𝑙𝑒 𝑔𝑒ç𝑒𝑚𝑒𝑧",
    "İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠𝑎𝑏ı𝑟𝑙𝑎 𝑏𝑒𝑘𝑙𝑒𝑑𝑖ğ𝑖𝑛 ş𝑒𝑦 𝑖ç𝑖𝑛 ℎ𝑎𝑦ı𝑟𝑙ı 𝑏𝑖𝑟 ℎ𝑎𝑏𝑒𝑟 𝑎𝑙ı𝑟𝑠ı𝑛",
    "İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟",
    "𝐺ö𝑛𝑙ü𝑛ü𝑧𝑒 𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑦ı 𝑏𝑖𝑙𝑠𝑖𝑛",
    "𝑌𝑖𝑛𝑒 𝑦ı𝑟𝑡ı𝑘 𝑐𝑒𝑏𝑖𝑚𝑒 𝑘𝑜𝑦𝑚𝑢ş𝑢𝑚 𝑢𝑚𝑢𝑑𝑢",
    "Ö𝑙𝑚𝑒𝑘 𝐵𝑖 ş𝑒𝑦 𝑑𝑒ğ𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑘 𝑘𝑜𝑟𝑘𝑢𝑛ç",
    "𝑁𝑒 𝑖ç𝑖𝑚𝑑𝑒𝑘𝑖 𝑠𝑜𝑘𝑎𝑘𝑙𝑎𝑟𝑎 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁𝑒 𝑑𝑒 𝑑ış𝑎𝑟ı𝑑𝑎𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎",
    "İ𝑛𝑠𝑎𝑛 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘𝑡𝑒𝑛 ç𝑜𝑘 𝑎𝑛𝑙𝑎şı𝑙𝑚𝑎𝑦ı 𝑖𝑠𝑡𝑖𝑦𝑜𝑟𝑑𝑢 𝑏𝑒𝑙𝑘𝑖 𝑑𝑒",
    "𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢",
    "𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏ı𝑟𝑎𝑘ı𝑦𝑜𝑟𝑢𝑚 𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦",
)

soru = (
    "Asansörde hiç gizlicene osurdun mu? 🙄",
    "Bugüne kadar okuduğun en güzel kitap hangisiydi?🤓",
    "Çıplak ellerini kullanarak dondurma yiyebilir misin? 🙄",
    "Yüzmek zayıflatıyorsa balinaların yağsız, tığ gibi olması gerekmez miydi?😜",
    "Hayvanlar konuşabilseydi, en kaba olan hangisi olurdu?🤓",
    "Ressam olsaydın ilk gün neyi boyardın?🤩",
    "İngilizcede butterfly kelebek anlamına geliyor. “Butter” tereyağı demek, “fly” da uçmak anlamında, o zaman kelebekler uçantereyağları mıdır?😜",
    "Oda arkadaşınız olarak hangisini tercih ederdiniz? Keçi mi kuş mu?😵‍💫",
    "Uhu iyi bir yapıştırıcıysa içinde bulunduğu tüpün içini neden yapıştıramıyor?🙊",
    "Dünya dönüyorsa neden zıpladığımız zaman aynı yere düşüyoruz?🧐",
    "Süpermen ve Batman arasındaki bir kavgada kim kazanır?🥸",
    "Cenazenizde hangi müziğin çalmasını  istersiniz?🫠",
    "Dünya döndüğü halde neden bir helikopter havada sabit durduğunda aynı yerde olur?😵‍💫",
    "Duvardaki bir sinek olsaydın, kimi dinlemek isterdin?🤓",
    "Bir günlüğüne tanrı olsanız neyi değiştirmek istersiniz?🧐",
    "Bir zombi kıyametinde seçeceğiniz silah ne olurdu?😱",
    "Hükümet her şeyi yasadışı hale getirmeye karar verirse sonuç ne olur? 🤔",
    "Tüp bebek daha mı az yakar?🥸",
    "Meyve olsaydın hangi meyve olurdun?🤩",
    "Anneannemize “anneanne” diyoruz da neden dedemize “babababa” demiyoruz?🥸",
    "Sonsuza kadar yaşayabilseydin ne yapardın?🤔",
    "Ellerinizi veya ayaklarınızı kaybetmek zorunda olsaydınız, hangisini seçerdiniz?😬",
    "En gereksiz kelime nedir?🫣",
    "Gördüğünüz en kötü veya en tuhaf rüya neydi?🤯",
    "Tüm dünya borç batağındaysa tüm para nereye gitti?🤔",
    "Paraşütle atlamak ister miydin?🥳",
    "Hayat bir video oyunuysa, en çok hangi hile kodunu kullanmak istersiniz?😂",
    "Yaşadığın şehri aşık olduğun biri için değiştirir misin?🥹",
    "Hala hatırlayabiliyorsan, en komik çocukluk anın ne?😄",
    "Bir insanda çekici gördüğün en garip şey nedir?😐",
    "Evde yalnız kalmaktan korkuyor musunuz?🤔",
    "Gerçek anlamda en son ne seni hayal kırıklığına uğrattı?🥲",
    "Biri seni aynanın önünde dans ederken yakaladı mı?😁",
    "Hayatında denemek istediğin çılgın maceralardan biri ne?🤔",
    "Kutudan doğrudan bir pastel boya yemek zorunda kalsaydınız ne renk isterdiniz?🤔",
    "Hiç iç çamaşırı giymeden bir gün geçirdin mi?😳",
    "Şimdiye kadar yediğin en tuhaf yemek neydi?👀",
    "Çocukken hiç kağıttan uçak ya da gemi yaptın mı?🥰",
    "Başkaları ile benim hakkımda hiç konuşuyor musun?🤔",
    "Çok sevdiğin sevgilin seni aldatsa ama çok pişman olsa onu affeder misin?🙄",
    "Zaman yolculuğunu nereye yapmak istersiniz: geçmişe mi yoksa geleceğe mi?🤔",
    "Kıyı asla geri sallamadığı için denizin tuzlu olduğunu düşünüyor musunuz?🤨",
    "Ölüm listenizdeki ilk kişi kimdir?🙄",
    "Gerçekten sarhoş olduktan sonra yaptığınız en çılgınca şey nedir?😅",
    "Bir keresinde bir yemek için ödeme yapmayı planlarken cüzdanınızı getirmeyi unuttunuz mu?😯",
    "İdam cezasına çarptırıldıysan son yemeğin ne olacağını düşünüyorsun?🤷🏻‍♂️",
    "Sahip olduğun en garip alışkanlığın nedir?😵‍💫",
    "Kaç defa aşık oldun?🤔",
    "Uyurken yürüyüşe çıkma alışkanlığınız var mı?😁",
    "İnsanlar çorbayı içer mi yoksa yer mi?😑",
    "Sence bir kişinin bir arkadaşlık uygulamasında biyografisine koyabileceği en kötü şey ne?🤮",
    "Köpek bulunan eve melek girmezmiş. Azrail de bir melek. Evimizi köpeklerle doldurursak ölümsüz olmaz mıyız?🫣",
    "Su altındayken bir balonu şişirmenin mümkün olduğuna inanıyor musunuz?🤓",
    "Kurgusal bir karakter olabilseydin, kim olurdun?😎",
    "Hangi Disney prensesi en iyi casusluk yapabilir?🙀",
    "En gereksiz kelime nedir?😒",
    "Hangisini tercih edersiniz: Burnunuz yok ama gerçekten güzel kokan parmaklarınız mı var? Ya da kör ol ama gerçekten güzel bir gülüşün var mı?😵",
    "Bir yıl 365 gün 6 saat sürüyor ise neden her yıl yılbaşını gece 12’de kutluyoruz?🎅🏻",
    "Vücudunun hangi bölümüne ekleme yapmak isterdin?🙂",
    "Köpeğimin adını “Hoşt” koyarsam çağırdığım zaman ne yapar?🐶",
    "Eğer uçağın karakutusu kaza anında parçalanmıyorsa neden bütün uçak o maddeden yapılmıyor?✈️",
    "Dünya döndüğü halde neden bir helikopter havada sabit durduğunda aynı yerde olur?🚁",
    "Bir zombi kıyametinde seçeceğiniz silah ne olurdu?🔫",
    "Tüp bebek daha mı az yakar?😵‍💫",
    "İngilizcede butterfly kelebek anlamına geliyor. “Butter” tereyağı demek, “fly” da uçmak anlamında, o zaman kelebekler uçantereyağları mıdır?😂",
    "Süpermen ve Batman arasındaki bir kavgada kim kazanır?🥵",
    "En büyük parti hayvanı hangisidir?😺",
    "Dünya dönüyorsa neden zıpladığımız zaman aynı yere düşüyoruz?🙃",
    "Yüzmek zayıflatıyorsa balinaların yağsız, tığ gibi olması gerekmez miydi?👀",
    "Hayvanlar konuşabilseydi, en kaba olan hangisi olurdu?😃",
    "Ressam olsaydın ilk gün neyi boyardın?👨🏻‍🎨",
    "Uhu iyi bir yapıştırıcıysa içinde bulunduğu tüpün içini neden yapıştıramıyor?🙊",
    "Mağara adamlarının mağara kadınları hakkında kabus gördüğünü düşünüyor musunuz?🫨",
    "Özellikle güzel kokmamasına rağmen koklamak istemeye devam ettiğin şey ne?🤪",
    "Bir zombi kıyametinde ne kadar hayatta kalabileceğin düşünüyorsun?😱",
    "Özellikle güzel kokmamasına rağmen koklamak istemeye devam ettiğin şey ne?🤪",
    "En çok hangi ünlüyle hayat değiştirmek istersiniz?😒",
    "Gördüğünüz en kötü veya en tuhaf rüya neydi?😪",
    "Zaman yolculuğunu nereye yapmak istersiniz: geçmişe mi yoksa geleceğe mi?🤔",
    "Kıyı asla geri sallamadığı için denizin tuzlu olduğunu düşünüyor musunuz?🤨",
    "Ölüm listenizdeki ilk kişi kimdir?🙄",
    "Gerçekten sarhoş olduktan sonra yaptığınız en çılgınca şey nedir?😅",
    "Bir keresinde bir yemek için ödeme yapmayı planlarken cüzdanınızı getirmeyi unuttunuz mu?😯",
    "İdam cezasına çarptırıldıysan son yemeğin ne olacağını düşünüyorsun?🤷🏻‍♂️",
    "Sence bir kişinin bir arkadaşlık uygulamasında biyografisine koyabileceği en kötü şey ne?🤮",
    "Köpek bulunan eve melek girmezmiş. Azrail de bir melek. Evimizi köpeklerle doldurursak ölümsüz olmaz mıyız?🫣",
    "Korku filmlerinden korkuyor musunuz?😱",
    "Vampir ile kurt evlenirse çocukları kumpir mi olur?🤭",
    "Başkalarına bildirmek için hangi gizli komployu yapmak istersin?🥶",
    "Eğer bugün hava sıcaklığı 0 derece ise ve yarın iki kat daha soğuk olacaksa, yarın hava yine 0 derece olmaz mı?😁",
    "Köpeklerin konuşabilseydi imajını tamamen mahvedecek bir şey söyleyebilir mi?🤕",
    "Neden sa yazarken as yazılıyoda hi yazılırken ih yazılmıyor?😶‍🌫",
    "İnekler ot yiyip süt üretiyorsa sütün hammaddesi ot mudur?🫤",
    "Uçakta uçmaktan korkuyor musunuz? 😁",
)


gunaydin = (
    "Günaydın ☺️",
    "Gün aydı hadi sende uyan🌄",
    "Sen daha uyanmadın mı? Günaydın ☺️",
    "Bugün Uyanmaya niyetin yok herhalde 😅",
    "Sen uyanmazsan yüzüne su dökerim bak 🙄",
    "Günaydın çiçeğim kahvaltı hazır 😂",
    "Neden tüm öğünlere yemek diyoruz da sabah kahvaltı diyoruz 🙄",
    "155 i arayalım mı uyanmak için baskın mı bekliyorsun 😅",
    "Uyansana Uykucu Güneş Doğdu 🌞",
    "Üsküdarda sabahboldu kalksana 🧸",
    "Horozlar ötmedi diye mi Uyuyorsun daha 😁",
    "Güneş doğarken sizin ev karanlık kalıyor galiba daha uyanmadığına göre 😳",
    "Ee Sabah Oldu sen yoksun ❓",
    "Artık Uyanacak mısın 🤔",
    "Kalk Kahvaltı hazırla sabah oldu 😂",
    "Ya Uyansana seni bekliyorum 🤗",
    "Çalışkan insanlar Erken uyanırlar..☺️",
    "Pişt Uyandın mı? 🤔",
    "Hadi Uyanda balığa gidelim 😁",
    "Seni de sürekli isminle seslenip uyandıran biri var mı ? 😁",
    "Uyanmak için Kaç para istiyorsun Uleeynnn😎",
    "Sakince Elindeki yastığı yere bırak ve Uyan artık 😁",
    "Uyanmak Zorundasın İşe gitcen Kalk 😅",
    "Hadi Uyan Bugğn Pkulun Yok mu Senin 😂",
)

unotag = ( 
	"Gel Hadi Uno Oynayalım...🫡",
	"Uno oynadın mı sen daha önce?🤭",
	"Uno Kart Oyununu Bilir misin?🤔",
	"Heyy Uno Var gell 🤗‼️",
	"Aloo Uno Oynuyoruz. gelll 🙄!!",
	"Uno Başladı /katil yazarak sende katılabilirsin. ☺️",
	"Bu grupta Uno Zevki Bir Başka 😂",
)

iyigeceler = (
    "**Sana da iyi Gecelerr**",
    "**İyi gecelerin olsun.**",
    "**Gecenin karanlığı düştü iyi geceler.**",
    "**Hayırlı geceler kardeş 🥱**",
    "**Nasıl İyi mi geceler?**",
    "**İyi akşamlar canım**",
    "**Yeni mi gece oldu ya?**",
    "**Gecenin yarısı olmuş iyi uykular 😁**",
)

anonim = (
    "**Anonim Oynayacağız sese koş 🥳**",
    "**Seslide anonim var gelsene ☺️**",
    "**Anonim oyununu biliyor musun seste oynuyoruz gel anlatalım..**",
    "**Anonime koş hadi 😎**",
    "**Sesli Sohbette anonim oynuyoruz 😁**",
    "**Anonim oyunu ile birbirimizi tanırız gel hadi 🥳**",
    "**Bu grupta anonim bir başka eğlenceli çık sesli sohbete 😎**",
    "**Anonim oyununu cezalı oynuyoruz, gel ceza al 😁**",
)

mani = (
    """**Çadıra serdim keçe
Koyunu sürdüm gece
O günlerde gelir mi?
Elin elime geçe**""",
    """**Çalıştım arı gibi
Peteğin balı gibi
Kız sen beni erittin
Dağların karı gibi**""",
    """
**Patlıcanı haşladım
Doldurmaya başladım
Dediler yarin gelmiş
Oynamaya başladım**""",
    """**Su gelir akmayınan
Dereyi yıkmayınan
Seven yâre doyar mı?
Uzaktan bakmayın**""",
    """**Portakal dilim dilim
Gel otur benim gülüm
Ben sana ne dedim ki
Tutulsun benim dilim**""",
    """**Mani maniyi açar
Mani gönlümü açar
İki sen söyle bir ben
Hangimiz üste çıkar**""",
    """**Bahçelerde babaçça
Açılır akça akça
Kaçtım karşıma çıktı
Tombul yanaklı Hatça**""",
    """**Çilekten yaptım reçel
Kara gün gelir geçer
Derdimi söyleyemem
Kalbimden neler geçer**""",
    """**Leçenin bucağında
Od olur ocağında
Allah canımı alsın
O yârin kucağında**""",
    """
**Bağa girdim hurmaya
Avcı geldi vurmaya**""",
    """**Ele bağışlanır mı
Bahçede ekşi elma**""",
    """**Dolu vurdu bağıma
Yel attı yaprağını
Korkarım garip ölem
El atar toprağımı**""",
    """**Penceresi Orhun’dan
Bir yar sevdim Zorkun’dan
Keşke sevmez olaydım
Ödü koptu korkudan**""",
    """**Bahçelerde mum direk
Suyu nerden indirek
İrezil gelin gidiyo
Uyuz ite bindirek**""",
    """**Sıra sıra kazanlar
Kara yazı yazanlar
Cennet yüzü görmesin
Aramızı bozanlar**""",
    """**Bağa girdim hurmaya
Avcı geldi vurmaya**""",
    """**Dürüp cebime koydum
Ne güzelsin Maşallah
Macirin kızlarını
Şeytan çarpar inşallah**""",
    """**Faytonun penceresi
Elindedir ceresi
Küçükken gelin olmuş
Ne bunun acelesi**""",
    """**Kaleden indim durdum
Bir çift güvercin vurdum
Kız mendilin ne güzel**""",
    """**Postanede pulcusun
Ormanlarda kolcusun
Meyil versem söz versem
El kulakta yolcusun**""",
    """**Höbek höbek dikenler
Aba gömlek biçenler
Bakışından bellidir
Kara sevda çekenler**""",
    """**Kaşların karasına
Mim çekmiş arasına
Seni cerrah diyorlar
Yürekler yarasına**""",
    """**Hapisanenin kapısı
Demirdendir yapısı
Yârimin günü varmış
Bir ay daha hapisi**""",
    """**Örtünü eğirmişsin
Kaşına değirmişin
Çokta güzel değildin
Kendini sevdirmişin**""",
    """**Kız entarin eflatun
Dön de arkana bakın
Senin gibi güzeli
Vermem ellerden sakın**""",
    """**Bir dalda iki vişne
Güzelim aşka düşme
Bu aşkın sonu yoktur
Boş yere dile düşme**""",
    """**Bahçede ekşi elma
Ne güzelsin Maşallah
Macirin kızlarını
Şeytan çarpar inşallah**""",
    """**Mantuvarım mantuvar
Mantuvarın vakti var
Mantuvara gelenin
Cennette bir tahtı var**""",
    """**Nazlıya bak nazlıya
Evin engin değil mi?
Doğru söylen komşular
Nazlı dengim değil mi?**""",
    """**Oğlanın adı Yılmaz
Olmaz aslanım olmaz
İçin gel gel demezse
O evde geçim olmaz**""",
    """**Ay doğar sini gibi
Sininin yanı gibi
Oyar beni seviyor
Beden de canı gibi**""",
    """**Merdiveni kırkayak
Kırkına vurdum dayak
Yar geliyor dediler
Seyirttim yalınayak.**""",
    """**Şu tepenin alıcı
Kırmızıdır pabucu
Şeftali vermeyenin
Kabul olmaz orucu.**""",
    """**Yeşil sandık kilidi
Üstünü gül bürüdü
Kız sen orada ben burda
İman tahtam çürüdü**""",
    """**Kekliğim seker ağlar
Tüyünü döker ağlar
Anasız gelin olan
İçini çeker ağlar**""",
    """**Sırma belikli yârim
Beyaz bilekli yârim
Nasıl bensiz durursun
Mermer yürekli yârim**""",
    """**Sunam sesemi geldin
Ayak basamı geldin
Sağlığımda gelmedin
Öldüm yasamı geldin**""",
    """**Küçük ovalı geldi
Atlı develi geldi
Başıma bu sevdalar
Seni seveli geldi**""",
    """**Kaşların emi emi
Ne bakan kinle beni
Yat dizimin üstüne
Çekeyim sana ninni.**""",
    """**Yanamam bile bile
Ben düştüm gurbet ile
Yedi mendil çürüttüm
Gözüm yaşın sile sile.**""",
    """**Siyah zülüflü canım
Neşter vur aksın kanım
Nar göbek fincan olsun
Doldur içeyim canım.**""",
    """**Ağaçlarda mazılar
Gönül seni arzular
Yar aklıma gelince
Yüreciğim sızılar.**""",
    """**Karşıda duran sensin
Zülfünü buran sensin
Bana cellât kar etmez
Boynumu vuran sensin.**""",
    """**Bugün hava karardı
Betim benzim sarardı
Baş ecel yastığında
Kolum yâri sarardı.**""",
    """**Kar yağar kiriş gibi
Eridim gümüş gibi
Ben yâri arzuladım
Tufanda yemiş gibi.**""",
    """**Yel vurur kazak oynar
Başımda tozak oynar
Ben yârime ne yaptım
O benden uzak oynar**""",
    """**Tarla başı pıtırak
Duralım tarak tarak
Çok çalıştık yetmez mi?
Gelin kızlar oturak**""",
    """**Mendilleri kokulu
Yan cebinde sokulu
Ne zaman kapanacak
Dağıstan’ın Okulu**""",
    """**Gel yakına yakına
Çeşmenin arkasına
Kırmızı gül takayım
Ceketin yakasına**""",
    """**Kayalardan kayarım
Bu kız benim ayarım
Ayşe benim olmazsa
Kaderime yanarım**""",
    """**Yel vurur kazak oynar
Başımda tozak oynar
Ben yârime ne yaptım
O benden uzak oynar**""",
    """**Tarla başı pıtırak
Duralım tarak tarak
Çok çalıştık yetmez mi?
Gelin kızlar oturak**""",
    """**Mendilleri kokulu
Yan cebinde sokulu
Ne zaman kapanacak
Dağıstan’ın Okulu**""",
    """**Gel yakına yakına
Çeşmenin arkasına
Kırmızı gül takayım
Ceketin yakasına**""",
    """**Kayalardan kayarım
Bu kız benim ayarım
Ayşe benim olmazsa
Kaderime yanarım**""",
    """**Bahçe bahçe gezerim
İnci boncuk düzerim
Bakın işte yüzüme
Bu köyde en güzelim**""",
    """**Kara taşın kenarı
Üstünde kırdım narı
Tutulası dillerim
Nasıl darılttın yarı**""",
    """**Yuvasında kırlangıç
Kanadı ayrıç ayrıç
Döne Kızı sevenler
Kan kussun avuç avuç**""",
    """**Elinde var yelpaze
Kuş dadanmış kiraza
Yakında geleceğim
Çekme kendini naza**""",
    """**Mani mani nideyim
Hangi günde geleyim
Ellerin yâri güzel
Ben çirkini nideyim**""",
    """**Masa üstünde bıçak
Sanki bana vuracak
Anne haberin olsun
Abim kız kaçıracak**""",
    """**Gül gibi oyum oyum
Kısacık kaldı boyum
Alacaksan al kalan
Yeter ettiğin oyun**""",
    """**Çaya vardım çayladım
Çayda balık avladım
Balık değil amacım
Ben gönlümü eğledim**""",
    """**Tren yolunda tütün
Yaprağı bütün bütün
Hem ana hem babadan
Koyma Allah’ım yetim**""",
    """**Gide gide yoruldum
Bir kenara oturdum
Güzelliğine değil
Çalımına vuruldum**""",
    """**Caminin minaresi
Mektebin penceresi
Şu Macirin kızları
Bulaşık tenceresi**""",
    """**Kiraz dalı budaklı
Meryem kiraz dudaklı
Yârim dünya güzeli
Elma gibi yanaklı**""",
    """**Derelere gidelim
Koyun kuzu güderim
İkimizi görmüşler
Nasıl inkâr ederim**""",
    """**Mezarlığın taşını
Koyun mu sandın yârim
Sevipte ayrılmayı
Oyun mu sandın yârim**""",
    """**Al giydim alsın diye
Mor giydim sarsın diye
İsteyene varmadım
Sevdiğim alsın diye**""",
    """**Karşıdan yar geliyor
Fistanı dar geliyor
Ben sevdim eller aldı
O bana ar geliyor**""",
    """**Gökyüzünde tayyare
Önündedir pervane
Kaş göz oynatsam oğlan
Olacak bir divane**""",
    """**Bakkallarda toz şeker
Şekerler kilo çeker
Seni gâvurun oğlu
Gördüğüne ah çeker**""",
    """**Kızın adı gül Fatma
Ayranlara su katma
Utanıyorum canım
Yolda bana laf atma**""",
    """**Gide gide yoruldum
Bir duldaya oturdum
Pezevengin oğluna
Bir bakışta vuruldum**""",
    """**Annem entari almış
Beyaz çizgisi varmış
Bir yar sevdim bilmeden
Onunda yâri varmış**""",
    """**Karalar karda kaldı
Bülbüller zarda kaldı
Gönül kapısı kitli
Anahtar yarda kaldı**""",
    """**Kara kütük yanıyor
İçinde çay kaynıyor
Hele bakın eltiler
Ne de güzel oynuyor**""",
    """**Kahve piştiği yerde
Pişip taştığı yerde
Güzel çirkin aranmaz
Gönül düştüğü yerde**""",
    """**Osmaniye üst başta
Oturma kışın taşta
Ben senle eğleniyom
Benim sevdiğim başka**""",
    """**Mendilim yelleniyo
Şu gönlüm eğleniyo
Şu macirin kızları
Oğlanmı beğeniyo**""",
    """**Konağın penceresi
Ne zalimdir gecesi
Sana kim âşık olur
Sokaklar eğlencesi**""",
    """**Çeşmenin taşı gibi
Gözünün yaşı gibi
Öyle bir kız sevdim ki
Kanarya kuşu gibi**""",
    """**Kayalarda kayarım
Yoktur benim ayarım
Ben sevdadan ölürsem
Kaderime yanarım**""",
    """**Arabalar geliyo
Ablam gelin oluyo
O kocaya gidince
Sıra bana geliyo**""",
    """**Çay kıyında çalılık
Boğazında altılık
İyi bakın oğlanlar
Oynayanlar satılık**""",
    """**Kaşları ok sevdiğim
Canımdan çok sevdiğim
Hep güzeller geliyor
İçinde yok sevdiğim**""",
    """**Yumurtası hollukta
Oturuyor yollukta
Eller düğün yapıyor
Bizim düğün bollukta**""",
    """**Dam üstünde yuvarlak
Dere akıyor şarlak
Benim sevdiğim yârim
Doğan aylarda parlak**""",
    """**Sıra sıra çarşılar
Yârim beni karşılar
Gizli gizli konuştum
Şimdi duydu komşular**""",
    """**Bir taş attım kargaya
Dönüp baktım arkaya
Evvel candan severdim
Şimdi vurdum dalgaya**""",
    """**Elmayı yüke koydum
Ağzını dike koydum
Aldım yârin elinden
Boynunu büke koydum**""",
    """**Karanfil haşlanır mı?
Saksısı taşlanır mı?
Küçücükken yar sevdim
Ele bağışlanır mı?**""",
    """**Pencerede duran kız
Bayram geldi dolan kız
Kurbansız bayram olmaz
Sana olam kurban kız**""",
    """**Karşıdan bakma yârim
Kaşlarını çatma yârim
Ben eski zamparayım
Hiç çalım satma yârim**""",
    """**Kar yağar saçaklara
Dökülür sokaklara
Nasıl ana doğurmuş
Sığmıyor kucaklara**""",
    """**Yüzüğüm taşa geldi
Bir kalem başa geldi
Sevda nedir bilmezdim
Ne çare başa geldi.**""",
    """**Hapsanenin kapısı
Demirdendir yapısı
Yârimin günü varmış
Bir ay daha hapisi**""",
    """**Örtünü eğirmişsin
Kaşına değirmişin
Çokta güzel değildin
Kendini sevdirmişin**""",
    """**Kız entarin eflatun
Dön de arkana bakın
Senin gibi güzeli
Vermem ellerden sakın**""",
    """**Bir dalda iki vişne
Güzelim aşka düşme
Bu aşkın sonu yoktur
Boş yere dile düşme**""",
    """**Mantuvarım mantuvar
Mantuvarın vakti var
Mantuvara gelenin
Cennette bir tahtı var**""",
    """**Nazlıya bak nazlıya
Evlerin engin değil mi?
Doğru söylen komşular
Nazlı dengim değil mi?**""",
    """**Oğlanın adı Yılmaz
Olmaz aslanım olmaz
İçin gel gel demezse
O evde geçim olmaz**""",
    """**Ay doğar sini gibi
Sininin yanı gibi
Oyar beni seviyor
Beden de canı gibi**""",
    """**Dağda fıstık olur mu?
Ateş yastık olur mu?
Sen orada ben burada
Böyle dostluk olur mu?**""",
    """**İn dereye dereye
Dere çakıllı yârim
Her geçene bakıyor
Gel geç akıllı yârim**""",
    """**Bahçelerde portakal
Gitme yârim burada kal
Sen şehre inersen
Bana çam bardak al**"""

)

# emojileri bir listeye atıyoruz
emoji = (
    "💋",
    "💘",
    "💝",
    "💖",
    "💗",
    "💓",
    "💞",
    "💕",
    "💌",
    "❣️",
    "💔",
    "❤️",
    "🧡",
    "💛",
    "💚",
    "💙",
    "💜",
    "🖤",
    "💟",
    "💍",
    "💎",
    "💐",
    "💒",
    "🌸",
    "💮",
    "🏵️",
    "🌹",
    "🥀",
    "🌺",
    "🌻",
    "🌼",
    "🌷",
    "🌱",
    "🌲",
    "🌳",
    "🌴",
    "🌵",
    "🌾",
    "🌿",
    "☘️",
    "🍀",
    "🍁",
    "🍂",
    "🍃",
    "🍄",
    "🥭",
    "🍇",
    "🍈",
    "🍉",
    "🍊",
    "🍋",
    "🍌",
    "🍍",
    "🍎",
    "🍏",
    "🍐",
    "🍑",
    "🍒",
    "🥬",
    "🍓",
    "🥝",
    "🍅",
    "🥥",
    "🥑",
    "🍆",
    "🥔",
    "🥕",
    "🌽",
    "🌶️",
    "🥯",
    "🥒",
    "🥦",
    "🥜",
    "🌰",
    "🍞",
    "🥐",
    "🥖",
    "🥨",
    "🥞",
    "🧀",
    "🍖",
    "🍗",
    "🥩",
    "🥓",
    "🍔",
    "🍟",
    "🍕",
    "🌭",
    "🥪",
    "🌮",
    "🌯",
    "🥙",
    "🥚",
    "🧂",
    "🍳",
    "🥘",
    "🍲",
    "🥣",
    "🥗",
    "🍿",
    "🥫",
    "🍱",
    "🍘",
    "🍙",
    "🍚",
    "🍛",
    "🍜",
    "🥮",
    "🍝",
    "🍠",
    "🍢",
    "🍣",
    "🍤",
    "🍥",
    "🍡",
    "🥟",
    "🥠",
    "🥡",
    "🍦",
    "🍧",
    "🍨",
    "🍩",
    "🍪",
    "🧁",
    "🎂",
    "🍰",
    "🥧",
    "🍫",
    "🍬",
    "🍭",
    "🍮",
    "🍯",
    "🍼",
    "🥛",
    "☕️",
    "🍵",
    "🍶",
    "🍾",
    "🍷",
    "🍸",
    "🍹",
    "🍺",
    "🍻",
    "🥂",
    "🥃",
    "🥤",
    "🥢",
    "🍽️",
    "🍴",
    "🥄",
    "🏺",
    "🙈",
    "🙉",
    "🦝",
    "🐵",
    "🐒",
    "🦍",
    "🐶",
    "🐕",
    "🐩",
    "🐺",
    "🦊",
    "🐱",
    "🐈",
    "🦁",
    "🐯",
    "🐅",
    "🐆",
    "🐴",
    "🐎",
    "🦄",
    "🦓",
    "🦌",
    "🐮",
    "🦙",
    "🐂",
    "🐃",
    "🐄",
    "🐷",
    "🦛",
    "🐖",
    "🐗",
    "🐽",
    "🐏",
    "🐑",
    "🐐",
    "🐪",
    "🐫",
    "🦒",
    "🐘",
    "🦏",
    "🐭",
    "🐁",
    "🐀",
    "🦘",
    "🐹",
    "🦡",
    "🐰",
    "🐇",
    "🐿️",
    "🦔",
    "🦇",
    "🐻",
    "🐨",
    "🐼",
    "🐾",
    "🦃",
    "🐔",
    "🦢",
    "🐓",
    "🐣",
    "🐤",
    "🦚",
    "🐥",
    "🐦",
    "🦜",
    "🐧",
    "🕊️",
    "🦅",
    "🦆",
    "🦉",
    "🐸",
    "🐊",
    "🐢",
    "🦎",
    "🐍",
    "🐲",
    "🐉",
    "🦕",
    "🦖",
    "🐳",
    "🐋",
    "🐬",
    "🐟",
    "🐠",
    "🐡",
    "🦈",
    "🐙",
    "🐚",
    "🦀",
    "🦟",
    "🦐",
    "🦑",
    "🦠",
    "🐌",
    "🦋",
    "🐛",
    "🐜",
    "🐝",
    "🐞",
    "🦗",
    "🕷️",
    "🕸️",
    "🦂",
    "🦞",
    "👓",
    "🕶️",
    "👔",
    "👕",
    "👖",
    "🧣",
    "🧤",
    "🧥",
    "🧦",
    "👗",
    "👘",
    "👙",
    "👚",
    "👛",
    "👜",
    "👝",
    "🛍️",
    "🎒",
    "👞",
    "👟",
    "👠",
    "👡",
    "👢",
    "👑",
    "👒",
    "🎩",
    "🎓",
    "🧢",
    "⛑️",
    "📿",
    "💄",
    "🌂",
    "☂️",
    "🎽",
    "🥽",
    "🥼",
    "🥾",
    "🥿",
    "🧺",
    "🚂",
    "🚃",
    "🚄",
    "🚅",
    "🚆",
    "🚇",
    "🚈",
    "🚉",
    "🚊",
    "🚝",
    "🚞",
    "🚋",
    "🚌",
    "🚍",
    "🚎",
    "🚐",
    "🚑",
    "🚒",
    "🚓",
    "🚔",
    "🚕",
    "🚖",
    "🚗",
    "🚘",
    "🚙",
    "🚚",
    "🚛",
    "🚜",
    "🚲",
    "🛴",
    "🛵",
    "🚏",
    "🛣️",
    "🛤️",
    "⛵️",
    "🛶",
    "🚤",
    "🛳️",
    "⛴️",
    "🛥️",
    "🚢",
    "✈️",
    "🛩️",
    "🛫",
    "🛬",
    "🚁",
    "🚟",
    "🚠",
    "🚡",
    "🛰️",
    "🚀",
    "🛸",
    "🌍",
    "🌎",
    "🌏",
    "🌐",
    "🗺️",
    "🗾",
    "🏔️",
    "⛰️",
    "🗻",
    "🏕️",
    "🏖️",
    "🏜️",
    "🏝️",
    "🏞️",
    "🏟️",
    "🏛️",
    "🏗️",
    "🏘️",
    "🏚️",
    "🏠",
    "🏡",
    "🏢",
    "🏣",
    "🏤",
    "🏥",
    "🏦",
    "🏨",
    "🏩",
    "🏪",
    "🏫",
    "🏬",
    "🏭",
    "🏯",
    "🏰",
    "🗼",
    "🗽",
    "⛪️",
    "🕌",
    "🕍",
    "⛩️",
    "🕋",
    "⛲️",
    "⛺️",
    "🏙️",
    "🎠",
    "🎡",
    "🎢",
    "🎪",
    "⛳️",
    "🗿",
    "💦",
    "🌋",
    "🌁",
    "🌃",
    "🌄",
    "🌅",
    "🌆",
    "🌇",
    "🌉",
    "🌌",
    "🌑",
    "🌒",
    "🌓",
    "🌔",
    "🌕",
    "🌖",
    "🌗",
    "🌘",
    "🌙",
    "🌚",
    "🌛",
    "🌜",
    "🌡️",
    "☀️",
    "🌝",
    "🌞",
    "🌟",
    "🌠",
    "☁️",
    "⛅️",
    "⛈️",
    "🌤️",
    "🌥️",
    "🌦️",
    "🌧️",
    "🌨️",
    "🌩️",
    "🌪️",
    "🌫️",
    "🌬️",
    "🌀",
    "🌈",
    "☔️",
    "❄️",
    "☃️",
    "⛄️",
    "☄️",
    "💧",
    "🌊",
    "🎑",
    "💤",
    "💥",
    "💨",
    "💫",
    "💬",
    "🗨️",
    "🗯️",
    "💭",
    "🕳️",
    "🚨",
    "🛑",
    "⭐️",
    "🎃",
    "🎄",
    "✨",
    "🎈",
    "🎉",
    "🎊",
    "🎋",
    "🎍",
    "🎎",
    "🎏",
    "🎐",
    "🎀",
    "🎁",
    "🃏",
    "🀄️",
    "🦷",
    "🦴",
    "🛀",
    "👣",
    "💣",
    "🔪",
    "🧱",
    "🛢️",
    "⛽️",
    "🛹",
    "🚥",
    "🚦",
    "🚧",
    "🛎️",
    "🧳",
    "⛱️",
    "🔥",
    "🧨",
    "🎗️",
    "🎟️",
    "🎫",
    "🧧",
    "🔮",
    "🎲",
    "🎴",
    "🎭",
    "🖼️",
    "🎨",
    "🎤",
    "🔍",
    "🔎",
    "🕯️",
    "💡",
    "🔦",
    "🏮",
    "📜",
    "🧮",
    "🔑",
    "🗝️",
    "🔨",
    "⛏️",
    "⚒️",
    "🛠️",
    "🗡️",
    "⚔️",
    "🔫",
    "🏹",
    "🛡️",
    "🔧",
    "🔩",
    "⚙️",
    "🗜️",
    "⚖️",
    "⛓️",
    "⚗️",
    "🔬",
    "🔭",
    "📡",
    "💉",
    "💊",
    "🚪",
    "🛏️",
    "🛋️",
    "🚽",
    "🚿",
    "🛁",
    "🛒",
    "🚬",
    "⚰️",
    "⚱️",
    "🧰",
    "🧲",
    "🧪",
    "🧴",
    "🧷",
    "🧹",
    "🧻",
    "🧼",
    "🧽",
    "🧯",
    "💠",
    "♟️",
    "⌛️",
    "⏳",
    "⚡️",
    "🎆",
    "🎇",
)


karakter = (
    "/ban ",
    
)



slapmessage = [

    "{}, {}**'a Fosfor Bombası Attı! Yasalara Aykırı😰!**",
    "{}, {}**'in Suratına Domates Fırlattı! Suratı kıpkırmızı oldu 😁**", 
    "{}, {}**'in Saçını Çekti!**", 
    "{}, {}**'nin Suratına Yumruk attı ! Buz koy morarmasın 🤕**", 
    "{}, {}**'e Kafa Attı! Burnu kırıldı sanırım 😱**", 
    "{}, {}**'e Uçan Tekme Attı! Jetli misin mübarek 👀**", 
    "{}, {}**'e Kanepeyi Fırlattı! Öyle ölmez füze atsaydın 😱**", 
    "{}, {}**'e İğne sapladı! Bu acıtmıştır sanırım 🥲**", 
    "{}, {}**'a Yumurta Fırlattı! Tam isabet 🎯**", 
    "{}, {}**'e Omuz attı! Ne bakıyon birader**", 
    "{}, {}**'e Sana Çelme taktı!**", 
    "{}, {}**'e Damacana Fırlattı! Damacanaya bişey olmamıştır umarım 👀**", 
    "{}, {}**'e Üstüne Çay Döktü! Yanıyorsun Fuat Abii 🔥**", 
    "{}, {}**'in Kafasında Şişe Kırdı! Acımış olmalı 🥲**",
    "{}, {}**'in Yüzüne Tükürdü! İşte bunu yapmayacaktın 🤬**", 
    "{}, {}**'e Taş Attı! Aha kafası yarıldı 🤭**", 
    "{}, {}**'e Osmanlı Tokatı Attı! Resmen şamar oğlana çevirdi 😱**", 
    "{}, {}**'e Kavanoz Fırlattı! Başka bişey bulamadı sanırım 🙄**",
    "{}, {}**'in Ayağının Önüne Muz Fırlattı! Basıp Kaydı 😂**",
    "{}, {}**'e Çöp Kovası Fırlattı! Üstü Başı Hep Çöp Oldu 😥**",
    "{}, {}**'in Üzerine Kamyon Sürdü! Kamyon'un Altında Kalmaktan Son Anda Kurtuldu 😱**",
    "{}, {}**'in Gözüne Parmağını Soktu! Bu Gerçekten Acımış Olmalı 😭**", 
    "{}, {}**'e Yolda Yürürken Ensene Tokat Attı ! Ve Kaçmaya Başladı🤣**",
    "{}, {}**'in Yüzüne Kezzap Attı! Ah Be Bergenim🥹**",   
    "{}, {}**'i Kıyma Makinesine Attı! Yenir Omega5😋**",  
    "{}, {}**'e F35 Fırlattıı!! Savaş Başlasın🫣**",   
    "{}, {}**'e Pasta Attı!! Duş Almak Şart Oldu.😝**",
    "{}, {}**'eTerlik Fırlattı!! Tam İsabet Anne Adayı mısın Beee😱🤣**",  
    "{}, {}**'in Üzerine Benzin Döktü Ve Ateşe Verdi!😳**",
    "{}, {}**'in Kafasını Balık Dolu Bir Kovaya Soktu😁**",
    "{}, {}**'in Yüzüne Pasta Fırlattı!😳**",
    "{}, {}**'in Yüzüne Kahve Döktü!😰**",
    "{}, {}**'in Yüzüne 150TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne Çay Döktü!😰**",
    "{}, {}**'in Yüzüne Su Döktü!🥹**",
    "{}, {}**'İçin Aldığı Hediyeyi Parçaladı!🥹**",
    "{}, {}**'in Yüzüne 200TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne Kola Döktü!😰**",
    "{}, {}**'e Tüplü TV Fırlattı!🥹**",
    "{}, {}**'in Kalbini Kırdı!🥹**",    
    "{}, {}**'in Yüzüne 1TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne 5TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne 10TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne 20TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne 50TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne 100TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne 150TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne 200TL Fırlattı!😁**",
    "{}, {}**'in Yüzüne Bira Döktü!😷**",
    "{}, {}**'in Yüzüne Tokat Attı!😡**",
    "{}, {}**'in Kafasını Öptü!🥹**",
    "{}, {}**'e Çicek Verdi😳**",
    "{}, {}**'e Su Fırlattı! Kurutma Makinası şart oldu🤩!**",
    "{}, {}**Al Şu 200'ü Bugün Eve Erken Git😂!**",
    "{}, {}**'e Tabanca Çekti! Seninde Boş Olmaman Lazım🙄!**",
    "{}, {}**'e Şarj Aleti Fırlattı ! Elektrik Saçıyorsun Bebeğim?⚡️**",
    "{}, {}**'e Kitap Fırlattı! Al Şu Kitabı Da Biraz Oku Akıllan🤓!**",
    "{}, {}**'e TDK Sözlüğü Fırlattı ! Konuşmayı Bilmiyor Musun Yoksa😰!**",
    "{}, {}**'e Çilek Fırlattı ! Al Ye Şunu🥹!**",
    "{}, {}**'e Ayna Fırlattı ! Bi Aynaya Bak Da Milletin Gözü Gönlü Açılsın?🤪**",
    "{}, {}**'e Tasma Fırlattı! Lazım Olur Takarsın😳!**",
    "{}, {}**'e Çiçek Fırlattı ! Evlenme Yaşın Gelmiş🤭!**",
    "{}, {}**'e Pantolon Fırlattı! Bizde Unutmuşsun😳!**",
    "{}, {}**'e Keleş Fırlattı! Kürtlük Damarınız Tuttu TaTaTaTa😄!**",
    "{}, {}**'e Erosun Okunu Fırlattı ! Sanırım Sana Âşık (çaktırma)🤭!**",
    "{}, {}**'e Arı Kovanı Fırlattı! Hızlı Kaç Arılar Geliyooor🏃🏻!**",
    "{}, {}**'e Terazi Fırlattı! Dengine Göre Aslanım😜!**",
    "{}, {}**'e Tartı Fırlattı! Oha Çok Kilolusun😳!**",
    "{}, {}**'e Çanta Fırlattı! Okula Git Oku Oku😡!**",
    "{}, {}**'e Premium Fırlattı! Sana Premium Alması Şart🥹!**",
    "{}, {}**'e Domestos Fırlattı! Süper Güçlerin Var Artık😁!**",
    "{}, {}**'in Yanağından Öptü😡**",
    "{}, {}**'nin üzerine benzin döktü ve ateşe verdi!** 🔥",
    "{}, {}**'nin kafasını balık dolu kovaya soktu!** 🐠",
    "{}, {}**'nin yüzüne pasta fırlattı! 🎂**",
    "{}, {}**'nin yüzüne bir fincan kahve döktü! **☕️",
    "{}, {}**'nin yüzüne 150 $ fırlattı!** 💴",
    "{}, {}**'nin yüzüne bir demlik çay döktü!** 🫖",
    "{}, {}**'nin yüzüne bir bardak su döktü** 🚰",
    "{}, {}** için aldığı hediyeyi parçaladı! **🎁",
    "{}, {}**'nin yüzüne 200 $ fırlattı!**🤑",
    "{}, {}**'nin yüzüne bir şişe kola döktü! **🍾",
    "{}, {}**'nin üzerine tüplü TV fırlattı!** 📺",
    "{}, {}**'nin kalbini kırdı!**💔",
    "{}, {}**'ye çiçek verdi **💐",
    "{}, {}**'nin yanağından öptü 😘**",
    "{}, {}**'nin internetinin kablosunu kopardı** 😈",
    "{}, {}**'nin proje ödevini yırttı!**😳",
    "{}, {}**'nin camına taş attı! **🪨",
    "{}, {}**'nin ağzına tuvalet terliği ile vurdu **🩴",
    "{}, {}**'nin kafasına pofuduk terlik fırlattı**🩴", 
    "{}, {}**'nin burnuna leblebi tıkadı** 😁",
    "{}, {}**'nin dişini kırdı** 🦷",
    "{}, {}**'nin arabasının lastiğini patlattı** 🛞",
    "{}, {}**'nin ciğerini çıkarıp kedilere verdi **🐈",
    "{}, {}**'nin kolunu cimcirdi** 😝",
    "{}, {}**'nin saçlarına sakız yapıştırdı** 😧",
    "{}, {}**'yi Satürn'e kaçırdı** 🪐",
    "{}, {}**'nin saçlarına yıldız taktı** 🌟",
    "{}, {}**'yi Everest'in tepesinden aşağıya attı** 🏔",
    "{}, {}**'ye kız kulesinde çay ısmarladı** 🍵",
    "{}, {}**'yi valse davet etti**💃🕺",
    "{}, {}**'nin kafasını su dolu kovaya daldırdı** 😁",
    "{}, {}**'nin çayına bisküvi bandırdı** 🍪",
    "{}, {}**'ni duş alırken kombiyi kapattı **😶‍🌫️",
    "{}, {}**'ya kendisini çekemiyor diye anten aldı**📡",
    "{}, {}**'nin fırın küreğiyle ağzına vurdu** 😐",
    "{}, {}**'nin akşam yemeği yerine kafasının etini yedi** 😮‍💨",
    "{}, {}**'e dengesizsin diyip terazi aldı **⚖️",
    "{}, {}**'ya sayısalcıyım seni bir güzel çarparım dedi **✖️",
    "{}, {}**'yi yanlışlıkla gruptan banladı** 🙀",
    "{}, {}**'nin doğum gününü kutlarken pastaya kafasını soktu** 🎂",
    "{}, {}**'nin ensesine şaplak attı** 👀",
    "{}, {}**'nin kafasını kuma gömdü **😔",
    "{}, {}**'nin komple vücudunu kuma gömdü **😃",
]
sarkilar = (
	"{},\n\n {}, için şarkı önerdi :\n\n**Müslüm Gürses - ayrılık**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İsmail yk - Allah belanı versin**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Güllü - Unut gitsin**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ceza - Holocost**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Mutlu Ol yeter**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Mavi Mavi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mahsun Kırmızıgül - Beşminare",
	"{},\n\n {}, için şarkı önerdi :\n\n**Halay - Delilo**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Derya uluğ - okyanus**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İntizar - Bu senede kahpelik moda**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Arka Mahalle**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Herai Zerdüş - Mavi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Herai Zerdüş - Sevgilim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Taladro - Dem**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Cem Karaca - Ben Ekmeğimi Böldüm de Yedim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Erkal - Gönül**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Tripkolic - Gözlerinin Yeşilini Özledim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Dilber Ay - Zorundamıyım**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Aramam**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Kıraç - Yalnızlığın Kapıları**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Bu Yalnızlık Benim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Rei - Ah Canım Sevgilim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Erkal - Çare Gelmez**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Bayhan - Tiryakinim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ali Kınık - Ben Seni Severken Çocuk Gibiyim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Yıldız Tilbe - Yürü Anca Gidersin**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Yıldız Tilbe - Şarkıların Şarkısı",
	"{},\n\n {}, için şarkı önerdi :\n\n**İntizar - Uykum Firari**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Hadise - Aşk Kaç Beden Giyer**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Berk Baysal - Zamanla Geçer**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Yakamoz**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Tarkan - Kuzu Kuzu**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Herai Zerdüş - Sende Beni Sevdin mi?**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Taladro - Deniz Kızı**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ankaralı Yasemin - Çıldıralım**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Davut Güloğlu - Nurcanım**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Nalan - Acemi Balık**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Sandal - Aşka yürek gerek**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Leylim ley**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Nil İpek - Son Mektup**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Blok3 - Affetmem**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Blok3 - Vur**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Yıldızdoğan - Ölür müydün?**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İntizar - Ihlamurlar Altında**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Zara - Seni Yazdım Kalbime**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Zara - Beni Unutma**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Yıldız Tilbe - Emi",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ebru Yaşar - Yoksun**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Burak Bulut - Cano**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sura İskenderli - Dinle**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Nahide babashlı - Söz Verdim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Deniz Toprak - Bilmeden Oldu**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Ceceli - Gün Ağarmadan**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Semicenk - Kader Sağolsun**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Semicenk - Batık Gemi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Kazım Koyuncu - Hayde**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Kazım Koyunca - Koyverdin Gittin**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Dilber Ay - Zoruna mı gitti gardaş**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İbrahim Tatlıses - Ayağında Kundura**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Gazapizm - Süzülerek**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sezen Aksu - İki Gözüm**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sezen Aksu - Herkes Yaralı**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Celal Yarıcı - Dışarda Mevsim Baharmış**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Celal Yarıcı - Seni Sevmeyen Ölsün**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sinan Akçıl - Bir Zamanlar Deli Gönlüm**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Ceceli - Maşallah**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sezen Aksu - Tükeneceğiz",
	"{},\n\n {}, için şarkı önerdi :\n\n**Gülnare - Bir Yari var**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Merve Özbey - Haram**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Onurcan Özcan - Yaramızda Kalsın**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Söyle**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Beni vur**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mustafa Ceceli- Sevgilim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Kum Gibi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Cem Karaca - Dağlar Dağlar**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Emircan İğrek - Müzik Kutusu**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Tripkolic - Koyu Kahverengi**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Selda Bağcan - Sivasın Yollarına**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Tarkan - Öp**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Manga - Cevapsız Sorular**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Müslüm Gürses - Nilüfer**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Müslüm Gürses - Yıllar Utansın**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Hakkı Bulut - Kıskanıyorum**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Emircan İğrek - Can Dostum**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mabel Matiz - Sultan Süleyman**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mabel Matiz - Antidepresan**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Ümit Besen - Nikah Masası",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mor Ve Ötesi - Bir Derdim Var**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Seksendört - Ölürüm Hasretinle**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Model - Pembe Mezarlık**",
        "{},\n\n {}, için şarkı önerdi :\n\n**Ahmet Kaya - Metrisin önü**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Herai Zerdüş - Papatya**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Belkıs Akkale - Dağlar seni delik delik delerim**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Sıla - Boş Yere**",
	"{},\n\n {}, için şarkı önerdi :\n\n**İzzet Altınmeşe - Maden Dağı**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Neşet Ertaş - Gönül Dağı**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Uygar Doğanay- Duydum Bir oğlun Olmuş**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Şehinşah - Nabız**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Neşet Ertaş - Ah Yalan Dünya**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Gazapizm - Heyecanı Yok**",
	"{},\n\n {}, için şarkı önerdi :\n\n**Mehmet Akça - Bakma Doktor Yarama**",
)

sarki1 = [ 
	"Yaw sahibime neden Şarkı önereyim.😂",
	"Sahibime Şarkı Önermem O zaten Kendi Bilir ne dinleyeceğini 🥳",
]
sarki2 = [ 
	"Yaw kendi kendime şarkı önermem ben botum 😁",
	"Ben şarkı dinlemem ben botum canım ❤️ ",
]

dontslapme = [
    "**Yahu beni niye tokatlamaya çalışıyorsun** 🥺",
    "😳😳",
    "**Bunu yapmayacağım** 😊",
    "** :Dsfgasd?**",
    "**Kendimi tokatlattırmayacağım.** 😑"
]
dontslapown = [
    "**Sahibimi tokatlayamam :/**",
    "**Bunu çok istiyorum ama yapamam** 😔",
    "**Şaka yapıyor olmalısın :D**",
    "**Keşke mümkün olsa...**"
]

noadmin = "**➻ ☹️ ᴜᴢɢᴜɴᴜᴍ ᴀᴍᴀ ʏᴏɴᴇᴛɪᴄɪ ᴅᴇɢɪʟsɪɴɪᴢ .**"
nogroup = "**➻ ⚠️ ᴋᴏᴍᴜᴛʟᴀʀ sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**"
nomesaj = "**➻ 💬 ʙᴀɴᴀ ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .**"

galp = (
    "🤍",
    "🤎",
    "♥️",
    "❣️",
    "❤️",
    "💕",
    "💖",
    "💗",
    "💘",
    "💙",
    "💚",
    "💛",
    "💜",
    "💝",
    "💞",
    "💟",
    "🖤",
    "🩷",
    "🩶",
    "🩵",
    "🧡",
    "❤️‍🔥",
)



espri = [
    "Son gülen en geç anlayandır.",
    "İnsanların seni ezmesine izin verme. Ehliyet al, sen onları ez…",
    "İlahi Azrail … Sen adamı öldürürsün!",
    "Ben mafya babasıyım çünkü oğlumun adı Mafya.",
    "Kim vurduya gittim birazdan geleceğim.",
    "Zenginler et, fakirler hayalet yer.",
    "Hava korsanı uçağı kaçıracaktı ama yapamadı çünkü uçağı kaçırdı.",
    "GİT’Arı’ getir de biraz şarkı söyleyelim.\n   -Abi arı sokmasın!",
    "Canın sıkıldıysa gevşet.",
    "Almanya’da Almanlar, Sakarya’da sakarlar yaşar.",
    "Sana bir kıllık yapayım, kıllarını koyarsın.",
    "Seven unutmaz oğlum, eight unutur.",
    "Cem Uzan, üstünü örteyim.",
    "Haydi Unkapanı’na gidip birkaç kapan kuralım. Belki un yakalarız",
    "Adamın biri güneşte yanmış, ay da düz.",
    "Sinemada on dakika ara dedi, aradım aradım açmadı.",
    "Röntgen Filmi çektirdik, yakında sinemalarda.",
    "Geçen gün taksi çevirdim hala dönüyor.",
    "Ben hikâye yazarım Ebru Destan.",
    "Geçen gün geçmiş günlerimi aradım ama meşguldü.",
    "Tebrikler kazandınız, şimdi tencere oldunuz!",
    "Kaba kuvvet uygulama, kap kırılabilir.",
    "Ayna’nın karşısında süslenme, Manga’nın karşısında süslen.",
    "Geçen file çorap aldım, zürafaya almadım.",
    "Yılanlardan korkma, yılmayanlardan kork.",
    "Ben kahve içiyorum, Nurgül Yeşilçay.",
    "Bak şu karşıdaki uçak PİSTİ, ama bir türlü temizlemediler.",
    "Geçen gün geçmiş günlerimi aradım ama meşguldü.",
    "Adamın birisi televizyona çıkmış bir daha indirememişler.",
    "Adamın biri gülmüş, saksıya koymuşlar.",
    "Funda Arar dediler ama hala daha aramadı.",
    "Adamın kafası atmış bacakları eşek.",
    "Uzun lafın kısası: U.L.",
    "Yağmur yağmış, kar peynir!",
    "Sakla samanı, inekler aç kalsın.",
    "Baraj dendi mi, akan sular durur.",
    "Dünya dönermiş ay da köfte…",
    "Son gülen en geç anlayandır.",
    "Bu erikson, başka erik yok.",
    "Sen kamyonu al, Leonardo da vinci.",
    "Adamın biri gülmüş, bahçeye dikmişler.",
    "Top ağlarda, ben ağlamaz mıyım?",
    "Ben yürüyelim diyorum Gerard Depardieu.",
    "Ahmet Saz çaldı. Polis tutukladı.",
    "Beni ayda bir sinemaya götürme, Marsta bir sinemaya götür.",
    "Ben ekmek yedim Will Smith.",
    "Aaaaa siz çok terlemişsiniz durun size terlik getiriyim.",
    "Kalbinin sesini dinle güzelse kaset yap",
    "Bağırsaklarda yaşayan tenya kurtları bağırsakta yaşarlar bağırmasak da yaşar.",
    "Çiçeğin biri solmuş diğeri de sağ.",
    "Lütfen sessiz olun telefon faturasını yeni yatırdım uyuyor şimdi uyanmasın",
    "Nuri ölünce Çin’e gömsünler, nur içinde yatsın.",
    "Temel kahvede işe başlar, müşterilerden biri seslenir:\n   -Temel bize üç çay, biri açık olsun.\n   -Hangisi?",
    "Temel bir gün Fransa’ya gitmiş:\n   -Aaa burayı da mı Sabancı aldı, demiş.",
    "İngilizcem yok, tanıdığım bütün Cem’ler Türk.",
    "Sarımsağı havanda dövmüşsün, Ha Muş’ta.",
    "Dondurmayı ben yalamam, himalayalar.",
    "Yarasa yararlı bir hayvandır. Yararlı bir hayvan olmasaydı yaramasa derlerdi.",
    "Kelebekler, köstebekler ama ben beklemem.",
    "Bütün umutlarım suya düştü ama boğulmadılar. Çünkü onlara yüzme öğretmiştim",
    "Bu gece seni kınıyorum, çünkü kına gecesi.",
    "Basamakta durmayın otomatik kapı çarpar, böler, karekökünü alır.",
    "Hayırlı olsun Araba almışsın. Evet aldık. Niye Araba aldın ki kendine alsaydın.",
    "Çok Makbule geçti, şimdi de Fatma geçiyor.",
    "Alinin selamı var.\n   Hangi Ali?\n   Şehirlerarası otobüs termin-ali",
    "-Abi sana Sıla’nın selamı var.\n   -Hangi Sıla?\n   -Gayri Safi Milli HaSıla”",
    "Sen o çeteyi tanıyor musun\n   -Hangi çeteyi\n   -Peçeteyi.”",
    "Gözlüklerin numaralı mı?\n   -Yok kale arkası”",
    "Erkek ata ne denir?\n   Bayat”",
    "En güzel çay hangi dağda içilir?\n   Çay bar-dağı’nda”",
    "4. Murat neden intihar etmiş?\n   – İlk 3’e giremediği için",
    "Geçen gün arkadaşlarla fırında patates yiyorduk, fırın sıcak geldi bahçeye çıktık.",
    "Masada hangi örtü kullanılmaz?\n   – Bitki Örtüsü.",
    "Adamın kafası atmış bacakları eşek.",
    "Geçen gün geçmiş günlerimi aradım ama meşguldü.",
    "Sinüs 60, kosinüs tutmuş…",
    "Yağmur yağmış, kar peynir!",
    "Baraj dendi mi, akan sular durur.",
    "Kediler niçin havaalanına gidemez? Çünkü pist var."
]



commandList = [
    "zar",
    "dart",
    "basket",
    "basket",
    "futbol",
    "bowling",
    "slot",
    "para",
    "mani",
    "saka",
    "d",
    "c"
]



C_LİST=[
	"Seçtiğiniz bir sosyal medya hesabınızdan çok çirkin bir fotoğrafınızı paylaşın.","Mesaj yazma bölümünüzü telefonunuzdan açın gözlerinizi kapatın ve rasgele bir kişiye körü körüne bir metin gönderin.",
	"Önümüzdeki 5 dakika boyunca söylediğin her şeyden sonra “mee” diyeceksin",
	"Önümüzdeki 5 dakika içinde birinin hayvanı olun.","İnstagramını oyunculardan birine ver. 5 dk boyunca her yere bakmak serbest.",
	"Oyundan bir kişiye serenat yap (kız ise erkeğe, erkek ise kıza)","Sonraki 3 tur boyunca şiveyle konuş.",
	"3 dakika boyunca bebek taklidi yap!","Telefonunda ki en sevmediğin fotoğrafını at","En beğendiğin fotoğrafını at",
	"Whatsapp’da 2 konuşmanı at","Özel mesajlarını ssi al ve gruba at","Whatsapp’da son konuşmanı at",
	"Bir deftere 20 kez ben çatlağım yaz ve resmini at","Telegramda son konuşmanı ss at.","Biyografine +18 bir cümle yaz; 3 Saat duracak.!",
	"Galerinin bir kısmını ss alıp at","Galerindeki 16. Fotoğrafı at.","Instagram yada telegramdan tanımadığın birine komik olmayan bir fıkra anlat.",
	"Ninni Söyleyerek Ses At","Bugununle ilgili kısa bir hikaye uydur.","Grupta ki en çok hoşuna giden karşı cinse seni seviyorum diye mesaj at.",
	"Galerindeki 16. Fotoğrafı at.","Galerindeki 30. Fotoğrafı at.","Whatsapp’da konuşduğun kişilerin ss ini at",
	"Grubun üye listesine gir ve 7. kişiye anlık at. (Grup daha az kişiyse ya da aktif sayısı azsa üstten saymaya devam et)",
	"En son konuştuğun kişiye \"Hayırlı Cumalar\" diye mesaj at.(platform farketmez)",
	"Şuan ki halini fotoğraf çekip  atar mısın?","Grupta üyeler kısmına gir 11. kişiye \"Analar neler doğuruyor bee\" diye ses at ve cevabını grupla paylaş.",
	"Profil fotoğrafına nefret ettiğin bir ünlünün resmini koy.","Kafanda yumurta kır ve fotosunu at",
	"Gruptan sevdiğin bir kişinin fotoğrafını profil resmi yap","Balkona veya pencereye cık dısardakılerın duyacagı sekılde sarkı soyle videoya al gruba at.",
	"İtiraf et: üye çalmak için kaç hesabın var?","Gruptaki 5 abazaya seni seviyorum de","İki dakika tavuk gibi davran.","Seçtiğiniz bir hayvanı taklit edin.",
	"Seçtiğin bir nesneyi yalayın ve gruba fotosunu atın.","Gruba gerçekten utanç verici bir fotoğrafını göster.",
	"Çirkin bir selfie çek ve sosyal medya uygulamalarından birinde yayınla 1.5 saat kalacak.","Bir kaşık un ye ve video ya al gruba at",
	"Hiç tanımadığın birine Kurban Bayramınızı kutlarım deyin","Sevdiğin bir kişiye \"`ben seni neden sevdim niçin sevdim niye sevdim bunların bi izahı yok gördün işte sevdim. Yaw sahi ben seni nidennn sevdim `\" de. Cevap geldiğinde grupla paylaş biz de gülelim",
	"Telegram'daki en kalabalık grubu aç ve \"`Benim adım turşu bidonu!`\" diyerek ses kaydedip en kalabalık gruba gönder.","Hemcinsin olan yakın bir arkadaşına ona aşık olduğunu söyle.","Sürahiden su iç ve fotoğraf at.",
	"En çok konuştuğun karşı cinsten arkadaşına \" `Seni çok seviyorum galiba aşık oldum`\" yaz ve tepkisini bizimle paylaş",
	"İsmini 1 saatliğine Abdül<ismin> yap. (örneğin adın Berk ise AbdülBerk yap)","İnstagram'da dm kutunu (mesajlar bölümü) ss al gruba at.",
	"Tanımadığın birisine şu cümleyi atıp sohbet başlat: \"`Aşkımızın suya düşeceğini bilseydim , balık olurdum`\"",
	"En komik fotoğrafını grupla paylaş.","Grupta üyeler kısmına gir 11. kişiye \"`Analar neler doğuruyor bee`\" diye ses at ve cevabını grupla paylaş.",
	"Tanımadığın birine şu mesajı at sonra cevabını grupla paylaş ➡️\n  \"`Bu mesaj özel bir frekansla gönderilmiştir. Zekilerde hafıza kaybı, aptallarda kısa sureli körlük ibnelerde de bir anlık gülümseme yapar!`\"",
	"@ yaz çıkan ilk kişiyi etiketle ve seni seviyorum yaz.","Tanımadığın birine \" `sanırım sana aşık oldum`\" diye mesaj at.",
	"Telegram hakkında kısmına \"`Babasının Prensesi`\" yaz 1 saat boyunca dursun.","Birine Sesli Öpücük At Ve Etiketle",
	"Telegramda son konuşmanı ss at.","🎀 ŞANSLI MESAJ🎊 Grupdan İstediğin Birinin Google/Youtube/İnstagram Arama Geçmişini İste",
	"Galerinin En Alttan 7. Fotosunu gönder",
	"Sonraki 3 tur boyunca şiveyle konuş. Farklı şivelere kayış olursa /zar Komutunu kullanarak 6 ya en cok yaklaşan oyuncu sana ceza verecek",
	"Üç çorba kaşığı acı salça (veya buna benzer bir şey) ye ve video ya al gruba at",
	"5 dakika boyunca oyundaki birinin evcil hayvanı olmasını isteyebilirsin.","Yeri yala Ve fotoğraf/videosunu gruba at",
	"/zar Komutunu kullanarak 6 ya en cok yaklaşan oyuncuya sosyal medya hesaplarından birini 5dk ver",
	"3 dakika boyunca bir ünlüyü taklit et.", "Birisi taklit edilen sanatçıyı tahmin edene kadar bir sanatçıyı taklit et",
	"Grubun ortaya koyduğu bir konu etrafında sekiz satır ve iki mısralık bir şiir yaz",
	"Oyundaki kişilerin ortak kararıyla gruptan birini öp ses atarak (ortak karar verilemezse /zar komutundan 1 e en yakın oyuncuyu öp).",
	"5 dakika boyunca oyundaki bir kişinin kölesi ol.", "Bir süpürgeyle veya paspas ile dans et ve videosunu at",
	"Gerçek aşkının kim olduğunu ilan et","Ağzını hareket ettirmeden baştan sona alfabeyi oku okurken video at", "Aklına gelen ilk kelimeyi hemen söyle.",
	"Oyundaki oyunculardan biri hakkında hikaye uydur", "15 saniye içerisinde sondan başa doğru alfabeyi oku okurken ses at", "Bir köpek gibi havla havlarken ses at",
	"Bir şarkıyı baştan sona söyle söylerken ses at","Çıktığın en kötü ve en iyi kişiyi açıkla.",
	"Bir dakika boyunca karşı cinsten biri gibi yürü.","Sevgiline atıp atabileceğin en acımasız mesajı gönder.","Oyunda yer alan her kişi hakkında bildiğin komik bir şey anlat.",
	"Ünlü restoranlardan birini ara ve menülerini öğrenirken dalga geç.","Eski bir şarkıyı aç ve onu taklit ederek söylemeye çalış söylerken ses at","1 tur boyunca farklı bir dilde konuş.",
	"Eski sevgiline mesaj at ve onu unutamadığını söyle.","2 tur boyunca “sen” kelimesini duyunca kuş gibi ses çıkart.",
	"Telefondaki tarayıcı geçmişini herkese göster.","Odadan birisi için satın alacakmış gibi iç çamaşırı araştırması yap.",
	"En yakın dürümcüyü ara ve 300 tavuk dürüm siparişi ver. 1 dakika sonra siparişi başka yerden verdik diye iptal et.",
        "Telefonunu yanında ki kişiye ver. 5 dk boyunca her yere bakmak serbest.",
        "Eğer erkekse makyaj yapmasını isteyin. Eğer kızsa makyajını silmesini isteyin.",
        "1 dakika boyunca hiç müzik olmadan dans edin.",
        "Birine telefonunu ver ve istediği herhangi birine mesaj atsın.",
        "Odada ki herkesin koltuk altını koklayın.",
        "Odanın bir ucundan diğer ucuna ellerinizin üzerinde yürüyün. Gerekirse birisinden bacaklarınızı tutmasını isteyebilirsiniz.",
        "Kafanın üstünde iki yumurta kır.",
        "Önümüzdeki 5 dakika içinde birinin hayvanı olun.",
        "Elbiselerinizle bir duş alın.",
        "Size bir tokat atmak için gruptan birini seçin.",
        "Seçtiğiniz bir sosyal medya hesabınızdan çok çirkin bir fotoğrafınızı paylaşın.",
        "Mesaj yazma bölümünüzü telefonunuzdan açın gözlerinizi kapatın ve rasgele bir kişiye körü körüne bir metin gönderin.",
        "3 dakika boyunca stand-up gösteri yap.",
        "1 dakika açacağımız müzikte break dansı yap.",
        "Ayağıma masaj yap.",
        "Komşunun evine git ve muz iste.",
        "Başkasının dişlerini fırçala.",
        "Önümüzdeki 5 dakika boyunca söylediğin her şeyden sonra “mee” diyeceksin deyin.",
	
]

D_LİST = [
	"Telefonunda en son aradığın şey neydi?","Birisi kız arkadaşın / erkek arkadaşından ayrılmak için sana 1 milyon tl önerseydi, yapar mıydın?",
	"Bu grupda en az kimi seviyorsun ve neden?","Hiç sınıfta yüksek sesle geğirdin mi?",
	"Hiç sınıfta yüksek sesle geğirdin mi?","Yerden bir şeyi alıp hiç yedin mi?",
	"Bir gün karşı cins olarak uyanırsan, ilk yapacağın şey nedir?",
	"Hiç havuzda işedin mi?","Asansörde hiç gaz kaçırdın mı?",
	"Tuvalette otururken aklınıza gelen şeyler nelerdir?","Büyüyen hayali bir arkadaşınız var mıydı?",
	"En kötü alışkanlığınız nedir?","Burnunu karıştırır mısın?","Banyoda şarkı söyler misin?",
	"Hiç üzerine işedin mi?","Toplumda en utanç verici anınız neydi?","Aynada kendinle hiç konuştun mu?",
	"Web geçmişinizi, birileri görürse utanacağınız şey ne olurdu?","Uykunda konuşur musun?",
	"Gizli aşkın kim?","Benim hakkımda neyi sevmiyorsun?","Şu an ne renk iç çamaşır giyiyorsun?",
	"Son attığın mesaj neydi?","İnsanları yanan bir binadan kurtarıyor olsaydınız ve bir kişiyi bu grupdan geride bırakmak zorunda kalırsanız, kim olurdu?",
	"İç çamaşırlarını ne sıklıkla yıkıyorsun?","Hiç kulak kiri tattın mı?",
	"Hiç osurup başka birini suçladın mı?","Hiç terinin tadına baktın mı?",
	"Bu odadaki kim bugüne kadarki en kötü insan olurdu? Neden?",
	"Yeniden doğmuş olsaydın, hangi yüz yılda doğmak isterdin?","Söylediğiniz veya yaptığınız bir şeyi silmek için zamanda geriye gidebilseydiniz, bu hangi yıl olurdu?",
	"Erkek arkadaşın veya kız arkadaşın seni hiç utandırdı mı?","Birdenbire görünmez olsaydın ne yapardın?",
	"Banyoda kaldığınız en uzun süre nedir ve neden bu kadar uzun süre kaldınız?","Şimdiye kadar gördüğüm en garip rüyayı anlat.",
	"Duşta işiyor musun?","Hala yaptığın en çocukça şey nedir?","Hangi çocuk filmini tekrar tekrar izleyebilirsin?",
	"Ayak kokunuz kötü mü?","Saçma takma adların var mı?","Telefonunuzda hangi uygulamada en çok zaman harcıyorsunuz?",
	"Tek bir oturuşta yediğin en çok yemek ne?","Tek başınayken dans ediyor musun?","Karanlıktan korkar mısın?",
	"Bütün gün evdeysen ne yapardın?","Günde kaç öz çekim yapıyorsunuz?","En son ne zaman dişlerini fırçaladın?",
	"En sevdiğin pijamalar neye benziyor?","Hiç yerden bir şey yedin mi?","Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?",
	"Vücudunun hangi bölümünü seviyorsun, hangi kısmından nefret ediyorsun?","Hiç bitlendin mi?",
	"Pantolonunu hiç kestin mi?","Tabağını yalıyor musun?","Kimsenin senin hakkında bilmediği bir şey nedir?",
	"Hiç tabağını yaladın mı?","Dirseğini yalayabilir misin?","Eğer buradaki herkesi yanan bir binadan kurtarmaya çalışıyor olsaydın ve birini geride bırakmak zorunda kalırsan, kimi geride bırakırdın?",
	"Telefonda aradığın son şey neydi?","Bir uygulamayı telefonunuzdan silmek zorunda kalsanız hangisini silerdiniz?","Bir ilişkideki en büyük korkun nedir?",
	"Odanın her bir kişi hakkında bir tane olumlu, bir tane olumsuz şey söyleyin.","Sevmediğin kötü huyun var mı?",
	"Hayatında yaptığın en çılgın şey nedir?","Üç gün boyunca bir adada mahsur kalmış olsaydınız, bu grupdan kimleri seçerdiniz?",
	"Bu odadaki en sinir bozucu kişi kim?","Bu grupdan biriyle evlenmek zorunda kalsan kim olurdu?","En uzun ilişkiniz ne kadar sürdü?",
	"Bir ünlü Instagram’da seni takip etseydi bu ünlünün kim olmasını isterdin?","Instagram’da 5 kişiyi silmek zorunda olsan kimleri silerdin?",
	"Kaç çocuk sahibi olmak istersin?","Hayallerinizdeki kişiyi tarif edin.","Messi mi Ronaldo mu?","Pes mi Fifa mı?",
	"İlk işin neydi?","Üniversite hakkındaki en büyük korkun nedir?","En iyi arkadaşının seninle aynı üniversiteye gitmesini ister misin?",
	"Mevcut erkek arkadaşının ya da kız arkadaşının seninle aynı üniversiteye gitmesini ister misin?","Hayalindeki iş ne?",
	"Hiç bir dersten başarısız oldun mu?","Hiç kopya çektin mi?","Hiç sınıfta uyudun mu?","Sınıfta asla yanında oturmak istemeyeceğin kim?",
	"Derse hiç geç kaldın mı?","Bir öğretmenin önünde yaptığın en utanç verici şey nedir?","Hiç masanın altına sakız attın mı?",
	"Hiç okulda kavga ettin mi?","Bir sınavdan aldığın en kötü puan neydi?","Sınıfta hiç uyuya kaldın mı?","Hiç gözaltına alındın mı?",
	"Eğer görünmez olsaydın hangi derse gizlice girerdin?","En kötü grup hangisidir?","Bu grupdaki sır tutma  konusunda en çok zorlanan kişi kimdir?",
	"Söylediğin en son yalan neydi?","Spor yapar mısın?","Hayatının geri kalanında sadece bir kıyafet giyebilseydin, bu kıyafetin hangi renk olurdu?",
	"Sizce Türkiye’nin eğitim sisteminde yapılması gereken en önemli değişiklik nedir?","Karanlıktan/yükseklikten korkar mısın?",
	"Kendi görünuşünü 1 ile 10 arasında puanla :)","Yaptıgın en yasadışı şey neydi?","Şimdi sana bir evlenme teklifi gelse ve sevmediğin biri olsa, ve bu sana son gelecek evlilik teklifi olsa kabul edermiydin?",
	"Şu anki ruh haline bakarak ne tür film izlersin (aksiyon/dram/bilim kurgu/romantik komedi/biyografi/fantastik)",
	"Kendini en ezik hissettiğin an hangisiydi ?","ilerde çocuğun olursa ne isim koymak istersin?",
	"Unicorun mu olmasını isterdin ejderhan mı?","Kaç sevgilin oldu?","Hayatta unutmadığın biri var mı?",
	"en sevdiğin şarkı?","Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?","En sevdiğin sanatçı kim?",
	"karşı cinste ilk dikkatini çeken ne?","bu yıl hayatında neyi değişmeyi uygun görüyorsun?",
	"Birinin telefonunda gördüğün en tuhaf şey nedir?","Süper kahramanlar gerçekten var olsaydı Dünya nasıl bir yer olurdu?",
	"Hayatın size öğrettiği en önemli ders nedir?","Kültürümüzün en çok sevdiğiniz yanı nedir?","Ailenizin uyguladığı en tuhaf gelenek nedir?",
	"Aileniz dışında, yaşamınız üzerinde en büyük etkisi olan kişi kimdir?","Kadın/Erkek olmanın en kötü ve en iyi yanı nedir?",
	"Beynini bir robota yerleştirebilir ve sonsuza kadar bu şekilde yaşayabilsedin,bunu yapar mıydın?","Evinizde ağırladığın en kötü misafir kimdi ve ne oldu?",
	"İnsanların size ne sormasından bıktınız?","En tuhaf korkunuz nedir?","En sevdiğiniz TV programı hangisidir?","Girdiğiniz en saçma tartışma nedir?",
	"En son söylediğin yalan nedir?", "Biriyle çıkarken yaptığın en utanç verici şey neydi?",
	"Hiç arabanla (varsa) yanlışlıkla bir şeye birine çarptın mı?",
	"Hoşuna gittiğini düşündüğün ama bir türlü açılamadığın biri oldu mu?","En tuhaf takma adın nedir?",
	"Fiziksel olarak sana en acı veren deneyimin ne oldu?","Hangi köprüleri yakmak seni rahatlattı?",
	"Toplu taşıma araçlarında yaptığın en çılgınca şey neydi?","Şişeden bir cin çıksa üç dileğin ne olurdu?","Dünyadaki herhangi birini Türkiye’nin başkanı yapabilseydin bu kim olurdu?",
	"Şimdiye kadar bir başkasına söylediğin en acımasızca şey neydi?","Birini öperken kendini hiç kötü hissettin mi?","Hiçbir sonucu olmayacağını bilsen ne yapmak isterdin?",
	"Bir aynanın önünde yaptığın en çılgınca şey nedir?","Şimdiye kadar başkasına söylediğin en anlamlı şey neydi?",
	"Arkadaşlarınla yapmayı sevdiğin ama sevgilinin önünde asla yapmayacağın şey nedir?","Bu hayatta en çok kimi kıskanıyorsun?",
	"En sevdiğin pijamaların neye benziyor?","Bir buluşmadan kaçmak için hiç hasta numarası yaptın mı?","Çıktığın en yaşlı kişi kim?",
	"Günde kaç tane özçekim yaparsın?","Aşk için her şeyi yaparım ama “bunu” yapmam dediğin şey nedir?","Haftada kaç kez aynı pantolonu giyiyorsun?",
	"Bugün şansın olsa lise aşkınla çıkar mısın?","Vücudunun hangi bölümlerinden gıdıklanıyorsun?",
	"Çeşitli batıl inançların var mı? Varsa onlar neler?","Sevdiğini itiraf etmekten utandığın film hangisidir?","En utan verici kişisel bakım alışkanlığın nedir?","En son ne zaman ve ne için özür diledin?","Sözlü destanlar hakkında ne düşünüyorsun?",
	"Utanç verici kokularınızın çoğu nereden geliyor?","Hiç sevgilini anlatmayı düşündün mü?","Hiç sevgilini biriyle aldattın mı?","Boxer mı yoksa külot mu?","Hiç havuza veya denize işedin mi?","Saçlarını uzatmayı düşünsen ne kadar uzatırdın?","Kimsenin bilmeyeceği garanti olsa kimi öldürmek isterdin?","Başkası için aldığın en ucuz hediye nedir?",
	"Zamanının çoğunu en çok hangi uygulamada harcıyorsun?","Otobüste yaptığın en tuhaf şey nedir?","Hiç toplum içinde çıplak kaldın mı?","Günde ne kadar dedikodu yaparsın?","Çıkmak isteyeceğin en genç kişi kaç yaşında olurdu?","Hiç toplum içindeyken burnunu karıştırdın mı?",
	"Hiç yaşın hakkında yalan söyledin mi?","Telefonundan bir uygulamayı silmek zorunda olsan bu hangisi olurdu?",
	"Gece geç saatte yaptığın en utanç verici şey nedir?","Duş almadan en uzun süre ne kadar durdun?","Hiç sahte kimlik kullandın mı?","Kırmızı halıda beraber yürümek istediğin ünlü isim kim?","Gizli aşkın kim?",
        "Çocuk sahibi olmak istersiniz?",
        "Hakkınızda bilmem gereken utanç verici bir gerçek nedir?",
        "Çocukluktaki lakabın neydi?",
        "En sevdiğiniz yemek nedir?",
        "En sevdiğiniz renkleriniz nedir ve neden?",
        "Hayalindeki meslek ne?",
        "Bir adada 3 gün sıkışıp kalırsan, ne yaparsın?",
        "En sevdiğiniz kişi kimlerdir ve neden?",
        "Tuvalet kağıdınızı ruloya nasıl koyarsınız?",
        "İlk görüşte aşka inanır mısın?",
        "Aşka inanıyor musunuz?",
        "Hayalinizdeki düğün nedir?",
        "Şansınız olursa hangi ülkede yaşamak istersiniz?",
        "En çok neyi hayal ediyorsun?",
        "Şimdiye dek yaşadığınız en garip rüyayı açıklayabilir misiniz?",
        "En büyük pişmanlığın nedir?",
        "Beni seviyor musun",
        "Saçını yıkamadan en uzun ne kadar süre bekledin?",
        "Herhangi bir ünlü ile evlenseydin, kim olurdu?",
        "Kaç tane erkek arkadaşın 0ldu?",
        "Sizden en az 10 yaş büyük bir kişiye hiç aşık oldunuz mu?",
        "Şu an kiminle çıkıyorsun?",
	"Hayalindeki meslek ne?",
	"Tek başınayken dans ediyor musun?",
	"Kıskanılmaktan hoşlanır mısın?",
	"Hiç sevgilini aldatmayı düşündün mü?",
	"beni'i seviyor musun?",
	"Gruba +30 üye ekle",
        "Sevdiğiniz birinin önünde söylediğiniz veya yaptığınız en utanç verici şey nedir?",
        "Vücudunun hangi bölümünü seviyorsun, hangi kısmından nefret"
]

koc = [
    "13 Aralık'ta Yay burcunda gerçekleşecek yeniay ile birlikte hayatınıza yeni insanlar, yeni konular ve yerler dahil olabilir. Özellikle kadın dostlarınız ve kadın iş insanı figürleriyle yapacağınız görüşmeler size kendiniz için yaptığınız planları uygulama fırsatı sunabilir. Kararsız kaldığınız, nasıl bir yol izlemek gerektiğini bilmediğiniz ve olumsuz tecrübeler edindiğiniz bir dönemin ardından hem bu haftaya hem de yeni yıla iyi bir etki bırakmak isteyebilirsiniz. Yaşamakla nefes almak arasındaki farkı daha net görebilirsiniz. Feda ettiğiniz ama karşılığını bulamadığınız alanların sizdeki yerini değiştirebilirsiniz. Hayat felsefenizi bu yönde değiştirdiğinizde yaptığınız işlerin, kurduğunuz arkadaşlıkların da etki yönü değişecektir. Tecrübelerinizi anlatacağınız yazılı veya görsel içerikler, sosyal medya ve yazı işleri, uluslararası platformlar, seyahat planları veya seyahat ederek yapacağınız işler gündeme gelebilir. Artık hazırsınız, sahneye çıkıyorsunuz.",
    "Neptün'ün 6 Aralık'ta Balık burcundaki geri hareketini sonlandırmasıyla, yaz döneminden bu yana kendi içinizde savaşını verdiğiniz her şeyin bir geri dönüşünü alabilirsiniz. Yanılgıya uğradığınız, anlaşılamadığınız, maddi ve manevi kandırılmalarla karşılaştığınız konularda artık nasıl bir tutum sergilemeniz gerektiğini çok iyi biliyorsunuz. Bilginize uygun şekilde hareket etmek sizin kurtarıcınız olacaktır. Doğru olandan vazgeçmemelisiniz. İnsani hırslarınızın ağır basması durumda, eleştirdiğiniz ya da sizi zorlayan kişilerden bir farkınızın kalmayacağını düşünün ve bu konuyu kapatın. Kendinizden başlayarak birilerini suçlu ilan etmekle vedalaşmalısınız. Almanız gereken derslerin hayat boyu devam edeceğini bildiğinizde, karşılaştığınız hiçbir şeyin sizi eskisi gibi yormadığını görebilirsiniz. Yaratıcılığını koyduğunuz, hayallerinizi yaşatmayı planladığınız işler için daha hızlı ve belirgin neticeler almaya başlayabilirsiniz. Neyin peşinden koştuğunuzu bu vesileyle daha net görebilirsiniz. Bu konuda, daha önce çalışma yapmış ya da fikrine güvendiğiniz kişilerle iletişime geçebilirsiniz. Dışa dönük olsa da, sosyal anksiyete yaşadığınız ya da kendinizi geride tutma gereği hissettiğiniz durumları da bu sayede aşmanız mümkün olacaktır. Sağlık, maddi kazanç, ilişkiler hatta iyilik yapma konusunda bile seçimlerinizi, sonrasında üzülmeyeceğiniz düzeyde yapmalısınız. Herkes gibi sizin de bir sınırınız var."
    "13 Aralık'ta Merkür'ün Oğlak burcunda geri hareketine başlamasıyla iş hayatınız, kariyeriniz, duruşunuz ve aldığınız geri dönüşlerle ilgilenebilirsiniz. İnsanlarla nasıl iletişim kurduğunuza, otorite figürleriyle yapacağınız konuşmalara özen göstermeniz gerekebilir. İş veren konumunda iseniz, hem ekibinize hem de ortaklık kurduğunuz kişilere karşı sizin de aynı hassasiyeti göstermeniz gerekebilir. Konuşulmayan konular gündeme gelebilir, ödemelerle ilgili süreçleri değerlendirebilir ve aksama olması halinde uygulamak üzere bir b planı hazırlayabilirsiniz. Bir değişim yapmadan, bir karar vermeden, bir anlaşmaya varmadan önce bunu nasıl bir zeminin üstüne koyduğunuza dikkat etmelisiniz. Gözünüzden bir şey kaçırmak, sonrasında başka fırsatlar kaçırmanıza neden olabilir. Mümkünse bekleyebilir, beklemek mümkün değilse üzerinde daha iyi çalışarak hatayı en aza indirebilirsiniz. Daha önce çalıştığınız işler ya da insanlarla ilgili bazı geri dönüşler gündeme gelebilir. Hakkınızı alabilir ya da bir ortaklık konusunu gündeme getirebilirsiniz. Geçmişte yaşadıklarınızdan dersler çıkararak ilerlemenizde fayda var.",
    "22 Aralık'ta Güneş'in Oğlak burcuna geçişi ile kariyerinizde perde aralanıyor. Daha çok sorumluluk almak isteyeceğiniz, bunları neticelendirebileceğiniz bir döneme giriyorsunuz. İş hayatınızla ilgili pürüzleri daha net görebilir, bazı şeylerin neden yürümediğini daha iyi anlayabilirsiniz. Bu sayede ilerlemeniz kolaylaşacak ve alacağınız verim yükselecektir. Sistemli olmalı, ne yapacağınızı doğru planlamalısınız. Fiziksel olarak aşırı yorulmanın önüne geçebileceğiniz gibi psikolojik açıdan da üzerinizde fazla yük hissetmeyeceksiniz. Atamalar, işleri sonuçlandırma ve büyütme, kendi işini kurma, yönetici pozisyonunu güçlendirme, gelir artışı gibi konular gündeminizde yer bulacaktır. Ailenizin otorite figürleri öne çıkabilir, sizi destekleyebilirler. Başkalarının kurallarına uyum sağlama noktasında sorun yaşayacağınızı hissettiğinizde sakin ve makul olmaya çalışın. Güneş'in geri hareketteki Merkür ile burada kavuşumu ile bazı prensipleri yeniden hatırlamanız gerekebilir. Size başarı getiren, iyi kazanmanızı sağlayan konular ve bu yönde sizi destekleyen insanlarla olan iletişiminiz önem kazanabilir. Gecikmiş ödemeler, zamanında tamamlanmayan işler ve bunların etkileri üzerine düşünebilirsiniz. Yeni bir plan yapmak için eski planlarınıza hakim olmalısınız. Aceleden ve baskıdan kaçının, bunu yapmaya çalışan kişilere de fikirlerinizle yol gösterin.",
    "Chiron'un burcunuzdaki geri hareketini 27 Aralıkta sonlandırmasıyla birlikte bir başlangıca doğru yürüyorsunuz. Bu sadece bir yılın değil, o yıl yapacaklarınızın da başlangıcı olabilir. Yaşadıklarınızdan neler çıkardığınızı, bugüne kadar kendinizde neyi ertelediğinizi ve bunların sizde bıraktığı hisleri düşünün. Kendinizi sevmek, bazı özelliklerinizi kabullenmekle ilgili sorunların kaynağını görebilirsiniz. Olduğu gibi devam ettirdiğiniz her şeyin bir kırılma noktası olduğunu bilerek yaşamalısınız. Bu noktalar size ilişkilerde, iş hayatınızda, fiziksel durumunuzda daha iyiye nasıl ulaşacağınızın yolunu gösterecektir. Dolayısıyla yaşadıklarınızı, onları fırsata çevirecek şekilde değerlendirmelisiniz. Şimdi bunları kullanmanın, dönüştürmenin zamanındasınız. Sizi baskısı ve etkisinde altında bırakan durumlara, insanlara müdahale edebilirsiniz. Adına 'baştan başlamak' diyeceğiniz ilişkileriniz olabilir, bazıları hayatınızdan tamamen çıkabilir. Dış görünüş için verdiğiniz emeğin özgüven, hafiflik ve rahatlık olarak döndüğünü görebilirsiniz. Bu sizin için bir süreç değildi, bunu bir yaşam tarzına dönüştürüyorsunuz.",
    "Yengeç burcunda 27 Aralık'ta gerçekleşecek dolunay, yılın başında aldığınız bazı kararların geldiği son noktayı gösterebilir. Ev ve aile hayatınızı mercek altına alabilirsiniz. Oturduğunuz evle vedalaşabilir, yeni bir düzene geçiş yapma fikirlerinizi netleştirebilirsiniz. Bu durum iş gereği ya da farklı bir sebeple de olsa, duygusal bağ kurduğunuz bir şeylerin neticesi olarak gerçekleşecektir. Dolayısıyla üzüldüğünüz, bu yüzden öfke duyduğunuz anlar yaşayabilirsiniz. Ancak kırıcı olmamaya, direnmemeye, ailenizle/eşinizle çatışmamaya çalışmalısınız. Ev sahibi olmak, evlenmek, farklı bir yaşam tarzı sürmek, eşin ya da aile üyelerinden birinin kararlarına göre hareket etmek gibi konularla karşılaşabilirsiniz. Önünüze çıkan fırsatları değerlendirin. Her şey netlik kazanıyor ancak bunları uygulamak için Merkür retrosunun tamamlanmasını beklemenizde fayda var.",
    "29 Aralık'ta Venüs'ün Yay burcuna geçişi ile kendinize yeni deneyimler ve seçenekler bulabilirsiniz. İşinizi geliştirmek, bir hobi edinmek, zamanı değerlendirmek için eğitimlere başvurabilir ya da bunların düzenlendiği yerlere seyahat edebilirsiniz. Hareketli olduğu kadar verimli bir süreç olması için, seçtiğiniz konuyu derinlemesine ele almalı ve sıkılmayacağınız şekilde planlamalısınız. Bu yönünüz size farklı kapılar açabilir. Ticari konular, uluslararası alanlar, sosyal mecralar ve yazılı işler odağınızda olabilir. Özellikle internette geçirdiğiniz zamanı kazanca dönüştüreceğiniz çalışmalar yapabilirsiniz. E ticaret, danışmanlıklar, sesinizi ya da yazı becerinizi kullanacağınız alanlarda şansınız yüksek olabilir. Ancak bunların hukuki süreçlerini ve gerekliliklerini takip etmeyi da ihmal etmemelisiniz. Uzun süredir görüşmediğiniz kişilerle bir araya gelebilir, yer değişikliği yapabilirsiniz. Pasaport ve vize işlemlerinizi gözden geçirmenizde fayda var."
]

kova = [
    "Bir başlangıç yapmadan önce çok iyi hazırlanmanız gereken bir süreçtesiniz. Kayıplar yaşadığınızı ya da zaman kaybettiğinizi düşünmeyin. Bu konuda çevrenizden, iş ortamınızdan veya ailenizden bazı destekler alabilirsiniz. Özellikle duygusal ilişkilerden, kadın /anne figürlerinden gelecek bu destekler özgüveninizi arttıracaktır. İnsanların sizin hakkınızda doğru düşüncelere sahip olması için gereksiz gizem ve mesafeden kaçınmalısınız.",
    "6 Aralık'ta Neptün'ün Balık burcunda ileri hareketine başlaması parasal konularda yaşadığınız karışıklık, belirsizlik gibi konuları sonlandırabilir. Bu konuda hızlı bir akışa ihtiyaç duyuyorsanız önünüze set çeken durumlara daha fazla kayıtsız kalmamalısınız. Sorumluluklarınızı, bunun sınırlarını ve doğru kaynaklarla, doğru insanlarla ilerlemeniz gerektiğini unutmayın. Hayatınıza uzaktan, farklı bir gözle bakmak bu ilerleyişi kolaylaştırabilir. Ekonomik beklentileriniz, iş hayatınız ve buna bağlı olan yaşam düzeninizle ilgili pürüzleri düzeltebilirsiniz. Kendinize yüklenmeyin, bir hatanız ya da eksiğiniz olduğunda daha yapıcı olmaya çalışın. Bu öğretileri kalıcı hale getirmeyi başarırsanız işlerin daha kolay ilerlediğini görebilirsiniz. Aklınızdan bu işaretlerinin çıkması, hayatın manevi ve duygusal konularına daha rahat eğilmenizi ve bunları daha iyi anlayıp yaşamanızı sağlayacaktır.",
    "13 Aralık'taki Yay yeniayı ile çevrenizi, beklentilerinizi ve ilişkilerinizi yeniliyorsunuz. Yeni misyonlar edinmek, farklı konularda çalışmak, bulunduğunuz konumu değiştirmek isteyebilirsiniz. Bir eğitim ya da proje amacıyla kısa süreli yer değişiklikleri, yurtdışı trafiği gündeme gelebilir. Kendinizi ait hissettiğiniz yeri bulma konusunda soru işaretlerinize yanıt bulabilirsiniz. Bu da size başta istediğiniz misyon ve çevre için destek sunacaktır. Arkadaşlarınızdan öğrenecekleriniz, onlarla beraber hareket edeceğiniz konular, birbirinizi destekleyeceğiniz ya da birbirinizden etkileneceğiniz gelişmeler söz konusu olabilir. Kimin ve neyin etkisinde kaldığınıza, insanların sizi nasıl bir arkadaş olarak gördüğüne önem verebilirsiniz. Bu size, bazı mesafeleri kapatmak ya da ilişkileri sonlandırmak için cesaret verebilir. Ekonomik açıdan yatırım planları yapabilir, işinizi daha büyük bir organizasyona dönüştürebilir, yurt içinde ve yurt dışında sesinizi daha çok duyuracağınız platformlarda yer alabilirsiniz. Dil bilmenin avantajlarını yakalayabilir, bu konudaki eksiklerinizi kapatacak çalışmalar yapabilirsiniz. Enerjinizin, motivasyonunuzun dikkatleri çekeceği bir dönemdesiniz. Duygusal etkileşimlere açık olabilirsiniz.",
    "Merkür'ün 13 Aralık itibariyle Oğlak burcunda geri hareketine başlamasıyla beraber geçmişten bugüne gelen süreçleri düşünebilirsiniz. Bu ertelenmiş ya da zaman bulunamamış bir süreç olabilir. Şimdi zaman ayırmaya, sorunları çözmeye odaklanın ve bir daha aynı döngünün tekrarlanmaması için kesin çizgiler çizin. Hayattan beklentilerinizin, iş planlarınızın vardığı noktayı görmelisiniz. Şartları zorlayan, ütopik sayılabilecek ve anlaşılması zor gündemleriniz varsa bunlara ket vurulabilir, aksaklıklar yaşayabilirsiniz. Standartların dışına çıkmak istediğiniz için yanlış seçimlerin sonuçlarıyla yüzleşmeniz gerekebilir. Bu da bazı planları revize etmeye, durdurmaya, daha iyi bir versiyonunu hazırlamaya zemin oluşturabilir. Bazı konuların ya da insanların sizin düşündüğünüz gibi olmadığını görebilirsiniz. İnsanlara verdiğiniz değeri, bu yüzden yaptığınız harcamaları, verdiğiniz tavizleri gözden geçirmelisiniz. Bir şeyleri ağırdan alarak ilerlemenizde fayda var. Özel hayatınız, maddi gündemleriniz, işiniz, sağlığınız kısaca hayatınızla ilgili önemli noktaları paylaştığınız kişilere dikkat etmelisiniz. Kendi sırlarınızı saklamayı, rahatsızlıklarınızı ise uygun bir dille ifade etmeyi rutinleştirin.",
    "22 Aralık itibariyle Güneş'in Oğlak burcunda hareket edecek olmasıyla hayatınızda neyin kalıp kalmayacağını netleştirebilirsiniz. Bir başlangıç kararından ziyade artık son vermek istediğiniz konular ağır basabilir. Arka planda kalmayıp hayatınıza etki eden, sizi baskılayan ya da emeklerinizi çürüten konuların ve insanların farkına varabilirsiniz. Şüphelenseniz de kesin olmadığı için bir hamle yapamadığınız her şeyle karşılaşabilirsiniz. Başta can sıkıcı, düzen bozucu gibi görünse de bu aşamada fark etmiş olmak sizin kurtarıcınız olacaktır. Biraz geri çekilebilir, tek başınıza çalışabilir, fikirlerinizi kendi araştırmalarınızla derinleştirebilirsiniz. Özellikle parasal yatırımlar ve işler konusunda güveneceğiniz kişileri iyi seçmelisiniz. Bu yüzden önce siz ne istediğinizden, neye ihtiyaç duyduğunuzdan emin olmalısınız. Bunu sağladığınızda, net olduğunuzda insanların görüş adı altındaki baskı ve dayatmalarını püskürtebilirsiniz. Bu dönemi tamamen yalnız kalmakla geçirmek yerine, kendinize has alanlarınıza kimleri dahil edebileceğinizi düşünmekle de geçirebilirsiniz. İnsanlardan ve dış dünyadan kopmamalı, sadece bu yöndeki seçimlerinizde daha akılcı olmaya çalışmalısınız. Rahatsızlık duyduğunuz her şeyi değiştirebilir, gündelik yaşantınız için yeni bir düzen belirleyebilirsiniz. Güneş'in geri hareketteki Merkür ile kavuşumu bu konuda sizi destekleyebilir. muhasebe yapmak, motivasyonunuzu değerlendirmek, istenmeyen sonuçlar doğuran durumları tespit etmek gerekebilir. Bundan kaçmamalı, karşılaştığınız sorunlara duyarsız olmamalısınız. Bir karar vermek, maddi ya da manevi bir yatırım yapmak, yardım faaliyetine dahil olmak gibi konularda işlerin arka planını iyi araştırın.",
    "27 Aralık'ta Chiron'un Koç burcunda ileri harekete geçmesiyle herkese anlattıklarınızın kendi hayatınızda da nasıl işe yaramaya başladığını görebilirsiniz. Retro döneminde bununla ilgili çalışmalara kafa yorduysanız şimdi ekmeğini yiyebilirsiniz. Yormadıysanız, kaldığınız yerden ama daha güçlü bir şekilde devam etme şansınız da olacaktır. Yeter ki, artık istemeyi bilin ve bundan çekinmeyin. Anlaşılmama endişesi sizi yalnızlaştırabilir. Bu yüzden susmayı, hislerinizi paylaşmayı, emeğinizi saklamayı bir yol olarak görmemelisiniz. Bunları yaptığınız için kaçırdığınız iş fırsatları maddi olarak da olumsuz etkilenmenize neden olabilir. Yeni işler ve arayışlar gündeminize gelebilir, teklifleri ve size verilen fikirleri değerlendirmeye alın. Emin olduğunuz, kendinizi geliştirdiğiniz konularda öne çıkmalısınız. Sosyal mecralar, arkadaş veya iş grupları bu anlamda size destek olabilir. Alacağınız geri dönüşler kendinize neler katacağınıza dair fikirler verebilir. Bunu öngörebilmek için başkasına yaptığınız geri dönüşlerin nasıl işe yaradığına bakabilir, bu kişilerle görüşebilirsiniz. Ehliyet ya da araç almak, trafik ve ulaşımla ilgili konularda aksaklıkları aşmak için iyi bir zaman olabilir. Merkür'ün geri hareketini devam ettirdiği bu günleri sadece araştırma yapmak ve iyi düşünmek için kullanmanız sonrası için daha iyi seçimler yapmanıza olanak tanıyacaktır.",
    "27 Aralık'ta Yengeç burcunda gerçekleşecek dolunay ile iş hayatınız, gündelik hayatınızla ilgili düzenlemeler gündeme gelebilir. Yaptığınız işlerin neticelerini görebilir, karşılığını almaya başlayabilirsiniz. Burada nasıl bir tutum sergilediğiniz, işinize ne kadar sahip çıktığınız, hayatınız için ne yönde emek verdiğiniz önemli olacaktır. Duygusal açıdan bağımlılık yaratan, inada bindiren ya da takıntıya dönüşen durumlardan sıyrılmalısınız. Bunların size nasıl etki ettiğini daha görebilirsiniz. Memnun olmadığınız işler, alanlar konusunda ısrarcı olmamalısınız. Bu size yeni alternatiflerin ve düzenlerin vaktinin geldiğinin bir işareti olabilir. Sağlığınızı, alışkanlıklarınızı düşünün. Geçmişteki bir rahatsızlığınızın gündeme gelmesi, yeniden ilgilenmek durumunda olmak sizi yorabilir. Bunu aşmanın yollarından biri de, sizi bu noktaya neyin getirdiğini bilmek ve onu ortadan kaldırmaktır. Doktorlarınızın, hayatınızı paylaştığınızın kişilerin önerilerine kulak vermenizde fayda var. Yılın başında uyguladığınız ve sonuç aldığınız yöntemlere yeniden dönüş yapabilir, devam ediyorsanız da geliştirmeye çalışabilirsiniz.",
    "29 Aralık'ta Venüs'ün Yay burcuna geçişi size yeni hayaller kurdurtabilir. Alanınızı genişletme fikriniz her zaman olsa da bu kez uygulama alanlarınız da genişleyecektir. Faydalı ve keyifli ilişkiler kurmaya odaklanabilirsiniz. Birden fazla ortama dahil olabilir, birçok insanla tanışabilir ve yapmak istedikleriniz için imkanlar bulabilirsiniz. Bu durum dikkat ve konsantrasyon dağınıklığı oluşturabilir, her şeye aynı anda sahip olma dürtüsü uyandırabilir. Çevrenizin ilgisini bu olumsuz etkiyle üzerinize çekmemek için abartıya kaçmamakta fayda var. Tarzınıza, seçimlerinize özen gösterin. Duygusal etkileşimlere açık olduğunuz bir dönemdesiniz."
]

balık = [
    "Bir süredir burcunuzda geri hareket eden Neptün, 6 Aralık itibariyle ileri hareketine geçerek taşları yerine oturtmanıza yardımcı olacaktır. Nelerle yüzleştiğinizi, nelerden kaçtığınızı, sınırlarınızın nereye vardığını yeterince gördüğünüz bir süreçten çıkıyorsunuz. Kendinize ve hayatınıza dair sorumluluklarınızı aksatmayacak bir plan içinde olmalısınız. İhtiyaçlarınızı dinleyin, gerektiği noktada uzman desteği alın. Bu süreç size kime güvenmemeniz gerektiğini açık bir şekilde gösterdiyse bu konunun artık hata kaldırmayacağını da kabullenmelisiniz. Geri çekildiğinizde kimin sizi öne çekmeye çalıştığını, öne çıktığınızda da kimin bundan rahatsız olduğunu görerek ilişkilerinizi düzenleyebilirsiniz. Fiziksel olarak da, kendinizde ihmal ettiğiniz konular varsa bunları tamamlamak adına iyi bir süreç olabilir. Yorgun, dalgın, isteksiz hissettiren yeme içme, hareket ve uyku gibi alışkanlıklarınızı düzene sokmanız kolaylaşacaktır. Ayağınızı bastığınız yerin farkına varıyorsunuz, bunu unutmayın.",
    "13 Aralık'ta Yay burcunda gerçekleşecek yeniay ile beraber iş hayatınıza yeni güncellemeler gelebilir. Beklediğiniz haberleri, hak ettiğiniz atama ve maaş gelişmeleri gündeminizde yer bulabilir. Daha özgür çalışabileceğiniz, motivasyonunuzun artacağı bir dönemdesiniz. Bu sadece kendi işini yapmakla değil, bağlı olduğunuz kişilerle de daha iyi bir iletişim kurmanız ve anlaşmanız da mümkün olacaktır. Bir şeylerin artık daha farklı olması gerektiğini görüyorsunuz. Bunun peşinden gidin ve kararlılığınızı sürdürün. Uzun vadeli, herkese hitap eden bir şeyler yapmak için bunun önemli bir madde olduğunu da unutmayın. Kendinize, becerilerinize, yapabileceklerinize inanmalısınız. Siz inandığınızda size inanan insanları da rahatça görebileceksiniz. Aslında yalnız olmadığınızı, size böyle hissettiren ortamlarda kaldığınızı fark edeceksiniz bu da ihtiyaç duyduğunuz değişimin kapısını aralayacaktır. Önemli bir viraj gibi görebilirsiniz ancak dikkatli, makul ve sorumluluk sahibi olduğunuzda bunu halledebilirsiniz. Tutumlarınızı kontrol edin, size hata yaptıran davranışlarınızı değiştirmeye çalışın. Yeni yerler göreceğiniz işler yapabilir, evlilik ya da ortaklık gibi konularla ilgilenebilirsiniz. Yurt dışına açılma planlarınızı detaylandırmak için iyi bir dönem olabilir.",
    "13 Aralık'ta Merkür'ün Oğlak burcundaki geri hareketinin başlaması iş arkadaşlığından doğan, resmi bir noktada olan arkadaşlıkları değerlendirmeye başlayabilirsiniz. Bu insanlara hayatınızda ne kadar yer verdiğinizi, onlarla neler paylaştığınızı doğru ayırt etmelisiniz. Dedikodu, söylenti, asılsız konular, ödenmeyen borçlarla muhatap olabilirsiniz. Bu süreç içerisinde güven vermeyen insanlara, gelecek vaat etmeyen işlere ödeme yapmamaya, bütçe ayırmanız gereken konular üzerinde de dikkatli çalışmaya özen göstermelisiniz. Bir geri dönüşünün olmayacağını bildiğiniz her şey sizi zarara uğratabilir. İnsanların gerçek niyetlerini görme konusunda önünüze bazı fırsatlar gelebilir, bunları geri çevirmeyin. Önyargı ve tedirginlik hata yapmanıza sebep olabilir, bu dürtüleri kontrollü bir şekilde yaşamaya ve karşınızdaki kişileri doğru anlamaya çalışmalısınız. Yeni bir işe başlamak, organizasyonlara dahil olmak, borsa ve yatırım kanallarıyla ilgilenmek isteseniz de bunları şimdilik askıya almanızda fayda var. Böyle zamanlarda mantığınız en yakın arkadaşınız olmalıdır.",
    "22 Aralık'ta Güneş Oğlak burcuna geçiyor ve sizi kabuğunuzdan çıkarıyor. Yalnızlıktan şikayet edip bunun için hiçbir şey yapmamak olmaz. Kafa yapınıza, düşüncelerinize, tarzınıza uygun insanlarla karşılaşabilirsiniz. Bunun için de yeni yerlere gidebilir, yeni işler alabilirsiniz. Her şey bir iş gibi başlasa da bunun devamını ne şekilde getireceğinizin kararını siz vereceksiniz. Sevdiğiniz, güven hissettiren kişilerle bir arada olduğunuzda hayatın daha yaşanılır ve anlamlı olduğunu görebilirsiniz. Bu durum size kurduğunuz yanlış ilişkileri, insanlar hakkındaki olumsuz düşünceleri ya da sizinle ilgili çıkarımları daha net gösterebilir. Sosyal sorumluluk projeleri, bağış gerektiren işler gündeminize gelebilir. Maddi ve manevi birikiminizle bir şeyler yapmak isteyebilir ve çevrenize de bu konuda öncülük edebilirsiniz. Hassasiyet gösterdiğiniz alanlarda yapacaklarınız ses getirebilir. Siz bunu kendi çıkarınız için yapmasanız da karşılığını alabilirsiniz. Duygusal, ticari ve sosyal tekliflere açık olun. Güneş'in geri hareketteki Merkür ile kavuşumu, bu teklifler ve gelişmeler karşısında daha ağırkanlı hareket etmenizi hatırlatabilir. Şans verin ama zamanla anlamaya çalışın, imzalı işleri, parasal konuları aceleye getirmemeye çalışın. Bunu yaparak temkinli olmak isterken kayıplar yaşamanızın önüne geçeceksiniz. Gerçeklerin önemini fark ediyorsunuz.",
    "27 Aralık'ta Chiron'un Koç burcunda ileri hareketine başlamasıyla içinizde taşıdıklarınızın bir yüke nasıl dönüşmeyeceğini daha iyi anlayabilirsiniz. Kendinizi iyileştirmeye gönüllü olmayı deneyimleyeceksiniz. Her zaman bir 'ileri' tuşunuzun olması gerektiğini gösteren konular yaşadınız. Düşündüğünüz, hayal ettiğiniz, beklediğiniz gibi sonuçlanmayan hiçbir şeye geçmişteki tepkileri vermemelisiniz. Özgüveninizden, yapabileceklerinizden, başkalarına sunup işe yarayan fikirlerinizden şüphe duymayın. Yeni hedefler üzerinde durabilir, mevcut çalışmalarınızı geliştirebilirsiniz. Toplumla beraber hareket edeceğiniz, yardım ya da farkındalık konularına öncülük edebileceğiniz gündemleriniz olabilir. Bir adım attığınızda bunun devamının geleceğini unutmayın.",
    "27 Aralık'ta Yengeç burcunda gerçekleşecek dolunay odağınızı mutlu olduğunuz yerlere ve insanlara çevirebilir. Sevdiğiniz insanlar, aileniz ve çocuklarınızla vakit geçirebilirsiniz. Sizi bunlardan alıkoyan konuların farkına varacağınız için artık arada kalmak, seçim yapmak durumunda değilsiniz. Daha özgüvenli, hissettiklerinin arkasında duran bir yapıya kavuşuyorsunuz. Aile olmak, aileyle hareket edeceğiniz işler yapmak ya da onlardan destek görmek gibi konularda şansınız yüksek olabilir. Yarım bıraktığınız hayalleriniz, işleriniz, eğitimleriniz, zaman ayıramadığınız etkinlik ve hobileriniz için şimdi yeni bir planlama yapabilirsiniz.",
    "29 Aralık'ta Venüs'ün Yay burcuna geçişi iş hayatınızla ilgili beklentilerinizi gerçekleştirerek size bir yeni yıl hediyesi verebilir. Ancak siz de buna uyum sağlamalı, kendinizi göstermelisiniz. İşinizi kurmak, sorumluluk almak, yeni hedefler geliştirmek için iyi bir dönem olabilir. Merkür'ün Yay burcunda gerilemeye devam ettiğini unutmadan bu dönemi iyi bir hazırlıkla, araştırmayla geçirebilirsiniz. Hakkınız olan size geri dönecektir, siz durmanız gereken yeri şaşırmayın ve orada kalmaya devam edin. Hukuksal konular, tazminat, sendika işlemleri gibi konulardan bazı geri dönüşler alabilirsiniz. Ailenizin, yakın çevrenizin desteğini alabileceğiniz konular gündeme gelebilir. Özellikle biriyle tanışma, ilişki ve evlilik gibi kararlar almak noktasında bu desteği daha fazla hissedebilirsiniz."
]

boga = [
    "6 Aralık'ta Neptün'ün Balık burcunda ileri hareketine geçmesiyle geleceğiniz ve bugünün arasında yaptığınız muhasebeyi kapatabilirsiniz. Yanlış arkadaşlıklar kurduğunuzu ya da yanlış bir arkadaş olduğunuzu gördüğünüzde buna kayıtsız kalmamakla alacağınız karşılığı güçlendirdiniz. Kendinizi yalnız hissetmenize neden olan seçimlerden uzaklaşıyorsunuz. Bunun bir kayıp olmadığını, bu hafta itibariyle ve sonrasında hayatınıza girecek doğru, nitelikli, iyi niyetli insanlarla daha iyi anlayacaksınız. Niş bir alan belirlemek, bununla ilgili çalışma ve araştırmalar yapmak sizi sadece bilgi ve donanım açısından desteklemeyecektir. Aynı zamanda sizinle benzer düşüncede olan insanları ve ortamları bulmanızı da sağlayacaktır. Bu anlamda, kendinizle ya da çevrenizle olan inatlaşmalarınızı, gereksiz kurgu ve takıntılarınızı bırakmalısınız. Her şey orada başlayacak. Gerçek olamayacak kadar güzel şeyler istemenin, oldukça gerçek nedenleri vardır. Kendinizi, zamanınızı ve imkanlarınızı buna adamalısınız. Sosyal ve ticari açıdan yeni kaynaklar edinmeli, mevcut çalışmalarınızı yoğunlaştırmalısınız. Üzerinde çalıştığınız projeler, yeni işler ve teklifler konusunda şanslısınız. Geri planda durmayın ve bir şeylerin size gelmesini beklemeyin.",
    "13 Aralık'ta Yay burcunda gerçekleşecek yeniay ile beraber ekonomik konularda bir toparlanma yaşayabilirsiniz. Kaynaklarınızı doğru yönetemediğiniz durumların yarattığı pürüzler, size yeni bir yol haritası belirlemek için fırsat tanıyabilir. Masraflarınız, ödemeleriniz kadar gelirinizin de artışa geçmesi önemli olacaktır. Bu yüzden üzerinde uğraştığınız işi geliştirmek, büyütmek, farklı alanlarda yer almak adına daha büyük düşünmelisiniz. Yeni bir vizyon ve hedef belirleyin. Bunun için gereken donanıma sahip olmak adına emek verin. Destekler alabilirsiniz ancak bunun için öncelikle sizin düğmeye basmanız gerekecektir. İşleri ya da gündeminizde olan konuları zamana yaymak sizin için sorun ya da aksamalar oluşturabilir. Kendinize hem fiziksel hem de mental açıdan iyi bakmalı, bulunduğunuz koşulların farkında olarak ilerlemelisiniz.",
    "Oğlak burcundaki Merkür'ün 13 Aralık'ta geri hareketine başlayacak olması bazı insanlarla aranıza mesafe koyabilir. Uzakta olan, sık görüşmediğiniz ya da iyi ilişkilerinizin olmadığı kişilerle yapacağınız konuşmalara dikkat etmenizde fayda var. Bitireceğiniz, hayatınızdan uğurlayacağınız bir şeyler olsa da retro bitiminde bunların bir faturasıyla karşılaşmamak adına ne yaptığınızdan, ne söylediğinizden emin olmalısınız. Bakış açınızı bu yönde geliştirmeyi deneyin. Parasal konulardaki şansınızı yükseltmek adına yeni çalışmalar yapmak isteyebilirsiniz. Özellikle sosyal medya alanına yönelmek, buradaki faaliyetleri incelemek ilginizi çekebilir. Oyunu kuralına göre oynadığınız sürece bir sorun olmayacaktır. Kendinizi bu kurallara adapte etmeye çalışın, aceleci olmayın. Her şeyin zamanla ve emekle ilgili olduğunu unutmadan ilerlediğinizde yaptığınız her işin, aldığınız her eğitimin bir anlamı olduğunu görebilirsiniz. Bu süreçte yapacaklarınız konusunda özenli ve dikkatli olmalı, zamanı ve maddi kaynaklarınızı dikkatli kullanmalısınız. Farkında olmadığınız, üzerinde durmadığınız her detay size bir aksama getirebilir. Özellikle bilet işlemleri, başvurular, yazılı işler ve bunları yürüttüğünüz cihazlarınız konusunda gerekli tedbiri alarak ilerlemenizde fayda var.",
    "22 Aralık'ta Güneş'in Oğlak burcuna geçişi ile beraber inanmak ve üzerine inşa etmek kavramlarını düşünebilirsiniz. Neye dokunduysanız istediğiniz etkiyi vermeyen her şeyden sıyrılarak asıl ihtiyaçlarınızı fark ediyorsunuz. Kendinizi geliştirmeye, yarım kalan eğitimlerinizi tamamlamaya, kazanç getirici faaliyetlerinizi ilerletmeye çalışmalısınız. Hayata karşı bir çabanızın olması sizi her zaman kazançlı çıkarır. Bu sayede istediğiniz standartlara erişebilirsiniz. Hırsınıza, tutkularınıza ve hayal kırıklıklarınızın getirdiği öfkeye kapılmayın. Elle tutulur olmayan, bir yere varmayan hiçbir şey için kendi yolunuzdan sapmamalısınız. Bunu deneyimleyeceğiniz konular, haberler, insanlar gündeminize gelebilir. Farklı görüşlere ve kurallara açık olun. Güven duygunuzu geliştirmek, kendinizi iyi hissedeceğiniz yeni yerler keşfetmek adına önemli bir dönemdesiniz. Taşınma, bulunduğunuz yerden daha uzak bir yere seyahat isteği ya da gerekliliği söz konusu olabilir. Resmi işlemlerinizi tamamlamaya gayret gösterin. Güneş'in geri hareketteki Merkür ile kavuşumu bu gayretin önemini ortaya çıkarabilir. Maddi açıdan güvencede olmak isteyebilir, harcamalarınızı daha dengeli tutmaya çalışabilirsiniz. Yatırım, seyahat, eğitim, iş gibi konulardaki ödemelerinizi ve işlerinizi aceleye getirmeden tamamlamanızda fayda var. Sözleriniz, ortaya sunduğunuz iş ve ürünleriniz çokça dikkat çekebilir. Bu dikkati iyi yönde çekmek zorlayıcı olsa da zoru başarmak adına da fırsatlarınız olacaktır. Bu fırsatları da yaşadığınız sorunların arasında bulabilirsiniz. Dikkatli bakmayı deneyin. Hukuki konularda beklentilerinize göre sonuç alamayabilir, zaman kaybı yaşayabilirsiniz. Her şeyin usulüne uygun olup olmadığından emin olun.",
    "27 Aralık'ta Chiron'un Koç burcunda ileri hareketine başlamasıyla yeni yıla biraz nefes alarak giriyorsunuz. Kendinizin farkında olduğunuz bir dönemi sonlandırdınız. Şimdi bu fark ettiklerinizi unutmadan bir hayat sürmelisiniz. Katı, zorlayıcı ve sabit düşüncelerinizin dışına çıkmanın korkutucu bir tarafı olmadığını görebilirsiniz. Bunu sizden gizlenen ya da kendinizden gizlediğiniz konuların gerçek yüzünü görerek fark etmiş olabilirsiniz. İçe dönük zamanlarınızı daha hareketli, verimli, üretken geçirebilirsiniz. Planlarınızı yürürlüğe koyabilir, başka insanların tecrübelerinden faydalanabilirsiniz. Baş edemediğiniz, çözüm bulamadığınız durumlarda bu tecrübeler size rehberlik edebilir. Alışkanlıklarınızın dışına çıkmaktan daha az korkuyorsunuz, bunun yerini alan cesaretle hayatınıza yeni bir düzen getirebilirsiniz. Rahatsızlıklarınızı, zaman yönetimine dair sorunlarınızı aşabilirsiniz. Her manada iyileşiyorsunuz.",
    "27 Aralık'ta Yengeç burcuna gerçekleşecek dolunay ile artık kapanan defterlere değil açılacak olanlara odaklanmayı öğreniyorsunuz. Üzerinde uğraştığınız konuları neticelendirebilir, eğitimlerinizi tamamlayabilir, hangi alanlarda uzmanlaşacağınızı seçebilirsiniz. Emek verip karşınıza geçip seyredeceğiniz bir süreç olabilir. Bu sadece bir işin, bir planın değil bir arkadaşlığın seyredilmesi şeklinde de yaşanabilir. Fedakarlık yaptığınız, sizin kurtarıcı olduğunuz bazı arkadaşlıkların artık son bulması gerekebilir. Bir süre görüşmemeyi, eskisi ilgilenmemeyi tercih ettiğiniz arkadaşlıklarınızın üzerinde bıraktığı etkiyi daha net görebilirsiniz. Manipüle edildiğiniz, toksikleştiğini düşündüğünüz konuları sonlandırıyorsunuz. Zamanınızı neye harcayacağınıza dair yeni kararlar alabilirsiniz. Resmi işlemleriniz sonuçlanabilir, aile dostlarınızdan destekler göreceğiniz gelişmeler söz konusu olabilir.    ",
    "29 Aralık'ta yönetici gezegeniniz Venüs'ün Yay burcuna geçişi ile beraber parasal konularda şansınız dönmeye başlıyor. Aksaklık yaşadığınız, beklemede kalan, üzerinde çokça durmanız gereken konuların geri dönüşlerini alabilirsiniz. Ek iş, hukuki konular, miras gibi alanlardan alacaklarınız olabilir. Bunları büyütmenin, devamlı hale getirmenin yollarını aramalısınız. Her zaman şanslı fırsatlar bulabilirsiniz ama her bunları uygulayacak kadar bu şansı kullanamayabilirsiniz. Şimdi hazırken değerlendirin, ertelemeyin. Hayatınızda maddi ve manevi açıkların kapanması, yaşadığınız zorlu psikolojik sorunları da sonlandırabilir. Kimseye belli etmeden kendi çabalarınızla çözmeye çalıştığınız durumlarda destek isteyebilirsiniz, gizlemenin ya da bastırmanın iyi bir seçenek olmadığını kabullenin. İyimser olun. Bu his, tehlikeleri önlemez ya da etkisiz hale getirmez ama sizi ne kadar, ne yönde etkileyeceğini bilmenize yardımcı olur; bu inancı oturtmaya çalışın."
]

ikizler = [
    "Neptün'ün 6 Aralık'ta Balık burcunda ileri hareketine başlamasıyla kariyerinizle ilgili beklenti ve hedeflerinizi değiştirebilirsiniz. Sizi yanılgıya ya da olmayacak hayallere sürükleyen durumlardan uzaklaşmalısınız. Hiçbir fayda göremediğiniz, karşılık alamadığınız yerlerde zamanınızı harcamamalısınız. Kendinizi yetiştireceğiniz yeni alanlar bulmanız gerekebilir, mevcut çalışmalarınızı derinleştirebilirsiniz. Bu konuda ipleri elinize almanız, hiçbir şeyin boşuna olmadığını anlamanıza yardımcı olacaktır. Retro döneminde başlattığınız işler söz konusu olduysa ve bu süreci her zamankinden daha dikkatli, gerçekçi geçirdiyseniz bundan sonra karşılaşacaklarınızı avantaja dönüştürebilirsiniz. Çünkü hızlı ve bereketli bir döneme giriyorsunuz, bundan sonra olacakları doğru anlamak ve yönetmek önemli olacaktır. Ekonomik koşullarda ödemeleriniz hızlanabilir, beklentileriniz karşılanabilir. Bu rahatlamanın kısa vadede kalmaması için, edindiğiniz tecrübelere güvenmeli ve bunları kullanmalısınız. Ev, taşınma, aile gibi konularda bazı belirsizlikler söz konusuysa bunları da çözüme kavuşturuyorsunuz. İhtiyaçlarınıza göre hareket etmenin önemli ve gerekli olduğunu unutmayın.",
    "13 Aralık'ta Yay burcunda gerçekleşecek yeniay ile yeni yılın size şimdiden göz kırptığını görebilirsiniz. Davranışlarınız, beklentileriniz, istekleriniz ve bunların insanlarda bıraktığı etkiler konusunda yenilikler yapabilirsiniz. Artık hayattan ne istediğini bilen ve buna göre hareket eden biri olduğunuzu fark edeceksiniz. Anlamadığınız durumlarda resti çekmek ya da kaçmak yerine kalıp mücadele etmenin, yapma cesareti göstermenin önemine dikkat çekebilirsiniz. Karşınızdaki insanın düşüncelerini, isteklerini anlamaya başladığınızda bazı şeylerin artık bir sorun niteliği taşımadığını görebilirsiniz. Önemli kararlar alabilirsiniz. Duygusal ve ticari ortaklıklarınızı ileriye taşıyabilirsiniz. Bunun getireceği heyecanı doğru yönetemediğinizde abartılı tepkiler, öfke patlamaları ve kafa karışıklığı gibi durumlar doğabilir. Yapıcı olmaya çalışarak bunu alt edebilirsiniz. Bunu başardığınızda, sizinle ilgili iyi düşünceleri olmayan kişilerle olan mücadelenizi de kazanabilirsiniz. Hukuki konular netleşebilir, anlaşmazlıkları sonlandırabilirsiniz. Her şeyin bir tecrübe olduğu ve bu tecrübelerle kendinizi geliştirip ağınızı büyüttüğünüzü görmek, sizi yürekledirecektir.",
    "Yönetici gezegeniniz Merkür'ün bu yılki son retrosu 13 Aralık itibariyle Oğlak burcunda başlıyor. Fikir ayrılıkları, harcama dengeleri, ailevi sorunlar gündeminizde sıkça yer bulabilir. Ödemelerinizi tamamlayarak, elinize kesin sonuçlar geçmeden hareket etmeyerek bu dönemin etkilerini en aza indirebilirsiniz. Her şey sizinle ilgili olmayabilir ya da kontrol altında tutamayabilirsiniz. Bu gibi durumlarda olanları ve bunlara konu olan insanları gözlemleyin, olayları iyi ve doğru anlamayı çalışın. Aksi halde, sizinle ilgili olmasa bile konulara fazlaca kafa yorduğunuz için fiziksel ve psikolojik birtakım rahatsızlıklarla karşılaşabilirsiniz. Sağlığınızı ve bedeninizi tehlikeye atmamak adına kontrollerinizi yaptırabilir, uzman görüşüyle ilerlemeye devam edebilirsiniz. Ek iş ve ek gelir faaliyetlerinde kiminle ne iş yaptığınıza, hangi ortamlarda bulunduğunuza dikkat etmenizde fayda var.",
    "22 Aralık'ta Güneş'in Oğlak burcuna geçişi ile beraber çevrenizin ya da ailenizin desteği ile elde ettiğiniz imkanlara daha çok eğilebilirsiniz. Bir sorumluluk alma, işi tamamlama ve hayatın gerçekleriyle ilgili olma konusu sizin için ağır basabilir. Özellikle ekonomik konularda yaşadığınız sorunların çözümü için bunu yapmanız gerektiğini fark ediyorsunuz. Ciddi, farkında ve somut verilere göre hareket eden biri olmanın karşılığını alabilirsiniz. Kuru endişelerin, olmayacak ihtimallerin yerini çabaya ve doğru harekete bırakması, karşılaşacağınız psikolojik zorlukların da önüne geçecektir. Sizinle uğraşan, sizi zorlayan konulara ve insanlara prim vermemelisiniz. Dikkatleri de bu yönde çekebilirsiniz. Dolayısıyla size gelecek tekliflerin, desteklerin de önünü açmış olacaksınız. Aile ve eş destekleri, ek iş konuları, miras ve diğer hak edişler rahatlamanıza yardım edebilir. Güneş'in geri hareketteki yönetici gezegeniniz Merkür ile kavuşumu geçmişe dönük konuları ve hakları gündeme getirebilir. Daha iyi ve sağlam planlar yapmak, kararlar almak ve mevcut durumu yönetmek için bu dönemi kullanabilirsiniz. Farkındalığınız yükseliyor. Geçmişi deşmek, sorunları büyütmek yerine yapıcı olmaya çalışmalısınız. Bu yaşadıklarınızın öğretisi, ders çıkarmak ve buna göre ilerlemektir. Konuşmalarınıza ve davranışlarınıza özen göstermeli, sağlık konusunu ihmale getirmemelisiniz.",
    "27 Aralık'ta Chiron'on Koç burcunda ileri hareketine başlamasıyla sizin için önemli olan arkadaşlıkları daha farklı bir gözle izleyebilir, daha farklı hislerle yaşayabilirsiniz. Eskiden gözünüze takılan, sizde rahatsızlık uyandıran durumlarla nasıl başa çıkacağınızı daha iyi biliyorsunuz. Bu bilginize yakışır bir şekilde hareket ettiğinizde, ilişkilerinizin size ne gibi faydalarının olduğunu anlayabilirsiniz. Enerjinizin hem yükselerek değiştiği bu süreçte ortaya koyacağınız işler de aynı etkiyi uyandırabilir. Üretken fikirler, insanları etkileme ve bir araya getirme becerinizle birleşiyor. Empati yapabildiğiniz ve zorluk yaşadığını düşündüğünüz gruplar için sosyal sorumluluk projeleri üretebilir, dijital platformlarda hareketlilik başlatabilirsiniz. Eğitim, sosyal mecralar ve bunlarla ilgili işlerde başarılı olabilirsiniz. Özgüveninizle barışıyorsunuz.",
    "27 Aralık'ta Yengeç burcunda gerçekleşecek dolunay ile beraber ekonomik konularda önemli gelişmeler elde edebilirsiniz. Borçlanma, ödemeler, hakkınızı alacağınız işler gündeminizde yer tutabilir. Ne yaptığınızı ve bu işin karşılığını bilerek ilerlemelisiniz. Ortaklı ya da aile destekli işlerle ilgilenebilir, bu konuda çalışmalarınız varsa üzerinde daha dikkatli çalışabilirsiniz. Değer verdiğiniz insanların, işlerin, konuların karşılığı hayal kırıklığı olabilir. Burada ipleri bırakmak ve vazgeçmek yerine, neler yapabileceğinizi bir dahaki sefere nasıl mutlu olacağınızı düşünmelisiniz. Zorluk her zaman olacaktır, siz her seferinde bunu nasıl aşacağınızı planlamalısınız; ama yapıcı bir tutum sergileyerek bunu başarabileceğinizi de unutmamalısınız.",
    "29 Aralık'ta Venüs'ün Yay burcuna geçişi ilişkilerinizi önemli ve hareketli bir noktaya çıkarabilir. Nasıl hissettiğinizi görüp buna göre karar vereceğiniz bir dönem olabilir. Kendinizi layık gördüğünüz konular ve insanlar mercek altına alınabilir. Önyargılı ya da ilgisiz olmamalısınız. Çünkü size her konuda destek verecek, farklı fikirlerle bakış açıları kazandıracak insanlarla tanışabilirsiniz. Burada kuracağınız dostluklar, ilişkiler hem de sosyal hayatta hem de işle ilgili konularda büyük kazanımlar elde etmenize yardımcı olacaktır. Yeni duygusal ilişkiler, evlilik kararları ve buna bağlı yer değişiklikleri gündeminize gelebilir. Gezerek yapacağınız işler, danışmanlıklar, sosyal faaliyetler, hukuki konularla ilgili çalışmalarınız hız kazanabilir, böyle bir gündeminiz yoksa değerlendirmeye alabilirsiniz.",
]

yengec = [
    "Neptün'ün 6 Aralık'ta Balık burcundaki geri hareketini sonlandırmasıyla, sizin de bazı defterleri kapatmanızın zamanı geliyor. İnsanların sizinle ilgili fikirlerini düşünerek kendinizle ilgili çıkarım yapmamanız gerektiğini öğrendiniz. Bu süreç itibariyle kendi kararlarınızın mekanizmasını kendi seçimlerinize, yetilerinize ve imkanlarınıza göre yapmalısınız. Manipüle edildiğiniz, hakkınızı alamadığınız alanlarda sessiz kalmak yerine sesinizi duyurmayı deneyimleyebilirsiniz. Hayal ve gerçekliğin karıştığını hissettiğiniz durumların netleştiğini, başvurularınızın ilerlediğini ve her şeyin kendi doğal akışına ulaştığını görebilirsiniz. Bu da endişelerinizin yerine planlarınızın ve isteklerinizin almasını sağlayacaktır. Hukuksal konular, miras ya da ekonomik destekler alacağınız görüşmeler, taşınma, farklı bir yaşam tarzı oluşturma gibi durumlarda uygulamaya geçebilir ya da mevcut çalışmalarınızı kaldığı yerden devam ettirebilirsiniz. Fark ettiklerinizi unutmadığınızda rüzgarın sizden yana eseceğini göreceksiniz.",
    "13 Aralık'ta Yay burcunda gerçekleşecek yeniay ile çalışma hayatınıza yeni bir soluk ve gündeme gelebilir. Kendi işinizi yapmak, bir fikirden yola çıkarak yeni bir sektöre girmek, çalışma ortamınızı ve sorumluluklarınızı değiştirmek adına çok iyi fırsatlar bulabilirsiniz. Bunları her zaman bulabilirdiniz belki ama şu an yeni yılı ve fırsatları daha keyifle karşılayacağınız bir enerjiye ve cesarete sahipsiniz. Büyümeyi, kabınızdan çıkmayı, yeni alanlar keşfedip yeni deneyimler elde etmeyi hedefliyorsunuz. Bu hedefleri gerçekleştirmek için sorumluluklarınızı arttırabilir, konu hakkında ilgili kişilerle görüşüp eğitim ve destek alabilirsiniz. Altını dolduracağınız her şeyin sağlam ve dik duracağı bir dönemdesiniz. Bunu sadece işinizde ve gündelik koşturmanızda değil sağlığınız konusunda da uygulamaya koymalısınız. Sakin ve akıllıca hareketler, heyecanı yönetmek görünmez kazaları önleyebilir. 'Bir şey olmaz' düşüncesiyle rahatsızlıklarınızı ihmal etmemeli, gerekli takviye ve kontrolleri tamamlamalısınız.",
    "13 Aralık'ta Merkür'ün Oğlak burcundaki geri hareketine başlaması, ikili ilişkilerle ilgili bazı gerçekleri ortaya çıkarabilir. Bunlar gizli saklı konularla ilgili olabileceği gibi sizin görmezden geldiğiniz ya da fark etmediğiniz konularla da ilgili olabilir. Her iki durumda da, yaşadıklarınıza ve muhataplarınıza dikkatli bakmalısınız. Buradaki sorunu ya da eksiği olabilecek en iyi ve kesin bir şekilde çözmeye çalışmalısınız. Gelişemediğiniz, mutlu olamadığınız, ilerlemekte güçlük yaşadığınız ilişkileri değerlendirebilirsiniz. Bir bitiş kararı vermeye hazırlanabilir, kafanızda bazı dengeleri değiştirebilirsiniz. Yeni bir adım atmak yerine mevcut durumla ilgili olmak hem sizi hem de karşınızdaki kişiyi koruyabilir. Zıtlaşma, yanlış anlaşılma, parasal konulardaki aksaklıklar problemi büyüteceği için ne kadar sakin ve ağırdan hareket ederseniz olabilecekleri öngörmeniz de o kadar kolay olacaktır.",
    "Güneş'in 22 Aralık'ta Oğlak burcuna geçmesiyle beraber sevdiğiniz insanlar ve onlarla ilgili konuları mercek altına alabilirsiniz. Söylemek istediklerinizle ağzınızdan çıkanların farklı olduğunu görebilir, nerede sıkıştığınız ya da takıldığınızı daha iyi anlayabilirsiniz. Bu da kendi isteklerinizi, hislerinizi, karşınızdaki kişinin beklentilerini görme konusunda size fırsat tanıyabilir. Kendinizi sorumluluk altında hissedebilirsiniz. Sevdikleriniz için bir şeyler yapmak isterken onların hayatına ve duygularına fazla müdahaleci olabilirsiniz. Dengeyi bilmek, herkesin sınırına göre hareket etmek önemli olacaktır. Gereksiz ve duygusal fedakarlıklar insanların sizinle ilgili düşüncelerini olumsuz yönde değiştirebilir. Makul olmalısınız. Bu, o kişilerin size olan yaklaşımlarını da değiştirebilir. İlişki kurmak, adım atmak, beraberlikleri daha ileriye götürmek adına istekleriniz varsa önce bunun karşılıklı olması için çaba göstermelisiniz. Duygusal açıdan güçlü olmalı, manipülasyon ya da kurgular yerine aklınızla, mantığınızla hareket edebilmelisiniz. Size bunu öğretebilecek, kendinizi geliştirmenize yardım edecek insanlarla tanışabilirsiniz. Gardınızı düşürün. Bu sayede sizinle ilgili olumsuz yargıları olan insanları fark edebilir, çözüme gidebilir ve değişiminizi sergileyebilirsiniz. Ortaklı işler ve ticari konularda şanslı olabilirsiniz. Disipline ve odaklanmaya önem verin, seçimlerinizi de bunları destekleyecek şekilde yapın. Güneş'in Oğlak burcunda geri hareket eden Merkür ile kavuşumu size bu konuda dikkate almanız gereken detayları gösterebilir. Alacak verecek konuları, statü beklentiniz, hukuksal sorunlarınız için telafi şansınız olabilir. Geçmişin iyi getirilerinin olması, daha önce doğru yaptığınız bazı hamleleri size hatırlatabilir. Bu hamleleri nasıl geliştireceğinizi, nasıl kalıcı hale getireceğinizi düşünmelisiniz.",
    "27 Aralık'ta Chiron'un Koç burcunda ileri hareketine geçişi ile beraber işinize ve verdiğiniz emeklere sahip çıkmaya başlıyorsunuz. Sorumluluklarınızın karşılamayan gelir ve statünün değişmesi için bir adım atabilir, kendinizi daha iyi ifade edeceğiniz alanlara geçiş yapabilirsiniz. İnsanlara anlattığınız ve ilham olduğunuz konuları kendi hayatınıza uyarlama zamanındasınız. Artık inisiyatif alıyor, becerilerinizi ortaya koyuyorsunuz. İpleri elinize almak isteyebilir, kendi işinizi kurabilir ya da bulunduğunuz yerde üst pozisyonlara geçebilirsiniz. Bu yükseliş halini sürekli kılmak ve bu motivasyonu beslemek önemli olacaktır. Bu konuda yeterliliğinizi sorgulamak yerine eksiklerinizi nasıl kapatacağınıza odaklanmalısınız. Evrenin hareketi alkışladığına, çabayı ödüllendirdiğine şahitlik edeceğiniz gelişmeler yaşayabilirsiniz. Adım atmaktan çekinmeyin",
    "27 Aralık'ta burcunuzda gerçekleşecek dolunay ile bu çekingenliği aşmanız mümkün olabilir. Size başta zor gibi gelse de, kurtulduğunuz her şeyin hafifliği şimdi işinizi kolaylaştıracaktır. Bu da başlangıç yapmanızı, yola çıkmanızı, hayatınızı yenilemenizi daha rahat bir ortamda gerçekleştirmenizi sağlayacaktır. Duygusal kararlar almanın sizi uğrattığı zararların farkına varıyorsunuz. Ortaklıklar, ilişkiler, bireysel alanlarınız gibi konulardaki kriterlerinizi değiştirebilirsiniz. Kendinize yönelin, alışkanlıklarınızı gözden geçirin, bunların bıraktığı etkileri anlamaya çalışın. Hem sağlığınız hem de psikolojik durumunuz için bunun gerekli olduğunu göreceksiniz. Tarzınızda ve dış görünüşünüzde bir değişiklik yapmak isteyebilirsiniz. Ancak Merkür'ün hala geri harekette olduğunu unutmadan hareket etmenizde fayda var.",
    "29 Aralık'ta Venüs'ün Yay burcunda hareket edecek olmasıyla iş hayatınız ve ortamınız daha renkli, daha hareketli bir hal alabilir. Emekleriniz görülüyor, siz de geçmişte ve şu anda yaptığınız işlerin nereye vardığını görüyorsunuz. Eğitim almak, yaptığınız işe değer katacak çalışmalar yapmak, sosyal projeler geliştirmek, dil öğrenmek ya da bilinen bir dili kullanarak iş yapmak gibi konularla ilgilenebilirsiniz. Ağınızı, kapasitenizi büyütmek için uygun bir zamandasınız. Bunun sadece psikolojik olarak değil maddi olarak da geri dönüşlerini alabilirsiniz. Sağlık sorunlarınızın iyileşmeye başladığı bir dönemdesiniz, yine de kontrollerinizi ve uygulamalarınızı aksatmamanızda, ani hareketlerden kaçınmanızda fayda var."
]

aslan = [
    "6 Aralık'ta Neptün'ün Balık burcunda ileri hareketine başlaması, hayatınızda neye yer verdiğiniz konusunun üstünü çizebilir. Çünkü artık altını çizerek önemsediğiniz konuların size bir faydasının, getirisinin olmadığını görüyorsunuz. Yaşadıklarınızı değerlendirme şeklinizi değiştirmeniz, yeni bir içgörü kazanmanıza yardımcı olacaktır. İlk ve tek adımın sizden geldiği konular, kendi sorumluluğunuzun dışındaki işler ve bunların hayatınıza olumsuz etkilerini net bir şekilde görebilirsiniz. Bunu görmezden geldiyseniz, retronun bitimiyle beraber büyük ve zorlayıcı yüzleşmeler yaşayabilirsiniz. Mutluluğunuzu, kazancınızı ve güvencelerinizi kendinizden ya da kendi imkanlarınızdan başka bir şeye bağlamamayı deneyimleyeceksiniz. Bunun da, yaşadığınız diğer deneyimler gibi sizi geliştireceğini bilmeli ve içinizdeki gizli umutsuzluğu yok etmelisiniz. Ekonomik koşullarınızı iyileştirecek haberler alabilir, yaptığınız işlerin geri dönüşlerini görebilir ve yapmak istediğiniz işler konusunda yeni atılımları daha güvenli ve gerçekçi bir sistemle ele alabilirsiniz.",
    "13 Aralık'ta Yay burcunda gerçekleşecek yeniay duygusal konularda yeni heyecanlar yaşatabilir. Evlenme, çocuk sahibi olma, aile bağlarını güçlendirme gibi gündemleriniz olabilir. Hayatınızın yeni bir seyri olduğunu görebilirsiniz. Enerjik ve iyimser hissediyor olmak, sizi sosyal ve duygusal açısından besleyecektir. Bunun bir getirisi olarak da, sosyal alanlara dahil olma, çalışmaları hızlandırma, hayatınıza başka pencereler açma gibi konularla sıklıkla ilgilenebilirsiniz. Duygularınızı yoğun ve uçlarda yaşıyor olmak, beklentilerinizi de bu seviyeye çıkarabilir. Karşınızdaki insan bu beklentiyi karşılayamadığında sorun çıkarmak yerine birbirini görüp anlayabileceğiniz bir seviye oluşturmaya çalışmalısınız. Yolculuklar, tatil planları, yeni insanlar veya konularla karşılaşacağınız etkinlikler, yurt dışı işlemleri, uzaktaki aile yakınlarından ve erkek figürlerinden destekler gibi konular gündeminizde yer bulabilir.",
    "Oğlak burcundaki Merkür'ün 13 Aralık'ta geri hareketine başlaması, önem verdiğiniz işlerin ve planların gözden geçirilmesi için fırsat tanıyabilir. Verim alamadığınız, kazancınızı yükseltemediğiniz, kendinizi rahat hissetmediğiniz koşulların değerlendirilmesi ve iyileştirilmesi için görüşmeler yapabilirsiniz. Bir değişiklik yapmak, yeni bir noktaya geçmek yerine mevcut koşullarla ilgilenmek daha akıllıca olabilir. Geçmişte çalıştığınız işler, bunların ödemeleri, daha önce başvurduğunuz yerlerle ilgili geri dönüşler alabilirsiniz. Ne istediğinizden emin olarak bu noktada bir karar verebilirsiniz. Yapabiliyorsanız izin alma, uzaktan çalışma, iş bölümüne gitme gibi seçenekler sizi fiziksel ve psikolojik olarak rahatlatabilir. Farklı alternatiflerin, kuralları esnetmenin bir sakıncasının olmadığını da böylece deneyimlemiş olabilirsiniz. Beslenme ve uyku düzensizlikleri, kemik sağlığı ve dişlerinizle ilgili konular, el becerisi gerektiren işler ve cihazlarınıza hassasiyet göstermelisiniz. Bakım, tedavi, yenileme gibi konulara gerekli zamanı ve bütçeyi ayırmanızda fayda var.",
    "22 Aralık'ta yönetici gezegeniniz Güneş'in Oğlak burcuna geçişi yeteneklerinizi sergileyeceğiniz, daha iyisini ortaya koyabileceğiniz bir dönemi başlatıyor. Kendinizi ifade edeceğiniz, emin olduğunuz konuları sunabileceğiniz alanlarda çalışabilir ya da bizzat bu alanların kurucusu olabilirsiniz. İyi olduğunuz, kendinizi geliştirdiğiniz bir işi profesyonelleştirip kazanç elde etmeye başlayabilirsiniz. Tüm odağınız, hayatınızı hem günlük hem de psikolojik olarak yüksek standartlara taşımak üzerine olabilir. Çevrenizle beraber olmayı, insanlara güvenmeyi, işbirliği önemsemeli ve bu konudaki açıklarınızı kapatmalısınız. Tüm sorumluluğu ele aldığınız durumlarda bunun yükünün de git gide ağırlaşacağını unutmayın. Ekonomik açıdan daha güçlü olabilir, kazancınızı arttırabilirsiniz. Bu sadece hayatınızı idame ettirmek üzerine değil yatırım konusunda size fırsatlar tanıyabilir. Yoğun bir tempo, artan sorumluluklar bir noktadan sonra hırs ve stresi, sağlık sorunlarını getirebilir. Masa başı çalışmalardan kaynaklanan kemik sağlığı sorunları, uyku ve beslenme eksikliği, bağışıklığın düşmesi gibi durumlar için önleminizi almalısınız. Bu konuda daha önce ihmal ettiğiniz tedavi ve takviyeler varsa şimdi yeniden gündeme getirebilirsiniz. Güneş'in retro hareketteki Merkür ile kavuşumu bu gündemi destekleyebilir. Kendinizi gereksiz yere zorlamamalı, dinlenmeye ve hayatı yakalamaya da zaman ayırmalısınız. Durup düşünmediğiniz, gözünüzü kararttığınız konuların olumsuz geri dönüşlerini almamak için temponuzu düşürmeyi denemelisiniz. Ciddi ve mesafeli duruşunuzun bıraktığı intibayı toparlamak için de şansınız var. Sadece bunu kabul edip gardınızı düşürmeli, insanların eleştirilerini ve söylemlerini yapıcı bir kulak ile dinlemelisiniz. Maddi kaynaklarınızı daha dengeli kullanmayı çalışın.",
    "27 Aralık'ta Chiron'un Koç burcunda ileri hareketine geçmesiyle mutlu olmanıza ve iyi hissetmenize gölge düşüren konulardan sıyrılıyorsunuz. Artık daha farkında, daha cesur hissedebilirsiniz. Özsaygı, özşefkat gibi kavramlara fazlaca zaman ayırabilir ve artık bastırmak yerine kabullenip çözme eğilimi göstermenin önemli olduğunu idrak edebilirsiniz. Eksiğinizin ne olduğunu bildiğinizde bunu tamamlamanın da o konuda ilerlemenin de kolay olduğunu fark edeceksiniz. Eleştirileri daha iyi karşılayabilir, tepkilerinizi daha yerinde ve abartısız bir şekilde gösterebilirsiniz. Bunun size yaşattığı zorlu zamanları, maddi ve manevi hak kayıplarını unutmamalısınız. Ders alın ve devam edin. Ek iş çalışmalarınıza dönebilir, bir şeyler üretmek istediğiniz alanlara dair araştırmalar yapabilirsiniz. Eşinizin, ailenizin desteğini her zaman hissetseniz de bunu neyin üzerine koyacağını belirlemek sizin sorumluluğunuzda olacaktır; bu sorumluluğu alıyorsunuz.",
    "27 Aralık'ta Yengeç burcunda gerçekleşecek dolunay gizli saklı konuları, size karşı kimin hangi niyeti beslediğini net bir şekilde gösterebilir. Egonuz kadar duygularınızın da zarara uğradığını gördüğünüzde, bunu değiştirmek için gereken cesarete sahip olduğunuzu fark edebilirsiniz. Şimdi bu cesareti kullanma zamanı! Eski ilişkiler, ailevi konularla ilgili haberler alabilirsiniz. Kafanızı ve gündeminizi meşgul eden bu konulara son kez yer vermeniz gerektiğini unutmayın. Bazı şeylerin dünde kalması gerektiğini, her şeyin ve herkesin sizinle yürümeyeceğini bilerek hayatınızı sürdürmelisiniz. Kararlarınızın ve beklentilerinizin değişmesi, iş ortamınızı, ilişkilerinizi de değiştirebilir. Buna hazır olduğunuzu hissedebilir, zincirleri tek seferde kırmak isteyebilirsiniz. Merkür'ün 2024 yılı Ocak ayında düz harekete geçeceğini unutmayın, bu dönemde sadece çalışın ve aklınızdakini şekillendirin.",
    "29 Aralık'ta Venüs'ün Yay burcuna geçişi hayatın yükünü atmanıza, keyif almanıza yardımcı olabilir. Tatil planları, yeni yerler görme isteği size yeni hayaller kurdurtabilir. Bir uğraşı işe dönüştürebilir, kitlenizi genişletebilir, sosyal mecraları kullanarak güçlenebilirsiniz. Durağan zamanların ardından şimdi, hareketi ve bereketi yaşantınıza dahil etmek isteyebilirsiniz. Bunun için yeni işler almak kadar yeni insanlar tanımak da gerekli olabilir. Duygusal ve sosyal etkileşimlere açık olduğunuz bir dönemdesiniz. İnsanların ilgisini çekmiş olmanın mutluluğu bu konudaki cömertliğinizi ortaya çıkarabilir. İlişkilerinizi ilerletmek, çocuk sahibi olmak gibi gündemleriniz olabilir. Heyecan ve hevesinizi dozunda yaşamanız, sonrasında rahatsız olacağınız ilişkilerin yaşanmasını ya da maddi kayıpları önleyebilir."
]

basak = [
    "6 Aralık itibariyle Balık burcunda ileri hareketine başlayacak olan Neptün, ilişkilerdeki kriterlerinizi ve hatalarınızı ortaya çıkardıktan sonra size daha mutlu olacağınız yeni alanlar getirebilir. Daha önce yaşadıklarınızı değerlendirme şansı bulduğunuz, geri planda tuttuklarınızla yüzleştiğiniz için rutinlerinizin dışına çıkmış gibi hissetmiş olabilirsiniz. Ancak rutinlerin ve düzenin iyi yönde değişebilmesi için bunu yaptığınızı kabulleniyorsunuz. Her şeyi tek başınıza ve fazlaca düşünüyor olmanın, olumsuz getirilerini konuşmak yerine ilişkilerde ve iş hayatında sorumlulukları paylaşmayı deneyimlemelisiniz. Seçimlerinizi ve beklentilerinizi değiştirmekle hayatınıza etki eden insanlar ve konularla ilgili gelişmeleri de değiştirebileceğinizi unutmayın. Siz nasıl olursanız hayatınıza bunu destekleyecek insanlar gelecektir. Destek ve köstek arasındaki farkı görüp daha fazla huzursuz olmamak için hayattan ve yaşadıklarınızdan keyif almayı öğrenmelisiniz. Evlilik kararı, işle ilgili konular, anlaşmazlık yaşadığınız kişilerle ilgili sorunları çözme açısından şanslı bir dönem olabilir. Daha farkındalıklı ve geniş açılı olmanın avantajlarını görebilirsiniz. İşleriniz açılıyor, yoğun ve keyifli bir tempoya girebilirsiniz. Kime güveneceğinizi bildiğinizde bu sürecin daha verimli geçeceğini unutmayın.",
    "13 Aralık'taki Yay yeniayı odağınızı evinize, evdeki düzene ve aile ilişkilerine çevirebilir. Taşınma, alım satım, aile büyüklerinin desteklediği yatırımlar gündeme gelirken evinizin fiziksel ihtiyaçlarıyla da ilgilenebilirsiniz. Tadilat ve dekorasyon işleri zamanınızı alabilir. Kendinizi özgür, rahat ve mutlu hissedeceğiniz bir düzen kurmalısınız. Bu isteği taşıdığınızı görebilirsiniz ancak kendinizle ve hayatın getirileriyle direnmemelisiniz. Aile içindeki konularla ilgilenebilir, sorunları çözebilirsiniz. Yüksek dozda yaşanan duygular gerilmenize ve olayları olduğundan daha fazla büyütmenize neden olabilir, aile içinde bazı gerginlikleri doğurabilir. Yapıcı ve iyimser olmaya gayret gösterin, herkesin iyi niyetinizi fark etmesini sağlayın. Bu üzerinizdeki yükü alacaktır. İmza gerektiren işler, anlaşmalar, evlilik kararı, evden çalışma gibi konularda beklediğiniz gelişmeleri yakalayabilirsiniz.",
    "13 Aralık'ta yönetici gezegeniniz Merkür'ün Oğlak burcundaki geri hareketi, size iyi hissettiren her şeyi sorgulatabilir. Burada amaç, bozmak ya da yıkmak değil daha iyisini bulabilmek, yaşayabilmektir. Bu farkı gözeterek ilerlediğinizde anlaşılmanız, karşınızdakini anlamanız ve sorunları çözmeniz kolaylaşacaktır. Zorlamak ya da kontrol etmek yerine akışa göre ilerlemeyi, sakinleşip beklemeyi ve kendi kurallarınızla değil hayatın kurallarıyla yaşamayı deneyimlemelisiniz. Bu tavrınızın aileniz/eşiniz, çocuklarınız, sosyal çevreniz üzerinde de olumlu etkileri olacaktır. Eski aşklar, arkadaşlıklar, parasal konular ve işlerden haberler alabilirsiniz. Şu an o haberlerin sizin için ne hissettirdiğine bakın ve önünüze geldi diye gündeminizde tutmak zorunda olmadığınızı da unutmayın. Çünkü bazı hikayeler, şu anda ne kadar mutlu kararlar içinde olduğunuzu anlamanız için başa sarar. Ekonomik planlar, bir işe ve hayale yatırım yapmak gibi konularda çok iyi araştırmalısınız. Emin olmadığınız, gelecek göremediğiniz alanlardan ve harcamalardan uzak durmanızda fayda var. Seyahat planlarınızda aksaklıklar olabilir, b planınızın olması daha az üzülmenize yardımcı olacaktır.",
    "22 Aralık'ta Güneş Oğlak burcuna geçerek kurduğunuz düzeni, yakaladığınız mutluluğu kalıcı hale getirmek için zemin hazırlıyor. Sevginin, mutlu olmanın, bir şeylerden keyif almanın somut haline daha çok odaklanabilirsiniz. Size bir peri masalından ziyade hayatınıza gerçek dokunuşları olan her şeyin daha iyi hissettirdiğini görebilirsiniz. Hem arkadaş hem fikir, etkinlik seçiminizde bunu göz önünde bulundurabilirsiniz. Bir şeyler üretebilmenin, değer katabilmenin ve sevginin emekle eşdeğer olduğunu anlatabilmenin ihtiyacı ve sorumluluğu ağır basabilir. Güven odaklı ilişkiler kurmanın sizi taşıdığı noktadan memnun olabilirsiniz. Aile kurmak, çocuk sahibi olmak, geleceğe yatırım yapmak, hayatınızı maddi ve manevi olarak daha iyi standartlara taşımak gibi gündemleriniz olabilir. Bu sorumlulukları almaya hazır olduğunuzu hissedebilirsiniz. Markalaşma, üretim yapma, bir fikri iş kapısına dönüştürme konularında şansınız açık olabilir. İşinizi şansa bırakmayı sevmediğiniz için her zaman çalışmanın ve emek vermenin karşılığını bu sayede daha iyi alabilirsiniz. Güneş ve geri hareketteki Merkür'ün Oğlak burcundaki kavuşumu, parasal konularda daha dikkatli hareket etmeniz gerektiğini hatırlatabilir. Yanlış giden, getirisi olmayan, belirsiz ve sonuçsuz kalan işlerinizi incelemek için fırsatlar bulabilirsiniz; bu fırsatları değerlendirin ve hatayı en aza indirmenin yollarını arayın. İkili ilişkilerle ilgili konuşmalarda gereksiz mesafeler koyabilirsiniz. Hissettiklerinizi nasıl dile getirdiğinizin önemini, geçmişte yaşanıp bugün önünüze gelen konularla anlayabilirsiniz.",
    "27 Aralık'ta Chiron'un Koç burcunda ileri hareketine başlamasıyla beraber alışkanlıkların, tahminlerin, rutinlerin dışına çıkmayı daha rahat bir ruh haliyle deneyimleyebilirsiniz. Bu konudaki endişelerinizin, daha önce denememiş ve adım atmamış olmaktan kaynaklandığını fark ediyorsunuz. Kendinize şans tanıma zamanına geldiniz. Kontrol altında tutmak, istediğiniz planda ilerletmek konularında esneklik gösterebilirsiniz. Bu sadece teoride değil, artık pratikte de kolay olacaktır. Kendinize, cesaretinize ve fikirlerinize güvenmelisiniz. Eşinizin, ailenizin, sizi seven, sizinle aynı paydada olan insanların daha fazla desteğini alacağınız gelişmeler yaşayabilirsiniz. Ancak bunun için öncelikle sizin adım atmanız, kendinize öncülük etmeniz ve sahaya çıkmanız gerekecektir. Bırakabilmenin size neler kazandıracağını hayal edin, yaşadığınız acıların ya da rahatsızlıkların size nasıl bir düzen kuracağını düşünün. Belirsizlikten şikayet etmek yerine bu konuyla ilgili neler yapabileceğinizi araştırabilirsiniz. Şayet bunu retro sürecinde yaptıysanız, en azından denediyseniz, şimdi karşılığını alabilirsiniz. Bir şeye bağlı olacaksanız kendi kaynaklarınıza bağlı olmayı tercih edin ve bunları her zaman güncel tutun.",
    "27 Aralık'taki Yengeç Dolunayı ile beraber arkadaş seçimi, ihtiyacı ve tek başınıza geçirdiğiniz zamanların kalitesi gibi konuları yoğun bir şekilde düşünebilirsiniz. Yılın başından bu yana hayatınızda olan bazı insanların şu an olmayışı ya da bunun tam tersi durumunda, hatanın nereden kaynaklandığını net bir şekilde görebilirsiniz. Duygularınıza yenik düştüğünüz, toksikleştiği için veda ettiğiniz her şeyin bir kazanımını elde edebilirsiniz. Bu konuda alacağınız bazı haberler ya da geri dönüşler, bazı detayları yeniden düşünmenizi gerektirebilir. Bu aşamada kendinizin hem de karşınızdaki kişinin hatalarının tekrarlamayacağı şekilde karar vermelisiniz, bu yüzden acele etmeyin ve sakin bir kafayla düşünün. Zira yönetici gezegeniniz Merkür'ün geri hareketi düşüncelerinizi netleştirmeyi zorlaştırabilir. Sosyal çevrenizle beraber yürüttüğünüz işlerin nihayetine ermesi, sonuç almanız üzerinizdeki baskı hissini azaltabilir. Kutlama, tatil, dinlenme gibi programlar düzenleyebilir, sevdiğiniz ve güvendiğiniz kişilerle olmanın keyfini çıkarabilirsiniz. Her gözyaşının, her zorluğun arkasından gelen iyi ve güzel imkanların farkında olun; bu şekilde yaşam kalitenizi arttırırken gelecek kaygılarınızı da en aza indirebilirsiniz.",
    "29 Aralık'ta Venüs'ün Yay burcuna geçmesiyle aile kurmak, aile üyeleriyle keyifli anlar yaşamak ve sorunları çözmek adına iyi bir döneme giriyorsunuz. Şansınızın döndüğü bir süreçtesiniz bu yüzden karşınıza çıkan fırsatları değerlendirmeye almalısınız. Bazen fırsatları sizin bulmanız gerekebilir, ihtiyaçlarınızın farkına varmak için kalbinizi ve sevdiklerinizi dinleyebilirsiniz. İş ya da evlilik gereği taşınma, ev alma gibi emlakla ilgili konularla ilgilenebilirsiniz. Tayin, kurum ya da şehir değişikliği gibi durumlar gündeminize gelebilir. Beklentilerinize göre hareket edebilmeniz için hem ailenizden hem de çevrenizden destek görebilirsiniz. Heyecanınızı, tepkilerinizi ve isteklerinizi doğru bir dille ifade etmeye özen göstermenizde fayda var."
]

terazi = [
    "6 Aralık'ta Neptün'ün Balık burcundaki geri hareketini sonlandırması, günlük akışınızı hızlandırabilir. Sorumluluk almaktan çekindiğiniz zamanların sonuna geldiniz. Çünkü artık kendinizi, çevrenizi ve yapmanız gerekenleri daha iyi biliyorsunuz. Bunları aşan konuların sizden fiziksel ve mental açıdan çok şey götürdüğünü bilmeli ve buna göre hareket etmelisiniz. İşinizi, size verilen değeri, sorumluluklarınızı ve bunları yapabilme gücünüzü kaybedeceğinize dair korkuların yersiz olduğunu görebilirsiniz. Eksiğinizin, yanlışınızın olduğu konuları bu korkulardan ayırt ederek telafi, geliştirme çabasına girebilirsiniz. Bu da size işinizi daha iyi noktaya çıkarma, maddi kazanımlarınızı arttırma, hayatınıza yeni bir düzen getirme konusunda önemli fırsatlar sunabilir. Açık bir zihin, sağlıklı bir yapıya sahip olduğunuz sürece bu fırsatları en güzel şekilde kullanabilirsiniz. Dolayısıyla sağlığınıza ve dış görünüşünüze de gereken özeni göstermelisiniz. Doktor kontrolleri, beslenme alışkanlıkları, dikkat ve konsantrasyon dağıtan konuları ihmal etmeyin.",
    "13 Aralık'ta Yay burcunda gerçekleşecek yeniay ile hem sosyal açıdan hem de eğitim açısından zengin ve yoğun bir döneme girebilirsiniz. Kendinize yeni bir yol çiziyorsunuz. Daha özgüvenli ve yapabileceklerinize inanan biri olmanın bir getirisi olarak, çevrenizin desteğini ve ilgisini de üzerinize çekebilirsiniz. Yolculuklar, iş görüşmeleri, aile/arkadaş ziyaretleri, eğitim ve kamplar gibi etkinliklerle vakit geçirebilirsiniz. Maddi kazanımlarınız artabilir, bu da beraberinde fazlaca harcama getirebilir. İyi bir amaçla da olsa bu harcamaları kontrol altında tutmaya çalışmanız, ilerisi için sizi risklerden koruyacaktır. Yasal ve hukuki konular önemli olabilir. Bir dava ya da hak arama konusu olmasa bile, yazılı başvuru süreci gerektiren işleriniz için daha fazla zaman ayırmanız gerekebilir. Bu konuda üzerinize düşeni hakkıyla ve doğru bir şekilde yapmaya çalışmalısınız. Yakın çevrenize, arkadaşlarınıza karşı duyarlılığınız artabilir. Daha çok zaman geçirmek ve onlar için bir şeyler yapmak isteyebilirsiniz. Aşırı dozun getireceği zararlar olabileceğini, suistimal edilme ihtimalini göz önünde bulundurursanız herhangi bir olumsuzluk karşısında aşırı tepki vermenizin de önüne geçebilirsiniz. Şanslısınız, bunun farkında olarak yaşadığınızda karşılaştığınız her şeyin size hizmet edecek bir tarafı olduğunu göreceksiniz.",
    "13 Aralık'ta Oğlak burcundaki Merkür'ün geri hareketine başlaması, aile büyüklerinizle ilgili konuları gündeme getirebilir. Sağlık sorunları, miras ve hukuki işlemler, alım satımla ilgili konularda uğraşmanız gerekebilir. Sorumluluğu sizin üstleneceğiniz durumlar doğduğunda tam olarak hangi aşamada olduğunuza, elinizdeki imkanlara dikkat etmelisiniz. Kaygılanmak insani olsa da bu kaygıyı büyütmeden, riskler için tedbir amaçlı kullanmayı öğrenmelisiniz. Bir haber alabilir, geçmişteki bir konu yeniden canlanabilir, ailenizle ilgili önemli bilgiler öğrenebilirsiniz. Doğru bir muhakeme ile bunların getireceği zararı önleyebilirsiniz; sağduyuyu elden bırakmayın. Evinizle ilgili aciliyeti olmayan düzenlemeleri yapabilir, eşyalarınızı kontrolden geçirebilirsiniz. Yüksek maliyetli harcamalar, gayrimenkul işlemleri gibi konularda mümkünse beklemelisiniz. Her şey sıralı ve zamanlı olsun isteyebilirsiniz ancak bu istek bazen hata yapmanıza neden olabilir. Sabredin, mantığınızı kullanın ve hayatın sizin için uygun gördüğü sıralamayı anlayarak yaşayın."
    "Güneş'in 22 Aralık'ta Oğlak burcuna geçişi ile beraber ev almak, evinizle ilgilenmek, maddi konuları yönetmek gibi konularla ilgilenebilirsiniz. İhtiyaçlarınızın farkında olacağınız için ne yapacağınız, nasıl bir planla ilerleyeceğinizi belirlemeniz de kolay olacaktır. Evden çalışma, aile destekli işler yapma, iş gereği ev düzeninde değişiklikler gibi konularla ilgilenebilirsiniz. Kontrat yenileme, farklı bir çevreye geçme ya da kendi evinizi alma gibi gelişmeler yaşanabilir. Güneş'in geri hareketteki Merkür ile kavuşmasını da hesaba katarak bu gibi işlemlerde daha dikkatli olmanızda fayda var. Resmi kurumlar, imzalı işler, görüşmeler, para transferleri, aile içindeki nakit akışında aksamalar yaşama ihtimaliniz olabilir. Konunuz, gündeminiz ne olursa olsun henüz kesinleşmeyen hiçbir şeyin kararını almamaya çalışın. Evde daha güvenli ve rahat bir düzen kurmak isteyebilirsiniz. Elektronik cihazlar, diğer ev eşyalarının tadilatı ve bakımlarıyla ilgilenebilir, artık miadı dolanları ayıklayabilir, kullanmadıklarınızı geri dönüşüme aktarabilirsiniz. Sade ve kullanışlı bir hayat kurma isteğinizi, aile içi ilişkilere taşıyabilirsiniz. Aile büyükleriyle yapacağınız konuşmalar, hane geliriniz, ailenizin talep ve ihtiyaçları gündeminizde yer bulabilir. Özellikle taşınma ya da alım satım gerektiren konularda ortak bir fikir bulmanız gerekebilir. Yapıcı ve mantıklı çözüm önerileriyle bu süreci daha rahat geçirebilirsiniz.",
    "27 Aralık'ta Chiron'un Koç burcunda ileri harekete geçişi ile kurduğunuz ilişkileri daha farklı bir gözle mercek altına alabilirsiniz. Her ilginin bir sevgi işareti olmadığını, acele etmemeniz gerektiğini kabul ediyorsunuz. Bu sizin için zor olabilir ama retro dönemindeki tutumlarınız şimdi her şeyi değiştirebilir. Yaşadıklarınızı gözardı etmeyin, yaptığınız hataları ya da size yapılan hataları anlamaya çalışın. Kendinizle mutlu olmanın önüne geçen, sizi tek başınıza bir şey yapmaktan alıkoyan, imkanlarınızı ve değerlerinizi suistimal eden insanlardan sıyrılacak özgüvene kavuşuyorsunuz. Daha doğrusu, bu özgüvene sahip olduğunuzu idrak ediyorsunuz. Hayatınıza bir insan almadan önce sadece sevginin değil, saygı ve anlayışın da karşılıklı olması gerektiğini bilerek hareket etmelisiniz. İş hayatında bir arada olduğunuz insanlara, hukuksal mücadele verdiğiniz kişilere de benzer davranışları sergileyebilirsiniz. Sizin duruşunuzun değişmesi onların da dikkatini çekecek ve bir değişime gitmelerinin önünü açacaktır.",
    "27 Aralık'ta Yengeç burcundaki dolunay ile kariyerinizi etkileyecek kararları netleştirmeye başlayabilirsiniz. Bazı kararları istemeden, mecbur kalarak vermiş olabilirsiniz. Ancak dolunay etkilerinde iken, bunun gerekli ve önemli olduğunu fark edebilirsiniz. Yaptığınız iş, geliriniz, bulunduğunuz ortam konusunda yenilikler yapmanız gerekebilir. Bu değişikliğin haberini ya da sinyalini daha önce aldıysanız, şu an geldiğiniz noktanın farkında olarak ilerlemelisiniz. Parasal konular, aile ile yapılan işlerdeki mal/kazanç paylaşımları, diğer maddi sorumluluklar konusunda hesabınızı iyi yapmalısınız. Gecikmeli borçlara, alınması gereken ödemelere göre plan yapmanız gerekebilir; mevcut durumunuzu bilerek hareket etmeniz daha sağlıklı olacaktır",
    "29 Aralık'ta yönetici gezegeniniz Venüs'ün Yay burcuna geçmesiyle beraber düşünceleriniz ve bunlarla ilgili uygulamalarınız hız kazanıyor. Kabuğunuzdan, sınırlarınızdan çıkıyorsunuz. Bu sınırdan çıkma işi sadece metafor değil, fiziksel olarak da yolculuklar yapabileceğiniz, yeni yerler görüp farklı imkanlarla karşılaşabileceğiniz bir dönemdesiniz. Dolayısıyla bunun için gerekli araçlarınızı, eşyalarınızı ve evraklarınızı da hazırlamanız gerekecektir. Merkür retrosunun hala devam ettiğini unutmadan, önleminizi alarak daha dikkat ederek hareket etmenizde fayda var. 2024'ün ilk haftaları bu konuda daha rahat sonuç almanıza imkan tanıyabilir. Bu süreç içerisinde üzerinde çalıştığınız işleri doğru seçmeli ve doğru hazırlık yapmalısınız. Kitap, sosyal medya, danışmanlıklar, e ticaret gibi konularda şansınız yüksek olabilir. Bunları bizzat yapan olmasanız da, yapan birileriyle tanışabilir ve katkıda bulunabilirsiniz. Bu durum, kendi yapabileceklerinize de ilham olabilir. Duygusal ve sosyal etkileşimlere açıksınız; alacağınız teklifleri değerlendirmeye çalışın."
]

akrep = [
    "6 Aralık'ta Neptün'ün Balık burcunda ileri hareketine başlamasıyla, yoğun hislerinizi ve sezgilerinizi nasıl kullanmanız gerektiğini daha iyi görebilirsiniz. Hayatınızı, sezgileri kural gibi değil öneri mahiyetinde kullanarak yaşamayı deneyimliyorsunuz. Bunun yaptırdığı hataları, düşürdüğü zorlukları ve kaybettirdiklerini daha iyi anlayabilirsiniz. Kendinizi aynı resmin içinde bir kez daha görmemek için gerçek olandan, hayatın gerekliliklerinden uzaklaşmamalısınız. Duygusal konularda bir adım atmadan önce karşınızdaki kişi adına düşünmek ya da karar vermekten vazgeçmelisiniz. Emin olmak isterken yanlış düşüncelerin ve şüphelerin ortasında kalabilirsiniz. Bunu sonlandırmak için konuşmayı, paylaşmayı ve gerektiğinde bırakabilmeyi alışkanlık haline getirmelisiniz. Ekonomik konularda yeni hamleler yapmak, var olan çalışmaları geliştirmek ya da bir becerinizi profesyonel boyuta taşımak için hazır olduğunuzu görebilirsiniz. Hayalinizi emekle, sorumlulukla gerçekleştireceğinizi unutmayın.",
    "13 Aralık'taki Yay yeniayı ile beraber ekonomik açıdan yüzünüz gülmeye başlıyor. Geride ne kalmış olursa olsun, artık önünüze bakmaya hazırsınız ve bu kez daha iyi bir şekilde ilerleyebilirsiniz. Sadece iş yapmak, işe girmek değil yaptığınız/yapacağınız şeyi büyütmek, daha geniş alanlara yaymak konusunda da pek çok fırsat yakalayabilirsiniz. Anlaşmalar, çevreyle daha iyi ilişkiler, ortaklıklar gündeminize gelebilir. Bu konuya daha yakın ve sıcak olduğunuzu fark ettiğinizde potansiyelinizi daha iyi kullanabilirsiniz. Hayatınızı yanlış olandan ve mutlu etmeyen şeylerden arındırmak istediğiniz bir hafta olabilir. Önemli kararlar almak isteyebilirsiniz. Geleceğinizi güvence altına almak, başkalarına ilham olmak ve toplum odaklı çalışmalar hazırlamak için birçok projeniz, kapınız ve bunlara gelen desteğiniz olabilir. Tutumlarınızda ve cömertliğinizde abartıya kaçmadıkça, insanların size verdiğin değerin farkında oldukça üzülme oranınız da azalacaktır. Bunu göz önünde bulundurmayı unutmayın.",
    "13 Aralık'ta Merkür'ün Oğlak burcunda geri hareketine başlamasıyla hangi fikirden, hangi konudan hareketle bir şeyler yapacağınıza dikkat etmelisiniz. Sorunlu olsa da bunları yönetebilecek bir dönemde olduğunuz için sadece dikkatli, özenli ve kuralları bilen biri olmak sizin kurtarıcınız olacaktır. Araç gereçler, ulaşım konuları ve yolculuklar, imza gerektiren işlerde kendi bildiğinizden önce olması gerekene ya da sizden istenene odaklanmanızda fayda var. Önyargılı olmanın, hem ilişkilerde hem de parasal konularda olumsuz sonuçlar doğuracağını unutmayın. Öğrenmeye, anlamaya, empatiye, başka fikirleri dinleyip önemsemeye daha çok zaman ayırmanız gerekebilir. Bir yere yetişme telaşı taşır gibi hareket etmek yerine daha sakin olmanız, sıralama yapmanız zamanı daha iyi kullanmanıza yardımcı olabilir. Riskli gördüğünüz, bir zemine oturtamadığınız konular ve konuşmalar üzerinde fazla zaman kaybetmeyin. Hayatınıza doğrudan etkisi olan, paylaşım halinde olduğunuz ve kendinize yakın gördüğünüz kişilerle aranızda geçecek konuşmalar önemli olabilir. Öğrenecekleriniz, unuttuğunuzu sandıklarınız sizde şok etkisi yaratabilir.",
    "22 Aralık itibariyle Güneş'in Oğlak burcunda hareket edecek olmasıyla tecrübeli olduğunuz konularla ilgili daha çok konuşabilir, buna yönelik işler yapmaya başlayabilirsiniz. Kaliteli ve saygın bir çevre oluşturma, buna yakışır davranışlar edinme konusunda kendinizi yetiştirmek isteyebilirsiniz. Hem çalışma hem sosyal hayatınızı hareketlendirecek gelişmeler yaşanabilir. Tanıştığınız insanlar ya da yakın çevrenizin vesilesiyle yeni işler alabilirsiniz. Yatırım ve borsa, danışmanlık, yönetici pozisyonları ilginizi çekebilir ya da iş kurma fikirlerinizi bu alanlarda değerlendirebilirsiniz. Bu konuda kardeşlerinizin, yakın aile üyelerinizin ya da aile büyüklerinizin desteğini alabilirsiniz. Hem maddi hem manevi açıdan bu desteğin nereden, nasıl geleceğini daha iyi görebilirsiniz. Bu da size ikili ilişkileri hangi dinamikte tutmanız gerektiğini daha iyi anlatabilir. Başvurularınızın sonuçlanması, emeklerinizin karşılığını alma, cihazlarınızı yenileme, kazancınızı arttırma gibi konularla ilgilenebilirsiniz. Ancak Güneş'in geri hareketteki Merkür ile kavuşacağını unutmadan, temkinli olmanızda fayda var. Yanlış anlaşılmalar, dikkat edilmeyen yazım hataları, zamanı geçen işlem ve ödemeler, sosyal mecralardaki sorunlar başınızı ağrıtabilir. Her zamankinden daha dikkatli olmanız gerekebilir. Gözlem yeteneğinize olan güveniniz, önyargılı olmanıza ve bu yüzden bazı noktaları kaçırmanıza neden olabilir. Karşı tarafı dinlemeden hareket etmemelisiniz. Eğer karşı taraf olan sizseniz, hakkınızda söylenenler karşısında doğru ifadeler seçmeye özen göstermelisiniz. Kırıcı ve baskıcı bir tutum size kayıplar yaşatır. Kazanmaya, yol almaya açık olduğunuz bir dönemdesiniz; bunun farkında olun.",
    "Koç burcundaki Chiron'un 27 Aralık itibariyle ileri hareket edecek olmasıyla sağlık konularında yaşadığınız zorlukların sonuna gelebilirsiniz. Artık iyileşmek kadar, sizi bu iyilik halinden uzak tutan konularla da ilgilenmeniz gerektiğini fark ediyorsunuz. Beslenme alışkanlıklarınızı düzenlemelisiniz. Duygusal sorunların buna etki etmemesi için bir uzmanla görüşmeniz alacağınız faydayı arttırabilir. Dış görünüşünüz hakkında kendi kendinizi baskıladığınızı, istediğiniz sonucu alamadığınızda da hırslandığınızı görebilirsiniz. Bu hırsa iyi enerjiye dönüştürmek için şimdi harekete geçin. Spora başlamak, yürüyüş yapmayı alışkanlık haline getirmek size yardımcı olabilir. Anlık keyif veren, kısa vadede iyi hissetmenizi sağlayan alışkanlıklar yerine bedeninizin, hayatınızın ihtiyaçlarına göre kalıcı alışkanlıklar geliştirmelisiniz. Bu fikirleri yaşamınızın her alanına taşıyabileceğiniz bir dönemdesiniz. Çalışma hayatınız, sorumluluklarınız konusunda beklediğiniz değişimler bu şekilde gelecektir. İşbirlikleri, mevcut çalışmalarınızın neticeleneceği gelişmeler yaşayabilirsiniz.",
    "27 Aralık'ta Yengeç burcunda gerçekleşecek dolunay ile bazı defterler kapanıyor. Neye inandıysanız elinizde kalmış gibi hissedebilirsiniz. Dostluk, duygusal konular, işbirlikleri gibi konularda emek verip karşılığını alamadığınızda mutsuz olabilirsiniz. Bu yüzden artık neye ne kadar inanacağınızı, neye emek vereceğinizi daha doğru ve akılcı seçmeniz gereken bir süreçtesiniz, bunun farkında olun. Kendinize yeni bir vizyon tanımlamak isteyebilir, araştırmalar yapabilir, hobilerinizi ya da küçük çaplı uğraşlarınızı genişleteceğiniz platformlara katılabilirsiniz. Bildiğinizin, güvendiğinizin dışında bir hayat olduğunu göreceksiniz. Bulunduğunuz yerden taşınma, kısa ya da uzun süreli seyahatler gündeminizde yer bulabilir. İhtiyaçlarınızı, planlarınızı gözeterek karar vermenizde fayda var. Bu süreçlerle ilgili resmi işlemlerinizi sonuçlandırmanız ya da tekrar düşünmeniz gereken noktalara hazırlıklı olun.",
    "29 Aralık'ta Venüs'ün burcunuzdan ayrılıp Yay burcuna geçmesiyle hayatı kendinize göre yaşamanın yollarını arayıp bulabilirsiniz. Sizin için ve hayatınızdaki insanlar için renkli, heyecanlı bir dönem olabilir. Emeklerinizin karşılığını alabilir ve bunu ertelediğiniz istekleriniz için kullanabilirsiniz. Ödemelerinizi, sorumluluklarınızı tamamlamadan arta kalan zamanı ve imkanları doğru değerlendirmeye çalışın. Düşünmeden yapacağınız harcamaların sonrasında sizi sıkıntıya uğratmaması için buna dikkat etmenizde fayda var. Nasıl hissederseniz her şeyi öyle şekillendireceğinizi fark ediyorsunuz. Bu da kendi üzerinizde kurduğunuz baskıyı azaltmanız, yok etmeniz için size bazı fırsatlar getirecektir. Gezme, ihtiyaçları karşılama, kendi işiniz ya da hobinizle ilgili yatırım yapma, evlilik gibi konular gündeminizde yer bulabilir."
]

yay = [
    "İhtiyacın ne olduğunu bildiğinizde, neyin bunu karşılayacağını ve karşılamayacağını da göreceksiniz. Bu da arınmanızın önünü açacaktır. Gizli ilişkiler, çevrenizdeki insanlardan öğreneceğiniz sürpriz bilgiler, bir haksızlığın önünüze gelmesi gibi konularla karşılaşabilirsiniz. Yapıcı bir sorgulama ve araştırma ile her şeyi daha net ve doğru bir şekilde öğrenebilirsiniz. Bu sizi kuruntu ve takıntılardan koruyacaktır. Farklı insanlarla görüşerek ve ihtiyaç sahibi kişilerle bir araya gelerek hem insanlara olan yaklaşımlarınızı değiştirebilir hemde mevcut imkanlarınızı kullanarak nasıl ve hangi konularda fayda sağlayacağınızı görebilirsiniz. Emin olmadığınız, garanti altına almadığınız ve somut bir şekilde elde etmediğiniz hiçbir şey için heveslenmemeye dikkat etmeli, ağzınızdan çıkacak sözlere ve bu sözleri duyuracağınız yerlere özen göstermelisiniz.",
    "6 Aralık'ta Neptün'ün Balık burcunda ileri hareketine başlamasıyla kendinizin ve tutumlarınızın farkında olduğunuz kadar kazanım elde edeceğiniz bir sürece giriyorsunuz. Koşulsuz kabul ettiğiniz, sevdiğiniz saydığınız kişilerin size aynı şekilde yaklaşmadığını gördüğünüzde bunu halının altına atmamalısınız. Ailevi konulardaki sorumluluğu tek başınıza üstlenmemelisiniz. Bu sizi bir ayrışmaya değil, tam tersi bir arada olmaya ve beraber hareket edebilmeye teşvik etmelidir. Bu yüzden birbirinizin düşüncelerini bilerek ilerlemenizde fayda var. İş ve ev düzeniniz hakkında bazı sorgulamalar yapabilirsiniz. Aldığınız kararların neticelerini daha iyi göreceğiniz bir dönemdesiniz. Bir değişikliğe gitmeniz gerekenleri noktalara daha rahat odaklanabilirsiniz. Taşınma, alım satım gibi yaşam düzeninizi etkileyecek konular hız kazanabilir, önünüzdeki engellerin kalktığını, maddi ve manevi olarak daha rahat hazırlanabileceğinizi görebilirsiniz. Hiçbir şeyin boşu boşuna ve gecikmeli olmadığını, her şeyin bir sebeple ve belli bir zamanda hayatınızda yer aldığını fark edeceksiniz.",
    "13 Aralık'ta yılın son yeniayı sizin burcunuzda gerçekleşiyor. Bir kapı kapatıp bir kapıyı açma fikrini fazlaca benimseyebilirsiniz. Sizin için her şeyin daha farklı olacağını hissedebilir, bu hissi somutlaştıracak işlere imza atabilirsiniz. Değişime ve yenilenmeye kendinizden başlayabilirsiniz. Fiziksel görüntünüz, tarzınız, giyim tercihleriniz, bulunduğunuz çevre, aldığınız eğitim, yapacağınız iş gibi konular önceliğiniz olabilir. Enerjik ruh haliniz daha da katlanabilir. Bunu doğru kullanmak için spora başlayabilir, etkinliklere katılabilir, beden gücü gerektiren işler yapabilirsiniz. Ancak kendinizi ve şartları fazlaca zorladığınızda kazalara davetiye çıkaracağınızı unutmayın. Fiziksel ve ruhsal olarak sinir sisteminize, dayanıklılığınıza sahip çıkmalı ve dikkat etmelisiniz. Alışkanlıklarınızı değiştirmek için öncelikle isteklerinizi değiştirmeniz gerektiğini idrak ediyorsunuz. Bu da size yeni başlangıçları getiriyor. İş hayatı, ortaklıklar, aile ve ilişkiler gibi konularda dikkat çekici hamleler yapabilirsiniz. Çevresel faktörlerden ve hayatınıza dahil ettiğiniz insanlardan öğrendiklerinizi unutmadan ilerlemelisiniz. Sorumlulukların, çalışma alanlarının değişimi gibi gelişmelerle karşılaşabilirsiniz. Maddi ve manevi açıdan tutumlu olmayı, sınırı aşmamayı ve birden heyecanla, yüksek duygularla hareket etmeyi rutinleştirmelisiniz.",
    "13 Aralık'ta Merkür'ün Oğlak burcundaki geri hareketi ekonomik konularda almanız gereken tedbirleri size gösterebilir. Hazırlığını iyi bir şekilde yapacağınız her işin getirisi de iyi olacaktır. Bu açıdan elinizdeki imkanları bilerek, bunların gerekliliklerine uymaya çalışarak ilerlemenizde fayda var. Muhasebe ve gelir gider işlemlerinde bir bilene danışmanız daha iyi sonuç almanıza yardımcı olabilir. Farklı ve ikinci bir göz hata payınızı en aza düşürecektir. Para sizin için her zaman bir araçtır, bunu amaca dönüştürmediğiniz için şimdi bazı kayıplar ya da aksamalar yaşamaktan olumsuz etkilenmeyeceksiniz. Ancak buradaki tutumunuzu insan ilişkilerinde de göstermenizde fayda var. Bazı insanların size, sizin düşündüğünüz kadar değer vermediğini, hakkınızı gözetmediğini fark edebilirsiniz. Bu ertelenmiş bir konuysa, görmezden geldiyseniz şimdi sert bir şekilde bununla yüzleşebilirsiniz. Kendi halinizde kalmaya, olaylara dışarıdan bir gözle bakmaya çalışın. Böylece insanların düşüncelerini ve ilişkilerinizi daha iyi anlayabilirsiniz. Beslenme de olduğu gibi değer kavramı konusunda da sağlıklı seçimler yapma zamanının geldiğini görebilirsiniz.",
    "22 Aralık'ta Güneş'in burcunuzdan ayrılıp Oğlak burcunda seyredecek olmasıyla artık çalışmalarınızı geliştirip bir düzene dönüştürmeye başlıyorsunuz. Bu düzende, hem kazanacağınız hem de hayatınızı iyileştirecek gelişmelerle karşılaşabilirsiniz. Bilgi ve deneyim kullanılmadığında yükleşir, bu yük de zamanla size ağırlık yapar. Kendinize yaptığınız yatırımın, biriktirdiğiniz motivasyonun sahneye çıkmasına izin verin. Maddi kaynaklarınızı büyütebilir, yeni kazanç kapıları açabilir, ödemelerinizi düzene sokabilir, mevcut çalışmalarınızı ilerletebilirsiniz. Aile desteği aldığınız konuları daha kalıcı hale getirmek için de projeler üretebilirsiniz. Bir ek işin ana işe dönüşmesi için çalışabilirsiniz. Çalışma ve bunun karşılığını alma odaklı yaşayacaksınız. Kulağa hoş gelse de, hayatın sadece bu iki konu üzerinden gitmeyeceğini unutmamalısınız. Yüksek standartlar kurmak, herkese fayda sağlamak isterken stres nedeniyle ya da tek odak noktasıyla ilerlerken yanlış anlaşılabilirsiniz. Özellikle Güneş'in geri hareketteki Merkür ile kavuşumu bu durumu tetikleyebilir. Hesabınızı doğru yapmaya, alma verme dengesini doğru kurmaya çalışmalısınız. Bunu sadece maddi konularda değil duygusal ve sosyal alanlarda da uygulamayı öğrenmelisiniz. Eğer buna direnç gösterdiyseniz, daha önce karşılaştığınız bazı olumsuzluklar ve hak kayıplarının yeniden gündeme gelmesiyle şimdi daha iyi anlayabilirsiniz. Yüklü harcamalar yapmamaya, kesinleşmeyen işleri duyurmamaya çalışın. Bunun size verilen bir fırsat olduğunu düşünün ve kesin çözümler bulun. Neyi konuştuğunuz, neyi sunduğunuz önemli olacaktır.",
    "27 Aralık'ta Chiron'un Koç burcunda geri hareketini sonlandırması size de kendi hayatınızda neyi sonlandırmanız gerektiğini gösterecektir. Fedakar ve beklentisiz yaklaşımlarınızla başta iyi hissettirseniz de, sonrasında görmezden geleceğiniz sorunlar doğurabilir. Bunlarla başa çıkmak için yönünüzü başka bir yere çevirmemeniz gerektiğini öğrendiniz. Şimdi sevme şeklinizi, mutluluğunuzu riske atmadan kendinizi dönüştürüyorsunuz. Hayatınızdaki insanlarla, konularla aranızda bir denge kurmak istiyorsanız bunun için kendi tarafınıza da bir şeyler koymalısınız. Bir şeylerin eksikliğinin rahatsızlık uyandırdığı durumları fark edebilir, karşı tarafa bu konudaki duygusal beklenti ve ihtiyaçlarınızı dile getirebilirsiniz. Çünkü artık bunun bencillik olmadığının farkında olarak yaşamayı seçiyorsunuz. Sadeleşmeye, abartıdan kaçmaya, çıtaları düşürmeye özen göstermeli ve bunu kalıcı hale getirmelisiniz. Retro döneminde yaşadığınız hayal kırıklıkları, biten ilişkiler, gerçekleştiremediğiniz hayaller, gidemediğiniz yollar bu kalıcılığı sağlamanın öğretileriydi. Bunları yeniden ve daha farklı bir zihinle düşünerek sorunu çözebilirsiniz.",
    "27 Aralık'ta Yengeç burcunuzda gerçekleşecek dolunay ile beraber maddi konularda bir kontrol yapmanız gerekebilir. Elinize geçen imkanları anlık değerlendirmemeye, geliştirmeye çalışmalısınız. Bunu yapabildiğiniz işlerin olumlu geri dönüşlerini ve desteklerini alabilirsiniz. Açık verdiğiniz durumlar, tutmayan hesaplar konusunda da önleminizi şimdiden almalısınız; her zararın dönülecek bir yeri vardır. Aile üyeleriniz ve onların sağlık durumlarıyla ilgili konular gündeminize gelebilir, beklediğiniz iyi haberleri alabilirsiniz. Alışkanlıklarınızı ve düşüncelerinizi yeniledikçe bunun hayatınıza nasıl sirayet ettiğini göreceğiniz bir dönemdesiniz. Yakaladıklarınızı kaçırmayın.",
    "29 Aralık'ta Venüs'ün burcunuza geçmesiyle her halinizle dikkatleri çekeceğiniz bir döneme giriyorsunuz. Günler sonra dışarıya çıkmış gibi hissedebilirsiniz. Enerjiniz ve özgüveniniz yükseliyor. Düşüncelerinizi uygulamanın, hislerinizi paylaşmanın zamanındasınız. Yaşadığınız yeri, kullandığınız eşyaları, giysilerinizi değiştirebilirsiniz. Hayattan başka şeyler istemenin ve beklemenin, çabalarınızla güzelleşeceği bir süreçtesiniz. Bunu, yaşamak istedikleriniz için kullanmayı ihmal etmeyin. Taşınma, iş bulma ya da işinizi geliştirme, evlilik, yeni kişisel hedefler, dış görünüş gibi konulara zaman ve bütçe ayırmalısınız. Heyecanınızla ve yaptıklarınızla çevrenizin ilgisini toplayabilirsiniz. Bunu kullanın ve yeni deneyimler geliştirin, yetilerinizi değerlendireceğiniz alanlarda bulunun. Yarını düşünmeden hareket edeceğiniz zamanlar maddi zorluklar yaşamanıza neden olabilir. Merkür'ün burcunuzda gerilemeye devam ettiğini unutmadan, hesabınızı ve ne yaptığınızı, söylediğinizi bilerek hareket etmenizde fayda var."
]

oglak = [
    "Araştırma ve bilgi edinme konularındaki yeteneklerinizi kullanabilirsiniz. Kendinizi geliştirdikçe bunu kullanma isteğiniz daha da artacaktır. Çizdiğiniz bu yeni çizgi size bir yol olduğu kadar aynı zaman bir sınır olabilir. Toksikleşen, sizi yalnızlaştıran, yanlış anlamanıza ya da anlaşılmanıza sebep olan konuları bu sınırın dışında bırakmaya başlıyorsunuz. Bazı ilişkilerin, arkadaşlıkların veya ortaklıkların bitmesi başta üzücü, kabul edilemez gelse de hayatınız için elzem olduğunu fark edebilirsiniz. Kazanımlarınızı arttırmak varken bile bile kaybedeceğiniz bir durumun içinde kalmamalısınız. Yeni olandan, yenileyenden korkmayın.",
    "6 Aralık'ta Neptün'ün Balık burcunda ileri hareketine geçmesiyle beraber bazı kuralları ve görüşleri esnetmeyi öğrenebilir, öğrendiklerinizi uygulamaya başlayabilirsiniz. Kontrol etme ve bir hizada tutma isteğinizi sınırlandırmalı, farklı görüşlere ve deneyimlere fırsat tanımalısınız. Bu sizin hayata bakış açınızı hep bir ölçüde tutmaktan öteye götürecek, insanları ve konuları daha iyi değerlendirmenizi sağlayacaktır. İletişimde dalgınlıklar, yanlış anlaşılmalar, uzun bekleyişler sona eriyor. Giden zamanı telafi edemeseniz de kalan ve akan zamana neler katabileceğinizi yeniden düşünmelisiniz. Eğitimlerinize devam etmek, aracınızı ve kullandığınız cihazları yenilemek, yeni yerler görmek, farklı işlere dahil olmak, beklentileriniz kadar hayatın sunduklarını da deneyimlemek konusunda yeni fırsatlarınız olabilir. Sizi gerçekten rahatlatan insanların varlığını görüyorsunuz.",
    "13 Aralık'ta Yay burcunda gerçekleşecek yeniay biraz kenara çekilip kendinizi fark etmeniz için bir fırsat olabilir. Başkalarına, dışarıya koşarken kendiniz için adım bile atmadığınızı görebilirsiniz. Dinlenmek, sağlık sorunlarınızla ilgilenmek, bazı ilişkileri sorgulamak ve yeni kararlar almak için ideal bir zaman dilimindesiniz. İyileşmeye, daha yüksek bir enerjiyle hayata dönmeye hazırsınız; buna göre hareket etmelisiniz. Bazı fikirleri derinleştirebilir, üzerinde daha çok çalışabilir, bu konuyla ilgili kişilerle ya da büyükleriniz görüşerek yeni bakış açıları kazanabilirsiniz. Ne yaptığınızı anlamak ve yaptığınız işi en versiyonuna taşımak için bir süre düşüncelerinizi herkesle paylaşmamaya dikkat etmelisiniz. Paylaşmanız gereken asıl konu, rahatsız olduğunuz konular ve bunların muhataplarıdır. Kendi başınıza çözmeye çalıştığınız, bilerek yalnızlığa itildiğiniz, hakkınızın yendiği konularda tepkilerinizi dışa vurmak isteyebilirsiniz. Hem hukuki hem de manevi olarak bunların karşılığını alabilirsiniz. Etik ve doğru bir platformda hak arama mücadelesinde olduğunuz sürece doğru anlaşılabilirsiniz. Aksi halde öfke patlamaları, abartılı tutumlar, kontrol edilemeyen dürtüler size hata yaptırabilir. Canınızı sıkan, işlerinizi yolundan eden şeylerin tam olarak bunlar olduğunu veya bunları yapan insanlar olduğunu unutmamalısınız. Bir terapi süreci, uzman görüşü, hukuki ve astrolojik danışmanlıklar nasıl yol alacağınız konusunda size destek olabilir.",
    "13 Aralık'ta burcunuzda geri hareketine başlayacak olan Merkür, kendinizi öncelikli hale getirme sürecinizi destekleyebilir. Davranışlarınızı, tarzınızı, aldığınız geri dönüşleri düşünmeniz gerekebilir. Bir yerlerde, bir şeylerin sizin istediğiniz gibi sonuçlanmamasını objektif bir şekilde ele almalısınız. Kendinizde bir hata, eksiklik arama konusunda aşırı tepki vermemelisiniz. Önyargı, şüpheler, başkası adına düşünme veya karar verme sonucu ilişkilerinizde bazı pürüzler oluşabilir. Doğruluğundan emin olmadan, muhatabınızdan dinlemeden ve dinlediklerinize güvenmeden sağlıklı bir netice alamayabilirsiniz. Dolayısıyla önemli konuşmalar ve kararlar için aceleci olmamakta, karşınızdaki insana baskı uygulamamakta fayda var. Sorunları çözmek mi istiyorsanız yapıcı ve anlayışlı olun, bu insanların da size açık olması için bir zemin oluşturacaktır. Eşyalarınızı, kullandığınız malzemeleri, kozmetik seçimlerinizi değiştirmek yerine bir süre daha mevcut durumu devam ettirebilirsiniz. Özellikle fiziksel ve sağlık açısından bir karar almanız gerekiyorsa bu konunun uzmanıyla, bir doktorla hareket etmeniz daha iyi olacaktır.",
    "22 Aralık'ta Güneş'in burcunuza geçiş yapmasıyla bir kez daha 'ben bitti demeden bitmez' diyorsunuz. Tıkanıp kaldığınız, bir çözüm bulamadığınız, kendi imzanızı atamadığınız günlerin sonuna geldiniz. Bunca zaman neye emek verip neyin tecrübesini edindiyseniz şimdi önünüze bunlarla ilgili yeni fırsatlar çıkacaktır. Hem ayı hem yılı kapatmaya hazırlanırken neler yaşadığınızın bir muhasebesini yapabilirsiniz. Bu size yeni planlar için ilham olabilir. Kendinizde özenmeniz gereken konuları fark edebilir, eksiklerinizi kapatabilir, beklettiğiniz işleri gündeme getirebilirsiniz. Her zaman yoğun olsanız da bu sefer daha sonuç alıp dikkat çekebilirsiniz. Yeni görevler edinebilir, sorumluluk alanlarınızı genişletebilirsiniz. Bu da pek çok insanın size ulaşması için bir kapı aralayacaktır. Tutumlarınızdaki ciddiyeti kırmaya, iletişime önem vermeye çalışmalısınız. Özellikle ikili ilişkilerde, duygusal konularda bu durum daha fazla önemli ve gerekli olabilir. Çünkü yeni başlangıçlar sadece kariyer konusunda değil özel hayatınızda da gündeme gelecektir. Güneş'in burcunuzda gerileyen Merkür ile kavuşumu burada nelere dikkat etmeniz gerektiğini size daha iyi gösterebilir. Eski ilişkileriniz, işleriniz hatta eski stiliniz bile gündeminiz olabilir. Dün ve bugün arasında gelgitler yaşayabilirsiniz. Burada savrulmamak için neyin faydalı neyin faydasız olduğunu ayırmaya çalışın. Alacağınız kararları, söyleyeceğiniz sözleri buna göre belirleyebilirsiniz. Fiziksel konularda değişikliğe gidebilir, beslenme, spor, giyim tarzı ve estetik işlemleriyle ilgilenebilirsiniz. Güvenilir ve temiz tercihler yapmanız önemli olacaktır.",
    "27 Aralık'ta Chiron'un Koç burcunda ileri hareketine geçmesiyle yaşadığınız yer, bulunduğunuz ortam ve mensubu olduğunuz aile ilgili kaygılarınız sona eriyor. Bunlara karşı öfke duymayı değil, sizi öfkelendiren konuları çözmeyi deneyimliyorsunuz. Bakış açınızı bu şekilde değiştirmek kolay olmasa da sonuç almanız bu kadar zor olmayacaktır. Hem ailenizde hem de kendinizde bunun nedenlerini bulabilir ya da bulduklarınızı daha iyi anlayabilirsiniz. Yaşamın devamlılığı ve ihtiyaç duydığunuz istikrar için evinizde, ilişkilerinizde bazı değişimlere gidebilirsiniz. Bu evde daha çok vakit geçirmek, istediğiniz eşyaları ya da evi almak, evlenmek gibi konularla mümkün olabilir. Özgürlüğünüze ve kişisel alanlarınıza imkan tanıdığınızda, burada geçireceğiniz zamanı da güzelleştirebilirsiniz. Her şeyin elinizde, evinizde olduğunu unutmayın.",
    "27 Aralık'ta Yengeç burcunda gerçekleşecek dolunay ile beraber ikili ilişkileriniz için önemli bir viraja gelebilirsiniz. İkilemde kaldığınızı hissedebilirsiniz. Merkür'ün halen ileri harekete geçmemesi bu hissi kuvvetlendirebilir. İki kere düşünüp bir kez konuşmanız faydalı olacaktır. Bazı konuların yeniden gündeme gelmesi canınızı sıkabilir, sizi öfkelendirebilir. Her defasında nasıl davranıyorsanız onun düşünün. Bu sayede izlediğiniz bu yolun size bir faydasının olmadığını ve bu sefer de olmayacağını fark edeceksiniz. Ortaklıkların bitmesi, boşanma, sözleşme feshi gibi konular gündeminize gelebilir. Hukuksal konularda anlaşmadan ziyade çekişme ağır basabilir. Kendinizi ve işinizi daha iyi göstereceğinize inanın, güçlü durun. Bu halinizi kimin desteklediğini gördüğünüzde her şeyin değişmeye başladığını da göreceksiniz.",
    "29 Aralık'ta Venüs'ün Yay burcuna geçmesi kendinize döndüğünüzde daha iyi hissetmenize, kavgalarınızı durdurmanıza yardımcı olabilir. Hafiflemeye, daha az düşünmeye ihtiyacınız olduğunu fark edebilir ve bunun yollarını arayabilirsiniz. Daha önce yaptığınız işler, kurduğunuz bağlantılar ve kendinize kattığınız alışkanlıkların hayatınıza nasıl etki ettiğini göreceksiniz. Bu etkiye, iyi niyetli olmayan kişilerin söylemleri ile arkanızdan çevirilen dolaplar da dahil olabilir. İyi niyetinizi ve dürüstlüğünüzü bozmadığınız sürece daha az etkilenebilirsiniz. Adaleti sağlamak adına tek başınıza mücadeleye girmemeli, tecrübeli ve uzman kişilerden destek almalısınız. Enerjinizi işinize, fikirlerinize, ertelediğiniz seyahatlerinize, sağlık sorunlarınıza ve kişisel ihtiyaçlarınıza ayırın. Kendinizi iyi hissettiğinizde, çevreye yansıtacağınız şey de bunu başkalarına yaptırmak olacaktır. Yardım kuruluşları ve bunlarla ilgili çalışmalara zaman ayırabilir, sosyal sorumluluk projeleriyle ilgilenebilirsiniz.",
]


    
