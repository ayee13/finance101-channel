VOICE = ("af_heart", 0.75)
SAY = {"$": "", "APY": "A.P.Y.", "FDIC": "F.D.I.C.", "NCUA": "N.C.U.A."}

CAST = {
    "maya": {"seed": "maya", "head": ["bun"], "skinColor": ["d08b5b"], "clothingColor": ["9ddadb"]},
    "jordan": {"seed": "jordan", "head": ["short3"], "skinColor": ["edb98a"], "clothingColor": ["ffcf77"]},
    "tech": {"seed": "tech", "head": ["noHair2"], "skinColor": ["ae5d29"], "clothingColor": ["8fa7df"]},
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


# ---- the examples, all numbers computed here (made-up amounts, real rates)
CARD_APR = 0.2236            # Fed G.19, Aug 2026, accounts assessed interest (released Oct 7, 2026)


def payoff(bal, pay, apr=CARD_APR):
    m = interest = 0
    while bal > 0.005:
        i = round(bal * apr / 12, 2); interest += i; bal += i
        bal -= min(pay, bal); m += 1
    return m, round(interest, 2)


REPAIR = 700
M25, I25 = payoff(REPAIR, 25)        # 40 months, $298.80 -> total $998.80 (~$999)
M50, I50 = payoff(REPAIR, 50)        # 17 months, $118.73
ESSENTIALS = dict(rent=750, groceries=300, transport=180, utilities=75, phone=45)   # made-up, sums to 1,350
MONTH = sum(ESSENTIALS.values())     # 1,350
THREE, SIX = 3 * MONTH, 6 * MONTH    # 4,050 / 8,100
NAT, HY = 0.0037, 0.04               # FDIC national savings avg (Sep/Oct 2026) vs ~4% online HYSA, early Nov 2026
# $1,000: $3.70 vs $40 a year. $4,050: ~$15 vs $162 a year. 3% inflation on $4,050: -$121.50.
# 7% example return on $4,050: $283.50, so safety "costs" ~$121.50 a year vs 4%.

R = lambda els, **k: dict(bg="room", els=els, **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="Same bill, two prices", text="Tuesday night, the week before finals. Jordan's laptop makes a sound laptops are not supposed to make, and then it makes no sound at all. Black screen. Twelve-page paper due Friday.",
         scenes=[R([ch("jordan", "driven", 560, flip=True), em("💻", 1320, 520, 240, None, "FINALS WEEK")], bgargs=dict(night=True)),
                 R([ch("jordan", "fear", 560, flip=True), em("💻", 1320, 520, 240, "red", "BLACK SCREEN")], bgargs=dict(night=True))]),
    dict(text="The repair shop has good news and bad news. Good news, it's fixable. Bad news, it's seven hundred dollars. Jordan has about ninety dollars in checking, so the laptop goes on a credit card.",
         scenes=[dict(bg="office", els=[ch("jordan", "concerned", 480, flip=True), ch("tech", "explaining", 1440), em("🧾", 960, 400, 180, "red", "REPAIR: $700")]),
                 R([ch("jordan", "tired", 560, flip=True), em("💳", 1320, 480, 220, "red", "ON THE CARD")])]),
    dict(text="Same week, across town, Maya's cat eats a hair tie. The vet bill? Also seven hundred dollars. Universe has a sense of humor. Maya moves seven hundred dollars out of a savings account she nicknamed \"break glass,\" pays the vet, and goes to bed.",
         scenes=[R([ch("maya", "concernedFear", 560), em("🐈", 1320, 560, 220, "red", "VET BILL: $700")], bgargs=dict(extra="couch")),
                 R([ch("maya", "eyesClosed", 560), em("🔨", 1320, 480, 220, "green", "BREAK GLASS FUND")], bgargs=dict(extra="couch"))]),
    dict(text="Same bill. Same week. But here's the twist. If Jordan pays the card down at twenty-five dollars a month, his seven-hundred-dollar repair ends up costing about nine hundred and ninety-nine dollars, and it takes him forty months. That's three years and four months of paying for one bad Tuesday.",
         scenes=[dict(bg="plain", els=[ch("maya", "calm", 420, h=540), ch("jordan", "concerned", 1500, flip=True, h=540), tagel("MAYA: $700. DONE.", 420, 200, "green", True, 54), tagel("JORDAN: ~$999", 1500, 200, "red", True, 54)]),
                 dict(bg="board", bgargs=dict(text="40 MONTHS OF PAYMENTS"), els=[])]),
    dict(text="Maya's seven hundred cost seven hundred. Jordan's cost almost a thousand. The difference isn't income. They make about the same. The difference is one boring account. Today we're building it.",
         scenes=[dict(bg="plain", els=[em("🏦", 960, 450, 340, "green"), big("ONE BORING ACCOUNT", y=860, size=96)])]),
    dict(text="Quick honesty note first. Maya and Jordan are made up. Composites. The repair, the vet bill and their budgets are examples. The credit card rate is a real average from Federal Reserve data. And this channel is education, not financial advice. It's math and options, not a plan for your specific life.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 320), tagel("EXAMPLES, REAL RATES", 560, 700, "green", True)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="An emergency fund sounds like the vegetable of personal finance. Nobody posts it. Nobody brags about it. But it's the thing that decides whether a bad week stays a bad week, or turns into three years of payments. Seven moves. Let's go.",
         scenes=[dict(bg="plain", els=[em("🥦", 700, 440, 280), tagel("NOBODY BRAGS ABOUT IT", 700, 720, "amber")]),
                 dict(bg="board", bgargs=dict(text="7 MOVES"), els=[])]),
    # ---------------- move 1
    dict(chapter="1. It's when, not if", text="First, the uncomfortable truth. Surprise bills are not a rare plot twist. They're a recurring character. Cars break. Phones crack. Teeth do things. Jobs cut hours. Over a few years, something like this is almost guaranteed to happen to you.",
         scenes=[R([num(1), em("🚗", 760, 420, 170, "red"), em("📱", 1080, 420, 170, "red"), em("🦷", 1400, 420, 170, "red"), tagel("A RECURRING CHARACTER", 1080, 720, "red", True)])]),
    dict(text="And a lot of people aren't ready. In the Federal Reserve's survey of households, published in May of twenty twenty-six, sixty-three percent of adults said they would cover a four-hundred-dollar surprise expense with cash or its equivalent. Flip that around, and more than a third would not. They'd borrow, put it on a card, sell something, or just not pay.",
         scenes=[dict(bg="board", bgargs=dict(text="$400 SURPRISE?"), els=[]),
                 dict(bg="plain", els=[tagel("63%: COVER IT IN CASH", 960, 360, "green", True, 70), tagel("37%: SOMETHING ELSE", 960, 600, "red", True, 70)])]),
    dict(text="So the question isn't \"will something break?\" It's \"when it breaks, who pays for it?\" Present you, from savings. Or future you, with interest.",
         scenes=[R([ch("maya", "serious", 560), em("⚖️", 1320, 470, 240, None, "WHO PAYS?")])]),
    # ---------------- move 2
    dict(chapter="2. Start with $1,000", text="Second. The full emergency fund we're about to talk about can sound huge. So don't start there. Start with a starter fund. A common first target is one thousand dollars. It won't cover everything. It covers a lot of the small disasters, like a repair, a co-pay, or a last-minute bus ticket home.",
         scenes=[R([num(2), ch("maya", "driven", 560), em("🫙", 1320, 520, 240, "green", "STARTER: $1,000")], bgargs=dict(extra="shelf"))]),
    dict(text="How long does a thousand take? At twenty dollars a week, fifty weeks. About a year. At twenty-five a week, forty weeks. At forty a week, twenty-five weeks, about six months.",
         scenes=[dict(bg="plain", els=[tagel("$20 / WEEK = 50 WEEKS", 960, 280, "amber", False, 66), tagel("$25 / WEEK = 40 WEEKS", 960, 480, "amber", False, 66), tagel("$40 / WEEK = 25 WEEKS", 960, 680, "green", True, 66)])]),
    dict(text="If that still feels slow, speed it up with one-time money. Birthday cash. A tax refund. Selling the game console you haven't turned on since the last console came out. One-time money is the cheat code, because it doesn't touch your monthly budget at all.",
         scenes=[R([ch("jordan", "cheeky", 560, flip=True), em("🎮", 1320, 480, 220, "green", "SOLD IT")], bgargs=dict(extra="couch")),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("🕹️", 960, 420, 300, "green"), big("ONE-TIME MONEY = CHEAT CODE", y=820, color="green", size=80)])]),
    dict(text="Here's the thing about the first thousand. It changes how a surprise feels. Without it, a broken phone is a crisis. With it, a broken phone is just annoying. Annoying is a huge upgrade.",
         scenes=[R([ch("maya", "smile", 560), tagel("CRISIS → ANNOYING", 1300, 420, "green", True, 64)])]),
    # ---------------- move 3
    dict(chapter="3. Then aim for 3 months", text="Third. Once the starter fund is there, the next common target is three to six months of essential expenses. That's the version that can carry you through the big ones, like losing a job or getting hours cut.",
         scenes=[dict(bg="board", bgargs=dict(text="3 TO 6 MONTHS"), els=[num(3)])]),
    dict(text="The key word is essential. Not what you spend. What you'd have to spend if things went sideways. Rent, groceries, getting to work, utilities, your phone. Not the streaming services, not the takeout, not the new skins in your favorite game.",
         scenes=[R([em("🏠", 560, 400, 160, "green"), em("🛒", 860, 400, 160, "green"), em("🚌", 1160, 400, 160, "green"), em("💡", 1460, 400, 160, "green"), tagel("ESSENTIALS ONLY", 1010, 680, "green", True)]),
                 R([em("📺", 660, 420, 170, "red"), em("🥡", 1010, 420, 170, "red"), em("🎮", 1360, 420, 170, "red"), tagel("NOT THESE", 1010, 680, "red", True)])]),
    dict(text="Let's do Jordan's. His share of rent is seven hundred and fifty. Groceries, three hundred. Bus pass and getting around, one eighty. Utilities, seventy-five. Phone, forty-five. Total: one thousand, three hundred and fifty dollars a month.",
         scenes=[dict(bg="board", els=[ch("jordan", "explaining", 1560, flip=True), tagel("RENT $750", 560, 220, "ink", False, 50), tagel("GROCERIES $300", 560, 330, "ink", False, 50), tagel("TRANSPORT $180", 560, 440, "ink", False, 50), tagel("UTILITIES $75", 560, 550, "ink", False, 50), tagel("PHONE $45", 560, 660, "ink", False, 50)]),
                 dict(bg="board", bgargs=dict(text="= $1,350 / MONTH"), els=[])]),
    dict(text="Three months of that is four thousand and fifty dollars. Six months is eight thousand, one hundred. Those are big numbers for someone who just put a laptop on a card. That's fine. Nobody builds this in a month. It's a goal you climb toward, not a test you pass or fail.",
         scenes=[dict(bg="plain", els=[tagel("3 MONTHS: $4,050", 960, 360, "green", True, 76), tagel("6 MONTHS: $8,100", 960, 600, "amber", False, 76)]),
                 dict(bg="outside", els=[ch("jordan", "driven", 600, flip=True), em("🧗", 1350, 480, 240, "green", "CLIMB, DON'T CRAM")])]),
    dict(text="Which end of the range? Lean toward six if your income bounces around, like tips, gig work, or commission. Or if you're the only income in your household. Or if your job would be hard to replace quickly. Lean toward three if your paycheck is steady and your costs are low.",
         scenes=[dict(bg="plain", els=[tagel("6: IF PAY IS UNSTEADY", 960, 360, "amber", False, 64), tagel("3: IF PAY IS STEADY", 960, 600, "green", False, 64)])]),
    # ---------------- move 4
    dict(chapter="4. Give it its own home", text="Fourth. Where does this money live? Not in your checking account. If it sits next to your spending money, it will slowly turn into spending money. Not because you're bad at this. Because you're a human with a debit card and a food delivery app.",
         scenes=[R([num(4), ch("jordan", "suspicious", 560, flip=True), em("📱", 1320, 480, 220, "red", "DELIVERY APP")], bgargs=dict(extra="couch"))]),
    dict(text="The usual home is a separate savings account. Ideally a high-yield one, which is just a savings account that pays more interest. You want it insured, which at a bank means FDIC insurance, or NCUA at a credit union, generally up to two hundred and fifty thousand dollars per depositor, per institution, per ownership category. So the safety part is handled.",
         scenes=[dict(bg="office", els=[ch("maya", "explaining", 520), em("🏦", 1300, 440, 240, "green", "SEPARATE SAVINGS")]),
                 dict(bg="plain", els=[em("🛡️", 960, 420, 260, "green"), tagel("INSURED UP TO $250K", 960, 720, "green", True, 64)])]),
    dict(text="Now the interest. The national average savings rate was about thirty-seven hundredths of a percent in the FDIC's recent figures. Meanwhile, in early November twenty twenty-six, some online banks were paying around four percent. Rates change all the time, so check the current number before you open anything.",
         scenes=[dict(bg="plain", els=[tagel("AVERAGE: ~0.37%", 560, 420, "red", True, 72), tagel("ONLINE: ~4%", 1360, 420, "green", True, 72)]),
                 dict(bg="board", bgargs=dict(text="RATES CHANGE. CHECK."), els=[])]),
    dict(text="On a thousand dollars for a year, point three seven percent pays about three dollars and seventy cents. Four percent pays about forty dollars. On Jordan's three-month goal of four thousand and fifty, it's about fifteen dollars versus about a hundred and sixty-two. Same money. Same safety. Just a different address.",
         scenes=[dict(bg="plain", els=[tagel("$1,000: $3.70 VS $40", 960, 360, "green", False, 70), tagel("$4,050: $15 VS $162", 960, 600, "green", True, 70)]),
                 R([ch("maya", "smileLOL", 560), em("📬", 1320, 480, 220, "green", "NEW ADDRESS")])]),
    dict(text="Out of sight, but not out of reach. A separate account at a different bank can take a day or two to move money back. That small delay is a feature. It gives you one night to ask, is this really an emergency?",
         scenes=[R([ch("maya", "calm", 560), em("⏳", 1320, 480, 220, "green", "1-2 DAY SPEED BUMP")], bgargs=dict(night=True))]),
    # ---------------- move 5
    dict(chapter="5. Not in the stock market", text="Fifth. Why not just invest the emergency fund and earn more? Because emergencies love bad timing. The stock market can drop thirty percent in a few months. And the same bad economy that knocks the market down is often the one that cuts your hours.",
         scenes=[dict(bg="office", els=[num(5), em("📉", 700, 440, 260, "red", "MARKET -30%"), em("✂️", 1300, 440, 220, "red", "HOURS CUT")])]),
    dict(text="Picture it. You need four thousand dollars, and your investments just turned four thousand into about two thousand eight hundred. You'd be selling at the worst possible moment. It's like being forced to sell your rare items in a game right after a patch made them worthless.",
         scenes=[R([ch("jordan", "concernedFear", 560, flip=True), tagel("$4,000 → $2,800", 1320, 380, "red", True, 72), em("💎", 1320, 620, 160, "red")])]),
    dict(text="So investing money is for goals years away. Emergency money is for this month. Different jobs, different homes. The emergency fund is what lets your investments stay invested.",
         scenes=[dict(bg="board", bgargs=dict(text="YEARS AWAY ≠ THIS MONTH"), els=[])]),
    # ---------------- move 6
    dict(chapter="6. Know what counts", text="Sixth. What is an emergency? Here's a simple test. Three questions. Is it unexpected? Is it necessary? Is it urgent? If the answer is yes, yes, yes, that's what the fund is for.",
         scenes=[R([num(6), em("✅", 560, 300, 120, "green"), tagel("UNEXPECTED?", 1060, 300, "green", False, 56), em("✅", 560, 480, 120, "green"), tagel("NECESSARY?", 1060, 480, "green", False, 56), em("✅", 560, 660, 120, "green"), tagel("URGENT?", 1060, 660, "green", False, 56)], bgargs=dict(win=False))]),
    dict(text="A broken laptop the week of finals? Yes. A cat who ate a hair tie? Yes. A Black Friday deal on a TV that's \"only today\"? No. Your friend's birthday trip? Fun. Not an emergency. Holiday gifts? They happen on the same date every single year. That's not a surprise. That's a calendar.",
         scenes=[R([ch("maya", "smileBig", 560), em("💻", 1150, 420, 150, "green"), em("🐈", 1500, 420, 150, "green"), tagel("YES", 1320, 680, "green", True)]),
                 R([ch("jordan", "cheeky", 560, flip=True), em("📺", 1150, 420, 150, "red"), em("🎁", 1500, 420, 150, "red"), tagel("NOT AN EMERGENCY", 1320, 680, "red", True)])]),
    dict(text="For the predictable stuff, use a separate little savings bucket. People call it a sinking fund. Gifts, car registration, the yearly software subscription. Set those aside on purpose, so they never raid the emergency fund.",
         scenes=[R([em("🪣", 560, 460, 200, "green", "GIFTS"), em("🪣", 1060, 460, 200, "green", "CAR STUFF"), em("🪣", 1560, 460, 200, "green", "YEARLY BILLS")], bgargs=dict(extra="shelf"))]),
    # ---------------- move 7
    dict(chapter="7. Automate it, then refill it", text="Seventh. Make it automatic. Pick a number, any number, and set a transfer for the day after payday. Ten dollars counts. The trick is that the money leaves before you get a chance to have opinions about it.",
         scenes=[R([num(7), ch("maya", "eyesClosed", 560), em("📲", 1320, 480, 220, "green", "AUTO-TRANSFER: ON")], bgargs=dict(extra="couch"))]),
    dict(text="And give the account a name. Maya's is called \"break glass.\" Some people use \"do not touch,\" or the name of the thing it protects them from, like \"not today, credit card.\" It sounds silly. It works, because it's a lot harder to spend money that has a job title.",
         scenes=[dict(bg="plain", els=[tagel("\"BREAK GLASS\"", 960, 300, "green", True, 72), tagel("\"DO NOT TOUCH\"", 960, 500, "green", False, 64), tagel("\"NOT TODAY, CARD\"", 960, 700, "green", False, 64)])]),
    dict(text="Then, when you use it, use it without guilt. That's literally what it's for. Using your emergency fund in an emergency is not failing. It's the plan working. The only rule is the refill. Point the same automatic transfer back at it until it's full again.",
         scenes=[R([ch("maya", "smile", 560), em("🧯", 1320, 480, 220, "green", "USED IT. NO GUILT.")]),
                 R([ch("maya", "driven", 560), em("🔁", 1320, 480, 220, "green", "NOW REFILL")])]),
    # ---------------- honesty check
    dict(chapter="Honesty check: the cost of safety", text="Honesty check. An emergency fund is not free. It has a cost, and nobody likes to mention it.",
         scenes=[dict(bg="board", bgargs=dict(text="THE CATCH"), els=[])]),
    dict(text="Cost one: inflation. If prices rise three percent in a year, Jordan's four thousand and fifty loses about a hundred and twenty-two dollars of buying power. At four percent interest, he earns about a hundred and sixty-two, so he stays a little ahead. At the national average rate, he earns about fifteen dollars, and falls behind by roughly a hundred dollars of buying power every year.",
         scenes=[dict(bg="plain", els=[tagel("INFLATION 3%: -$122", 960, 260, "red", True, 64), tagel("AT 4%: +$162", 960, 480, "green", False, 64), tagel("AT 0.37%: +$15", 960, 700, "red", False, 64)]),
                 R([em("🐢", 700, 520, 220, "red", "CASH AT 0.37%"), em("🐇", 1350, 520, 220, "green", "CASH AT ~4%")])]),
    dict(text="Cost two: opportunity cost. If that same four thousand and fifty earned seven percent in investments, as an example, not a prediction, that's about two hundred and eighty-four dollars in a year instead of one sixty-two. So the safety costs Jordan about a hundred and twenty-two dollars a year in that example.",
         scenes=[dict(bg="plain", els=[tagel("INVESTED AT 7%: ~$284", 960, 360, "amber", False, 66), tagel("SAVINGS AT 4%: ~$162", 960, 580, "green", False, 66)])]),
    dict(text="Now compare that to his laptop. The card version of one repair cost him about two hundred and ninety-nine dollars in interest. A single emergency, paid on a card, can wipe out more than two years of the money he'd \"lose\" by keeping cash. That's why people pay for the safety. It's insurance you own.",
         scenes=[dict(bg="plain", els=[tagel("SAFETY: ~$122 / YEAR", 560, 400, "green", True, 60), tagel("ONE CARD BILL: ~$299", 1360, 400, "red", True, 60)]),
                 R([ch("maya", "solemn", 560), em("☂️", 1320, 470, 240, "green", "INSURANCE YOU OWN")])]),
    dict(text="One more catch. If you have high-interest credit card debt, the order matters. A common approach is to build the starter thousand first, so new surprises stop landing on the card. Then throw extra money at the debt. Then build the full three to six months. The credit card rate in the Fed's latest data was over twenty-two percent. Your savings won't earn anything close to that.",
         scenes=[dict(bg="board", bgargs=dict(text="$1K → DEBT → 3-6 MONTHS"), els=[]),
                 R([ch("jordan", "serious", 560, flip=True), em("💳", 1320, 480, 220, "red", "22.36% APR")])]),
    # ---------------- common mistake
    dict(chapter="The mistake: a card is the plan", text="Now the most common mistake. \"I don't need an emergency fund. I have a credit card.\" A credit card is a loan with a very fast on-ramp. It's not savings.",
         scenes=[R([ch("jordan", "cheeky", 560, flip=True), em("💳", 1320, 480, 220, "red", "\"MY EMERGENCY FUND\"")], bgargs=dict(extra="couch"))]),
    dict(text="Here's what that plan looks like in numbers. Jordan's seven hundred at about twenty-two percent. Pay twenty-five a month, and it's forty months and about two hundred and ninety-nine dollars of interest. Double the payment to fifty a month, and it's seventeen months and about a hundred and nineteen in interest. Better. Still a fee for a Tuesday.",
         scenes=[dict(bg="plain", els=[tagel("$25/MO: 40 MONTHS", 560, 360, "red", True, 60), tagel("+$299 INTEREST", 560, 520, "red", False, 60), tagel("$50/MO: 17 MONTHS", 1360, 360, "amber", True, 60), tagel("+$119 INTEREST", 1360, 520, "amber", False, 60)])]),
    dict(text="And the card can change on you. Card companies can lower your credit limit, sometimes right when the economy gets shaky, which is exactly when you'd need it. A savings account doesn't send you a letter saying it's decided to be smaller.",
         scenes=[dict(bg="office", els=[ch("jordan", "fear", 560, flip=True), em("✉️", 1320, 460, 220, "red", "LIMIT LOWERED")])]),
    # ---------------- close
    dict(chapter="Back to finals week", text="So, back to finals week. Jordan turned in his paper, on a laptop that's now worth about a thousand dollars of his future money. Maya's cat is fine, and completely unbothered.",
         scenes=[R([ch("jordan", "tired", 560, flip=True), em("💻", 1320, 480, 220, "red", "~$999 LAPTOP")], bgargs=dict(night=True)),
                 R([ch("maya", "smileLOL", 560), em("🐈", 1320, 560, 220, "green", "UNBOTHERED")], bgargs=dict(extra="couch"))]),
    dict(text="But Jordan did something smart afterward. He set up a twenty-five-dollar transfer the day after every payday, into an account he named \"never again, laptop.\" He's paying the card at fifty a month now. And for the first time, the next surprise is already partly paid for.",
         scenes=[R([ch("jordan", "driven", 560, flip=True, glow="green"), em("🫙", 1320, 480, 220, "green", "\"NEVER AGAIN, LAPTOP\"")], bgargs=dict(extra="shelf"))]),
    dict(text="Here's the one-line version. An emergency fund doesn't make you rich. It makes the bad days cheaper.",
         scenes=[dict(bg="plain", els=[big("IT MAKES BAD DAYS CHEAPER", y=480, color="green", size=100)])]),
    dict(text="Your move this week. Open a separate savings account, check that it's insured, and look up its current rate. Set an automatic transfer for any amount. And add up your essential monthly costs, so you know what three months actually means for you.",
         scenes=[R([em("✅", 560, 300, 130, "green"), tagel("OPEN SEPARATE SAVINGS", 1100, 300, "green", False, 48), em("✅", 560, 480, 130, "green"), tagel("AUTOMATE ANY AMOUNT", 1100, 480, "green", False, 48), em("✅", 560, 660, 130, "green"), tagel("ADD UP YOUR ESSENTIALS", 1100, 660, "green", False, 48)], bgargs=dict(win=False))]),
    dict(text="Next time: Roth IRA versus 401(k) at nineteen. Tax now or tax later, and why an employer match is the closest thing to free money you'll find. Subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("maya", "smileBig", 330), ch("jordan", "smile", 930, flip=True), em("📺", 1500, 400, 240, "green"), tagel("NEXT: ROTH VS 401(K)", 1500, 700, "green", False, 48)], bgargs=dict(extra="couch", win=False))]),
]
