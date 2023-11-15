from math import*
import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1/10)
def assure(n):
    if n < 0 or n > 10:
        slowprint("\033[1;36m...Gülməli deyil. Heç qımıldamadım. Heç üz əzələlərim gərilmədi... Aaa axı mən botam... Görən sahibim necə hiss edərdi bu qədər izahatdan sonra belə bir cavabı.")
    else:
        print("\033[1;36m"+str(n))
slowprint("\033[1;36mSalam! Siz temperament tipinizi öyrənmək istəyirsinizmi? Elə isə, yaxın əyləşin və suallara dürüst cavab verin! Narahat olmayın, tam ödənişsizdir)")
slowprint("\033[1;36mBunun üçün sadəcə sualları diqqətlə oxyub, 0-10 arası şkala üzrə cavab verin. 0-uyğun deyil, 10-tam uyğundur, bu üzrə 0-10 arası dəyişir.")
slowprint("\033[1;36mAmma bundan əlavə cavab götürə bilmərəm haaaaaaaaa :)")
slowprint("\033[1;36mBaşlamağa hazırsınız?")
sure=input()
if sure.lower() =="hə" or "bəli" or "yes" or "yep" or "da" or "да":
    slowprint("\033[1;36mOk, başladıram)")
else:
    slowprint("\033[1;36mFikrinizi dəqiqləşdirdikdən sonra yenidən başladın. Vaxt verirəm)")
    time.sleep(5)
    slowprint("\033[1;36mBaşladıram haaa")
a = int(input(slowprint("\033[1;36m1)Mən hər hansı bir vacib işdən qabaq əsəbiləşirəm.")))
assure(a)
b = int(input(slowprint("\033[1;36m2)Mən sıçrayışlı, mütəmadi olmayaraq işləyirəm.")))
assure(b)
c=int(input(slowprint("\033[1;36m3)Bir işdən digərinə çox tez keçə bilirəm.")))
assure(c)
d = int(input(slowprint("\033[1;36m4)Əgər lazımdırsa, mən sakit gözləyə bilərəm.")))
assure(d)
e = int(input(slowprint("\033[1;36m5)İşlərim alınmayanda, çətinliklərdə təsəlliyə və köməyə ehtiyacım var.")))
assure(e)
f = int(input(slowprint("\033[1;36m6)Həmyaşıdlarımla söhbət zamanı özümdən tez çıxıram.")))
assure(f)
g = int(input(slowprint("\033[1;36m7)Mənim üçün seçim etmək çətin deyil.")))
assure(g)
z = int(input(slowprint("\033[1;36m8)Mən öz emosiyalarımı gizlətmirəm, bu öz-özünə baş verir.")))
assure(z)
slowprint("\033[1;36mCavabların vaxtıdır... Hiss edirəm heheheeee")
slowprint("\033[1;36mNəysə, cavabların nəticəsi:")
na = a+e
gi = b+f
to = c+g
ko=d+z
slowprint("\033[1;36mMelanxolik = "+str(na))
slowprint("\033[1;36mXolerik = "+str(gi))
slowprint("\033[1;36mSanqvinik = "+str(to))
slowprint("\033[1;36mFleqmatik = "+str(ko))
if na>gi:
    if na>to:
        if na>ko:
            slowprint("\033[1;36mTəbriks, siz təmiz melanxoliksiniz! Belə çıxır ki, siz küsəyən, bədbin, passiv, depressiyaya meyilli, qətiyyətsiz, əsasən mənfi emosiyalı, adamayovuşmaz, səksəkəli və ehtiyatlısınız.")
            slowprint("\033[1;36mƏlavə olaraq, sizə uyğun peşələr: araşdırmalar, incəsənət, təbiətşünaslıq, mühasibatlıq, administrasiya işləridir. Diqqətə görə sonsuz təşəkkürlər)")
elif gi > na:
    if gi > to:
        if gi > ko:
            slowprint("\033[1;36mTəbriks, siz təmiz xoleriksiniz! Belə çıxır ki, siz qıcıqlı, nikbin, enerjili, qətiyyətli, inadkar, tezcoşan və öz hərəkətlərinə fikir verməyən insansınız.")
            slowprint("\033[1;36mƏlavə olaraq, sizə uyğun peşələr: biznes, hüquq, texnologiya, mühafizəkarlıq, menecer, mühəndizlik və statistika üzrə işlərdir. Diqqətə görə sonsuz təşəkkürlər)")
elif to > gi:
    if to > na:
        if to > ko:
            slowprint("\033[1;36mTəbriks, siz təmiz sanqviniksiniz! Belə çıxır ki, siz ünsiyyətci, təmkinli, təşəbbüskar, hər şeyi bilmək istəyən, dünyagörüşlü, enerjili, soyuqqanlı və qayğısızsınız.")
            slowprint("\033[1;36mƏlavə olaraq, sizə uyğun peşələr: marketinq, müştəri xidmətləri, səyahət, idman və əyləncə sahələri üzrə işlərdir. Diqqətə görə sonsuz təşəkkürlər)")
elif ko > gi:
    if ko > to:
        if ko > na:
            slowprint("\033[1;36mTəbriks, siz təmiz fleqmatiksiniz! Belə çıxır ki, siz passiv, canyandıran, dərindüşüncəli, dinc, etibarlı, rəvan, sakittəbiətli və inadkarsınız.")
            slowprint("\033[1;36mƏlavə olaraq, sizə uyğun peşələr: tibb, təhsil, psixoloqiya, ofis işləri, assistent rolları, insan və ya sosial servislər üzrə işlərdir. Diqqətə görə sonsuz təşəkkürlər)")
elif na == gi:
    slowprint("\033[1;36mHmm... sizdə iki temperament tipinin xüsusiyyətlərinə rast gəlinir. O zaman hər iki tipə məxsus məlumatları əlavə edirəm: ")
    slowprint("\033[1;36mMelanxolik: siz küsəyən, bədbin, passiv, depressiyaya meyilli, qətiyyətsiz, əsasən mənfi emosiyalı, adamayovuşmaz, səksəkəli və ehtiyatlısınız.")
    slowprint("\033[1;36mƏlavə olaraq, melanxolikə uyğun peşələr: araşdırmalar, incəsənət, təbiətşibatlıq, administrasiya işləridir.")
    slowprint("\033[1;36mXolerik: siz qıcıqlı, nikbin, enerjili, qətiyyətli, inadkar, tezcoşan və öz hərəkətlərinə fikir verməyən insansınız.")
    slowprint("\033[1;36mƏlavə olaraq, xolerikə uyğun peşələr: biznes, hüquq, texnologiya, mühafizəkarlıq, menecer, mühəndizlik və statistika üzrə işlərdir. Diqqətə görə sonsuz təşəkkürlər)")
elif gi == to:
    slowprint("\033[1;36mHmm... sizdə iki temperament tipinin xüsusiyyətlərinə rast gəlinir. O zaman hər iki tipə məxsus məlumatları əlavə edirəm: ")
    slowprint("\033[1;36mXolerik: siz qıcıqlı, nikbin, enerjili, qətiyyətli, inadkar, tezcoşan və öz hərəkətlərinə fikir verməyən insansınız.")
    slowprint("\033[1;36mƏlavə olaraq, xolerikə uyğun peşələr: biznes, hüquq, texnologiya, mühafizəkarlıq, menecer, mühəndizlik və statistika üzrə işlərdir.")
    slowprint("\033[1;36mSanqvinik: siz ünsiyyətci, təmkinli, təşəbbüskar, hər şeyi bilmək istəyən, dünyagörüşlü, enerjili, soyuqqanlı və qayğısızsınız.")
    slowprint("\033[1;36mƏlavə olaraq, sanqvinikə uyğun peşələr: marketinq, müştəri xidmətləri, səyahət, idman və əyləncə sahələri üzrə işlərdir. Diqqətə görə sonsuz təşəkkürlər)")
elif to == ko:
    slowprint("\033[1;36mHmm... sizdə iki temperament tipinin xüsusiyyətlərinə rast gəlinir. O zaman hər iki tipə məxsus məlumatları əlavə edirəm: ")
    slowprint("\033[1;36mSanqvinik: siz ünsiyyətci, təmkinli, təşəbbüskar, hər şeyi bilmək istəyən, dünyagörüşlü, enerjili, soyuqqanlı və qayğısızsınız.")
    slowprint("\033[1;36mƏlavə olaraq, sanqvinikə uyğun peşələr: marketinq, müştəri xidmətləri, səyahət, idman və əyləncə sahələri üzrə işlərdir.")
    slowprint("\033[1;36mFleqmatik: siz passiv, canyandıran, dərindüşüncəli, dinc, etibarlı, rəvan, sakittəbiətli və inadkarsınız.")
    slowprint("\033[1;36mƏlavə olaraq, fleqmatikə uyğun peşələr: tibb, təhsil, psixoloqiya, ofis işləri, assistent rolları, insan və ya sosial servislər üzrə işlərdir. Diqqətə görə sonsuz təşəkkürlər)")
elif na==to:
    slowprint("\033[1;36mHmm... sizdə iki temperament tipinin xüsusiyyətlərinə rast gəlinir. O zaman hər iki tipə məxsus məlumatları əlavə edirəm: ")
    slowprint("\033[1;36mMelanxolik: siz küsəyən, bədbin, passiv, depressiyaya meyilli, qətiyyətsiz, əsasən mənfi emosiyalı, adamayovuşmaz, səksəkəli və ehtiyatlısınız.")
    slowprint("\033[1;36mƏlavə olaraq, melanxolikə uyğun peşələr: araşdırmalar, incəsənət, təbiətşibatlıq, administrasiya işləridir.")
    slowprint("\033[1;36mSanqvinik: siz ünsiyyətci, təmkinli, təşəbbüskar, hər şeyi bilmək istəyən, dünyagörüşlü, enerjili, soyuqqanlı və qayğısızsınız.")
    slowprint("\033[1;36mƏlavə olaraq, sanqvinikə uyğun peşələr: marketinq, müştəri xidmətləri, səyahət, idman və əyləncə sahələri üzrə işlərdir. Diqqətə görə sonsuz təşəkkürlər)")
elif na==ko:
    slowprint("\033[1;36mHmm... sizdə iki temperament tipinin xüsusiyyətlərinə rast gəlinir. O zaman hər iki tipə məxsus məlumatları əlavə edirəm: ")
    slowprint("\033[1;36mMelanxolik: siz küsəyən, bədbin, passiv, depressiyaya meyilli, qətiyyətsiz, əsasən mənfi emosiyalı, adamayovuşmaz, səksəkəli və ehtiyatlısınız.")
    slowprint("\033[1;36mƏlavə olaraq, melanxolikə uyğun peşələr: araşdırmalar, incəsənət, təbiətşibatlıq, administrasiya işləridir.")
    slowprint("\033[1;36mFleqmatik: siz passiv, canyandıran, dərindüşüncəli, dinc, etibarlı, rəvan, sakittəbiətli və inadkarsınız.")
    slowprint("\033[1;36mƏlavə olaraq, fleqmatikə uyğun peşələr: tibb, təhsil, psixoloqiya, ofis işləri, assistent rolları, insan və ya sosial servislər üzrə işlərdir. Diqqətə görə sonsuz təşəkkürlər)")
elif gi == ko:
    slowprint("\033[1;36mHmm... sizdə iki temperament tipinin xüsusiyyətlərinə rast gəlinir. O zaman hər iki tipə məxsus məlumatları əlavə edirəm: ")
    slowprint("\033[1;36mXolerik: siz qıcıqlı, nikbin, enerjili, qətiyyətli, inadkar, tezcoşan və öz hərəkətlərinə fikir verməyən insansınız.")
    slowprint("\033[1;36mƏlavə olaraq, xolerikə uyğun peşələr: biznes, hüquq, texnologiya, mühafizəkarlıq, menecer, mühəndizlik və statistika üzrə işlərdir.")
    slowprint("\033[1;36mFleqmatik: siz passiv, canyandıran, dərindüşüncəli, dinc, etibarlı, rəvan, sakittəbiətli və inadkarsınız.")
    slowprint("\033[1;36mƏlavə olaraq, fleqmatikə uyğun peşələr: tibb, təhsil, psixoloqiya, ofis işləri, assistent rolları, insan və ya sosial servislər üzrə işlərdir. Diqqətə görə sonsuz təşəkkürlər)")
else:
    slowprint("\033[1;36mBəlkə, testi yenidən və dəqiq götürəsiniz?")