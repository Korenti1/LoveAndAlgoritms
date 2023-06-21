﻿define config.mouse = {}

define config.mouse["default"] = [  ("gui/cursors/Asset 2@4x 1.png", 0,0)  ]
define config.mouse["quest"] = [  ("gui/cursors/Asset 30@4x 1.png", 16,0)  ]

# Определяем персонажей игры
define q = Character(_(" "), color="#681826", image="ru", kind=nvl)
define m = Character("Мама", color="#ffffff")
define g = Character("[ggname]", color="#e0d20d")
define o = Character("???", color="#0a84e7")
define a = Character("Миша", color="#eb670f")
define k = Character("Катя", color="#F86983")
define y = Character("Юля", color="#7722e6")
define t = Character("Анна Владимировна", color="#f3071b")
define l = Character("Маша", color="#e7d212")
define kl = Character("Кубара Теймуровна", color="#3d2be0")


define g_nvl = Character("[ggname]", kind=nvl, image="no", callback=Phone_SendSound)
define k_nvl = Character("Катя", kind=nvl, callback=Phone_ReceiveSound)
define m_nvl = Character("Маша", kind=nvl, callback=Phone_ReceiveSound)


# Спрайты
image Kate = "Katerin/Katerin1.png"
image KateLaugh = "Katerin/Katerin_Laugh.png"
image KateNormal = "Katerin/Katerin_Normal.png"
image KateSad = "Katerin/Katerin_Sad.png"
image KateShocked = "Katerin/Katerin_Shocked.png"
image KateSmile = "Katerin/Katerin_Smile.png"
image KateTalk = "Katerin/Katerin_Delighted.png"
image KateAnnoyed = "Katerin/Katerin_Annoyed.png"
image KateSmug = "Katerin/Katerin_Smug.png"
image KateSmugSad = "Katerin/Katerin_Sad_Blush_3.png"
image KateTalkSmug = "Katerin/Katerin_Delighte_Blush_1.png"
image KateSmileBlush = "Katerin/Katerin_Smile_Blush_3.png"
image KateBlush = "Katerin/Katerin_Blush_1.png"
image KateShockBlush = "Katerin/Katerin_Shocked_Blush_3.png"
image KateKiss = "Katerin/Katerin_Sleepy_Blush_3.png"

image Yulia = "Yulia/Yulia1.png"
image YulaNorm = "Yulia/Yulia_Normal.png"
image YulaSmile = "Yulia/Yulia_Smile.png"
image YulaTalk = "Yulia/Yulia_Delighted.png"

image Masha = "Maria/Maria1.png"
image MashaTalk = "Maria/Maria_Talk.png"
image MashaLaugh = "Maria/Maria_Laugh.png"
image MashaSad = "Maria/Maria_Sad.png"
image MashaShock = "Maria/Maria_Shocked.png"
image MashaSmile = "Maria/Maria_Smile.png"
image MashaNorm = "Maria/Maria_Normal.png"
image MashaAnnoBlush = "Maria/Maria_Annoyed_Blush_3.png"

image Anna = "Анна Владимировна/Обычный.png"
image AnnaAgr = "Анна Владимировна/Агр1.png" 
image AnnaAgr2 = "Анна Владимировна/Агр2.png" 

image Klass = "Класуха/обычный.png"
image KlassSad = "Класуха/Растроенная.png"
image KlassNorm = "Класуха/нормальный.png"

image Misha = "Миша/Обычный.png"
image MishaSad = "Миша/Растроенный.png"
image MishaHappy = "Миша/Смех2.png"



init python:        #Прикол
    import os
    usID = os.environ.get("USERNAME")

#Музыка и звуки
define audio.licence = "music/Panic! At The Disco - Bohemian Rhapsody (1).mp3"
define audio.alarm = "sounds/Куплинов - Будильник 2..mp3"
define audio.train = "sounds/train-interior-1.mp3"
define audio.iphone = "sounds/Звук-Смс-на-iphone.mp3"
define audio.people = "sounds/tolpa-ljudej.mp3"
define audio.rzd = "sounds/rzhd-i-z_uk.mp3"
define audio.scrimer = "sounds/scrimer.mp3"
define audio.rington = "sounds/БиС - КАТЯ, ВОЗЬМИ ТЕЛЕФОН (DOTA VERSION) (mp3cut.net).mp3"
define audio.sigma = "sounds/sigma.mp3"
define audio.rage = "sounds/rage.mp3"
define audio.lesson = "sounds/lesson.mp3"
define audio.street1 = "sounds/zvuki-na-ulice-goroda.mp3"
define audio.lesson = "sounds/zvuk-ulicy.mp3"
define audio.talk = "sounds/talk.mp3"
define audio.talk1 = "sounds/talk1.mp3"
define audio.doorcar = "sounds/car-door-closed-2_zydxyzvu.mp3"
define audio.close = "sounds/close.mp3"
define audio.open = "sounds/open.mp3"
define audio.stuck = "sounds/stuck.mp3"
define audio.ride = "sounds/ride.mp3"
define audio.hug = "sounds/hug.mp3"
define audio.bed = "sounds/bed.mp3"
define audio.laught = "sounds/laught.mp3"
define audio.evening = "sounds/evening.mp3"
define audio.night = "sounds/night.mp3"
define audio.park = "sounds/park.mp3"
define audio.kassa = "sounds/kassa.mp3"
define audio.magaz = "sounds/magaz.mp3"
define audio.ringtone = "sounds/iphone_ringtone.mp3"
define audio.alarm2 = "sounds/alarm2.mp3"
define audio.kitchen = "sounds/kitchen.mp3"
define audio.klass = "sounds/klass.mp3"
define audio.stas = "sounds/stas.mp3"
define audio.kuplinov = "sounds/kuplinov.mp3"
define audio.les = "sounds/les.mp3"
define audio.les2 = "sounds/les2.mp3"
define audio.naprag = "music/naprag.mp3"
define audio.naprag2 = "music/naprag2.mp3"
define audio.fon = "music/fon.mp3"
define audio.naprag3 = "music/naprag3.mp3"
define audio.end = "music/Кино - Группа крови.mp3"


default question_tally = 0                                  #variable used in question_selector

label start:
    scene bedroom-with-books with fade                                             #SCREEN 1

    #алгоритм задания имени главного героя

    $ ggname = renpy.input("Как вас зовут?", length=15, default="Ильшат", allow="ячсмитьбюфывапролджэйцукенгшщзхъ-ЯЧСМИТЬБЮФЫВАПРОЛДЖЭЙЦУКЕНГШЩЗХЪ").strip()

    if ggname == "":            #ловушка джокушкера, для тех кто любит ставить пустые имена
        $ ggname = "Влад"

    # if ggname == "Олег":
    #     # какая-то секретка

    # if ggname == "Сергей":
    #     # какая-то секретка

    "Сегодня наступил новый день, полный надежд и возможностей." 
    
    "Новая возможность начать свой день с чистого листа, сделать новые достижения, встретить любовь и получить удовольствие от жизни."

    " Подумал я…."
    #"[usID]"  #для прикола

    #show blink

    #show blinking
    "Но к сожалению, этот день это конец лета, конец каникул. И мне придется опять вставать рано. Идти в школу…."

    "Чтоп, сто?"

    "Тьфу, какую школу, я же ее закончил. Это придется ехать в колледж, фиг пойми куда…. эх…."

    play music alarm 

    "Сквозь сон, я протер глаза и зевнул"

    "Проснулся я оттого, что мой будильник уже начал сходить с ума"

    "Я только встал, а уже устал от учебы, от сна, от всего…."

    play sound bed

    "Я встал, одел шорты, майку"

    stop music fadeout 1

    scene bath with fade

    "Пошел умываться и слышу знакомый мне голос, это был голос мамы."

    "Живем мы с мамой вдвоем, в доме. У меня с ней бывают иногда разногласия, но мне кажется ей просто не хватает мужика, а может дело и во мне…. Ну не суть важна"

    m "Сынок, иди кушай, а то опоздаешь!"

    g "Да мам, сейчас умоюсь и приду"

    m "Я приготовила твои любимые блинчики!"

    "Блинчики ммм, а аромат какой стоял, аж слюнки уже потекли."

    scene kitchen 1 with fade
    play music kitchen

    "Я “Припудрил носик” как говорит мама. И спустился вниз на кухню"

    scene pancakes with fade

    "Там стояли мои блины и мама которая проходит мимо меня она уже собиралась уезжать на работу"

    m "Я поехала, а ты не опоздай в колледж, первый день все же. Будь умницей *Чмок*"

    "Она поцеловала меня в щеку, села в машину и уехала."
    "Я поел блины. Посмотрел на время."
    "Вроде успеваю"

    stop music fadeout 1

    scene enter with fade

    "Я пошел наверх, оделся в какой никакой, но приличный костюм, взял цветы для нового классного руководителя и вызвал такси"

    play sound close

    scene taxi with fade

    play sound doorcar
    play music ride

    "Вот сижу в такси и думаю"
    "Как все будет в новом месте, какие будут одногруппники, преподаватели, может я вообще там не приживусь…."
    "Бррр…. Эти мысли пугали и я решил не думать о них, а просто смотреть в окно"


    stop music fadeout 1
    scene kollege with fade

    play music street1

    "Когда я приехал к колледжу, я увидел много подростков у входа"
    "Мне стало не по себе и я решил просто подождать пока будут всех пускать"
    "Спустя 15 минут нас впустили и тут у меня начался ступор…."

    stop music fadeout 1

    play music talk

    scene hallway with fade
    "У меня была группа ИС-11, но я ее нигде не мог найти"
    "ИС-17"
    "СА-12"
    "КС-18"
    "Да где же?"
    "А вот"
    "ИС-12"
    "Не то"

    stop music fadeout 1

    play music talk1

    "Пока я ходил, уже никого не было в холле, я запаниковал"
    "Потом ко мне подошел то ли преподаватель, то ли кто-то из администрации, но я не вдавался мне просто хотелось найти свою группу."

    o "Привет"
    g "Здравствуйте"
    o "Потерялся?"
    g "Ну да, есть такое"
    o "Какая группа?"
    g "ИС-11"
    o "А, понял, пошли за мной"

    "Он повел меня на второй этаж и привел к 220-ой аудитории"
    
    o "Вот твоя аудитория"
    g "Спасибо большое"
    o "Да пожалуйста"
    o "Удачи!"
    g "Спасибо"

    stop music fadeout 1

    play sound stuck
    "(Тук-тук-тук)"

    g "Здравствуйте, можно?"
    o "Здравствуй, конечно заходи, как раз вовремя"

   

    scene cabinetus with fade
    play music klass
    
    "Я вошел и увидел много студентов которые расселись по местам"
    "Ну так как все первые ряды были заняты, я пошел и сел на самое ближайшее место"
    "Эта аудитория мне почему-то сразу не понравилась, какой-то необычный, висели рамки с какими-то цитами и дверца в стене…."
    "Со мной рядом сидели двое ребят. И вдруг, один из них заговорил"

    show Misha
    with dissolve

    o "Здорова, как тебя звать?"
    g "Привет, меня [ggname]"
    a "Меня Миша, приятно познакомиться!"
    g "Приятно...."

    hide Misha
    with dissolve

    "Дальше мы просто слушали то что нам говорит класный руководитель"
    "Там в основном были разговоры о колледже, что нам предстоит и всякое такое. Пока нам рассказывали все, я решил подсчитать сколько людей в группе."
    "Всего я насчитал 25 студентов - 15 девочек и 10 мальчиков включая меня...."
    "Ух ты, девочек больше чем, мальчиков.... Не думал, что в такие колледжи поступают девочки...."
    "По виду все девчонки красивые, миленькие, классно одеваются"
    "Пацаны как мне показалось самые простые"
    "Кто-то уже разошелся по группкам, а кто-то еще нет"
    "Ну я так подумал, что на парах узнаю каждого, сейчас не время"

    "Когда классный руководитель все рассказала, нас повели на экскурсию"

    scene cafeteria with fade

    "Нам показали столовую, которая выглядела как обычная придорожная шаурмячная, только больше"
    "Повели по всем кабинетам администрации, показали где находится учебная часть, наше отделение, спортзал, медпункт"
    "После экскурсии, нам рассказали, что со следующего дня начинаются занятия и отпустили"

    stop music fadeout 1

    scene street with fade

    play music street1

    "Я вышел и решил не к кому не подходить, а спокойно поехать домой"
    "Заказал такси и со спокойной душей поехал домой"

    stop music fadeout 1
    
    scene livingroom-night with fade

    play sound close

    "Когда я приехал, мама была уже дома"

    stop music fadeout 1

    "Я с недоуменым лицом удивился, посмотрел на время, а уже было 18 часов...."
    "Сильно удивлясь, что так быстро вре...."

    m "Ну как колледж ?"
    "Не закончив мысль, меня перебила мама"
    "Пока я потупливал, что она спросила, вопрос прозвучал еще раз"

    m "Все хорошо?"
    "И все???"
    "Ну, а что мне еще ответить ей....?"
    "Пока я ехал обратно, впечатления какие были, уже пропали и особо нечего рассказывать было"

    g "Ну так, прикольный колледж.... Нас провели по кабинетам, показали, что да как"
    m "Ммм, ну понятненько"
    m "А что классный руководитель говорил ?"
    g "Да особо ничего, рассказывала, что нас ждет в колледже рассказывала правила ну и все вроде"
    m "Замечательно, ну тогда иди переодевайся, а я тебе пока покушать наложу"
    g "Хорошо"
    "Я поднялся в свою комнату, переоделся и улегся на диван "

    scene bedroom-with-books with fade

    "Пока лежал, я размышлял о том, что сегодня было и как так быстро пролетело время…."
    "И не заметил как задремал"
    "Подняла меня мама, со словами идти есть, а то уже все остыло"
    "Я посмотрел время и опешил, было уже 20:00"
    "Я спустился вниз, поел и пошел в комнату"
    "Смотря на свой компьютер я думал играть или нет"

    
    label the_question:                                     #SCREEN 2
            #show eileen concerned at left with move        #для показа спрайтов
            g "{u}Играть{/u} или \"не играть\"?"
            call question_selector from _call_question_selector
            $ default_mouse = "quest"
            menu:                                            #SCREEN 3
                "Играть":
                    $ default_mouse = "default"                               #FOX
                    #show eileen vhappy at right with pixellate  #SCREEN 4-1
                    $ motion = 'play'
                    play sound rage
                    "" "Но взвесив все за и против, {b}все галактики которые проходят через мой мозг и какие нейтроны трогают мою чувствительную точку в мозгу{/b}, {size=-5}я решил!{/size} Играем!"
                    "Я поиграл где-то часик другой и улегся на кровать"
                "Не играть":
                    $ default_mouse = "default"                                  #DOG
                    #hide eileen with dissolve                   #SCREEN 4-1
                    $ motion = 'dont play'
                    "" "{i}Да не{/i}, устал я сегодня {size=+10}Очень{/size}"
                    "Я улегся на кровать"
                " [repeat_question]": #SCREEN 4-3
                    jump the_question
                    stop music fadeout 1
            jump continue

    label question_selector:
        $ NumberGenerator = renpy.random.randint(1, 3)
        if NumberGenerator == 3:
            $ repeat_question = "Что?"
        elif NumberGenerator >= 2 and NumberGenerator < 3 or NumberGenerator == 5:
            $ repeat_question = "Еще раз?"
        else:
            $ repeat_question = "Каво?"
        $ repeat_question = renpy.random.choice(["Что?", "Еще раз?", "Каво?"])
        $ question_tally += 1
        return

label continue:

    "Ну и как всегда я решил включить ютуб и посмотреть куплинова"
    play sound stas
    "Ой, не туда нажал"

    stop music

    play sound kuplinov

    "Во, другое дело"

    "Пролежал я так до 3 ночи и в итоге уснул"

    stop music fadeout 1

    jump day2

    return


# день 2
label day2:
    scene bedroom-with-books with fade

    "Проснулся я от будильника"
    "И тут до меня дошло, я не поменял будильник, а время было уже к 11"
    "{size=+10}Проспал{/size}"
    "Я в панике начал собираться"
    "Ну и опять вызвал такси…."
    "Дорогое удовольствие это такси однако"
    "Но делать нечего, надо было быстрее ехать"
    "Когда я приехал я посмотрел в каком кабинете была пара"
    "Пара была в 324 кабинете"
    "Я быстро побежал в кабинет"

    play sound open

    scene evening with fade

    play music klass
    
    g "Здравствуйте, извините за опоздание"
    o "На час опоздал, зовут?"
    g "[ggname]"
    o "Хорошо [ggname], садись"

    play sound close

    "Почти все места были заняты"
    "Проходя по аудитории я не заметил стул"
    "Да…. Стул, я сам не понял как так случилось"
    "Я упал, разбросав все тетради по полу"

    play sound laught

    "Класс разразился смехом"
    "Вот он, первый день \"позора\""

    o "{size=+15}А ну тихо!{/size}"
    o "Я на вас посмотрела бы если вы так упали!"

    stop music fadeout 1

    "Все замолчали, даже мне как-то страшно стало"
    "В моменте я увидел чью-то руку которая собирала мои тетради"

    g "Сп.. спасибо…."
    show Kate
    with dissolve
    k "Да не за что, не ушибся?"
    g "Нет, все нормально"
    k "Тогда чудно"

    hide Kate
    show KateTalk
    with dissolve
    k "Ты кстати можешь со мной сесть, у меня свободно"

    play music klass

    "И действительно, с ней одной и было свободное место."
    "Я с девушками особо не контактирую, чувствую себя неуверенно рядом с ними, да и вообще лишний раз боюсь что-то сказать им"
    hide KateTalk
    with dissolve
    "Мы разговорились и она оказывается была очень интересной девушкой"
    "Когда мне только казалось, что она была энергичной и общительной, теперь мне так не кажется, все что мне казалось все правда"
    "Еще узнал, что Катя увлекается мобильной разработкой и созданием игр. У нее даже был один проект, сказала, что потом как-нибудь покажет"
    "И вот так мы общались, до конца пары не слушая, что говорит преподаватель"
    "Когда прозвенел звонок, я с ней попрощался и сказал, что потом еще поговорим"
    "Ну а что…. Да, я не особо общаюсь с девушками, но тут мне понравилось, да и еще общие темы появились"

    "Оказывается, что перемена была длинной и я решил зайти в столовую, перекусить, а то дома я ничего и не поел толком"

    stop music fadeout 1

    scene cafeteria with fade

    play music people
    "В столовой было очень много студентов и опять не было мест…. Везет мне на сидячие места"
    "Я взял пиццу и сок"
    "Уходя поесть в другое место, я слышу как окликнули мое имя"
    o "{size=+10}[ggname]{/size}!!!"
    "Я обернулся и вижу мне рукой машет одногруппница, я не помнил ее имени…."
    o "Садись, тут свободное место есть"
    "Ну капец…. Опять свободное место и с девушкой"
    "То ли мне так начало везти на девушек, то ли на места, либо это просто совпадение, \"либо массонский заговор рептилоидов против человечества и меня впринципе\""
    g "Спасибо"
    g "Слушай, извини, что спрашиваю, я еще не всех запомнил, как тебя зовут?"
    o "Хи-хи, я тоже не всех запомнила, а вот тебя запомнила хорошо [ggname]"

    show Yulia
    with dissolve
    y "Меня зовут Юля"
    g "Понял…."
    hide Yulia
    with dissolve

    "Ели мы в тишине"
    "Юля ушла пораньше, боясь опоздать на пару"
    "Она была тоже красивой девочкой, довольно застенчивой и умной, как никак у нее красный аттестат"
    "Я тоже доел и не спеша пошел к кабинету"
    stop music fadeout 1

    scene evening with fade

    play music klass

    "На этот раз пара проходила на 1 этаже"
    "Была пара русского"
    "Рядом с Катей место было свободно и я хотел с ней сесть"
    "Но меня позвал к себе Миша"

    stop music fadeout 1

    menu :
        "Сесть с Катей":
            jump Kate


        "Сесть с Мишей":
            jump Misha

    return


label Kate:

    play music klass

    "Я решил все же сесть с Катей, обещал все же"
    "По ее виду она была рада, что я с ней сел"

    k "Я уже думала не сядешь со мной…."
    g "Ну я же обещал"

    "Она еще больше обрадовалась"
    "Пока я раскладывал вещи на парте, вошел преподаватель"

    show Anna
    with dissolve

    t "Дети здравствуйте, меня зовут Анна Владимировна и я буду вести у вас русский язык и литературу"
    t "И скажу сразу, не обижайтесь пожалуйста если я кого-то из вас не запомню"

    "Лично мне будет все равно, запомнит она или нет"

    hide Anna
    with dissolve

    "В течении 20 минут она рассказывала как у нас будут проходить пары, как мы будем сдавать сессию"
    "Я с Катей не обращали на нее внимание и общались о своем"
    "Я начал замечать как на нас посматривает учитель"
    "И я задумался, общаться с Катей дальше или слушать учителя"

    stop music fadeout 1

    menu:
        "Не обращать внимания на учителя":
            jump noisy

        "Успокоить Катю":
            jump smart

    return



label noisy:

    play sound sigma
    scene krash with fade
    "Да пофиг мне"
    stop sound

    scene evening with fade
    play music klass

    "Я решил общаться с Катей дальше, все равно я не любил этот предмет и на нем скучно было"
    "Нам сделали первое замечание"
    "Мы чуть притихли и продолжили"
    "Тут уже второе прилетело замечание"

    show AnnaAgr
    with dissolve

    t "Екатерина, [ggname], еще одно замечание и я зову классного руководителя!"

    "Мы притихли, но что вы думаете, конечно не на долго"
    "Тут поступило третье замечание…."

    hide AnnaAgr
    show AnnaAgr2
    with dissolve

    t "Ну все, мое терпение лопнуло, я пошла за вашим классным руководителем"

    stop music fadeout 1

    hide AnnaAgr2
    with dissolve

    "Весь класс будто сжался от ужаса, конечно это плохо что классного руководителя вызывают на 2 день, но обидно что из за нас, хотя общался весь класс."
    "Через несколько минут приходит кл.рук."

    show AnnaAgr2
    with dissolve

    t "Я им сделала 3 замечания, они не послушали, мое терпение лопнуло"
    t "Мешают остальным слушать лекцию, срывают всю пару"
    "Да да да, кто поверил, еще скажите что в Югославии..."
    t "Я уже просто незнаю как с ними справляться"
    "Звание самого (не)любимого учителя, с огромным отрывом от остальных преподавателей, забирает Анна Владимировна"

    hide AnnaAgr2
    with dissolve

    show KlassNorm
    with dissolve

    o "Хорошо Анна Владимировна, поговорим"
    o "Катя, [ggname], зайдете потом ко мне"
    k "Хорошо, Кубара Теймуровна."



    "Так вот как ее зовут"
    "А я даже не запоминал"
    "Хотя что то знакомое я где-то слышал"

    hide KlassNorm
    with dissolve

    "До конца пары было 20 минут, мы решили посидеть молча, пока ещё хуже не стало"
    "Пара кончилась"

    show KateNormal
    with dissolve

    k "Ну что пойдем"
    g "Пошли"

    scene hallway with fade

    k "Как думаешь, что нам будут говорить?"
    g "Не знаю…. Но точно ничего хорошего"
    k "Ну сейчас и узнаем"

    play sound stuck

    k "Кубара Теймуровна, можно?"
    kl "Да ребят, заходите"

    play sound close

    "Мы закрыли за собой дверь"

    hide KateNormal
    with dissolve

    show Klass
    with dissolve

    kl "Я понимаю, что вы только пришли со школы, другая обстановка, все дела"
    kl "Но давайте вести на парах себя прилично, не мешая себе и другим"

    hide Klass
    with dissolve
    show KateSad
    with dissolve

    k "Извините…."
    g "Извините…."

    hide KateSad
    with dissolve
    show KlassSad
    with dissolve

    kl "Да ничего страшного, вы первый раз на парах, я понимаю"
    kl "Но в следующий раз, ведите себя хорошо"
    k "Хорошо, Кубара Теймуровна "

    hide KlassSad
    show Klass
    with dissolve

    kl "Тогда я вас больше не задерживаю, можете идти"
    g "До свидания, Кубара Теймуровна "
    kl "До свидания, ребят"

    hide Klass
    with dissolve

    play sound open
    play sound close

    g "Я думал будет хуже…."

    show KateSmile
    with dissolve

    k "Я тоже так думала…."
    "Но слава богу пронесло"
    g "Пошли на выход"
    k "Пошли"

    "Мы дошли до выхода и вышли с колледжа"

    play music street1

    scene kollege with fade

    hide KateSmile
    show KateSmileBlush
    with dissolve

    k "Ну что, до завтра?"
    g "Да давай, до завтра"

    hide KateSmileBlush
    with dissolve

    play sound hug

    "Она меня обняла и я засмущался…."
    "Но меня быстро отпустило и я на радостях пошел в метро"

    stop music fadeout 1

    play sound rzd
    scene metro with fade
    play music train

    "Пока я ехал, увидел какое-то знакомое лицо"
    "Если мне не изменяет память это была {size=+7}Маша{/size}"
    "Я решил подойти к ней"

    g "Привет Маш!"
    show MashaSmile
    with dissolve
    l "Оо, привет, [ggname]"
    l "Ты что тут делаешь ?"
    g "Я домой еду, а ты куда ?"
    hide MashaSmile
    show MashaNorm
    with dissolve
    l "Я тоже домой"
    g "А на какую станцию ?"
    l "Орбитальная"

    "Вот тут я офигел, она живет рядом со мной ?"

    g "А на какой улице?"
    l "Таганрогская"

    "ВОУ, Еще и на моей улице"

    g "Я там же живу"
    hide MashaNorm
    show MashaSmile
    with dissolve
    l "Ух ты, славненько, будем значит вместе ездить"
    g "Да…."

    "Мы с ней разговаривали пока не приехали на станцию, а там уже разошлись"

    play sound rzd
    hide MashaSmile
    with dissolve
    stop music fadeout 1

    "Я пошел домой"

    jump writeKate

    return

label smart:

    play music klass

    g "Давай тихо посидим?"
    k "Хорошо…."

    "Всю пару мы просидели в тишине"

    stop music fadeout 1
    "Когда пара закончилась, мы вышли, попрощались, я вышел из колледжа и пошел в метро"
    "Метро находится недалеко от колледжа так и еще возле моего дома, повезло так повезло"

    jump train

    return


label Misha:

    play music klass

    show Misha
    with dissolve

    a "Садись со мной!"
    g "Хорошо, давай"

    hide Misha
    with dissolve

    "Пока я раскладывал вещи на парте, вошел преподаватель"

    show Anna
    with dissolve
    
    t "Дети здравствуйте, меня зовут Анна Владимировна и я буду вести у вас русский язык и литературу"
    t "И скажу сразу, не обижайтесь пожалуйста если я кого-то из вас не запомню"

    "Лично мне будет все равно, запомнит она или нет"
    "В течении 20 минут она рассказывала как у нас будут проходить пары, как мы будем сдавать сессию"
    "Эта пара казалось, что длилась вечность, я и сам не любил уроки русского языка, а сидеть на них это было испытанием для меня"

    hide Anna
    with dissolve

    "Пара наконец-то закончилась, я вышел из кабинета первый и был в восторге, что я оттуда вышел"

    stop music fadeout 1.0
    play music talk

    "Но мой восторг прервали щелбаном по затылку сзади"
    "Обернувшись, я увидел Катю которая стояла с грустным лицом"

    show KateSad
    with dissolve

    k "Ты чего со мной не сел?"
    k "Я тебя ждала, ты  обещал, что мы еще поговорим…."

    "Упс…. Я не знал как ей объяснить почему я к ней не сел, хотя хотел, надо было к ней сесть"
    "С Мишей было интересно сидеть, но с Катей было бы веселее"

    g "Извини, Кать…."
    g "Меня просто Миша позвал, я правда хотел к тебе пойти, но тут зашла Анна Владимировна и я уже с ним сел"

    hide KateSad
    

    show KateShocked
    with dissolve
    k "Ты запомнил как зовут учительницу по русскому ?"

    "Кстати и вправду, обычно я не сразу запоминаю имена, а тут …."

    g "Да…"
    g "Простишь ?"

    hide KateShocked
    
    show KateNormal
    with dissolve

    k "Прощаю, но на следующей паре садись со мной!"
    g "Хорошо"
    k "Давай, до завтра"

    hide KateNormal
    with dissolve

    "Я сначала не понял, почему до завтра, но собираясь идти на следующую пару, я вспомнил, что у нас на сегодня пар больше нет"
    "Я на радостях вышел из колледжа и пошел в метро"
    "Хватит с меня уже такси, больно дорого выходит ездить с конца города в центр, так еще когда пробки"
    "Метро находится недалеко от колледжа так и еще возле моего дома, повезло так повезло"

    stop music fadeout 1

    play sound rzd
    scene metro with fade
    play music train

    "Пока я ехал, увидел какое-то знакомое лицо"
    "Если мне не изменяет память это была {size=+7}Маша{/size}"
    "Я решил подойти к ней"

    g "Привет Маш!"
    show MashaSmile
    with dissolve
    l "Оо, привет, [ggname]"
    l "Ты что тут делаешь ?"
    g "Я домой еду, а ты куда ?"
    hide MashaSmile
    show MashaNorm
    with dissolve
    l "Я тоже домой"
    g "А на какую станцию ?"
    l "Орбитальная"

    "Вот тут я офигел, она живет рядом со мной ?"

    g "А на какой улице?"
    l "Таганрогская"

    "ВОУ, Еще и на моей улице"

    g "Я там же живу"
    hide MashaNorm
    show MashaSmile
    with dissolve
    l "Ух ты, славненько, будем значит вместе ездить"
    g "Да…."

    "Мы с ней разговаривали пока не приехали на станцию, а там уже разошлись"

    play sound rzd
    hide MashaSmile
    with dissolve
    stop music fadeout 1

    "Я пошел домой"
    jump weWrite

    return

label train:

    play sound rzd
    scene metro with fade
    play music train

    "Пока я ехал, увидел какое-то знакомое лицо"
    "Если мне не изменяет память это была {size=+7}Маша{/size}"
    "Я решил подойти к ней"

    g "Привет Маш!"
    show MashaSmile
    with dissolve
    l "Оо, привет, [ggname]"
    l "Ты что тут делаешь ?"
    g "Я домой еду, а ты куда ?"
    hide MashaSmile
    show MashaNorm
    with dissolve
    l "Я тоже домой"
    g "А на какую станцию ?"
    l "Орбитальная"

    "Вот тут я офигел, она живет рядом со мной ?"

    g "А на какой улице?"
    l "Таганрогская"

    "ВОУ, Еще и на моей улице"

    g "Я там же живу"
    hide MashaNorm
    show MashaSmile
    with dissolve
    l "Ух ты, славненько, будем значит вместе ездить"
    g "Да…."

    "Мы с ней разговаривали пока не приехали на станцию, а там уже разошлись"

    play sound rzd
    hide MashaSmile
    with dissolve
    stop music fadeout 1

    "Я пошел домой"
    jump loh
    return

label loh:

    scene livingroom-night with fade
    play sound open

    "Дома никого небыло"
    "Я себе разогрел поесть и пошел в свою комнату"
    "Включил комп и сел играть в свои онлайн-игры. Они как наркотик - приносят боль и раздражение, а перестать не можешь"
    "Просидел я до вечера"
    "Мама пришла"
    "Она знала, что я дома, но походу решила меня не отвлекать"
    "Я играл до часов 11"  
    "Сильно устав, я собирался лечь спать"
    "Как вдруг услышал, что кто-то шуршит под окном"
    "Мама была в комнате, она не могла выйти на улицу"
    "Я подошел к окну, осмотрелся и никого не увидел"
    "Может у меня уже крыша поехала"  
    "Или мне показалось"
    "Но мне сейчас было не до этого, я хотел спать"
    "Я улегся на кровать и уснул"

    jump notgulal

    return

label weWrite:
    scene livingroom-night with fade
    play sound open

    "Дома никого небыло"
    "Я себе разогрел поесть и пошел в свою комнату"
    "Включил комп и сел играть в свои онлайн-игры. Они как наркотик - приносят боль и раздражение, а перестать не можешь"
    "Просидел я до вечера"
    "Мама пришла"
    "Она знала, что я дома, но походу решила меня не отвлекать"

    play sound iphone
    "Опа, а что это было?"
    "А, это староста скинула расписание на завтра"
    "Вдруг резко накатило противное чувство, словно я всю планету, весь мир подставил"
    "Зря я наверно не сел с Катей"
    "Может я смогу загладить свою вину?"

    menu:
        "Написать":
            jump write

        "Не писать":
            jump dontWrite

    return

label write:
    "Я схватился за свой телефон"
    "Чтобы ей написать?"
    g "Привет, как дела?"
    "Нет, это тупо"
    g "Ты не сердишься?"
    "Жалко и по детски"
    g "Не хочешь прогуляться?"
    "Ну вот это уже более менее"

    nvl_narrator "ВКонтакте"

    g_nvl "Привет)"
    k_nvl "Привет {image=images/emoji/hi.png}"
    g_nvl "Это я, [ggname]"
    g_nvl "Не хочешь прогуляться? {image=images/emoji/smile2.png}"
    k_nvl "Решил загладить свою вину?)"

    "..."

    k_nvl "Ладно давай, место встречи выберу я"

    "Ух ты, вот так сразу"

    g_nvl "Хорошо"
    k_nvl "Сейчас скину адрес и место"

    k_nvl "{image=images/zra.png}"
    play sound scrimer

    nvl_narrator "ОБЕРНИСЬ."
    stop sound
    
    "Что это?"
    nvl clear

    nvl_narrator "Медиа"
    k_nvl "{image=images/restsmall.png}"
    "Показалось?"
    "Зря я вчера поздно лег"

    k_nvl "Жду тебя через пол часа"
    k_nvl "И не опаздывать! {image=images/emoji/happy.png}"
    "Ну все, в этот день я точно избежал смерти от рук маленькой девочки"
    "Я же иду просто погулять, надеюсь ничего страшного не случиться"
    g "Хе-хе-хе"
    "Шизик"
    "Я начинаю собираться, подхожу к выходу, обуваюсь"
    "И тут у меня спрашивает мама…."

    m "Ты куда?"
    g "Я гулять"
    m "С кем?"
    g "С друзьями"
    m "Какими?"
    g "Одногруппниками"

    "Да, мне стыдно было говорить, что я иду гулять с девочкой…."

    m "Ну хорошо, иди, только не долго"
    g "Хорошо мам"

    jump street
    return

label dontWrite:

    play sound sigma
    scene krash with fade
    "Лучше не буду писать ей"
    stop sound

    scene livingroom-night with fade
    "Думаю все будет хорошо, если я не буду лишний раз беспокоить людей"
    "Я играл до часов 11"
    "Сильно устав, я собирался лечь спать"
    "Как вдруг услышал, что кто-то шуршит под окном"
    "Мама была в комнате, она не могла выйти на улицу"
    "Я подошел к окну, осмотрелся и никого не увидел"
    "Может у меня уже крыша поехала"
    "Или мне показалось"
    "Но мне сейчас было не до этого, я хотел спать"
    "Я улегся на кровать и уснул "
    jump notgulal

    return


label writeKate:
    scene livingroom-night with fade

    "Дома никого небыло"
    "Я себе разогрел поесть и пошел в свою комнату"
    "Включил комп и сел играть в свои онлайн-игры. Они как наркотик - приносят боль и раздражение, а перестать не можешь"
    "Просидел я до вечера"
    "Мама пришла"
    "Она знала, что я дома, но походу решила меня не отвлекать"



    play sound iphone
    "Опа, а что это было?"
    "Это была Катя"
    "Я не ожидал ее сообщения"

    nvl_narrator "ВКонтакте"

    k_nvl "Привет)"
    g_nvl "Привет {image=images/emoji/hi.png}"
    k_nvl "Это я, Катя"
    k_nvl "Не хочешь прогуляться? {image=images/emoji/smile2.png}"

    "Ух ты, вот так сразу"
    "Но резко чувства страха и неуверенности накатили волной "

    g_nvl "Да незнаю, дел много, да и поздно уже"

    k_nvl "Да ладно, мы ненадолго)"

    "Вот неугомонная девчонка"

    g_nvl "Хорошо, давай"
    k_nvl "Ура, сейчас скину адрес и место"

    k_nvl "{image=images/zra.png}"
    play sound scrimer

    nvl_narrator "ОБЕРНИСЬ."
    stop sound
    
    "Что это?"
    nvl clear

    nvl_narrator "Медиа"
    k_nvl "{image=images/restsmall.png}"
    "Показалось?"
    "Зря я вчера поздно лег"

    k_nvl "Жду тебя через пол часа"
    k_nvl "И не опаздывать! {image=images/emoji/happy.png}"
    "Ухухуху, я запаниковал, но быстро пришел в себя"
    "Я же иду просто погулять, ничего страшного в этом нет"
    "Я начинаю собираться, подхожу к выходу, обуваюсь"
    "И тут у меня спрашивает мама…."

    m "Ты куда?"
    g "Я гулять"
    m "С кем?"
    g "С друзьями"
    m "Какими?"
    g "Одногруппниками"

    "Да, мне стыдно было говорить, что я иду гулять с девочкой…."

    m "Ну хорошо, иди, только не долго"
    g "Хорошо мам"

    jump street
    return

label street:

    scene nstreet with fade

    play music evening

    "Я вышел из дома, шел по улице"
    "Было не так темно, но фонари и вывески уже светились во всю"

    scene restaran with fade

    "Я подошел к месту назначения, но Кати не было"
    "Сказала мне не опаздывать, а сама опаздывает, ай ай ай"
    "Прошло минут 10 и я вижу как она идет"
    "Скорее запыхавшись плетется"

    g "Ну вот пожалуйста. И как это называется? Сама предупредила и забыла?"

    show KateSmugSad
    with dissolve

    k "Извини, меня дома задержали"
    g "Да ничего страшного"
    g "Куда пойдем?"

    hide KateSmugSad
    show KateTalkSmug
    with dissolve

    k "Я знаю! Я знаю! Я знаю!"
    k "В городе есть одно место, откуда можно посмотреть весь город, красиво выглядит"
    k "А именно крыша"
    "Ее глаза засияли от восхищения"

    "Да… Не ожидал я, что мы пойдем на крышу, у меня был вариант пойти в парк"
    "Хотя может не все потерянно"
    hide KateTalkSmug
    with dissolve

    stop music fadeout 1

    menu: 
        "Куда идти?"

        "Согласиться с Катей":
            jump krisha
        

        "Предложить свой выбор":
            jump park

    return

label krisha:

    g "Ну веди на крышу"

    show KateSmileBlush
    with dissolve

    k "Ураа, пошли только сначала зайдем в магазин и купим что-нибудь"
    g "Пошли"

    hide KateSmileBlush
    with dissolve

    play sound kassa
    "Мы зашли в магазин и купили колы, чипсов и пошли до той самой заветной крыши"
    "Пока мы шли успело конкретно потемнеть"
    "Мне кажется, от того, что стало еще темнее, город будет еще красивее"
    "Через какое то время, мы оказались на месте"

    show KateBlush
    with dissolve

    g "А как ты планируешь сюда зайти?"
    k "У меня тут подруга живет, я иногда прихожу сюда чтобы посмотреть на город"
    g "А, хорошо"

    "Через мгновение дверь открывается и мы заходим вовнутрь"
    "Вызываем лифт и едем на последний 20-й этаж"

    scene roof with fade
    play music night

    "Как только мы выходим на крышу, в глаза бросается красота города, как краски переливаются"

    hide KateBlush
    show KateSmug
    with dissolve
    k "Как вид?"
    g "Завораживающе"

    "Мы уселись, открыли колу, чипсы общались"

    g "А ты с этого города?"

    hide KateSmug
    show KateTalk
    with dissolve

    k "Нет, я за 120 километров отсюда жила"
    g "А почему сюда решила переехать?"
    g "Вроде есть другие города, где намного лучше чем тут"

    hide KateTalk
    show KateBlush
    with dissolve

    k "Ну и здесь колледж в котором мы учимся самый близкий по расположению"
    g "Понятно"
    k "А ты откуда?"
    g "Я тут живу, жил и буду скорее всего жить"
    k "А почему решил поступить в \"АКНИП?\""
    g "А я еще с детства понял, программирование это мое, поэтому с 13 лет и делал, что за компьютером сидел. Вот только определенное направление как то не выбрал еще"
    g "Так еще и некуда больше поступать было, это единственный и как говорят лучший колледж информатики на юге"

    hide KateBlush
    show KateLaugh
    with dissolve

    k "Ха-ха-ха, да, я тоже слышала"

    "Наш разговор прервал мой звонящий телефон"
    play sound rington

    hide KateLaugh
    show KateShocked
    with dissolve

    "Мне позвонила мама"
    "ЭТО ЧТО ВООБЩЕ ТАКОЕ?"
    "Сегодня точно что-то странное с телефоном"
    stop sound fadeout 1

    g "Да мам?"

    hide KateShocked
    show KateSmug
    with dissolve

    m "[ggname], ты где ?"
    g "Я гуляю еще"
    m "Это конечно все здорово, но пора и совесть иметь. Дуй домой, живо"
    "Катю похоже эта ситуация только забавляет"
    g "Хорошо, скоро буду"

    "Не вовремя мне позвонили…"
    "Да еще и позор какой, я тут как бы с девушкой гуляю, налаживаю отношения, а мне мама звонит как 10-летнему ребенку"

    hide KateSmug
    show KateSad
    with dissolve

    k "Домой уже зовут?"
    "Прервала Катя неловкую тишину"
    g "Да к сожалению…."
    g "Прости, что так получилось"

    hide KateSad
    show KateBlush
    with dissolve

    k "Ничего страшного, мне тоже уже пора идти"
    g "Тогда пошли?"
    k "Пошли"

    stop music fadeout 1

    hide KateBlush
    with dissolve

    play music evening

    scene restaran with fade

    "Мы спустились вниз"

    g "Может тебя домой проводить ?"

    show KateSmile
    with dissolve

    k "Да не, не стоит, я сама дойду. Да и далеко тебе идти придется."
    "А откуда она..."
    g "Хорошо, аккуратнее только"
    k "Хорошо, до завтра"
    g "Пока"

    hide KateSmile
    with dissolve

    "Мы попрощались и я поехал обратно домой"
    "Пока я шел у меня в голове жжужала мысль, а может все таки надо было настоять, может она хотела чтобы я ее провел, но стеснялась"
    "Или это {size=+15}я{/size} ее стеснялся"
    "Непонятно"

    stop music fadeout 1

    play sound open
    
    scene livingroom-night with dissolve

    "К моему приходу дом уже погрузился в глубокий сон, свет был везде выключен, а мама уже наверняка спала"
    "Я включил свет, разулся, поднимался в свою комнату"
    "Вдруг я услышал как в моей комнате кто-то роется или ходит"
    "Когда я зашел в комнату там никого не было"
    "Может у меня уже крыша поехала?"
    "Задался я уже многочисленным за день вопросом"
    "А может не может, а так и есть. Воспоминание про телефон сразу всплыло перед глазами. Как мне такое вообще показалось?"
    "Но мне сейчас было не до этого, больше всего на свете, сейчас, я хотел спать"
    "Я улегся на кровать и уснул "

    jump gulal


    return

label park:

    g "А может все же пойдем в парк?"

    show KateSad
    with dissolve

    k "Ну пошли в парк"

    hide KateSad
    show KateSmug
    with dissolve

    k "Но тогда пойдем в парк по моим правилам"

    play music park

    "Мы пошли с ней в парк революции, он был самый близкий от нас"

    scene fontan with fade

    hide KateSmug
    show KateShockBlush
    with dissolve

    "Катя завизжала"

    g "Что случилось?"
    k "Там фонтан!"
    g "И что….?"
    k "Идем в фонтан!"
    g "Я туда не пойду…."

    hide KateShockBlush
    show KateSmug
    with dissolve

    k "Пойдешь еще как!"

    "Я не очень то и хотел в фонтан, но меня туда повели насильно и у меня больше не оставалось выбора"
    "Мы в него вошли, меня сразу же обрызгали, а я в ответ"

    hide KateSmug
    show KateLaugh
    with dissolve

    k "Эй, ты мне волосы намочишь!"
    g "Первая начала"

    "В итоге мы были оба до нитки мокрые"
    "Я предложил ей пойти во ВкУсочку, чуть высохнуть"

    hide KateLaugh
    show KateSmile
    with dissolve

    k "Ну и как тебе ?"
    g "Довольно весело"
    k "Еще бы…."

    play music ringtone

    "Наш разговор прервал мой звонящий телефон"
    "Мне звонила мама"

    stop music fadeout 1

    g "Да мам?"
    m "[ggname], ты где ?"
    g "Я гуляю еще"
    m "Давай домой, поздно уже"
    g "Хорошо, скоро буду"

    "Не вовремя мне позвонили…"

    play music park

    hide KateSmile
    show KateNormal
    with dissolve

    k "Домой уже зовут?"
    g "Да к сожалению…."

    hide KateNormal
    show Kate
    with dissolve

    k "Ничего страшного, мне тоже уже надо идти"
    g "Тогда пошли?"
    k "Подожди... "
    k "Давай еще чуть просохнем и пойдем"
    g "Хорошо"

    "Мы просохли и вышли на улицу"

    g "Может тебя домой проводить ?"
    k "Да не, спасибо, не хочется лишний раз тебя обременять, я сама дойду"
    g "Хорошо, аккуратнее только, не заболей!"
    k "Хорошо, ты тоже, до завтра!"
    g "Пока"

    stop music fadeout 1

    hide Kate
    with dissolve

    "Мы попрощались  я пошел в сторону дома"
    "А я совсем не высох…. Главное и правда не заболеть"
    "Пока шел, я думал, что может надо было настоять, может она хотела чтобы я ее провел, но стеснялась"
    "Ну этого я уже не узнаю"

    scene livingroom-night with fade

    play sound open

    "Придя домой, свет был везде выключен, мама уже наверняка спала"
    "Я включил свет, разулся, пошел все мокрые вещи положил в ванну"
    "Потом я начал подниматься в свою комнату"
    "Вдруг я услышал как в моей комнате кто-то капашится и старается негромко ходить"
    "Когда я зашел в комнату там никого не было"
    "Может у меня уже крыша поехала"
    "Или мне показалось"
    "Но мне сейчас было не до этого, я хотел спать"
    "Я улегся на кровать и уснул "

    jump gulal

    scene black with fade


    return

label gulal:

    scene bedroom-with-books with fade

    play music alarm2

    "Да что это такое?!"
    "У меня походу реально крыша едет"
    "Вроде как 3-й день учебы, а голова уже поплыла"

    stop music fadeout 1

    "На удивление сегодня я встал без проблем"
    "У меня было открыто окно, хотя по моему я его закрывал вечером"
    "Я его закрыл"

    "Открыл телефон и начал смотреть расписание"
    "Ага, сегодня будет экономика, физика и физ-ра…."
    "Ненавидел физ-ру больше всего…."
    "Я взял свои блатные шорты, майку, все сложил в рюкзак и оделся"

    play sound iphone

    "Только я начал спускаться вниз чтобы позавтракать как мне пишет Маша"

    nvl clear

    nvl_narrator "ВКонтакте"

    m_nvl "Приветик, ты сегодня поедешь на метро?"

    "Не ожидал я ее сообщения, но отказать я могу так как я и вправду собирался поехать  на метро"
    g_nvl "Привет, да поеду"
    m_nvl "Хорошо, тогда в 7:40 жду тебя возле метро"
    g_nvl "Окей, буду"
    m_nvl "Жду"

    "Я думал поехать одному, слушая музыку, а то я давно ее не слушал, аж как-то не по себе"

    play music kitchen
    scene kitchen 1 with fade

    "Приготовив себе завтрак и поев, я посмотрел на время"
    "Было 7:20"
    "Вроде успевал"
    
    stop music fadeout 1

    scene street3 with fade
    play music street1

    "Выходя на улицу мой чуткий глаз заметил, что какая-то тень промелькнула за угол дома"
    "Чудится подумал"
    "Забив на эту тень, быстро побрел к метро"
    "Но все время, что я шел, не покидала мысль, что за мной следят"

    scene station with fade

    "Подошев к месту встречи, я осмотрелся, но Машу я не заметил"
    "Время было 7:38"

    g_nvl "Ты где?"
    m_nvl "Я уже иду, скоро буду"
    g_nvl "Хорошо, я уже подошел, жду"
    m_nvl "Иду иду"

    nvl clear

    "Ну долго ее и вправду ждать не пришлось"

    show MashaAnnoBlush
    with dissolve

    l "Привет"
    g "Привет, ты чего такая запыханная ?"
    l "Бежала, не успевала"
    g "Не бежала бы, ничего страшного небыло бы"
    l "Мы бы на пару тогда не успели бы"
    g "Ну ладно…."

    stop music fadeout 1

    hide MashaAnnoBlush
    with dissolve

    play sound rzd
    scene metro with fade
    play music train

    "Пока мы ехали, я все же успел послушать музыку"
    "Обожаю музыку, вайб всей моей жизни"

    play sound rzd
    stop music fadeout 1

    "Мы приехали, дошли вместе до колледжа и пошли к 118 кабинету"

    scene hallway with fade
    play music talk

    "Маше нужно было отойти, поэтому мы на время расстались"

    "Вдруг я слышу крики своих одногруппников"


    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"

    "Какие-то приколы у них…"
    "Как я подслушал, это был канал в Discord куда они скидывали веселые фразы которые говорят только из нашей группы и учителей"
    "Ну весело подумал я и начал осматриваться чтобы найти Катю"
    "Она стояла в углу что-то рассматривая в книге"
    "Хотя она обычно стоит с одногруппницами и общается"
    "Когда я к ней подошел она захлопнула книгу и посмотрела на меня"

    show KateSmileBlush
    with dissolve

    k "Привет"
    g "Привет"
    k "Как дела?"
    g "У меня хорошо, у тебя как?"
    k "У меня прекрасно"
    g "Выспалась после вчерашней прогулки?"
    k "Да"
    k "А ты?"
    g "А я сегодня впервые встал с нормально"
    k "Ну понятненько"

    "Такое чувство, что что-то случилось"
    "Но я не понимал, что"

    g "Что-то случилось?"

    hide KateSmileBlush
    show KateNormal
    with dissolve

    k "Нет, с чего ты взял?"
    g "Ты как-то не так отвечаешь…."
    k "Да вроде отвечаю как обычно…."
    g "Ну может мне показалось… Извини"
    k "Да ничего"

    hide KateNormal
    show KateSmile
    with dissolve

    k "Слушай, а ты не хочешь после пар кое-куда пойти?"
    g "Это куда?"
    k "Узнаешь, но думаю тебе понравится"

    "Интересно, куда она меня собралась повести"
    "Ну я решил лишних вопросов не задавать, а просто дождаться"

    hide KateSmile
    with dissolve

    play music naprag2

    menu: 
        "{sc}Не иди с ней{/sc}":
            jump dontgo

        "{swap=Иди@Беги отсюда@2}Иди{/swap}":
            jump go




    return

label notgulal:

    scene bedroom-with-books with fade

    play music alarm2

    "Да что это такое?!"
    "У меня походу реально крыша едет"
    "Вроде как 3-й день учебы, а голова уже поплыла"

    stop music fadeout 1

    "На удивление сегодня я встал без проблем"
    "У меня было открыто окно, хотя по моему я его закрывал вечером"
    "Я его закрыл"

    "Открыл телефон и начал смотреть расписание"
    "Ага, сегодня будет экономика, физика и физ-ра…."
    "Ненавидел физ-ру больше всего…."
    "Я взял свои блатные шорты, майку, все сложил в рюкзак и оделся"

    play sound iphone

    "Только я начал спускаться вниз чтобы позавтракать как мне пишет Маша"

    nvl clear

    nvl_narrator "ВКонтакте"

    m_nvl "Приветик, ты сегодня поедешь на метро?"

    "Не ожидал я ее сообщения, но отказать я могу так как я и вправду собирался поехать  на метро"
    g_nvl "Привет, да поеду"
    m_nvl "Хорошо, тогда в 7:40 жду тебя возле метро"
    g_nvl "Окей, буду"
    m_nvl "Жду"

    "Я думал поехать одному, слушая музыку, а то я давно ее не слушал, аж как-то не по себе"

    scene kitchen 1 with fade
    play music kitchen

    "Приготовив себе завтрак и поев, я посмотрел на время"
    "Было 7:20"
    "Вроде успевал"

    stop music fadeout 1

    scene street3 with fade
    play music street1

    "Выходя на улицу мой чуткий глаз заметил, что какая-то тень промелькнула за угол дома"
    "Чудится подумал"
    "Забив на эту тень, быстро побрел к метро"
    "Но все время, что я шел, не покидала мысль, что за мной следят"

    scene station with fade

    "Подошев к месту встречи, я осмотрелся, но Машу я не заметил"
    "Время было 7:38"

    g_nvl "Ты где?"
    m_nvl "Я уже иду, скоро буду"
    g_nvl "Хорошо, я уже подошел, жду"
    m_nvl "Иду иду"

    nvl clear

    "Ну долго ее и вправду ждать не пришлось"

    l "Привет"
    g "Привет, ты чего такая запыханная ?"
    l "Бежала, не успевала"
    g "Не бежала бы, ничего страшного небыло бы"
    l "Мы бы на пару тогда не успели бы"
    g "Ну ладно…."

    stop music fadeout 1

    play sound rzd
    scene metro with fade
    play music train

    "Пока мы ехали, я все же успел послушать музыку"
    "Обожаю музыку, вайб всей моей жизни"

    play sound rzd
    stop music fadeout 1

    "Мы приехали, дошли вместе до колледжа и пошли к 118 кабинету"

    scene hallway with fade
    play music talk

    "Маше нужно было отойти, поэтому мы на время расстались"

    "Вдруг я слышу крики своих одногруппников"


    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"
    o "В ЦИТАТНИК"

    "Какие-то приколы у них…"
    "Ну весело подумал я и начал осматриваться чтобы найти Катю, но ее не было"
    "Я думаю стоит ей написать"

    nvl_narrator "ВКонтакте"

    g_nvl "Привет, ты сегодня придешь?"
    k_nvl "Нет, не смогу"
    k_nvl "Дела просто, извини, повеселись пока без меня ;)"
    g_nvl "Эх, жалко"
    g_nvl "Удачки )"
    k_nvl "Спасибо и тебе)"

    "Ну я уже смирился"
    play sound iphone
    "Как вдруг слышу уведомление"

    k_nvl "Слушай, не хочешь пары прогулять и со мной кое-куда пойти ?"
    g_nvl "Кое-куда ?"
    k_nvl "Да, увидишь, думаю понравится"

    play music naprag2

    menu:
        "{sc}Не прогуливать пары{/sc}":
            jump repeat

        "{swap=Прогулять пары@Не делай этого@2}Прогулять пары{/swap}":
            jump notstay

    return

label repeat:

    g_nvl "Я наверное в колледже останусь, не хочу как-то пары прогуливать"
    k_nvl "Ну а если еще раз подумать?"

    menu:
        "{sc}Не прогуливать пары{/sc}":
            jump stay

        "{sc}Прогулять пары{/sc}":
            jump notstay

    return

label stay:

    stop music fadeout 1
    g_nvl "Нет, Кать, извини…."
    k_nvl "Ну ладно, ничего страшного, до завтра тогда"
    g_nvl "До завтра"
    nvl clear

    "Думая правильно я сделал или нет, не пойдя с ней, но думаю на парах было бы лучше остаться"
    "Звонок прозвенел и я зашел в аудиторию"

    stop music fadeout 1

    scene evening with fade
    play music klass

    "На это раз пришлось садиться с Мишей"

    show Misha
    with dissolve

    a "Здорова"
    g "Привет"
    a "Как дела?"
    g "Да ничего так, твои как ?"

    hide Misha
    show MishaHappy
    with dissolve

    a "У меня супер, даже мне кажется получше чем у тебя"

    "Как-то звучало агрессивно…"

    g "Ну так это хорошо же"
    "Ответа не последовало"

    hide MishaHappy

    "Дальше мы принялись слушать нового преподавателя"
    "Но я его не слушал, не запомнил как ее зовут и даже как она выглядит…."
    "Да мне было чуть все равно на эту пару" 
    stop music fadeout 1.0

    "Кое-как отсидев ее, я пошел на 3 этаж"
    "Я запомнил, что у нас там была пара, а какой кабинет, я не запомнил"

    scene evening with fade
    play music klass

    "Отсидев очередную пару, которую я не запомнил мне в голову пришла идея свалить с пары"
    "Все равно была физ-ра последняя на которую я не желал идти"

    stop music fadeout 1

    scene street3 with fade
    play music street1

    "Уходя с колледжа, я решаю пойти домой пешком"
    "Достав наушники, включив музыку я со спокойной душой пошел домой"
    "По пути увидел парк и решил там посидеть"

    stop music fadeout 1.0
    play music night

    scene park2 with fade

    "Пока сидел я увидел на соседней лавочке какой-то круглый светящийся предмет"
    "Я смотрел на него достаточно долго, вдруг его кто-то забыл"
    "В какой-то момент я встал и сел рядом с этим предметом"
    "Взяв его в руки, я покрутил его"
    "Посмотрев на него, я сложил его в рюкзак и быстро пошел домой чтобы там его тщательно рассмотреть"

    stop music fadeout 1

    play sound open
    scene livingroom-night with fade

    "Придя домой мама почему-то была дома, хотя по ощущениям был только ранний вечер"

    g "Ма, а чего ты дома ?"
    m "Да нас пораньше отпустили"
    g "А, понял"
    m "Как в колледже?"
    g "Да хорошо, пока не жалуюсь"
    m "Ну и отлично"

    "После этих слов я пошел в свою комнату"

    scene bedroom-with-books with fade

    "Достав эту штуку я принялся ее осматривать"
    "Она была необычная, посередине какая-то прозрачная труба в которой была какая-то жижа…."
    "А внешне выглядел как шар, но железный"
    "Я решил спрятать его в коробку с замком и спрятать под кровать"
    "Вскоре я пошел поел и снова пришел в комнату"
    "У меня из головы не выходила мысль"
    "Что это такое…."
    "А может мне не чудилось когда по моей комнате кто-то ходил или когда я увидел тень"
    "Да нет, чудилось, чего я накручиваю себя"
    "Посидев потупив я не заметил как вырубился"

    jump end



    return

label notstay:

    g_nvl "Хорошо, куда идти?"
    k_nvl "Замечательно"
    k_nvl "Выйди пока с колледжа, я тебе скину метку где я тебя ждать буду"
    g_nvl "Хорошо"
  

    scene kollege with fade

    stop music fadeout 1
    "Интересно, куда меня поведут"
    "Через время, Катя кидает мне метку"

    k_nvl "{image=images/metka.png}"
    k_nvl "Сюда едь"
    g_nvl "За город???"
    k_nvl "А ты как хотел?"

    "НИКАК Я НЕ ХОТЕЛ"

    k_nvl "Не бойся, все хорошо будет, я обещаю"
    g_nvl "Хорошо, скоро приеду"

    "Мда"
    "Один ответ лучше другого"
    "Ну ладно, думаю будет прикольно"
    "Я начал смотреть цены на такси, 700 рублей…. воу"
    "Ну ладно, поехали"

    scene highway 1 with fade

    "Меня таксист высадил возле дороги, потому что дальше мне надо было идти пешком"

    scene hiking-trail with fade
    play music les

    "Пока я шел по лесу я вышел к каким-то руинам, выглядело завораживающе"
    "Вдруг кто-то прыгает на меня сзади, валит на землю и закручивает руки"

    g "Это че за херня?"

    o "Не дергайся!"

    "Это был голос Кати"

    g "Ты че на меня накинулась?"
    k "Чтобы ты испугался"
    g "Испугала, довольна ?"

    show KateSad
    with dissolve

    k "Ну извини…."
    g "Ничего страшного, я не обижаюсь "
    "Да конечно, кто поверил"
    k "Ну и отлично"
    k "Тогда пошли"
    g "Куда?"

    hide KateSad
    show KateSmug
    with dissolve

    k "Увидишь"
    k "Как тебе виды?"
    g "Красиво"
    "Ужасно"

    stop music fadeout 1

    play music les2

    hide KateSmug
    with dissolve

    scene ruined with fade

    "По ощущениям мы прошли километра 2, а развалины все те же…"

    show KateNormal
    with dissolve

    k "Так, если заметишь круглый светящийся предмет, скажешь"
    g "Что?"
    k "Потом обьясню"
    g "Хорошо…."

    play music fon

    hide KateNormal
    with dissolve

    "И что это все значит?"
    "Интересно, что она от меня скрывает…."
    "Я решил с ней не спорить на счет этого, а просто искать то что она мне сказал"
    "Минут через 10, я прохожу через разрушенную арку и наступаю на что-то"
    "Это не было похоже на землю и я решил проверить"
    "Раскопав я увидел какую-то светящуюся штуку, примерно как мне описывала ее Катя"
    "Уже подумав крикнуть ей, меня что-то остановило и я решил забрать этот интересный объект себе"
    "Тут подходит Катя"

    show KateNormal
    with dissolve

    k "Нашел что-нибудь?"
    g "Нет"

    "Фух, вовремя я сложил это в рюкзак…."
    "Тело охватила непонятная дрожь"
    "И почему я резко перестал доверять этой девчонке?"
    "И зачем я вообще согласился с ней ехать?"
    "В голове был только один вопрос, зачем, ЗАЧЕМ, {size=10}{b}Зачем?{/b}{/size}"

    g "Слушай, а мы долго тут будем?"
    k "Нет, давай еще чуть поищем и пойдем"
    g "Ладно"

    "Мы искали то что лежит у меня в рюкзаке еще минут 10"

    k "Ладно, я думаю мы ее тут не найдем"
    "Что значит её?"
    k "Пойдем на дорогу"

    hide KateNormal
    with dissolve

    stop music fadeout 1

    scene highway 1 with fade

    "Когда мы пришли к дороге, где меня высадил таксист, Катя начала вызывать такси"
    "Такси приехало, мы сели"
    "Всю дорогу мы провели в тишине"
    "Мы подъехали к какому-то дому, как я понял тут живет Катя"

    g "Тут живешь?"
    k "Да"
    k "Ладно, давай, до завтра"
    g "А может расскажешь, что сегодня было?"
    k "Потом как-нибудь"
    g "Ну ладно…."

    play sound hug

    "Она меня обняла и ушла за двери"
    "Ну а мне, что делать, я тоже домой пошел"

    play sound close
    scene livingroom-night with fade

    "Придя домой мама почему-то была дома, хотя по ощущениям был только ранний вечер"

    g "Ма, а чего ты дома ?"
    m "Да нас пораньше отпустили"
    g "А, понял"
    m "Как в колледже?"
    g "Да хорошо, пока не жалуюсь"
    m "Ну и отлично"

    scene bedroom-with-books with fade

    "После этих слов я пошел в свою комнату"
    "Достав эту штуку я принялся ее осматривать"
    "Она была необычная, посередине какая-то прозрачная труба в которой была какая-то жижа…."
    "А внешне выглядел как шар, но железный"
    "Я решил спрятать его в коробку с замком и спрятать под кровать"
    "После таких приключений и тайн мне захотелось спать и я отрубился…."

    jump end

    return

label go:

    g "Хорошо, давай поедем"

    show KateSmileBlush
    with dissolve

    k "Ура!  Тогда после пар поедем"
    g "Договорились"

    "Это мне придется еще и на физру идти…"
    "Ну ладно, мне было очень интересно, что она мне показать хочет"

    hide KateSmileBlush

    "После физ-ры мое тело ныло так, как будто я пробежал 100 км не останавливаясь"
    "Я переоделся и пошел к выходу"
    "Тут выходит Катя с одногруппницами"

    show KateNormal
    with dissolve

    k "Поехали?"
    g "Поехали.."

    stop music fadeout 1

    hide KateNormal
    with dissolve

    "Мы вызвали такси"
    "Нас вывезли загород и остановили возле обочины"

    scene highway 1 with fade

    show KateNormal
    with dissolve

    k "Дальше нам надо будет идти пешком"
    g "..."

    "Меня это начинает {b}немного напрягать{/b}"
    "Я не мог сказать ей, что у меня все тело болит, поэтому просто молча пошел за ней"

    scene ruined with fade

    play music les2

    "Когда мы пришли, я увидел руины"
    "Они были уже заросшие, но выглядело сногсшибательно"

    hide KateNormal
    show KateSmug
    with dissolve

    k "Ну как тебе?"
    g "Красиво"
    k "Понятно"

    "Мы продолжили дальше идти"

    "По ощущениям мы прошли километра 2, а развалины все те же…"

    hide KateSmug
    show KateNormal
    with dissolve

    play music fon

    k "Так, если заметишь круглый светящийся предмет, скажешь"
    g "Что?"
    k "Потом обьясню"
    g "Хорошо…."

    "И что это все значит?"
    "Интересно, что она от меня скрывает…."
    "Я решил с ней не спорить на счет этого, а просто искать то что она мне сказал"

    hide KateNormal
    with dissolve

    "Минут через 10, я прохожу через разрушенную арку и наступаю на что-то"
    "Это не было похоже на землю и я решил проверить"
    "Раскопав я увидел какую-то светящуюся штуку, примерно как мне описывала ее Катя"
    "Уже подумав крикнуть ей, меня что-то остановило и я решил забрать этот интересный объект себе"
    "Тут подходит Катя"

    show KateNormal
    with dissolve

    k "Нашел что-нибудь?"
    g "Нет"

    "Фух, вовремя я сложил это в рюкзак…."
    "Тело охватила непонятная дрожь"
    "И почему я резко перестал доверять этой девчонке?"
    "И зачем я вообще согласился с ней ехать?"
    "В голове был только один вопрос, зачем, ЗАЧЕМ, {size=10}{b}Зачем?{/b}{/size}"

    g "Слушай, а мы долго тут будем?"
    k "Нет, давай еще чуть поищем и пойдем"
    g "Ладно"

    "Мы искали то что лежит у меня в рюкзаке еще минут 10"

    k "Ладно, я думаю мы её тут не найдем"
    "Что значит её?"
    k "Пойдем на дорогу"

    stop music fadeout 1

    hide KateNormal
    with dissolve

    scene highway 1 with fade

    "Когда мы пришли к дороге, где меня высадил таксист, Катя начала вызывать такси"
    "Такси приехало, мы сели"
    "Всю дорогу мы провели в тишине"
    "Мы подъехали к какому-то дому, как я понял тут живет Катя"

    g "Тут живешь?"

    show KateNormal
    with dissolve

    k "Да"
    k "Ладно, давай, до завтра"
    g "А может расскажешь, что сегодня было?"
    k "Потом как-нибудь"
    g "Ну ладно…."

    hide KateNormal
    with dissolve

    play sound hug

    "Она меня обняла и ушла за двери"
    "Ну а мне, что делать, я тоже домой пошел"

    play sound close
    scene livingroom-night with fade

    "Придя домой мама почему-то была дома, хотя по ощущениям был только ранний вечер"

 

    g "Ма, а чего ты дома ?"
    m "Да нас пораньше отпустили"
    g "А, понял"
    m "Как в колледже?"
    g "Да хорошо, пока не жалуюсь"
    m "Ну и отлично"

    scene bedroom-with-books with fade

    "После этих слов я пошел в свою комнату"
    "Достав эту штуку я принялся ее осматривать"
    "Она была необычная, посередине какая-то прозрачная труба в которой была какая-то жижа…."
    "А внешне выглядел как шар, но железный"
    "Я решил спрятать его в коробку с замком и спрятать под кровать"
    "После таких приключений и тайн мне захотелось спать и я отрубился…."

    jump end



    return

label dontgo:

    g "Я наверное сегодня домой пойду, надо дела делать"
    hide KateSmile
    show KateSad
    with dissolve
    k "Хорошо, а послезавтра прогуляемся ?"
    g "А вот послезавтра можно"
    k "Ну тогда договорились"
    g "Договорились"

    "У меня было {b}очень плохое предчувствие{/b}"
    "Как будто бы, от моих слов сейчас зависит судьба всего человечества"
    "Думая правильно я сделал или нет, не пойдя с ней, но мне сегодня не очень хотелось куда-то идти"

    stop music fadeout 1

    "После пар, я решаю пойти домой пешком"
    "Попрощался с Катей, достал наушники, включив музыку и со спокойной душой пошел"

    play music evening
    scene street3

    "По пути увидел парк и решил там посидеть"
    "Пока сидел я увидел на соседней лавочке какой-то круглый светящийся предмет"
    "Я смотрел на него достаточно долго, вдруг его кто-то забыл"
    "В какой-то момент я встал и сел рядом с этим предметом"
    "Взяв его в руки, я покрутил его"
    "Посмотрев на него, я сложил его в рюкзак и быстро пошел домой чтобы там его тщательно рассмотреть"
    stop music fadeout 1

    play sound close
    scene livingroom-night with fade

    "Придя домой мама почему-то была дома, хотя по ощущениям был только ранний вечер"

    g "Ма, а чего ты дома ?"
    m "Да нас пораньше отпустили"
    g "А, понял"
    m "Как в колледже?"
    g "Да хорошо, пока не жалуюсь"
    m "Ну и отлично"

    scene bedroom-with-books with fade

    "После этих слов я пошел в свою комнату"
    "Достав эту штуку я принялся ее осматривать"
    "Она была необычная, посередине какая-то прозрачная труба в которой была какая-то жижа…."
    "А внешне выглядел как шар, но железный"
    "Я решил спрятать его в коробку с замком и спрятать под кровать"
    "Вскоре я пошел поел и снова пришел в комнату"
    "У меня из головы не выходила мысль"
    "Что это такое…."
    "А может мне не чудилось когда по моей комнате кто-то ходил или когда я увидел тень"
    "Да нет, чудилось, чего я накручиваю себя"
    "Посидев потупив я не заметил как вырубился"

    jump end

    return

label end:

    scene black with fade

    play music naprag

    o "[ggname]"
    "Кто это?"
    o "[ggname]..."
    "Я я я, это кто ?"
    o "[ggname], спаси меня"
    "Вы кто? Куда идти"
    o "{b}[ggname]!!!{/b}"
    "ААА"

    stop music fadeout 1

    scene bedroom-with-books with fade

    "Ааа, что такое, кого спасать ?"

    "Я резко встал от кошмара, весь в холодном поту"
    "Давно у меня не было таких кошмаров…."
    "Время было ближе к 5 утра"
    "Ух нифига себе я встал…."
    "Я пытался еще уснуть, но не получалось"
    "Мама еще спала и я решил ее не будить"
    "Я встал, оделся и пошел на кухню"

    scene kitchen 1 with fade

    "Пока сидел на кухне, я обдумывал, свой сон"
    "«Спаси меня»"
    "Эти крики…. Кто меня звал?"
    "Все что происходило со мной эти три дня я еще думал, что я головой ударился может, а сейчас я думаю, что я сошел с ума, либо эти события связаны "
    "Посидев все осмыслив, я решил себя не загонять"
    "Вдруг я вспомнил про тот железный шар и побежал его проверить"
    "Он был на месте, я выдохнул"
    "Но все таки очень интересно, что это за шар…."
    "Может вскоре узнаю"
    "Время было уже 7:00"
    "Ждать до метро мне не хотелось, поэтому я оделся и решил пойти пешком"

    play music street1

    scene street3 with fade

    "Улицы уже заполнили люди, которые то ли на работу шли, то ли еще куда"
    "Такие беззаботные, казалось мне на тот момент"
    "Я не заметил как дошел до колледжа, а до начала пар оставалось 30 минут"
    "Не стоять же мне 30 минут под колледжем"
    "Подумав, я решил пойти в магазин и где-нибудь посидеть "

    stop music fadeout 1

    scene magaz with fade
    play music magaz

    "Зайдя в магазин я увидел как за мной заходит мужик, накаченный, широкий "
    "Я его приметил еще возле своего дома"
    "Ну может, случайность…."
    "Пока я ходил возле полок с продуктами"
    "Я почувствовал как меня кто-то толкнул в плече "
    "Это был как раз тот мужик"

    o "Извиняй, малой"

    "Он так это гордо и грозно сказал, что я испугался"
    "После этого он просто вышел из магазина"
    "Я купил колы и вышел из магазина"

    play sound kassa
    stop music fadeout 1

    "Этого мужика уже не было"
    "Посидев 20 минут на лавочке, я пошел к колледжу"

    scene kollege with fade
    play music street1

    "Подходя ко входу я увидел как Катя выходит из какой-то черной, тонированной машины "
    "За ней вышел мужчина лет 40, в строгом костюме, в черных очках"
    "Недовольно она подошла ко мне"

    k "Привет [ggname]"

    show KateKiss
    with dissolve

    g "При…"

    hide KateKiss
    with dissolve

    "Она подошла и поцеловала меня и пошла дальше"

    play music fon

    "Выпав в осадок я тупил еще секунд 30"
    "Что это было?"
    "Посмотрев на мужика который вышел за Катей, он смотрел на меня с угрожающем взглядом"
    "Я быстро пошел во внутрь колледжа"
    "От неожиданности таких действий, я сел на лавочку и в шоке сидел это обдумывал и обрабатывал у тебя в голове"


    "После долгого обдумывания, я пошел на пару"
    "Подойдя к кабинету, я боялся войти, но делать было нечего"

    scene evening with fade

    g "Здравствуйте, извините за опоздание…."
    o "Здравствуй, ничего страшного, заходи"
    "Проходя по кабинету я посмотрел на Катю"
    "Она на меня посмотрела смущенно"
    "Рядом с ней сидела одногруппница "
    "С Мишей я тоже не сяду, с ним сидел одногруппник "
    "Ну а свободное место было только в конце"
    "Всю пару я думал о Кате и о случившимся "
    "Думал подойти к ней поговорить"
    "Когда пара кончилась, я так и не решился подойти к Кате"
    "На парах дальше сидеть я не хотел потому что не было настроения"
    "Пока никто не видел, я вышел с колледжа, надел наушники и пошел гулять"

    scene street3 with fade

    "Мне писала Катя, Маша, Миша, почему я ушел ничего не сказав "
    "Не хочу никому отвечать, надоели"
    "Выключив звук на телефоне, я побрел дальше"
    "Я проходил с музыкой до вечера и уже думал идти домой"
    "Проходя по улице, мой глаз упал на тень которая идет за мной"
    "Я свернул в переулок, думая, что это не за мной, но я ошибся и это было за мной…."
    "Долго не думая, я побежал, параллельно сворачивая в переулки"
    "Вроде бы отстали"
    "Пока меня не нашли, я быстро пошел до дома"

    stop music fadeout 1

    scene livingroom-night with fade
    play sound close


    "По приходу домой, мамина обувь стояла на входе, она была дома"
    m "Кто там?"
    g "Это я ма"
    m "[ggname]?"
    g "Да я, а что такое?"

    play music naprag3

    m "Я думала ты в комнате, я шурашние там слышала, не хотела мешать"

    "С шоком я побежал в комнату, я увидел, что коробка была открыта, а странный шар забрали"
    "Окно было открыто, я быстро подбежал, посмотрел, увидел как с ним убегает какой-то парень"

    scene black with fade

    "Выбежав из дома, я побежал за ним, но меня кто-то схватил и заткнул тряпкой рот и нос"

    o "Тихо тихо, не дергайся"

    "И тут я начал терять равновесие, в глазах начало темнеть, звуки стали искаженными и в итоге я отключился"

    stop music fadeout 1



    jump credits
    return

init:
    transform txt_up:
        yalign -3
        linear 10.0 yalign 1.5

label credits:
    play music end
    scene black with dissolve
    show text 'Идея: Филиппов Олег(Korenti), Мирошников Сергей{p} \n Продюсер, Режиссёр: Мирошников Сергей, Филиппов Олег{p}\n Программисты: Филиппов Олег, Мирошников Сергей{p} \nГлавные сценарист: Мирошников Сергей{p} \nСценаристы: Мирошников Сергей, Филиппов Олег{p} \nЗвукорежиссёр: Филиппов Олег(Korenti){p} \nАвторы благодарят за помощь в создании визуальной новеллы{p} \nМанакову Ольгу Петровну за возможность реализовать данную идею и получить за неё автомат{p} \nСоздателей Renpy за упрощение в написании игры данного жанра{p} \nБлагодарим всех, кто прошёл данную игру{p} {p} \nЛюди не могут думать одинаково,\n но понимать друг друга они должны.\n На то они и люди!{p} \nВиктор Цой.{p}' at txt_up
    pause 40
    $ renpy.movie_cutscene('Продол.ogv')
    return


    #show eileen happy


#     label the_question:                                     #SCREEN 2
#         show eileen concerned at left with move
#         e "But am I the {u}quick fox{/u} or the \"lazy dog\"?"
#         call question_selector

#         menu:                                               #SCREEN 3
#             "The Quick Fox":                                #FOX
#                 show eileen vhappy at right with pixellate  #SCREEN 4-1
#                 $ animal = 'fox'
#                 "Eileen" "{i}Yes{/i}, because I am {size=+10}FAST!{/size}"
#             "The Lazy Dog":                                 #DOG
#                 hide eileen with dissolve                   #SCREEN 4-1
#                 $ animal = 'dog'
#                 "Eileen" "{b}Yes{/b}, because I am... {color=#808080}always... {size=-5}sleepy...{/size}{/color}"
#             "Question [question_tally]: [repeat_question]": #SCREEN 4-3
#                 jump the_question
#         jump end

# label question_selector:
#     $ NumberGenerator = renpy.random.randint(1, 3)
#     if NumberGenerator == 3:
#         $ repeat_question = "What?"
#     elif NumberGenerator >= 2 and NumberGenerator < 3 or NumberGenerator == 5:
#         $ repeat_question = "Say that again?"
#     else:
#         $ repeat_question = "Huh?"
#     # $ repeat_question = renpy.random.choice(["What?", "Say that again?", "Huh?"])
#     $ question_tally += 1
#     return

# label end:                                                  #SCREEN 5
#     play music "audio/Голосовое сообщение - Голосовое сообщение (mp3cut.net).mp3"
#     scene хата with vpunch:                             #new scene
#         zoom 0.55
#     e "I'm a [animal]!"
    return