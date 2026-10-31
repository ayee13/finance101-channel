VOICE = ("af_heart", 0.75)
SAY = {"$": "", "Pokemon": "Pokémon"}

CAST = {
    "maya": {"seed": "maya", "head": ["bun"], "skinColor": ["d08b5b"], "clothingColor": ["9ddadb"]},
    "jordan": {"seed": "jordan", "head": ["short3"], "skinColor": ["edb98a"], "clothingColor": ["ffcf77"]},
    "maya_old": {"seed": "maya", "head": ["grayBun"], "skinColor": ["d08b5b"], "clothingColor": ["9ddadb"], "accessories": ["glasses"]},
    "jordan_old": {"seed": "jordan", "head": ["grayShort"], "skinColor": ["edb98a"], "clothingColor": ["ffcf77"], "accessories": ["glasses2"]},
    "boss": {"seed": "boss", "head": ["noHair2"], "skinColor": ["ae5d29"], "clothingColor": ["8fa7df"], "facialHair": ["full"]},
}


def ch(who, face, x, **k):
    return dict(t="char", who=who, face=face, x=x, **k)


def em(e, x, y, size=200, glow=None, label=None):
    return dict(t="emoji", e=e, x=x, y=y, size=size, glow=glow, label=label)


def num(n):
    return dict(t="num", n=n)


def tagel(text, x, y, color="ink", glow=False, size=56):
    return dict(t="tag", text=text, x=x, y=y, color=color, glow=glow, size=size)


def big(text, x=960, y=300, color="ink", size=120):
    return dict(t="bigtext", text=text, x=x, y=y, color=color, size=size)


R = lambda els, **k: dict(bg="room", els=els, **k)
J_FLIP = dict(flip=True)

BEATS = [
    # ---------------- cold open
    dict(chapter="Two apartments, same hallway", text="Two apartments, same hallway, outside Columbus. Door one: Maya. Eighteen. Works the morning shift at a coffee shop. Her phone has a cracked screen she's decided is \"character.\"",
         scenes=[dict(bg="hallway", els=[em("🍕", 1000, 740, 140)]),
                 dict(bg="cafe", els=[ch("maya", "smile", 620), em("📱", 1250, 640, 180, "green", "CRACKED. STILL WORKS.")])]),
    dict(text="Door two: Jordan. Also eighteen. Works at the same coffee shop, the afternoon shift. His phone is brand new. He's still paying for it. He will be paying for it for twenty-two more months.",
         scenes=[dict(bg="room", bgargs=dict(extra="couch"), els=[ch("jordan", "smileBig", 620, flip=True), em("🎮", 1500, 420, 160)]),
                 dict(bg="room", bgargs=dict(extra="couch"), els=[ch("jordan", "cheeky", 620, flip=True), em("📱", 1300, 520, 200, "red", "22 PAYMENTS LEFT")])]),
    dict(text="Same job. Same pay. Same hallway. Both will set aside the same hundred dollars a month. And forty-seven years from now, one of them will have more money than the other, after putting in less than a third as much.",
         scenes=[dict(bg="hallway", els=[ch("maya", "calm", 480), ch("jordan", "calm", 1440, flip=True)]),
                 dict(bg="outside", els=[ch("maya_old", "smileBig", 520, glow="green"), ch("jordan_old", "concerned", 1480, flip=True), big("47 YEARS LATER", y=150, size=110)])]),
    dict(text="Less than a third. And still ahead. This isn't a video about getting rich. It's about the one thing you have at eighteen that nobody older can buy back, and why almost nobody tells you what it's worth.",
         scenes=[dict(bg="plain", els=[em("⏳", 960, 470, 380, "green"), big("THE ONE THING YOU CAN'T BUY BACK", y=880, size=84)])]),
    dict(text="Quick honesty note. Maya and Jordan are made up. Composites. The math around them is real, and you can check every number, but it's an example, not a promise. Real investments go up and down, sometimes a lot. And this channel is education, not financial advice. It's arithmetic, not a plan for your specific life.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 320), tagel("EXAMPLE, NOT A PROMISE", 560, 700, "green", True)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="Okay. Here's the thing nobody says out loud. When people tell you to \"start investing early,\" it sounds like a vitamin. Good for you, vaguely, someday. Nobody shows you the bill for waiting. So that's what we're doing. Seven moves. Every one of them is cheap, boring, and unfair in your favor. The first one is happening in Maya's hallway right now.",
         scenes=[dict(bg="room", els=[em("💊", 700, 420, 260), tagel("\"START EARLY\"", 700, 700)]),
                 dict(bg="room", els=[em("🧾", 1000, 430, 300, "red", "THE BILL FOR WAITING")]),
                 dict(bg="board", bgargs=dict(text="7 MOVES"), els=[])]),
    # ---------------- move 1
    dict(chapter="1. Start the clock", text="Maya opens an investing account the month she turns eighteen. Not because she understands the stock market. She doesn't. She watched one video, got mildly annoyed, and set up a hundred dollars a month to move automatically. That's about three dollars and thirty cents a day. Roughly one fancy coffee, which she can't afford anyway, because she makes them.",
         scenes=[R([num(1), ch("maya", "driven", 560), em("💻", 1300, 600, 240), em("🫙", 1650, 600, 180, "green", "$100 / MONTH")], bgargs=dict(extra="shelf")),
                 dict(bg="cafe", els=[ch("maya", "smileLOL", 560), em("☕", 1300, 560, 240, "green", "$3.30 A DAY")])]),
    dict(text="Jordan has a plan too. The plan is \"later.\" He'll start when he's making real money. He has decided that real money begins at twenty-eight, which is the age everyone at eighteen believes is basically rich.",
         scenes=[R([ch("jordan", "cheeky", 600, flip=True), em("🥡", 1300, 580, 220, "red", "THE PLAN: LATER")], bgargs=dict(extra="couch")),
                 R([ch("jordan", "lovingGrin1", 600, flip=True), em("🎂", 1350, 520, 260, None, "28 = RICH (?)")])]),
    dict(text="So here's the setup. Maya invests a hundred a month from eighteen to twenty-eight. Then life happens, and she stops. Completely. Never adds another dollar. Jordan starts at twenty-eight and does everything right after that. A hundred a month, every month, for thirty-seven years, all the way to sixty-five.",
         scenes=[dict(bg="board", els=[ch("maya", "calm", 380), tagel("MAYA: 18 → 28, THEN STOPS", 1060, 330, "green")]),
                 dict(bg="board", els=[ch("jordan", "serious", 1560, flip=True), tagel("JORDAN: 28 → 65", 860, 330, "amber")])]),
    dict(text="Count what they put in. Maya: twelve thousand dollars. Jordan: forty-four thousand, four hundred. Jordan puts in almost four times as much. In a normal world, Jordan wins this in a landslide.",
         scenes=[dict(bg="plain", els=[ch("maya", "smile", 420), ch("jordan", "smileBig", 1500, flip=True), em("🐷", 760, 380, 200, "green", "$12,000"), em("🐷", 1140, 380, 300, "amber"), tagel("$44,400", 1140, 620, "amber")])]),
    dict(text="Let's assume a seven percent average yearly return, the number we'll use all video. At twenty-eight, Maya has about seventeen thousand, three hundred. Jordan has zero, and a really nice phone.",
         scenes=[dict(bg="board", els=[dict(t="lines", age=28, ymax=250000, label="7% a year (example)", series=[dict(kind="maya_stop", color="green", name="Maya"), dict(kind="jordan", color="amber", name="Jordan", dy=30)], box=(300, 110, 1640, 740))])]),
    dict(text="At thirty-eight, Jordan has saved his way up to about seventeen thousand. Exactly where Maya was ten years earlier. Meanwhile, Maya, who hasn't added a dollar in ten years, has doubled to about thirty-four thousand, eight hundred.",
         scenes=[dict(bg="board", els=[dict(t="lines", age=38, ymax=250000, label="Age 38", series=[dict(kind="maya_stop", color="green", name="Maya", dy=-25), dict(kind="jordan", color="amber", name="Jordan", dy=25)], box=(300, 110, 1640, 740))]),
                 R([ch("maya", "eyesClosed", 600), em("📈", 1350, 380, 240, "green", "$34,800")], bgargs=dict(extra="couch"))]),
    dict(text="At forty-eight, Maya's around seventy thousand. Jordan, fifty-two. At fifty-eight, Maya one forty. Jordan, one twenty-two. And at sixty-five, Maya has about two hundred and twenty-nine thousand. Jordan has about two hundred and ten.",
         scenes=[dict(bg="board", els=[dict(t="lines", age=58, ymax=250000, label="Age 58", series=[dict(kind="maya_stop", color="green", name="Maya", dy=-25), dict(kind="jordan", color="amber", name="Jordan", dy=25)], box=(300, 110, 1640, 740))]),
                 dict(bg="board", els=[dict(t="lines", age=65, ymax=250000, label="Age 65", series=[dict(kind="maya_stop", color="green", name="Maya", dy=-25), dict(kind="jordan", color="amber", name="Jordan", dy=25)], box=(300, 110, 1640, 740))])]),
    dict(text="Four times the money in, and he still loses. Not because Maya picked better stocks. In our example they got the exact same return. Maya had one thing Jordan couldn't buy at any price: ten extra years for the money to sit there and multiply. That's compound interest. Your money earns money, and then that money earns money. It's basically your savings having kids, and then grandkids, and the grandkids also have jobs.",
         scenes=[R([ch("jordan_old", "awe", 620, flip=True), em("🧾", 1300, 520, 240, "red", "4X THE MONEY. STILL LOST.")]),
                 dict(bg="plain", els=[em("⏳", 700, 460, 300, "green"), tagel("+10 YEARS", 700, 760, "green"), em("🪙", 1250, 380, 160, "green"), em("🪙", 1450, 520, 120, "green"), em("🪙", 1150, 600, 100, "green"), em("🪙", 1600, 330, 90, "green"), em("🪙", 1500, 700, 80, "green")])]),
    dict(text="And to be clear, the lesson is not \"invest for ten years and quit.\" We'll come back to that, because the real version is even more lopsided.",
         scenes=[R([ch("maya", "suspicious", 700), tagel("NOT THE LESSON: QUIT AT 28", 1300, 400, "red")])]),
    # ---------------- move 2
    dict(chapter="2. Count the doublings", text="Here's the shortcut people learn way too late. It's called the rule of seventy-two. Divide seventy-two by your yearly return, and that's roughly how many years it takes your money to double. At seven percent, seventy-two divided by seven is about ten. So your money roughly doubles every decade.",
         scenes=[dict(bg="board", bgargs=dict(text="72 ÷ 7 ≈ 10"), els=[num(2)]),
                 dict(bg="board", bgargs=dict(text="DOUBLES EVERY ~10 YRS"), els=[num(2)])]),
    dict(text="Start at eighteen, and you get four or five doublings before sixty-five. Start at forty, you get about two. And the doublings you lose are never the small early ones. You lose the last ones. The biggest ones. It's like quitting a Minecraft world right before you find the diamonds.",
         scenes=[dict(bg="plain", els=[tagel("START AT 18", 420, 300, "green"), *[em("🟩", 760 + i * 210, 300, 150, "green") for i in range(5)], tagel("START AT 40", 420, 620, "red"), *[em("🟥", 760 + i * 210, 620, 150) for i in range(2)]]),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("💎", 960, 420, 340, "green"), big("DON'T QUIT BEFORE THE DIAMONDS", y=860, color="green", size=80)])]),
    dict(text="Put a price on it. A hundred a month from eighteen to sixty-five, at seven percent, comes to about four hundred and thirty-nine thousand. Start at nineteen instead, about four hundred and eight thousand. Waiting one single year, from eighteen to nineteen, costs about thirty-one thousand dollars by sixty-five. Start at twenty-five, about two hundred and sixty-two thousand. At twenty-eight, about two hundred and ten.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(200, 120, 1720, 760), items=[("Start 18", 438643, "green"), ("19", 407915, "green"), ("20", 379259, "amber"), ("22", 327613, "amber"), ("25", 262481, "red"), ("28", 209654, "red")])]),
                 dict(bg="room", els=[em("🎂", 960, 400, 320, "red", "1 YEAR LATER = -$31,000")])]),
    dict(text="Flip it around. If Jordan starts at twenty-eight and wants to end up where never-stopping Maya does, about four hundred and thirty-nine thousand, he can't just match her hundred a month. He'd need about two hundred and nine dollars a month. More than double. Every month. For thirty-seven years. That's the price of ten years of \"later.\" Not a fine anyone sends you in the mail. Just a quiet surcharge on every month for the rest of your working life.",
         scenes=[R([ch("jordan", "concerned", 600, flip=True), em("🧾", 1300, 460, 240, "red", "$209 / MONTH TO CATCH UP")]),
                 dict(bg="plain", els=[tagel("THE \"LATER\" SURCHARGE", 960, 300, "red", True, 76), tagel("$100 → $209 A MONTH", 960, 560, "red", False, 76)])]),
    dict(text="Your birthday is, financially speaking, a little bit expensive.",
         scenes=[R([ch("jordan", "concernedFear", 700, flip=True), em("🎉", 1350, 420, 220, "red")])]),
    # ---------------- move 3
    dict(chapter="3. Small and early beats big and late", text="Maybe a hundred a month isn't realistic right now. Rent, school, a car that makes a new noise every week. Fine. Let's shrink it.",
         scenes=[dict(bg="outside", els=[num(3), ch("maya", "concerned", 560), em("🚗", 1250, 680, 260, "red", "NEW NOISE")])]),
    dict(text="Twenty-five dollars a month, from eighteen to sixty-five, at seven percent. Less than a dollar a day. That grows to about a hundred and ten thousand dollars. Fifty a month, about two hundred and nineteen thousand.",
         scenes=[R([em("🫙", 400, 440, 170, "green"), tagel("$25 / MONTH", 400, 670, "green", False, 54), tagel("→ $110K", 400, 790, "green", False, 54),
                    em("🫙", 960, 430, 200, "green"), tagel("$50 / MONTH", 960, 670, "green", False, 54), tagel("→ $219K", 960, 790, "green", False, 54),
                    em("🫙", 1520, 420, 230, "green"), tagel("$100 / MONTH", 1520, 670, "green", False, 54), tagel("→ $439K", 1520, 790, "green", False, 54)], bgargs=dict(extra="shelf"))]),
    dict(text="For comparison, Jordan's hundred a month starting at twenty-eight got him about two hundred and ten. So twenty-five bucks started at eighteen gets you to roughly half of what four times the money gets you ten years later. The amount matters. But at your age, the start matters more. You can always make the snowball bigger later. You can't make the hill longer.",
         scenes=[dict(bg="plain", els=[ch("maya", "smile", 460), ch("jordan", "calm", 1460, flip=True), tagel("$25 AT 18 → $110K", 460, 260, "green"), tagel("$100 AT 28 → $210K", 1460, 260, "amber")]),
                 dict(bg="outside", els=[em("⛄", 960, 560, 300, "green"), big("YOU CAN'T MAKE THE HILL LONGER", y=180, size=86)])]),
    # ---------------- move 4
    dict(chapter="4. Ask what it costs every year", text="Now, a quick detour, because Wall Street has its own version of a phone payment. Fees. A lot of investments charge a yearly fee, shown as a small percentage. One percent sounds like nothing. It sounds like the battery icon you ignore.",
         scenes=[dict(bg="office", els=[num(4), em("🏦", 560, 460, 280), em("🔋", 1250, 520, 220, "red", "1% A YEAR")])]),
    dict(text="Take the version of Maya who never stops: a hundred a month from eighteen to sixty-five. At seven percent, about four hundred and thirty-nine thousand. Now take one percent off for fees, so she earns six. She ends up with about three hundred and thirteen thousand. That one percent quietly cost her about a hundred and twenty-six thousand dollars. More than ten times everything Maya put in during her first decade.",
         scenes=[dict(bg="board", els=[dict(t="lines", age=65, ymax=480000, label="$100/month, 18 to 65", series=[dict(kind="maya_all", color="green", name="7%", dy=-20), dict(kind="fee", color="red", name="6% after fee", dy=25)], box=(300, 110, 1640, 740))]),
                 R([ch("maya_old", "rage", 600), em("👹", 1300, 480, 240, "red", "THE 1% TOOK $126K")])]),
    dict(text="So before you put money anywhere, ask one boring question: what does this cost me every year? Lower is better. Boring is the point.",
         scenes=[dict(bg="office", els=[ch("maya", "serious", 600), tagel("WHAT DOES THIS COST ME EVERY YEAR?", 1220, 330, "green", True, 48)])]),
    # ---------------- move 5
    dict(chapter="5. Debt runs the same trick", text="Compound interest is a superpower, and like every superpower in every Marvel movie, it has a villain version. When you invest, compounding works for you. When you owe money, it works for someone else.",
         scenes=[dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[num(5), em("🦸", 640, 480, 300, "green", "INVESTING"), em("🦹", 1280, 480, 300, "red", "DEBT")])]),
    dict(text="The average interest rate on credit cards that charge interest was about twenty-two percent in the Federal Reserve's latest data. Say Jordan puts a thousand dollars on a card at twenty-two percent and doesn't pay it down for a year. That thousand becomes about one thousand, two hundred and forty-four. Same snowball, rolling straight at him.",
         scenes=[R([ch("jordan", "fear", 600, flip=True), em("💳", 1300, 460, 260, "red", "22% A YEAR")]),
                 R([ch("jordan", "concernedFear", 600, flip=True), tagel("$1,000 → $1,244", 1300, 330, "red", True, 72), em("☃️", 1300, 600, 180, "red")])]),
    dict(text="So here's an unpopular but true one. If you're carrying a balance like that, paying it off is one of the best guaranteed returns you'll ever get. Deal with that first. Invest after.",
         scenes=[dict(bg="board", bgargs=dict(text="1. KILL THE 22%   2. THEN INVEST"), els=[])]),
    # ---------------- move 6
    dict(chapter="6. Never interrupt it", text="At twenty-five, Maya's car needs a five-thousand-dollar repair. She could pull it from her investments. It's right there. One tap.",
         scenes=[dict(bg="outside", els=[num(6), ch("maya", "tired", 520), em("🚗", 1200, 680, 260), em("🔧", 1500, 470, 180, "red", "$5,000")])]),
    dict(text="Here's what that tap really costs. Five thousand dollars left alone at seven percent from twenty-five to sixty-five grows to about eighty-one thousand. So the repair isn't five grand. It's eighty-one grand, paid in installments by future Maya, who did nothing wrong.",
         scenes=[dict(bg="plain", els=[tagel("$5,000 TODAY", 560, 420, "red", True, 72), em("➡️", 960, 420, 160), tagel("$81,000 AT 65", 1360, 420, "red", True, 72)]),
                 R([ch("maya_old", "concerned", 600), em("🧾", 1300, 480, 240, "red", "BILL FROM AGE 25")])]),
    dict(text="This is why people keep a separate emergency fund, in a plain savings account, for exactly this. It's not exciting. It's a fire extinguisher. The whole job of an emergency fund is to make sure the investing money never has to get interrupted.",
         scenes=[R([ch("maya", "calm", 560), em("🧯", 1250, 520, 260, "green", "EMERGENCY FUND")], bgargs=dict(extra="shelf"))]),
    # ---------------- move 7
    dict(chapter="7. Make it automatic", text="Maya's real secret isn't discipline. She set up an automatic transfer once and then forgot about it, which is the most underrated financial strategy on Earth. Money she never sees is money she never spends.",
         scenes=[R([num(7), ch("maya", "eyesClosed", 560), em("📲", 1300, 480, 240, "green", "AUTO-TRANSFER: ON")], bgargs=dict(extra="couch"))]),
    dict(text="Think of it like a Netflix subscription, except instead of charging you for a show you forgot you were watching, it's paying future you. The best money systems are the ones that still work on the days you don't. And at eighteen, most of your days are going to be busy.",
         scenes=[R([ch("maya", "smileBig", 560), em("📺", 1300, 460, 240, "green", "SUBSCRIBED TO FUTURE YOU")], bgargs=dict(extra="couch"))]),
    dict(text="And if a job ever offers a retirement plan with a match, pay attention. A match means if you put money in, your employer adds some too. Say Maya's hundred a month gets a fifty percent match. Now a hundred and fifty goes in every month. From eighteen to sixty-five at seven percent, that's about six hundred and fifty-eight thousand. For the same hundred dollars out of her paycheck. Every plan has its own rules, so read yours, but free money is free money.",
         scenes=[dict(bg="office", els=[ch("maya", "smileBig", 520), ch("boss", "smile", 1400, flip=True), em("✉️", 960, 400, 200, "green", "MATCH")]),
                 dict(bg="plain", els=[tagel("$100 + $50 MATCH", 960, 330, "green", True, 76), tagel("≈ $658,000 AT 65", 960, 560, "green", False, 76)])]),
    # ---------------- honesty check
    dict(chapter="Honesty check: lower returns", text="Now, we've used seven percent all video, and that matters, so let's stress-test it. Same story, but five percent a year.",
         scenes=[dict(bg="board", bgargs=dict(text="7% → 5% ?"), els=[])]),
    dict(text="At five percent, the plot twist flips. Maya, who quit at twenty-eight, ends up with about ninety-eight thousand. Jordan, with his thirty-seven years of saving, ends up with about one hundred and twenty-eight. Jordan wins that round.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(560, 120, 1760, 760), items=[("Maya stopped", 98378, "green"), ("Jordan", 128050, "amber")]), ch("jordan", "smileBig", 300, h=560)])]),
    dict(text="But look at the third bar. The version of Maya who starts at eighteen and never stops ends up with about two hundred and twenty-six thousand at five percent, and about four hundred and thirty-nine at seven. Ahead of Jordan both times. By a lot.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(560, 120, 1760, 760), items=[("Maya stopped", 98378, "green"), ("Jordan", 128050, "amber"), ("Maya, never stopped", 226428, "violet")]), ch("maya", "smileLOL", 300, h=560)])]),
    dict(text="So the lesson that survives any rate you plug in isn't \"stop early.\" It's \"start early, and don't stop.\" Change the rate and the details change. The direction doesn't. That's also exactly why every number here is an example, not a promise.",
         scenes=[dict(bg="board", bgargs=dict(text="START EARLY. DON'T STOP."), els=[])]),
    dict(chapter="Honesty check: inflation", text="One more honesty check, because nobody likes this one. Inflation. Prices tend to creep up over time. Say they rise three percent a year, as an example. Run the rule of seventy-two again: seventy-two divided by three is twenty-four. So prices roughly double every twenty-four years. A hundred-dollar bill in a drawer would buy about half as much in twenty-four years.",
         scenes=[dict(bg="board", bgargs=dict(text="72 ÷ 3 = 24 YEARS"), els=[]),
                 R([em("💵", 420, 460, 260, "red", "$100 IN A DRAWER"), em("➡️", 960, 460, 140), em("🛒", 1500, 460, 260, "red", "BUYS ~$49 OF STUFF")])]),
    dict(text="That also means the big numbers in this video are in future dollars. Maya's two hundred and twenty-nine thousand at sixty-five, at three percent inflation, would buy roughly what fifty-seven thousand buys today. The version of Maya who never stops, about one hundred and nine thousand in today's money. Still real money. Still way more than the drawer. But it's the honest version, and you deserve the honest version.",
         scenes=[dict(bg="plain", els=[tagel("$229K IN 2073", 560, 360, "amber", False, 72), em("➡️", 960, 360, 140), tagel("≈ $57K TODAY", 1360, 360, "amber", True, 72)]),
                 R([ch("maya", "serious", 600), tagel("THE HONEST VERSION", 1300, 380, "green", True, 64)])]),
    dict(text="And here's the part that actually matters. Inflation is exactly why money sitting still loses ground, and money that compounds has a shot at staying ahead. The drawer doesn't compound. Time in the market at least gives your money a chance to outrun rising prices. Not a guarantee. A chance. At eighteen, a chance with forty-seven years attached is a pretty good deal.",
         scenes=[dict(bg="outside", els=[em("🐢", 450, 620, 220, "red", "CASH IN A DRAWER"), em("🐇", 1360, 620, 220, "green", "MONEY THAT COMPOUNDS")])]),
    # ---------------- close
    dict(chapter="Back to the hallway", text="So, back to the hallway. Same job, same pay, same hundred dollars a month. The difference between them is not intelligence, or luck, or some secret stock. It's a ten-year head start that cost Maya three dollars and thirty cents a day and an afternoon of mild annoyance.",
         scenes=[dict(bg="hallway", els=[ch("maya", "smile", 480), ch("jordan", "calm", 1440, flip=True), em("☕", 760, 640, 120), em("☕", 1160, 640, 120)])]),
    dict(text="And here's the good news for the Jordans watching. You're not twenty-eight yet. Nobody gave you a deadline. The clock just started, and it's still on your side.",
         scenes=[dict(bg="hallway", els=[ch("jordan", "driven", 960, flip=True, glow="green"), em("📱", 1400, 520, 180, "green")])]),
    dict(text="One small step this week: find out where your money could start compounding. Ask your job if there's a retirement plan and a match. Or open a savings or investing account and set up an automatic transfer. Ten dollars a week counts. The amount doesn't have to be big. It just has to start.",
         scenes=[R([em("✅", 560, 300, 130, "green"), tagel("FIND WHERE IT CAN COMPOUND", 1100, 300, "green", False, 48), em("✅", 560, 480, 130, "green"), tagel("AUTOMATE ANY AMOUNT", 1100, 480, "green", False, 48), em("✅", 560, 660, 130, "green"), tagel("ASK ABOUT FEES + MATCH", 1100, 660, "green", False, 48)], bgargs=dict(win=False))]),
    dict(text="Next video, we're breaking down what an index fund actually is, and why so many people who know a lot about money end up owning boring ones. If this one changed how you think about your eighteenth birthday, subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("maya", "smileBig", 330), ch("jordan", "smile", 930, flip=True), em("📺", 1580, 420, 280, "green", "NEXT: INDEX FUNDS")], bgargs=dict(extra="couch", win=False))]),
]
