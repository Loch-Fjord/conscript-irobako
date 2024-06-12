import turtle
import math

wagahai = 'wagahaiwanekodearu.namaewamadanai.dokodeumaretakatontokentougatukanu.nandemousuguraijimejimesitatokorodeniyaaniyaanaiteitakotodakewakiokusiteiru.wagahaiwakokodehajimeteningentoiumonowomita.sikamoatodekikutosorewasiyoseitoiuningentiyuudeitibandouakunasiyuzokudeattasouda.'
wagahai = 'wagahaiwanekodearu.namaewamadanai.dokodeumaretakatontokentougatukanu.nandemousuguraijimejimesitatokorodeniyaaniyaanaiteitakotodakewakiokusiteiru.wagahaiwakokodehajimeteningentoiumonowomita.sikamoatodekikutosorewasiyoseitoiuningentiyuudeitibandouakunasiyuzokudeattasouda.'

wagahai = 'hitoribottinokakeoti.kimikakeotittesitakotoarukai.nai.soudarouna.arewaaiteganakiyadekinaimondakarane.jiyaiedegurainara.aruttehitomotasiyouwairunjiyanaika.maabokudattebetuniiedeyakakeotiwosusumeyouttewakejiyanai.'

#wagahai = 'aiueokakikukekosasisusesotatitutetonaninunenohahihuhehomamimumemoyaayuayoararirurerowaanawo.aaaaagagigugegozajizuzezodadidudedoaaaaapapipupepobabibubeboaaaaaaaaaaaaaaa.'

wagahai = ('irobako.')

#                 a        i         u          e         o      blankness
colors_hex = ['#F47068','#FFB3AE','#1697A6','#0E606B','#FFC24B','#f4f1de']
colors_hex = ['#01130F','#FAEEB3','#F3AE53','#0F97D2','#086F72','#FFFFFF']
colors_hex = ['#081905','#255D14','#4AA022','#993DD6','#B481E4','#D8C4F3']
#colors_hex = ['#ff99c8','#fec8c3','#fcf6bd','#a9def9','#e4c1f9','#f4f1de']
#colors_hex = ['#010304','#1C454F','#CE2212','#40918F','#BA7D8D','#FED8B9']
#colors_hex = ["#ffee65","#ffb55a", "#bd7ebe", "#beb9db", "#8bd3c7", "#fdcce5"]#ffee65
#colors_hex = ["#ffb400", "#22a7f0", "#63bff0", "#a7d5ed", "#e14b31", "#e2e2e2"]

vowels = ['a','i','u','e','o']

outline_pos = 0

stora = ['#FFF4F1',(255,244,241)]
colors_rgb = []

left_ness = 300

background_hex = colors_hex[5]

consonant_codes = {'k':'oxxxx',
                   'g':'xoxxx',
                   's':'ooxxx',
                   'z':'xxoxx',
                   't':'oxoxx',
                   'd':'oooxx',
                   'n':'xxxox',
                   'h':'oxxox',
                   'b':'ooxox',
                   'p':'xxoox',
                   'm':'oxoox',
                   'y':'xxxxo',
                   'r':'oxxxo',
                   'w':'ooxxo',
                   'j':'oxoxo'}

dakuten_list = {'g':'k',
                'z':'s',
                'd':'t',
                'b':'h',
                'j':'s'}

blank = 'xxxxx'
nn = 'xxooo'
nn = 'ooooo'

for color in colors_hex:
# from https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    h = color.lstrip('#')
    colors_rgb.append(tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)))

background_rgb = tuple(int(background_hex.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

def determine_fill(kana):
    dakuten = 'none'
    if len(kana) < 2:
        if kana in vowels:
            return [blank,colors_rgb[vowels.index(kana)],'none']
        elif kana == 'n':
            return [nn,colors_rgb[0],'none']
    if len(kana) > 2:
        if (kana[2] == 'q'):
            dakuten = 'circle'
        else:
            dakuten = 'two lines'
    #print(consonant_codes[kana[0]],colors_rgb[vowels.index(kana[1])], dakuten)
    return (consonant_codes[kana[0]],colors_rgb[vowels.index(kana[1])], dakuten)

def flower_layer(cx,cy,size,tilt,kana):
    t.setheading(tilt)

    ftype, fcolor, dakuten = determine_fill(kana)

    pattern = ftype
    t.fillcolor(fcolor)

    for petal in range(5):
        t.goto(cx,cy)
        t.setheading(petal*72 + tilt)
        t.fillcolor(background_rgb)
        t.pendown()
        t.begin_fill()
        if pattern[petal] == 'x':
            t.fillcolor(fcolor)
            t.begin_fill()
            t.pendown()
        for i in range(12):
            t.left(20 * math.cos(i / 2))
            t.forward(size)
        t.right(180)
        t.left(10)
        for i in range(12):
            t.left(20 * math.cos(i / 2))
            t.forward(size)
        num = 0
        t.left(19.45)
        #print(num)
        t.right(10)
        t.end_fill()

text_sample = 'koaranonamaewa'

def parse_text(text):
    kana_list = []
    kana = ''
    for index in range(len(text)):
        kana += text[index]
        if text[index] in vowels:
            kana_list.append(kana)
            kana = ''
        if len(kana) == 2:
            if kana[0] == 'n' and kana[1] == 'n':
                kana_list.append('n')
                kana = ''

    for kana in kana_list:
        if len(kana) > 2:
            if kana[0] == 'n':
                kana_list = kana_list[0:kana_list.index(kana)] + ['n'] + [kana[1:]] + kana_list[kana_list.index(kana) + 1:]
            if kana[0] == kana[1]:
                kana_list = kana_list[0:kana_list.index(kana)] + ['tu'] + [kana[1:]] + kana_list[kana_list.index(kana) + 1:]


    return kana_list

def draw_flower(cx,cy,scale,text):
    t.penup()
    text = parse_text(text)

    t.goto(cx,cy)

    text = text[::-1]
    #print(text)

    count = 0
    for kana in text:
        # print(kana)
        flower_layer(cx,cy,(len(text)+5 - count)/2,count*60,kana)
        count += 1

    size_two = 6
    t.setheading(0)
    t.goto(cx,cy-size_two)
    t.fillcolor(background_rgb)
    t.begin_fill()
    t.circle(size_two)
    t.end_fill()

    '''
    for i in range(4):
        size_two = 33 + i*6
        t.setheading(0)
        t.goto(cx, cy - size_two)
        t.fillcolor(background_rgb)
        t.circle(size_two)'''

testing_text = 'wagahai.wa.neko.dearu.namae.wa.mada.nai.aiueo.zutto.kurai.tokoro.de.niyaa.niyaa.naite.ita'
testing_text = 'hanabatake.ga.kareru.mae.ni.'
#testing_text = 'ka.ka.ka.ka.ka'
#testing_text = 'a.ka.ga.sa.za.ta.da.na.ha.ba.pa.ma.ya.ra.wa.ja.n.'
#testing_text = 'a.i.u.e.o.'
testing_text = 'yuki.toke.te.mura.ippai.no.kodomo.kana.'
testing_text = 'wakai.koro.suki.datta.natu.no.nioi.yo.'
testing_text = 'hanabi.no.daibakuhatuonn.ga.hibiku.kono.yoru.'
testing_text = 'sensou.no.bakudann.no.daibakuhatuonn.ga.hibiku.kono.yoru.'
testing_text = 'yuki.tokete.mura.ippai.no.kodomo.kana.'
testing_text = 'wakara.nai.'
testing_text = 'hanabatake.ga.kareru.mae.ni.'
testing_text = 'bangohan.no.ato.wa.pan.wo.taberu.'
testing_text = 'a.ka.ga.sa.za.ta.da.na.ha.ba.pa.ma.ya.ra.wa.ja.nn.'
testing_text = 'yuki.tokete.mura.ippai.no.kodomo.kana.'
testing_text = 'hanabatake.'
testing_text = 'yuki.tokete.mura.ippai.no.kodomo.kana.'
testing_text = 'beiru.wa.saikou.na.utaite.kenn.sakusiya.dearu.'






def draw_stem(text):
    t.penup()
    t.goto(200,250)
    t.pendown()
    t.pencolor(colors_rgb[3])
    t.pensize(15)
    pos_list = []
    for segment in range(3):
        for i in range(30):
            t.left(10*(math.sin((4*(i/10)/5) + 3*math.sin((i/7)/5 + 3/2))))
            t.forward(7)
            pos_list.append(t.pos())
        for i in range(30):
            t.right(10*(math.sin((4*(i/10)/5) + 3*math.sin((i/7)/5 + 3/2))))
            t.forward(7)
            pos_list.append(t.pos())
    #print(pos_list)

    sentence_list = ['aiueo']
    sentence = ''
    for index in range(len(text)):
        if text[index] == '.':
            sentence_list.append(sentence)
            sentence = ''
        else:
            sentence += text[index]
    prev_pos = pos_list[0]
    radius = 50

    print(sentence_list)
    count = 0
    t.pensize(1)
    t.pencolor(colors_rgb[outline_pos])
    for pos in pos_list:
        distance = math.sqrt((prev_pos[0]-pos[0])**2+(prev_pos[1]-pos[1])**2)
        if distance > radius and count < len(sentence_list) + 1:
            draw_flower(pos[0],pos[1],1,sentence_list[count % len(sentence_list)])
            radius = (33 + len(parse_text(sentence_list[count % len(sentence_list)]))*6)/2 + 2*(33 + len(parse_text(sentence_list[(count + 1) % len(sentence_list)]))*6)/3
            prev_pos = pos
            count += 1
        #print(distance)
        #33 + i * 6


    t.pensize(1)

def draw_paragraph(turt,text,size,starting_y,dimensions):
    sentence_list = []
    sentence = ''
    for index in range(len(text)):
        if text[index] == '.':
            sentence_list.append(sentence)
            sentence = ''
        else:
            sentence += text[index]

    column = 0
    line = 0
    count = 0
    off = starting_y
    total = 0
    for s in sentence_list:
        sentence_length = len(parse_text(s))
        if sentence_length % 5 > 3:
            sentence_length = (sentence_length - sentence_length % 5) / 5
        else:
            sentence_length = (sentence_length-sentence_length%5)/5 + 1
        if column == 0:
            print('first col')
            sentence_length += 1

        total += sentence_length

        if total > dimensions and total != sentence_length:
            line += 1
            column = 0
            off = starting_y
            total = sentence_length

        off = render_text(turt,s,size,off,column,line)
        column += 1
        count += 1

    print(sentence_list)



screen = turtle.Screen()
#s = turtle.getscreen()
screen.colormode(255)
screen.bgcolor(background_rgb)

t = turtle.Turtle()
turtle.tracer(0, 0)

t.color(colors_rgb[0])
t.fillcolor(colors_rgb[1])
t.speed(10)

draw_stem(testing_text)


#flower_layer(0,0,10,0)
#flower_layer(0,0,5,40)

patterns = ['xoxo','xxxo','xoox','ooox','xooo','xxxo','xoox']
#draw_flower(0,0,1,text_sample)
#draw_flower(100,100,1,'bokuwakakedasite')
'''
draw_flower(-270,270,1,'aiueo')
draw_flower(-200,200,1,'baitosakiga')
draw_flower(-130,160,1,'nakanaka')
draw_flower(-180,80,1,'mitukaranaito')
draw_flower(-90,60,1,'tomodatino')
draw_flower(-20,0,1,'tanakakunga')
draw_flower(40,-40,1,'itta')'''
draw_flower(-270,270,1,'aiueo')
draw_flower(-240,200,1,'baito')
draw_flower(-190,170,1,'saki')
draw_flower(-150,200,1,'wo')
draw_flower(-90,210,1,'mitukeru')

'''
for i in range(20):
    t.color(colors_rgb[i%5])
    t.pencolor((0,0,0))
    #flower_layer(0, 0, 25-i, i*70)
    flower_layer(0, 0, (25 - i)/2, i * 70,patterns[i % 7])

t.begin_fill()
for i in range(12):
    t.left(20*math.cos(i/2))
    print(math.sin(180*i))
    t.forward(8)
t.right(180)
t.left(10)
for i in range(12):
    t.left(20*math.cos(i/2))
    print(math.sin(180*i))
    t.forward(8)
t.end_fill()'''

t.hideturtle()

turtle.update()


#time.sleep(4)

turtle.mainloop()
