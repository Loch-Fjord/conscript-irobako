import turtle

wagahai = 'wagahaiwanekodearu.namaewamadanai.dokodeumaretakatontokentougatukanu.nandemousuguraijimejimesitatokorodeniyaaniyaanaiteitakotodakewakiokusiteiru.wagahaiwakokodehajimeteningentoiumonowomita.sikamoatodekikutosorewasiyoseitoiuningentiyuudeitibandouakunasiyuzokudeattasouda.'
wagahai = 'wagahaiwanekodearu.namaewamadanai.dokodeumaretakatontokentougatukanu.nandemousuguraijimejimesitatokorodeniyaaniyaanaiteitakotodakewakiokusiteiru.wagahaiwakokodehajimeteningentoiumonowomita.sikamoatodekikutosorewasiyoseitoiuningentiyuudeitibandouakunasiyuzokudeattasouda.'

wagahai = 'hitoribottinokakeoti.kimikakeotittesitakotoarukai.nai.soudarouna.arewaaiteganakiyadekinaimondakarane.jiyaiedegurainara.aruttehitomotasiyouwairunjiyanaika.maabokudattebetuniiedeyakakeotiwosusumeyouttewakejiyanai.'

#wagahai = 'aiueokakikukekosasisusesotatitutetonaninunenohahihuhehomamimumemoyaayuayoararirurerowaanawo.aaaaagagigugegozajizuzezodadidudedoaaaaapapipupepobabibubeboaaaaaaaaaaaaaaa.'

wagahai = ('irobako.')
wagahai = ('hanabinodaibakuhatuongahibikukonoyoru.')
wagahai = ('kangaegakangaenikasanatteiku.kangaewokangaetatokinokaogadounandarou.')
wagahai = ('aiwaaimainamonoda.maikaiwaaiwotowareiminoeguiumu.')
wagahai = ('irohanihoheto.tirinuruwo.wagayotarezo.tunenaramu.urunookuyama.kehukoete.asakiyumemiji.ehimosezu.')
wagahai = ('kaerupiyokopiyoko.mipiyokupiyoku.awasetepiyokupiyokumupiyokupiyoku.')
wagahai = ('akapajiyama.aopajiyama.kipajiyama.')
wagahai = ('sumomomomomomomomonouti.')
wagahai = ('bouzugabiyoubunijiyouzuni.bouzunoewokaita.')
wagahai = ('toukiyoutokkiyokiyokakiyoku.')
wagahai = ('kattakatatatakikitakakatta.')
wagahai = ('namamuginamagomenamatamago.')
wagahai = ('butagabutawobuttarabutareta.butagabuttabutawobuttanodebuttabutatobutaretabutagabuttaoreta.')
wagahai = ('yukitokete.muraippaino.a.kodomokana.')

wagahai = ('aiueo.kakikukeko.gagigugego.sasisuseso.zazizuzezo.tatituteto.dadidudedo.naninuneno.hahihuheho.babibubebo.papipupepo.mamimumemo.yaayuayo.rarirurero.wawiwuwewo.nnnnn.')
wagahai = ('aiueokakikukekogagigugegosasisusesozazizuzezotatitutetodadidudedonaninuneno.hahihuhehobabibubebopapipupepomamimumemoyaayuayorarirurerowawiwuwewonnnnnnnnnn.')

wagahai = 'wagahaiwanekodearu.namaewamadanai.dokodeumaretakatontokenntougatukanu.nanndemousuguraijimejimesitatokorodeniyaaniyaanaiteitakotodakewakiokusiteiru.wagahaiwakokodehajimeteninngentoiumonowomita.sikamoatodekikutosorewasiyoseitoiuninngentiyuudeitibanndouakunasiyuzokudeattasouda.'

wagahai = ('aiwaaimainamonoda.maikaiwaaiwotowareiminoeguiumu.')
wagahai = ('beiru.a.')
#                 a        i         u          e         o          blankness
colors_hex = ['#617073','#0B0014','#D3C4E3','#A0A0E3','#FF4365']
colors_hex = ['#F47068','#FFB3AE','#1697A6','#0E606B','#FFC24B','#f4f1de']
#colors_hex = ['#01130F','#FAEEB3','#F3AE53','#0F97D2','#086F72','#FFFFFF']
colors_hex = ['#081905','#255D14','#4AA022','#993DD6','#B481E4','#D8C4F3']
#colors_hex = ['#ff99c8','#fec8c3','#fcf6bd','#a9def9','#e4c1f9','#f4f1de']
vowels = ['a','i','u','e','o']

stora = ['#FFF4F1',(255,244,241)]
colors_rgb = []

left_ness = 300

background_hex = colors_hex[5]

consonant_codes = {'k':'xxox',
                   's':'xxxo',
                   't':'xxoo',
                   'n':'xoxx',
                   'h':'xoox',
                   'm':'xoxo',
                   'y':'xooo',
                   'r':'oxxx',
                   'w':'oxox',}

dakuten_list = {'g':'k',
                'z':'s',
                'd':'t',
                'b':'h',
                'j':'s'}

blank = 'xxxx'
nn = 'ooxx'

for color in colors_hex:
# from https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    h = color.lstrip('#')
    colors_rgb.append(tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)))

background_rgb = tuple(int(background_hex.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

def determine_fill(kana):
    # returns the fill pattern, the fill color, and the type of dakuten

    # default dakuten value
    dakuten = 'none'

    # if kana is less than 2 characters long
    if len(kana) < 2:
        if kana in vowels:
            return [blank,colors_rgb[vowels.index(kana)],'none']
        elif kana == 'n':
            return [nn,colors_rgb[0],'none']

    # determines if there is a dakuten or not
    if len(kana) > 2:
        if (kana[2] == 'q'):
            dakuten = 'circle'
        else:
            dakuten = 'two lines'

    # executes if kana is more than 1 character long
    return (consonant_codes[kana[0]],colors_rgb[vowels.index(kana[1])], dakuten)
def draw_kana(turt,size,kana):
    # gets pattern, fill color, and dakuten from the kana input
    ftype, fcolor, dakuten = determine_fill(kana)

    # sets fill color
    turt.fillcolor(fcolor)

    # makes sure pen is up before moving
    turt.penup()

    # draws 4 squares in this order when facing right
    #  3 4
    #  2 1
    for i in range(4):
        # draws square if x in pattern
        if(ftype[i] == 'x'):
            turt.begin_fill()
            for e in range(4):
                turt.forward(size)
                turt.right(90)
            turt.end_fill()

        # faces to draw next square
        turt.right(90)

    # if there is a dakuten
    if dakuten != 'none':

        # positions turtle to start drawing dakuten
        turt.backward(size/2)
        turt.right(90)
        turt.forward(size/2)
        turt.left(90)

        # sets fill color to background color (in order to draw a "cut out")
        turt.fillcolor(background_rgb)

        # if dakuten type is circle (handdakuten), pendown()
        if dakuten == 'circle':
            turt.pensize(size/3)
            turt.color(background_rgb)
            turt.pendown()
        else:
            # else, fill it in
            turt.begin_fill()

        for i in range(4):
            turt.forward(size)
            turt.left(90)
        turt.end_fill()
        turt.penup()

        turt.left(90)
        turt.forward(size/2)
        turt.right(90)

        turt.forward(size/2)
        #turt.speed(100)
    turt.forward(size*2)

text_sample = 'kodomonokorokarazuttopikapikanahousekiwoteniiretakatta'

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
    for kana in kana_list:
        if kana[0] in dakuten_list:
            #print('has dakuten')
            kana_list[kana_list.index(kana)] = dakuten_list[kana[0]] + kana[1] + 'd'
        if kana[0] == 'p':
            kana_list[kana_list.index(kana)] = 'h' + kana[1] + 'q'


    return kana_list

def render_text(turt,text,size,starting_y,column,line):
    turt.penup()
    text = parse_text(text)

    if column == 0:
        text = vowels + text
    offset = starting_y

    if len(text)%5 > 3:
        text = text + vowels[len(text)%5:5] + vowels
    else:
        text = text + vowels[len(text) % 5:5]

    count = 0
    for kana in text:
         #print(kana)
        if count % 5 == 0:
            turt.goto(line*size*2*5-left_ness,offset)
            offset -= size*2
        count += 1
        draw_kana(turt,size,kana)

    return offset

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
t.speed('fastest')

draw_paragraph(t,wagahai,10,300,10)

t.hideturtle()

turtle.update()


#time.sleep(4)

turtle.mainloop()
