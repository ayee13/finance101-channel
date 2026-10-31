VOICE = ("af_heart", 0.75)
SAY = {"$": "", "ETF": "E.T.F.", "S&P": "S and P"}

CAST = {
    "maya": {"seed": "maya", "head": ["bun"], "skinColor": ["d08b5b"], "clothingColor": ["9ddadb"]},
    "jordan": {"seed": "jordan", "head": ["short3"], "skinColor": ["edb98a"], "clothingColor": ["ffcf77"]},
    "theo": {"seed": "theo", "head": ["pomp"], "skinColor": ["f1c3a5"], "clothingColor": ["e78276"]},
    "maya_old": {"seed": "maya", "head": ["grayBun"], "skinColor": ["d08b5b"], "clothingColor": ["9ddadb"], "accessories": ["glasses"]},
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


def fv_path(m, r, years):
    """Balance at the end of each year, $m a month, monthly compounding at yearly rate r."""
    out, b = [0.0], 0.0
    for _ in range(years):
        for _ in range(12):
            b = b * (1 + r / 12) + m
        out.append(b)
    return out


R = lambda els, **k: dict(bg="room", els=els, **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="The group chat stock contest", text="Friday night. Maya's apartment. Six friends, two pizzas, one terrible idea. Theo, who has never been wrong in a group chat, proposes a contest. Everyone gets a pretend thousand dollars. Pick any investments you want. In one year, whoever has the most wins. The loser buys pizza forever.",
         scenes=[R([em("🍕", 700, 600, 220), em("🍕", 1200, 620, 180), em("🎲", 1550, 420, 140)], bgargs=dict(extra="couch", night=True)),
                 R([ch("theo", "cheeky", 560), em("🏆", 1300, 460, 240, "green", "PRETEND $1,000 EACH")], bgargs=dict(night=True))]),
    dict(text="Theo picks five companies he has a very good feeling about. Jordan spends three weeks watching videos with red arrows and dramatic music, and puts his whole thousand on one company he is sure is about to explode.",
         scenes=[R([ch("theo", "driven", 560), em("🔥", 1300, 480, 220, None, "5 HOT PICKS")]),
                 R([ch("jordan", "awe", 600, flip=True), em("🚀", 1300, 460, 240, "red", "ALL IN ON ONE")], bgargs=dict(extra="couch"))]),
    dict(text="Maya picks everything. Not one company. Not five. Basically all of them. She types it in, closes the app, and goes back to her pizza. The group chat calls it the coward pick.",
         scenes=[R([ch("maya", "eyesClosed", 600), em("🧺", 1300, 480, 240, "green", "ALL OF THEM")], bgargs=dict(extra="couch")),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("💬", 700, 450, 260), tagel("\"THE COWARD PICK\"", 1250, 450, "red", False, 70)])]),
    dict(text="Here's the twist the group chat doesn't know. The coward pick is what most professional stock pickers, people paid full time to do this, fail to beat over the long run. In the twenty years up to the end of twenty twenty-five, roughly nine out of ten big-company stock funds run by pros did worse than the plain index they were trying to beat.",
         scenes=[dict(bg="office", els=[em("👔", 600, 450, 260), em("📉", 1300, 450, 260, "red", "PROS VS THE INDEX")]),
                 dict(bg="plain", els=[big("~9 IN 10", y=380, color="red", size=200), big("TRAILED THE INDEX OVER 20 YRS", y=640, size=76)])]),
    dict(text="So how does the laziest move at the party beat the people in suits? That's this video. What an index fund actually is, why it works, and the catches nobody puts in the ad.",
         scenes=[dict(bg="plain", els=[em("🛋️", 600, 460, 280, "green"), tagel("VS", 960, 460, "ink", False, 80), em("💼", 1320, 460, 280, "red")])]),
    dict(text="Quick honesty note first. Maya, Jordan and Theo are made up. Composites. The contest is pretend money. The research numbers are real and sourced in the description, and every calculation can be checked, but examples aren't promises. Investments go up and down, sometimes a lot. This channel is education, not financial advice. We explain categories, never specific stocks or funds to buy.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 320), tagel("EXAMPLE, NOT A PROMISE", 1220, 430, "green", True)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="Seven ideas. By the end, you'll know what's inside an index fund, what it costs, why it's boring on purpose, and the one mistake that wrecks it. Let's go.",
         scenes=[dict(bg="board", bgargs=dict(text="7 IDEAS"), els=[])]),
    # ---------------- 1
    dict(chapter="1. An index is just a list", text="First, the word that scares people. An index is just a list. A list of companies, with a rule for who gets on it. That's it. Nobody's buying anything yet. It's a scoreboard for a slice of the market.",
         scenes=[dict(bg="board", bgargs=dict(text="INDEX = A LIST"), els=[num(1)]),
                 dict(bg="office", els=[num(1), em("📝", 700, 450, 280), em("🏟️", 1300, 450, 260, "green", "A SCOREBOARD")])]),
    dict(text="The famous one, the S&P 500, is a list of about five hundred of the biggest companies in the United States. A total market index is a much longer list, thousands of companies, big and small. There are indexes for other countries, for bonds, for almost anything.",
         scenes=[dict(bg="plain", els=[tagel("~500 BIG U.S. COMPANIES", 960, 330, "green", False, 68), tagel("TOTAL MARKET: THOUSANDS", 960, 560, "green", False, 68)]),
                 dict(bg="plain", els=[em("🌎", 500, 460, 220, None, "OTHER COUNTRIES"), em("📜", 1400, 460, 220, None, "BONDS")])]),
    dict(text="Think of it like a playlist. The index is the playlist. Somebody decided which songs are on it. You haven't bought anything. You're just looking at the track list.",
         scenes=[R([ch("maya", "smile", 560), em("🎧", 1300, 480, 240, None, "THE PLAYLIST")], bgargs=dict(extra="shelf"))]),
    # ---------------- 2
    dict(chapter="2. The fund buys the whole list", text="An index fund is what happens when someone actually buys the playlist. All of it. The fund pools money from lots of people, and buys every company on the list, in the same proportions as the list. Bigger companies get a bigger slice. Nobody in a meeting decides which ones look exciting.",
         scenes=[R([num(2), em("🧺", 760, 480, 260, "green", "BUY THE WHOLE LIST")]),
                 dict(bg="plain", els=[em("🥧", 600, 460, 300, "green"), tagel("BIGGER CO = BIGGER SLICE", 1300, 460, "green", False, 56)])]),
    dict(text="When you put in a hundred dollars, you don't get one share of one company. You get a tiny slice of the whole basket. A hundred dollars can make you a part-owner of hundreds or thousands of businesses at once. Very small part-owner. Your vote at the shareholder meeting is not going to swing anything.",
         scenes=[dict(bg="plain", els=[em("💵", 520, 460, 240, None, "$100"), em("➡️", 960, 460, 140), em("🏙️", 1400, 460, 260, "green", "A SLICE OF ALL")]),
                 R([ch("jordan", "cheeky", 600, flip=True), em("🗳️", 1300, 480, 220, None, "VOTE: TINY")])]),
    dict(text="You'll see two main wrappers. An index mutual fund, and an index ETF, which trades like a stock during the day. Different packaging, same idea inside. Like the same game on two consoles.",
         scenes=[dict(bg="plain", els=[em("📦", 600, 460, 240, None, "MUTUAL FUND"), em("📦", 1320, 460, 240, None, "ETF"), big("SAME IDEA INSIDE", y=860, size=90)]),
                 R([em("🎮", 700, 480, 220), em("🎮", 1220, 480, 220), tagel("SAME GAME", 960, 760, "green")])]),
    # ---------------- 3
    dict(chapter="3. Why picking winners is so hard", text="Now back to Jordan's plan. One company. To beat the market, Jordan has to pick a company that does better than average. Sounds easy. There are a lot of companies. Some of them must be good.",
         scenes=[R([num(3), ch("jordan", "driven", 600, flip=True), em("🎯", 1300, 460, 240, None, "PICK THE WINNER")])]),
    dict(text="Here's the problem. In the stock market, a small number of huge winners do most of the heavy lifting. One well known study looked at U.S. stocks from nineteen twenty-six to twenty sixteen. It found that just four percent of listed companies accounted for all of the stock market's net wealth creation over that whole stretch. The other ninety-six percent, as a group, roughly matched what you'd have earned in short-term government bills.",
         scenes=[dict(bg="plain", els=[big("4%", y=380, color="green", size=220), big("DID THE HEAVY LIFTING", y=640, size=86)]),
                 dict(bg="board", bgargs=dict(text="1926 → 2016, U.S. STOCKS"), els=[])]),
    dict(text="So picking a few stocks is like searching for a needle in a haystack, where the needles are rare and you can't tell them apart from hay until years later. An index fund doesn't search. It buys the haystack. Which means it's guaranteed to own the needles, whichever ones they turn out to be.",
         scenes=[dict(bg="outside", els=[em("🌾", 700, 600, 300), em("🪡", 1300, 460, 180, "red", "FIND THE NEEDLE?")]),
                 dict(bg="outside", els=[em("🌾", 560, 600, 240, "green"), em("🌾", 960, 600, 240, "green"), em("🌾", 1360, 600, 240, "green"), big("BUY THE HAYSTACK", y=180, color="green", size=110)])]),
    dict(text="There's also a sneaky reason. Every share Jordan buys, someone else sold. To win, he has to know something the seller doesn't. And the seller is often a professional with a research team and fast computers. Jordan has a phone at nine percent battery.",
         scenes=[dict(bg="plain", els=[ch("jordan", "suspicious", 420), em("🤝", 960, 450, 200), em("🏢", 1500, 450, 240, "red", "THE OTHER SIDE")]),
                 R([ch("jordan", "tired", 600, flip=True), em("🔋", 1300, 500, 220, "red", "9% BATTERY")], bgargs=dict(extra="couch"))]),
    # ---------------- 4
    dict(chapter="4. The scoreboard: pros vs the index", text="This isn't just a theory. There's a scorecard. A research team at S&P Dow Jones Indices publishes one twice a year, comparing professionally managed stock funds against the index they're trying to beat.",
         scenes=[dict(bg="office", els=[num(4), em("📊", 960, 460, 300, None, "THE SCORECARD")])]),
    dict(text="In twenty twenty-five alone, about seventy-nine percent of actively managed big-company U.S. stock funds trailed the S&P 500. That's one year, and one year can be noisy. So stretch it out. Over twenty years, it's about nine in ten.",
         scenes=[dict(bg="office", els=[em("📅", 600, 440, 240, "red", "2025: ~79% TRAILED")]),
                 dict(bg="plain", els=[tagel("2025: ~79% TRAILED", 960, 330, "red", False, 70), tagel("20 YEARS: ~9 IN 10", 960, 560, "red", True, 70)])]),
    dict(text="And the few who win one stretch rarely keep winning the next one. It's like a hot streak in a battle royale. It feels like skill, and sometimes it is, but you can't tell in advance which player is going to do it again.",
         scenes=[dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("🏅", 640, 460, 260, "green", "WON LAST ROUND"), em("❓", 1300, 460, 260, None, "NEXT ROUND?")])]),
    dict(text="The fair way to say it: some pros do beat the index. The hard part is finding them before they do it, not after. An index fund skips that guessing game completely. It doesn't try to beat the market. It tries to be the market. And being the market, it turns out, beats most of the people trying.",
         scenes=[dict(bg="board", bgargs=dict(text="DON'T BEAT IT. BE IT."), els=[]),
                 R([ch("maya", "smileLOL", 600), em("🧺", 1300, 480, 240, "green", "BE THE MARKET")], bgargs=dict(extra="couch"))]),
    # ---------------- 5
    dict(chapter="5. The fee is the secret weapon", text="Why do the pros lose so often? A big reason is cost. Picking stocks means paying analysts, researchers and managers. That gets charged to you every year as a fee called the expense ratio, a percentage of what you have invested.",
         scenes=[dict(bg="office", els=[num(5), em("🧑‍💼", 640, 460, 240), em("🧾", 1300, 460, 240, "red", "EXPENSE RATIO")])]),
    dict(text="In twenty twenty-five, index stock mutual funds averaged about point zero five percent a year, weighted by how much money was in them. Actively managed stock funds averaged around point six percent. Some charge one percent or more.",
         scenes=[dict(bg="plain", els=[tagel("INDEX: ~0.05% A YEAR", 960, 300, "green", True, 70), tagel("ACTIVE: ~0.6% A YEAR", 960, 520, "red", False, 70), tagel("SOME: 1%+", 960, 740, "red", False, 70)])]),
    dict(text="On ten thousand dollars, point zero five percent is five dollars a year. Point six percent is sixty dollars. One percent is a hundred. Five dollars versus a hundred doesn't sound life changing. Until you remember the last video. Fees compound too. In the wrong direction.",
         scenes=[dict(bg="plain", els=[tagel("$10,000 INVESTED", 960, 220, "ink", False, 64), em("🪙", 420, 520, 160, "green", "$5 / YR"), em("💰", 960, 520, 180, "red", "$60 / YR"), em("💸", 1500, 520, 200, "red", "$100 / YR")])]),
    dict(text="Say you invest a hundred dollars a month from eighteen to sixty-five. We'll assume the market earns seven percent a year before fees, as an example, not a prediction. With a point zero five percent fee, you end up with about four hundred and thirty-one thousand dollars. With a one percent fee, about three hundred and thirteen thousand.",
         scenes=[dict(bg="board", els=[dict(t="chart", box=(200, 110, 1780, 760), label="$100/month, 7% before fees (example)", xlabels=["18", "28", "38", "48", "58", "65"],
                                             series=[dict(name="0.05%", color="green", ys=fv_path(100, .0695, 47), dy=-25), dict(name="1%", color="red", ys=fv_path(100, .06, 47), dy=25)])])]),
    dict(text="Same money in. Fifty-six thousand, four hundred dollars of your own. Same market. The only difference is the fee, and it's worth about a hundred and eighteen thousand dollars. Even the point six percent fund leaves you around seventy-three thousand behind the cheap index fund.",
         scenes=[dict(bg="plain", els=[tagel("YOU PUT IN: $56,400", 960, 260, "ink", False, 66), tagel("1% FEE COST: ~$118K", 960, 480, "red", True, 66), tagel("0.6% FEE COST: ~$73K", 960, 700, "red", False, 66)]),
                 R([ch("maya_old", "rage", 600), em("👹", 1300, 480, 240, "red", "THE FEE GOBLIN")])]),
    dict(text="So the index fund has a head start before the race even begins. The pros have to beat the market by more than their fee, every year, just to tie. That's why cheap is not a side detail. Cheap is the strategy.",
         scenes=[dict(bg="outside", els=[em("🐢", 600, 620, 220, "green", "CHEAP + AVERAGE"), em("🐇", 1320, 620, 220, "red", "FAST + EXPENSIVE")]),
                 dict(bg="board", bgargs=dict(text="CHEAP IS THE STRATEGY"), els=[])]),
    # ---------------- 6
    dict(chapter="6. Boring protects you", text="Back to the contest. Six months in, Jordan's one company has a bad quarter. The stock drops sixty percent. His pretend thousand dollars is now four hundred. The group chat goes quiet in a very loud way.",
         scenes=[R([num(6), ch("jordan", "fear", 600, flip=True), em("📉", 1300, 460, 240, "red", "-60%")], bgargs=dict(extra="couch")),
                 R([ch("jordan", "concernedFear", 600, flip=True), tagel("$1,000 → $400", 1300, 400, "red", True, 72)], bgargs=dict(extra="couch"))]),
    dict(text="Now imagine that same company is one of hundreds in an index fund, and it makes up a tenth of a percent of the fund. A sixty percent drop in that company moves the whole fund by about six hundredths of a percent. Maya's fund barely blinks. She didn't even open the app.",
         scenes=[dict(bg="plain", els=[tagel("ONE CO = 0.1% OF FUND", 960, 300, "ink", False, 66), tagel("IT DROPS 60%", 960, 500, "red", False, 66), tagel("FUND MOVES ~0.06%", 960, 700, "green", True, 66)]),
                 R([ch("maya", "calm", 600), em("📱", 1300, 500, 200, "green", "APP: NOT OPENED")], bgargs=dict(extra="couch"))]),
    dict(text="That's diversification. Not putting all your eggs in one basket, except the basket has thousands of eggs and some of them are secretly golden. One company can go to zero. Companies do fail. For a total market fund to go to zero, basically every public company in the country would have to fail at once. At that point, your portfolio is not your biggest problem.",
         scenes=[dict(bg="plain", els=[em("🥚", 600, 460, 200, "red", "ONE EGG"), em("🧺", 1320, 460, 260, "green", "THOUSANDS")]),
                 dict(bg="outside", els=[em("🧟", 960, 520, 300), big("BIGGER PROBLEMS", y=180, size=110)])]),
    # ---------------- 7
    dict(chapter="7. How people actually use them", text="So how do people actually use index funds? Not with a hot tip. With a short checklist. We're talking categories here, not specific funds to buy.",
         scenes=[R([num(7), ch("maya", "explaining", 560), em("📋", 1300, 480, 240, "green", "THE CHECKLIST")], bgargs=dict(extra="shelf"))]),
    dict(text="One. Broad beats narrow. A fund that follows a wide index, like a total market or a large company index, spreads your money out. A fund that follows one trendy industry is still a bet, just in a trench coat.",
         scenes=[dict(bg="plain", els=[em("🌐", 600, 460, 240, "green", "BROAD INDEX"), em("🧥", 1320, 460, 240, "red", "A BET IN A COAT")])]),
    dict(text="Two. Check the expense ratio. It's printed on every fund's page. For a broad index fund, you're looking for a small number. If it has a one in front of the decimal, ask why.",
         scenes=[dict(bg="office", els=[ch("maya", "suspicious", 560), em("🔍", 1300, 460, 240, None, "FIND THE FEE")])]),
    dict(text="Three. Put it in the right account. A retirement plan at work, an individual retirement account, or a regular brokerage account can all hold index funds. Which one comes first is a whole topic, and we'll get there in a future video.",
         scenes=[dict(bg="plain", els=[em("🏢", 420, 460, 200, None, "WORK PLAN"), em("🏦", 960, 460, 200, None, "IRA"), em("📂", 1500, 460, 200, None, "BROKERAGE")])]),
    dict(text="Four. Automate it and leave it alone. Same amount, every month, on autopilot. The less you check it, the less tempted you are to do something dramatic. Your index fund is not a Tamagotchi. It does not need feeding every hour.",
         scenes=[R([ch("maya", "eyesClosed", 560), em("📲", 1300, 480, 240, "green", "AUTO: EVERY MONTH")], bgargs=dict(extra="couch")),
                 dict(bg="plain", els=[em("🥚", 700, 450, 260), tagel("NOT A PET", 1300, 450, "green", False, 72)])]),
    # ---------------- honesty check
    dict(chapter="Honesty check: the catches", text="Time for the honesty check, because index funds have catches too, and the ads don't lead with them.",
         scenes=[dict(bg="board", bgargs=dict(text="THE CATCHES"), els=[])]),
    dict(text="Catch one. An index fund will never beat the market. That's the deal. You get the market's return, minus a small fee. Every year, somebody in the group chat will beat you, and they will tell you about it.",
         scenes=[R([ch("theo", "smileBig", 560), em("💬", 1300, 460, 220, "red", "\"I BEAT YOU\"")])]),
    dict(text="Catch two. When the market falls, you fall with it. All of it. In the two thousand eight financial crisis, the S&P 500 lost more than half its value from peak to bottom. In early twenty twenty, it fell about a third in roughly a month. An index fund doesn't dodge those. It rides them all the way down.",
         scenes=[dict(bg="board", els=[dict(t="chart", box=(240, 110, 1680, 760), label="Illustration: a big drop and recovery", fmt="", xlabels=["", "", "", "", ""],
                                             series=[dict(name="", color="red", ys=[100, 110, 70, 48, 60, 85, 105])])]),
                 R([ch("maya", "concerned", 600), tagel("-50% HAPPENS", 1300, 400, "red", True, 72)])]),
    dict(text="Catch three. Not every index fund is cheap. Some charge a lot for something simple. The word index on the label doesn't do the checking for you.",
         scenes=[dict(bg="office", els=[em("🏷️", 960, 460, 280, "red", "CHECK THE FEE ANYWAY")])]),
    dict(text="Catch four. Our seven percent is an assumption. Over some stretches, the market has done much worse, for a decade or more. Over others, much better. Nobody knows the next forty years. The case for index funds isn't that they're guaranteed to do well. It's that they give you the market's result cheaply, and most alternatives give you less.",
         scenes=[dict(bg="plain", els=[tagel("7% = ASSUMPTION", 960, 330, "amber", True, 76), tagel("NOT A PREDICTION", 960, 560, "amber", False, 76)])]),
    # ---------------- common mistake
    dict(chapter="The mistake that wrecks it", text="And here's the mistake that turns a good tool into a bad result. Panic selling. The market drops, it feels like the end, and people sell to make the pain stop.",
         scenes=[R([ch("jordan", "fear", 600, flip=True), em("🔴", 1300, 480, 220, "red", "SELL EVERYTHING?")], bgargs=dict(night=True))]),
    dict(text="The math is brutal. Say you have ten thousand dollars and the market drops fifty percent. Now you have five. To get back to ten, you don't need fifty percent. You need a hundred percent gain. If you sell at the bottom, you lock in the loss and you're out for the recovery, which historically has been where a lot of the gains happened.",
         scenes=[dict(bg="plain", els=[tagel("$10,000", 420, 400, "green", False, 70), em("➡️", 720, 400, 120), tagel("-50% = $5,000", 1150, 400, "red", True, 70)]),
                 dict(bg="plain", els=[tagel("BACK TO $10,000", 960, 330, "green", False, 70), tagel("NEEDS +100%", 960, 560, "red", True, 70)])]),
    dict(text="So the real skill with index funds isn't picking. There's nothing to pick. It's sitting still when everything in your feed says to move. That's why people keep a separate emergency fund, so a bad month in the market never forces them to sell.",
         scenes=[R([ch("maya", "calm", 600), em("🧘", 1300, 480, 240, "green", "SIT STILL")], bgargs=dict(extra="couch")),
                 R([em("🧯", 960, 480, 260, "green", "EMERGENCY FUND")], bgargs=dict(extra="shelf"))]),
    # ---------------- close
    dict(chapter="Back to the contest", text="One year later. Pizza night. Final scores. Theo's five picks are down. Jordan's one company bounced back and then some, and he finished first. He has not stopped talking about it. Maya finished in the middle. Boring. Right around the market.",
         scenes=[R([ch("theo", "tired", 330, h=500), ch("jordan", "smileLOL", 960, h=500, flip=True, glow="green"), ch("maya", "calm", 1590, h=500)], bgargs=dict(extra="couch", night=True)),
                 R([ch("jordan", "lovingGrin1", 600, flip=True), em("🏆", 1300, 460, 240, "green", "1ST PLACE. THIS YEAR.")], bgargs=dict(night=True))]),
    dict(text="And honestly? That's the point. Jordan might win next year too. Or he might be the one buying pizza forever. Maya doesn't have to know which. In one year, the stock picker can win. Over twenty, the scorecard says most don't.",
         scenes=[dict(bg="plain", els=[tagel("1 YEAR: ANYONE CAN WIN", 960, 330, "amber", False, 66), tagel("20 YEARS: MOST DON'T", 960, 560, "green", True, 66)])]),
    dict(text="So here's the one line to keep. You don't have to find the needle. You can just buy the haystack, keep the fee small, and leave it alone.",
         scenes=[dict(bg="outside", els=[em("🌾", 960, 520, 300, "green"), big("BUY THE HAYSTACK", y=180, color="green", size=120)])]),
    dict(text="Next video, we're opening your first paycheck and finding out why it's smaller than you expected, and where the missing money actually went. If this one made index funds less mysterious, subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("maya", "smileBig", 330), ch("jordan", "smile", 930, flip=True), em("📺", 1480, 400, 260, "green", "NEXT: YOUR PAYCHECK")], bgargs=dict(extra="couch", win=False))]),
]
