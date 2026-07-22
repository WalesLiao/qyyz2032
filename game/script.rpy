define l = Character("李爷爷", color="#bb9900")
define w = Character("“我”", color="#00ffdd")
define gm = Character(" ", color="#00ffdd")
define narrator = nvl_narrator
image ending_movie = Movie(play="videos/qyyz2032.webm",loop=False)

transform ending_fadeout:
    alpha 1.0
    time 69.0
    linear 1.0 alpha 0.0

screen ending_video_screen():
    modal True
    add "#000"
    add "ending_movie" at ending_fadeout
    timer 70.0 action [Function(renpy.movie_stop), Return()]

# 开场画面

# 开场LOGO
image pure_black = "#000"
image pure_white =  "#ffffff"

label before_main_menu:
    play music "BV1Wx7H62EUu.ogg" loop
    scene pure_black
    show pure_white with Dissolve(1.5)
    show logo at truecenter with Dissolve(2.0)
    pause 2.5
    hide logo with Dissolve(1.5)
    return


# 游戏在此开始。

transform speaker:
    zoom 0.4
    # 左上角为原点，向右向下为正。
    pos (0,1080)
    anchor (0,1.0)
label start:
    image bg xsg = Transform("bg xsg.jpg", zoom=0.48)
    scene bg xsg with bites
    play music "Days_of_love.ogg" loop fadein 2.0
    "2032年春天，学校筹备一百二十周年校庆，启动了新版校史的编纂工作。我和几位同学作为学生代表参与其中，帮忙整理资料。"
    "指导我们的是李爷爷，退休多年的老教师，他曾参与过多次校史的编纂工作。"
    image bg das = Transform("bg das.jpg", zoom=0.675)
    scene bg das with w19
    "跟着李爷爷，我们走进校史馆档案室，来这里查找相关史料。"
    "李爷爷从档案架上抽出一本资料，翻开封皮。"
    play sound "audio/page_flip.ogg"
    image xs 0 = Transform("xs 0.jpg", zoom=0.675)
    show xs 0 with w9
    show lyy stand at speaker
    l "“这一页是学校创办时的记录，字迹还很清楚——‘祁阳县立中学堂创办，以县城九塘冲延寿寺为校址，唐学任校长，招收初中1个班。’”"
    "他若有所思地点点头。"
    l "一百多年了，纸黄了，字还在。"
    image xs 1 = Transform("xs 1.jpg", zoom=0.675)
    play sound "audio/page_flip.ogg"
    show xs 1 with w9
    l "“可第二页就不行了。污渍、虫蛀、水泡……有些被盖住了，有些已经残缺不全了。”"
    l "“这本册子，前面几页还能看，越往后翻，被盖住的地方越多。”"
    "他抬起头看着我。"
    l "“每一块污渍下面，都压着一段故事。如果没有人去把它弄干净，那些故事就永远被盖住了。”"
    l "“你来吧，用橡皮擦试试。从第一块开始，能擦掉多少是多少。”"
    "李爷爷说着，递给我一块橡皮擦。"
    w "“好，我试试。”"
    hide lyy with Dissolve(0.8)
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 2 = Transform("xs 2.jpg", zoom=0.675)
    show xs 2 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 3 = Transform("xs 3.jpg", zoom=0.675)
    show xs 3 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 4 = Transform("xs 4.jpg", zoom=0.675)
    show xs 4 with w12
    "……"
    image bg st1 = Transform("bg st1.jpg", zoom=0.6216)
    scene bg st1 with bites
    show lyy stand at speaker
    l "“一九四三年四月，祁阳县立中学在浯溪中官寺复办。”"
    l "“首任校长文星三，清华大学毕业，留过美。”"
    l "“他接手的时候学校一穷二白，筹资金、借校舍、聘教师，什么都从头来。”"
    l "“可他有个习惯——招来的两班新生，七十一人，他一个一个当面谈话。”"
    l "“有人后来写文章回忆：‘一个夜晚，油灯如豆，校长找学生谈话。’”"
    l "“那时候晚自习点的还是植物油灯，檐低窗小，采光差得很。”"
    l "“第二年九月，日寇陷祁，校舍被炸，学校停办。”"
    l "“可第二年抗战胜利，九月就复办了。校长雷声溢接手的时候，校舍已经炸毁了，校具荡然无存。”"
    l "“他四处奔波，租民房、借桌椅，让学校如期开了学。”"
    l "“战火里，这所学校搬了三次家，炸了一次，停了一次。可每次停了，第二年就复办。学生接回来，课继续上。”"
    l "{color=#ff0000}“一所学校可以被炸毁，但教育不会。”{/color}"
    "……"
    play sound "audio/page_flip.ogg"
    image xs 5 = Transform("xs 5.jpg", zoom=0.675)
    scene xs 5 with w9
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 6 = Transform("xs 6.jpg", zoom=0.675)
    show xs 6 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 7 = Transform("xs 7.jpg", zoom=0.675)
    show xs 7 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 8 = Transform("xs 8.jpg", zoom=0.675)
    show xs 8 with w12
    "……"
    image bg jyt = Transform("bg jyt.jpg", zoom=0.5)
    scene bg jyt with Dissolve(0.8)
    show lyy stand at speaker
    l "“一九四七年，校长何觐光增收学生的‘俸谷’——说白了就是加收学费米。”"
    l "“那时候家里本来就困难，这一加，好些人读不起了。”"
    l "“学生们没有忍。初一班的李蟠，连夜写了一封‘合同’，让同学们签名。那天晚上熄了灯，训育员把他叫到校长办公室。”"
    l "“何觐光满脸怒气：‘合同书是不是你写的？’李蟠当场认了：‘学校加收俸谷违法，应该取消。’何觐光吼了一声：‘滚！’”"
    l "“第二天清早，布告贴了出来——李蟠、朱建国、管志城、于震球、黄月华，五人被开除学籍。”"
    l "“可这五个人没有认。他们分头到县里各个部门申诉，家里托人说情，可何觐光一律不答应。”"
    l "“县城里走遍了，没有结果。李蟠和管志城两个人，决定上长沙，找省教育厅。”"
    l "“第一次去，回来没办成。再去第二次，当面陈辞。省教育厅终于下了批复：‘责令学校收回成命，五名学生回校复学，发还非法收取的俸谷。’”"
    l "“消息传回祁阳那天，全校同学列队到县城迎接，给五个人戴上大红花，沿途贴标语、呼口号。后来他们给自己取了个外号，叫{color=#ff0000}‘五虎’{/color}。”"
    l "“档案里有一句原话：‘映出学生受到民主思想浸润，有着坚强的斗争精神。’”"
    l "“后来五虎各奔东西。李蟠成了湖南师大外语学院的翻译家，朱煦成了湖南画报社主任。但不管走到哪里，他们都记得祁阳一中。”"
    l "“用组织、用文字、用规则，十七八岁的年轻人争回了自己应有的东西。”"
    l "{color=#ff0000}“祁阳一中学生‘不服输’的劲头，从那时候就种下了。 ”{/color}"
    "……"
    play sound "audio/page_flip.ogg"
    image xs 9 = Transform("xs 9.jpg", zoom=0.675)
    scene xs 9 with w9
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 10 = Transform("xs 10.jpg", zoom=0.675)
    show xs 10 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 11 = Transform("xs 11.jpg", zoom=0.675)
    show xs 11 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 12 = Transform("xs 12.jpg", zoom=0.675)
    show xs 12 with w12
    "……"
    image bg qyyzold = Transform("bg qyyzold.jpg")
    scene bg qyyzold with bites
    show lyy stand at speaker
    l "“一九四九年五月，湖南解放在即。祁阳县中地处湘江和湘桂公路交叉口，是桂系军队进出湖南必经之地。溃退的部队常到学校停留吃住，学校被迫停课。”"
    l "“校长张雨生有‘组织应变’的打算，进步师生联合起来，和他面对面斗争了两次，硬是没让他得逞。”"
    l "“就在那段时间，初四班有个学生叫徐祯安，刚从武昌回祁阳不久。”"
    l "“八月，他受党组织派遣去北区开展工作，不幸被桂系军逮捕，杀害在白茅滩太平岭。”"
    l "“牺牲的时候，他才十八岁。 是解放战争时期祁阳县牺牲的唯一一名地下党员。”"
    "李爷爷停了一下，声音沉了些。"
    l "“八月下旬，校长跑了，教师散了，学生也都回了家。学校里只剩下食堂里存着不少粮食。管食堂的学生怕粮食丢了，开学没着落，便都留了下来”"
    l "“白天守着粮仓，夜里轮流巡逻。这就是祁阳一中历史上最后的‘护校队’。 ”"
    l "“没过多久，解放军先遣部队到了。战士们跟守校的学生处得很好，教他们唱《解放区的天是明朗的天》，还一起写标语。”"
    l "“第二天部队开拔，走之前在桌上留了一封感谢信和一块钱——头天晚上借了煤油灯，不小心打坏了一只灯泡。”"
    l "“十月九日，祁阳解放。仅仅过了一个月——十一月，学校就创办了高中部。 首任校长陈秋云，大学毕业，地下党员。”"
    l "“战火刚熄，校舍还带着弹痕。为什么这么急？”"
    l "“因为护校的师生们说：{color=#ff0000}新中国需要人才，我们一天都不能等。{/color} ”"
    "……"
    play sound "audio/page_flip.ogg"
    image xs 13 = Transform("xs 13.jpg", zoom=0.675)
    scene xs 13 with w9
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 14 = Transform("xs 14.jpg", zoom=0.675)
    show xs 14 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 15 = Transform("xs 15.jpg", zoom=0.675)
    show xs 15 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 16 = Transform("xs 16.jpg", zoom=0.675)
    show xs 16 with w12
    "……"
    image bg yct = Transform("bg yct.jpg", zoom=0.48)
    scene bg yct with bites
    show lyy stand at speaker
    l "“祁阳一中从浯溪迁来的时候，这块地方坑坑洼洼，除了一些古树，别的什么都没有。”"
    l "“五十年代，学校领导带着师生自己动手，植树造林，把黄土山坡改成了绿树成荫的校园。”"
    l "“一九五一年，校长陶自强做了一件出人意料的事——拿出自己的工资，在校园里修了一座亭子。”"
    l "“他给亭子取名‘迎潮亭’，还亲手写了一副对联——”"
    l "{color=#ff0000}‘风景四时佳，如临山水画图，烟树晴岚开粉本；’{/color}"
    l "{color=#ff0000}‘江山千里碧，可有人才妙笔，落霞孤骛写新词。’{/color}"
    l "“上联写景——湘江、宝塔、烟树、晴岚，都是祁阳的景；”"
    l "“下联写人——他盼着从这所学校走出去的人，将来能用妙笔写新词、写新篇。”"
    l "“一九五一年，陶铸回到祁阳，看了这座亭子，也看了这副对联。”"
    image bg 1968black = Transform("bg 1968black.jpg")
    scene bg 1968black with Dissolve(0.8)
    $ renpy.pause(2.0, hard=True)
    image bg yct = Transform("bg yct.jpg", zoom=0.48)
    scene bg yct with bites
    show lyy stand at speaker
    "李爷爷声音沉了些。"
    l "“后来那几年，祁阳一中和其他学校一样，经历了很多事。七位老师被关过，十八位老师被遣送回家。”"
    l "“可我听说，在最难的那段日子里，有人在迎潮亭的柱子上，用铅笔悄悄刻了四个字——{color=#ff0000}‘还会好的’{/color}。”"
    l "“刻字的人是谁，后来没人找得到。可那四个字留下来了。”"
    l "“一座亭子，从五十年代初立在那里，看尽了花开花落、人来人往，替我们守住了那段岁月里最珍贵的东西——{color=#ff0000}求知的火种，和对未来的念想{/color}。 ”"
    w "“刻字的那个人……后来回来过吗？”"
    l "“不知道。也许回来过，站在亭子前面看了看，什么也没说。也许没有。但字还在，就够了。”"
    "……"
    play sound "audio/page_flip.ogg"
    play music "qyyzxg.ogg" loop fadeout 2.0 fadein 2.0
    image xs 17 = Transform("xs 17.jpg", zoom=0.675)
    scene xs 17 with w9
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 18 = Transform("xs 18.jpg", zoom=0.675)
    show xs 18 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 19 = Transform("xs 19.jpg", zoom=0.675)
    show xs 19 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 20 = Transform("xs 20.jpg", zoom=0.675)
    show xs 20 with w12
    "……"
    image bg gp = Transform("bg gp.jpg")
    scene bg gp with bites
    show lyy stand at speaker
    l "“这张歌谱，写于八十年代后期。”"
    l "“写词的叫桂兹孝，那时候是学校的党总支书记。他给自己揽了个活——为祁阳一中写一首校歌。”"
    l "“有人说他何必呢？又不是本职工作，写好了也没人给你发奖金。”"
    l "“他说：‘祁阳人吃得苦、霸得蛮，祁阳一中的校歌，也得有点这股子劲。’”"
    image bg wct = Transform("bg wct.jpg")
    scene bg wct with bites
    show lyy stand at speaker
    l "“他一个人翻县志、走山水。跑到文昌塔下看‘宝塔巍巍’， 爬上石头山看‘天马腾飞’。”"
    image bg mysk = Transform("bg mysk.jpg")
    scene bg mysk  with bites
    show lyy stand at speaker
    l "“走进浯溪碑林看那些唐宋留下来的石刻，写下‘书岩万卷哺群英’。”"
    image bg sy = Transform("bg sy.jpg")
    scene bg sy with bites
    show lyy stand at speaker
    l "“‘书岩’这两个字，取的就是咱们祁阳的文脉——几千年的石刻，风吹雨打，一个字都没少。”"
    l "“桂老师说，祁阳一中的学子，就要像浯溪的石刻一样，经得起风雨，留得下印记。”"
    l "“写好了词，音乐老师高清元接过曲谱。那时候没有打谱软件，他就在五线谱纸上一格一格地用钢笔画。”"
    image bg gp = Transform("bg gp.jpg")
    scene bg gp with bites
    show lyy stand at speaker
    l "“‘进行速度，信心百倍，充满朝气’——这行字写在曲谱最上面。”"
    l "“桂兹孝写词，高清元谱曲，一个党总支书记、一个音乐老师，就这么把那首歌唱起来了。”"
    l "“八九年前后，校歌开始在校园里传唱。新入学的新生要学，毕业班离校前要唱，运动会开幕式上要放。”"
    l "“一届一届传下来，没人组织，就是到了时候自然就唱起来了。”"
    l "{color=#ff0000}“写一首歌不难。难的是一届又一届的学生一直唱下去。而这歌，一唱就是四十多年。”{/color}"
    "……"
    play sound "audio/page_flip.ogg"
    play music "hpdzdjqr.ogg" loop fadeout 2.0 fadein 2.0
    image xs 21 = Transform("xs 21.jpg", zoom=0.675)
    scene xs 21 with w9
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 22 = Transform("xs 22.jpg", zoom=0.675)
    show xs 22 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 23 = Transform("xs 23.jpg", zoom=0.675)
    show xs 23 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 24 = Transform("xs 24.jpg", zoom=0.675)
    show xs 24 with w12
    "……"
    image bg syzx = Transform("bg syzx.jpg")
    scene bg syzx with Dissolve(0.5)
    show lyy stand at speaker
    l "“一九八九年九月，省教委批准祁阳一中为湖南省实验中学。一九九三年五月正式授牌。”"
    image bg zdzx = Transform("bg zdzx.jpg")
    scene bg zdzx with bites
    show lyy stand at speaker
    l "“第二年学校又申报省重点，一九九五年十二月获批，一九九六年元月举行双挂牌仪式。全省同时挂这两块牌子的学校只有三所：师大附中、郴州市一中，和咱们祁阳一中。”"
    l "“就在那几年，学校出了几本书——《风华正茂》《书林星墨》《校园风范》。几位老师四处奔走，请名家题写书名。”"
    image bg wy = Transform("bg wy.jpg")
    scene bg wy with bites
    show lyy stand at speaker
    l "“桂夏至和唐文新去长沙，到省作协主席未央家里，请他为《风华正茂》题写书名。”"
    image bg yxy = Transform("bg yxy.jpg")
    scene bg yxy with bites
    show lyy stand at speaker
    l "“蒲定去北京出差，到姚雪垠家请题词。门卫拦住不让进，说姚老不见客。”"
    l "“蒲定写了一张纸条递进去，姚老一看，得知是五十年代武汉大学的老学生来了，连忙让他进来。”"
    l "“姚老说：‘我现在不给任何人题词了。’”"
    l "“蒲定说：‘老老师，我奉学校领导之命，从湖南到北京来请您题词，您不题词，我怎么回去交差？’”"
    l "“姚老笑了，认认真真写下‘书林星墨’四个字。”"
    image bg zkj = Transform("bg zkj.jpg")
    scene bg zkj with bites
    show lyy stand at speaker
    l "“第二天，蒲定又去著名诗人臧克家家，也请到了‘校园风范’的题字。”"
    l "“几位名家，有的与祁阳素不相识，可当听说是为一所县城中学的书写书名，都愿意动笔。”"
    l "“省重点只是开始。挂牌之后，学校没有歇脚。”"
    image bg kxl = Transform("bg kxl.jpg", zoom=0.48)
    scene bg kxl with bites
    show lyy stand at speaker
    l "“一九九八年，学校建了永州市第一个多媒体教室。二〇〇〇年十月，教育部授牌：‘全国现代教育技术实验学校’。”"
    l "“从‘省重点’到‘全国实验校’，前后不到十年。祁阳一中用十年时间，从全省名校走到了全国平台。”"
    l "“粉笔黑板变成了多媒体教室，油印试卷变成了校园网络。”"
    l "“那一代祁阳一中人，硬是把一所县城中学推上了全国教育的舞台。”"
    image bg black = Transform("bg black.jpg")
    scene bg black with Dissolve(0.8)
    show lyy stand at speaker
    w "“那几年……变化真大。”"
    l "“是啊。可你要记住——{color=#ff0000}飞得再高，根还在这块地上。{/color}”"
    "……"
    play sound "audio/page_flip.ogg"
    image xs 25 = Transform("xs 25.jpg", zoom=0.675)
    scene xs 25 with w9
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 26 = Transform("xs 26.jpg", zoom=0.675)
    show xs 26 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 27 = Transform("xs 27.jpg", zoom=0.675)
    show xs 27 with w12
    gm "（单击以擦除污渍）"
    $ renpy.pause(0.5, hard=True)
    image xs 28 = Transform("xs 28.jpg", zoom=0.675)
    show xs 28 with w12
    "……"
    image bg st2 = Transform("bg st2.jpg", zoom=0.649)
    scene bg st2 with bites
    show lyy stand at speaker
    l "“二〇一〇年四月，县委县政府主持召开预备会议，决定成立校友总会。”"
    l "“一个月后，祁阳一中第一届校友总会成立，审议通过了校友总会章程。校史资料收集编纂工作也同步启动。”"
    image bg xq6 = Transform("bg xq6.jpg")
    scene bg xq6 with bites
    show lyy stand at speaker
    l "“高四班校友、中国工程院院士刘大响为母校题词：”"
    l "{color=#ff0000}“‘读万卷，蹈砺文昌；明德修身，诚信做人。’”{/color}"
    image bg xq4 = Transform("bg xq4.jpg")
    scene bg xq4 with bites
    show lyy stand at speaker
    l "“此后，北京、深圳、广州、华东各地校友分会相继成立。校长和校友总会会长专程去广州、深圳走访校友，商量筹备事宜。”"
    image bg xq3 = Transform("bg xq3.jpg")
    scene bg xq3 with bites
    show lyy stand at speaker
    l "“校友们也纷纷行动，高112班校友李作友捐赠了电子白板——那是百年校庆收到的第一笔捐赠。”"
    image bg xq1 = Transform("bg xq1.jpg")
    scene bg xq1 with bites
    show lyy stand at speaker
    l "“二〇一二年十月，校庆庆典正式举行。老校友们从四面八方赶回来，有白发苍苍的八旬老人，有正值壮年的行家里手，也有刚毕业没几年的年轻人。”"
    image bg xq2 = Transform("bg xq2.jpg")
    scene bg xq2 with bites
    show lyy stand at speaker
    l "“年龄差了大半个世纪，可有一个共同的身份——祁阳一中的学生。”"
    image bg xq5 = Transform("bg xq5.jpg")
    scene bg xq5 with bites
    show lyy stand at speaker
    l "“一百年，从延寿寺那间老教室到今天的几万平米校园，从一个初中班到今天的三千多学生。{color=#ff0000}可一百年没变的，是这首歌、这个校训、这份认同。{/color}”"
    image bg das = Transform("bg das.jpg", zoom=0.675)
    scene bg das with bites
    show lyy stand at speaker
    "李爷爷合上档案，看了看我。"
    l "“今天轮到你们了。”"
    w "“我们这一章……从哪里写起？”"
    "李爷爷笑了笑。"
    l "“就从你刚才擦掉的那块污渍写起。”"
    hide lyy with Dissolve(0.8)
    image xxs 0 = Transform("xxs 0.jpg", zoom=0.7987)
    scene xxs 0 with dissolve
    gm "于是我提笔写道："
    image xxs 1 = Transform("xxs 1.jpg", zoom=0.7987)
    scene xxs 1 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}一九四四年，炮火中我们没有消失{/color}"
    image xxs 2 = Transform("xxs 2.jpg", zoom=0.7987)
    scene xxs 2 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}一九四七年，不公前我们没有沉默{/color}"
    image xxs 3 = Transform("xxs 3.jpg", zoom=0.7987)
    scene xxs 3 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}一九四九年，解放后我们亲手开创{/color}"
    image xxs 4 = Transform("xxs 4.jpg", zoom=0.7987)
    scene xxs 4 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}一九五一年，风雨中我们守住火种{/color}"
    image xxs 5 = Transform("xxs 5.jpg", zoom=0.7987)
    scene xxs 5 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}八十年代，歌声中我们找到彼此{/color}"
    image xxs 6 = Transform("xxs 6.jpg", zoom=0.7987)
    scene xxs 6 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}九十年代，新世界我们迎头赶上{/color}"
    image xxs 7 = Transform("xxs 7.jpg", zoom=0.7987)
    scene xxs 7 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}二〇一二年，百年时我们重新相聚{/color}"
    image xxs 8 = Transform("xxs 8.jpg", zoom=0.7987)
    scene xxs 8 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}二〇三二年，百廿后我们再度重逢{/color}"
    image xxs 9 = Transform("xxs 9.jpg", zoom=0.7987)
    scene xxs 9 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}这就是祁阳一中人的一百二十年：{/color}"
    image xxs 10 = Transform("xxs 10.jpg", zoom=0.7987)
    scene xxs 10 with dissolve
    play sound "audio/write.ogg"
    gm "{color=#ff0000}活下来、不服输、站起来、守得住、唱出来、飞出去、传下去。{/color}"
    gm "——2032年，百廿校庆，新版校史扉页"
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    $ quick_menu = False
    $ _game_menu_screen = None
    call screen ending_video_screen
    $ quick_menu = True
    $ _game_menu_screen = "save"
    return