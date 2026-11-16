VOICE = ("af_heart", 0.75)
SAY = {"$": "", "APR": "A P R"}

CAST = {
    "zoe": {"seed": "zoe", "head": ["buns"], "skinColor": ["edb98a"], "clothingColor": ["fcd34d"]},
    "sam": {"seed": "sam", "head": ["hatBeanie"], "skinColor": ["ae5d29"], "clothingColor": ["86efac"]},
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


# ---- the example, every number computed here (assumptions, not predictions)
import datetime as _dt


def pmt(p, r, n):
    i = r / 12
    return p * i / (1 - (1 + i) ** -n)


_D = _dt.date
BUYS = [("headphones", 200, _D(2026, 11, 20)), ("jacket", 120, _D(2026, 11, 27)), ("console bundle", 480, _D(2026, 11, 30)),
        ("concert", 160, _D(2026, 12, 5)), ("gifts", 240, _D(2026, 12, 12))]          # pay in 4: every 2 weeks, first at checkout
PAYS = sorted((d + _dt.timedelta(days=14 * k), a / 4) for _, a, d in BUYS for k in range(4))
PAYDAYS = [_D(2026, 11, 20) + _dt.timedelta(days=14 * i) for i in range(6)]
WINDOWS = [sum(a for d, a in PAYS if PAYDAYS[i] <= d < PAYDAYS[i + 1]) for i in range(5)]   # [200, 300, 300, 300, 100]
TOTAL = sum(a for _, a, _ in BUYS)          # $1,200 in 20 payments
TAKE_HOME, REGULAR = 600, 380               # assumed: take-home per 2-week paycheck, phone/gas/food/rent to parents
FREE = TAKE_HOME - REGULAR                  # $220 free per paycheck -> $80 short in each $300 window
OVERDRAFT, LATE = 27, 8                     # Bankrate: overdraft fees run about $25-$30; assumed $8 late fee (check your terms)
LAPTOP = pmt(900, 0.30, 12)                 # $87.74 a month, $152.86 interest on a 12-month plan at an assumed 30% APR
CARD6 = pmt(1200, 0.2236, 6) * 6 - 1200     # $79.46 interest: $1,200 on a card at 22.36%, paid off over 6 months
NO_SPLIT = 120 + 240                        # what Zoe says she'd have bought at full price: jacket + gifts
OWED_DEC12 = TOTAL - sum(a for d, a in PAYS if d <= _D(2026, 12, 12))   # $820
FUND = 22 * 50                              # $50 per paycheck, Jan 29 to Nov 19, 2027 = 22 paychecks -> $1,100
assert len(PAYS) == 20 and TOTAL == 1200 and WINDOWS == [200, 300, 300, 300, 100] and FREE == 220
assert round(LAPTOP, 2) == 87.74 and round(LAPTOP * 12 - 900) == 153 and round(CARD6) == 79 and TOTAL - NO_SPLIT == 840 and OWED_DEC12 == 820

R = lambda els, **k: dict(bg="room", els=els, **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="Five buttons, one January", text="The Friday before Thanksgiving. Zoe is nineteen, on her lunch break, scrolling. A pair of wireless headphones. Two hundred dollars. Too much. But right under the price, in friendly little letters: or four payments of fifty dollars. Zero interest. Tap.",
         scenes=[R([ch("zoe", "calm", 560), em("📱", 1300, 520, 220)], bgargs=dict(extra="couch")),
                 R([ch("zoe", "smileBig", 560), em("🎧", 1300, 480, 240, "green", "4 × $50. 0% INTEREST")], bgargs=dict(extra="couch"))]),
    dict(text="A week later it's Black Friday. A jacket, four payments of thirty. Then a game console bundle on Cyber Monday, four payments of a hundred and twenty. Concert tickets. Holiday gifts for the whole family. Every one of them split into four. Every one of them small.",
         scenes=[R([ch("zoe", "cheeky", 480), em("🧥", 1150, 420, 170, None, "4 × $30"), em("🎮", 1600, 420, 170, None, "4 × $120")]),
                 R([ch("zoe", "smileLOL", 480), em("🎟️", 1150, 420, 170, None, "4 × $40"), em("🎁", 1600, 420, 170, None, "4 × $60")])]),
    dict(text="Here's the twist. Zoe never paid a single cent of interest. Not one. And by January, she had a bill of three hundred dollars due every two weeks. That's half her paycheck. Gone, before rent, before gas, before food.",
         scenes=[dict(bg="board", bgargs=dict(text="0% INTEREST. HALF HER PAYCHECK."), els=[]),
                 R([ch("zoe", "concernedFear", 600), em("🧾", 1320, 480, 260, "red", "$300 EVERY 2 WEEKS")])]),
    dict(text="Nobody tricked her with a hidden interest rate. Something sneakier happened. And you've probably seen the same button this week, because stores are pushing it harder than ever right now.",
         scenes=[dict(bg="plain", els=[em("🔘", 960, 440, 340, "red"), big("THE FRIENDLIEST BUTTON ONLINE", y=860, size=86)])]),
    dict(text="Quick honesty note. Zoe and her friend Sam, who you'll meet in a minute, are made up. Composites. The data comes from real sources, and every number is calculated on screen, but it's an example, not your situation. And this channel is education, not financial advice. Use it to understand the button, not as a plan for your money.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 320), tagel("EXAMPLE, NOT A PROMISE", 560, 700, "green", True)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="Buy now, pay later is huge this time of year. Adobe forecast about twenty-one billion dollars of online holiday shopping paid this way in November and December alone, with more than a billion on Cyber Monday. So here are seven things to understand before you tap it. Zoe learned them in January. You can learn them now.",
         scenes=[dict(bg="plain", els=[tagel("$21.3 BILLION", 960, 330, "amber", True, 96), tagel("NOV + DEC, FORECAST", 960, 560, "ink", False, 56)]),
                 dict(bg="board", bgargs=dict(text="7 THINGS BEFORE YOU TAP"), els=[])]),
    # ---------------- 1
    dict(chapter="1. Know which kind it is", text="First, buy now, pay later is not one thing. It's two. The kind Zoe used is the classic pay in four. You pay a quarter at checkout, then a quarter every two weeks. Usually zero interest. Six weeks and you're done.",
         scenes=[dict(bg="board", bgargs=dict(text="PAY IN 4: 6 WEEKS, 0%"), els=[num(1)]),
                 dict(bg="plain", els=[num(1), *[em("🟩", 600 + i * 240, 440, 170, "green") for i in range(4)], tagel("TODAY · 2 WK · 4 WK · 6 WK", 960, 680, "green", False, 52)])]),
    dict(text="The other kind is a monthly plan, usually for bigger stuff, like a laptop. Twelve monthly payments, sometimes twenty-four. And those often charge interest. Some plans charge an APR above thirty percent. Others are zero. The checkout screen looks almost the same for both.",
         scenes=[dict(bg="office", els=[ch("zoe", "suspicious", 560), em("💻", 1300, 440, 240, "amber", "12 MONTHS. APR?")]),
                 dict(bg="plain", els=[tagel("PAY IN 4: OFTEN 0%", 560, 400, "green", False, 56), tagel("MONTHLY: CAN BE 30%+", 1360, 400, "red", False, 56)])]),
    dict(text="Here's what that difference looks like. A nine hundred dollar laptop on a twelve month plan at an assumed thirty percent APR. That's about eighty-seven dollars and seventy-four cents a month. Sounds fine. But by the end you've paid about a hundred and fifty-three dollars extra, for the same laptop.",
         scenes=[dict(bg="office", els=[em("💻", 560, 440, 260), tagel("$900 AT 30% APR", 560, 720, "amber")]),
                 dict(bg="plain", els=[tagel("$87.74 A MONTH", 960, 330, "ink", False, 76), tagel("+$153 INTEREST", 960, 560, "red", True, 76)])]),
    dict(text="So before you tap, find two numbers on the screen: the APR, and the total you'll pay. If you can't find them, that's an answer too.",
         scenes=[R([ch("zoe", "serious", 560), tagel("FIND: APR + TOTAL", 1300, 420, "green", True)])]),
    # ---------------- 2
    dict(chapter="2. Count the stack, not the slice", text="Now, back to Zoe's zero percent plans. Each one is tiny on its own. That's the design. Your brain sees fifty dollars, thirty dollars, forty dollars. It does not see the stack.",
         scenes=[dict(bg="plain", els=[num(2), em("🍕", 960, 460, 300), tagel("YOU SEE ONE SLICE", 960, 780, "amber")])]),
    dict(text="Let's stack it. Five purchases. Twelve hundred dollars total. That's twenty separate payments, landing on twenty separate dates. It's basically a game of Tetris, except the blocks are bills and they never clear a line.",
         scenes=[dict(bg="board", bgargs=dict(text="5 BUYS = $1,200 = 20 PAYMENTS"), els=[num(2)]),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[*[em("🟥", 660 + (i % 4) * 200, 300 + (i // 4) * 130, 120, "red") for i in range(12)], big("BILLS NEVER CLEAR A LINE", y=900, color="red", size=80)])]),
    dict(text="Zoe gets paid every other Friday. Line her payments up against her paychecks and here's what's due in each two-week stretch. Two hundred dollars in the first. Then three hundred. Then three hundred. Then three hundred again. Then a hundred, and finally she's free.",
         scenes=[dict(bg="plain", els=[dict(t="chart", series=[{"name": "Due", "color": "red", "ys": WINDOWS}], xlabels=["NOV 20", "DEC 4", "DEC 18", "JAN 1", "JAN 15"], label="Due per 2-week paycheck", fmt="${v}", ymax=400, box=(300, 140, 1640, 760))])]),
    dict(text="Zoe takes home about six hundred dollars a paycheck, in our example. Her regular stuff, phone, gas, food, and the rent her parents charge her, is about three eighty. That leaves two hundred and twenty. And her stack wants three hundred. She's eighty dollars short, three paychecks in a row.",
         scenes=[R([ch("zoe", "concerned", 520), tagel("$600 IN", 1300, 300, "green"), tagel("− $380 REGULAR STUFF", 1300, 450, "ink"), tagel("= $220 FREE", 1300, 600, "amber")]),
                 R([ch("zoe", "fear", 520), tagel("STACK WANTS $300", 1300, 380, "red", True), tagel("SHORT $80", 1300, 560, "red")])]),
    dict(text="So the question is never \"can I afford fifty dollars?\" It's \"can I afford everything I already owe, plus fifty, on every payday until it's done?\" Write the dates down. A notes app is fine. The math takes two minutes, and it's two minutes January Zoe would have paid a lot for.",
         scenes=[dict(bg="board", bgargs=dict(text="ALL OF IT + THIS ONE?"), els=[]),
                 R([ch("zoe", "explaining", 560), em("🗓️", 1300, 460, 240, "green", "WRITE THE DATES")])]),
    # ---------------- 3
    dict(text="And notice what the app shows you. Usually just the next payment, the one coming up. Not the total. Not the other three plans you have with other companies. Each app sees its own slice. You're the only one holding the whole pizza, and it's a lot heavier than it looked on the menu.",
         scenes=[R([ch("zoe", "suspicious", 560), em("📱", 1300, 460, 220, "amber", "NEXT PAYMENT: $50")]),
                 dict(bg="plain", els=[em("🍕", 960, 440, 320, "red"), tagel("YOU HOLD THE WHOLE PIZZA", 960, 760, "red", True)])]),
    dict(chapter="3. Check the date, not just the amount", text="Here's the part nobody mentions at checkout. Those payments come out automatically, usually from your debit card, on their schedule. Not on payday. On their day.",
         scenes=[R([num(3), ch("zoe", "tired", 560), em("📅", 1300, 460, 240, "red", "THEIR DAY, NOT PAYDAY")])]),
    dict(text="December twenty-eighth. Zoe's console payment, a hundred and twenty dollars, hits her account three days before her next paycheck. She doesn't have it. Her bank covers it anyway, and charges an overdraft fee. Bankrate says those usually run about twenty-five to thirty dollars. Call it twenty-seven.",
         scenes=[R([ch("zoe", "concernedFear", 560), em("🏦", 1300, 440, 240, "red", "OVERDRAFT: $27")]),
                 dict(bg="plain", els=[tagel("DEC 28: $120 DUE", 560, 400, "red", False, 60), tagel("PAYDAY: JAN 1", 1360, 400, "green", False, 60)])]),
    dict(text="Two weeks later, a different payment gets declined instead. Now the lender charges a late fee. Fees vary by company, so check your terms, but let's say eight dollars. Two little fees, thirty-five dollars, on stuff that was supposed to be free. It's the blue shell of personal finance. You were doing fine, and then, out of nowhere.",
         scenes=[R([ch("zoe", "rage", 560), em("⏰", 1300, 460, 220, "red", "LATE FEE: $8 (EXAMPLE)")]),
                 dict(bg="plain", els=[tagel("$27 + $8 = $35", 960, 340, "red", True, 90), tagel("ON \"0% INTEREST\"", 960, 580, "ink", False, 64)])]),
    dict(text="And Zoe is not unusual. In LendingTree's 2026 survey, forty-seven percent of buy now, pay later users said they'd paid late at least once in the past year. That's almost half. Up from about a third two years before.",
         scenes=[dict(bg="plain", els=[tagel("47% PAID LATE", 960, 330, "red", True, 96), tagel("IN THE PAST YEAR (SURVEY)", 960, 560, "ink", False, 56)])]),
    dict(text="The most common way it goes wrong is not one big purchase. It's the small ones that keep coming. A plan for shoes, then one for takeout, then one for a game, each one fine alone. In the same LendingTree data from a year earlier, a quarter of users said they'd used it for groceries. When you're splitting food, the stack never ends, because you get hungry again.",
         scenes=[R([ch("zoe", "tired", 520), em("👟", 1150, 440, 150, "red"), em("🥡", 1400, 440, 150, "red"), em("🎮", 1650, 440, 150, "red")]),
                 dict(bg="plain", els=[tagel("1 IN 4 USED IT FOR GROCERIES", 960, 330, "red", True, 72), tagel("LENDINGTREE, 2025 SURVEY", 960, 560, "ink", False, 56)])]),
    dict(text="One fix: if you use it at all, pick the payment card on purpose, and keep a small cushion in that account. Or set a reminder the day before each payment. Boring. Works.",
         scenes=[R([ch("zoe", "calm", 560), em("🛟", 1300, 460, 240, "green", "KEEP A CUSHION")], bgargs=dict(extra="shelf"))]),
    # ---------------- 4
    dict(chapter="4. Notice the feels-small trick", text="Here's a question worth asking. If buy now, pay later is free for you, who pays? Mostly the store. Stores usually pay the lender a fee on each sale. Why would a store happily pay to let you pay later?",
         scenes=[dict(bg="office", els=[num(4), em("🏬", 600, 460, 280), em("❓", 1300, 460, 260, "amber", "WHO PAYS?")])]),
    dict(text="Because splitting the price makes it feel smaller, and people who feel like they're spending less tend to buy more, or buy bigger. Two hundred dollars is a decision. Fifty dollars is a vibe. It's the same reason games sell you a battle pass instead of one big price. Small, repeated, easy.",
         scenes=[dict(bg="plain", els=[tagel("$200 = A DECISION", 560, 400, "amber", False, 60), tagel("$50 = A VIBE", 1360, 400, "red", True, 60)]),
                 R([ch("zoe", "cheeky", 560), em("🎮", 1300, 460, 220, None, "BATTLE PASS ENERGY")], bgargs=dict(extra="couch"))]),
    dict(text="So in January, Zoe did an honesty check on her five purchases. Would she have paid the full price, all at once, on the day she bought it? The jacket, yes. The gifts, yes. That's three hundred and sixty dollars. The other eight hundred and forty? Honestly, no. The split made the price feel like a different number.",
         scenes=[R([ch("zoe", "solemn", 520), tagel("FULL PRICE? YES: $360", 1300, 380, "green"), tagel("FULL PRICE? NO: $840", 1300, 560, "red", True)])]),
    dict(text="That's the test. Before you tap, ask: would I buy this today if I had to pay the whole thing right now? If the answer is no, four payments doesn't make it cheaper. It just makes it later.",
         scenes=[dict(bg="board", bgargs=dict(text="WOULD I PAY IT ALL TODAY?"), els=[])]),
    # ---------------- 5
    dict(chapter="5. Returns don't pause the bill", text="Okay, a quick one that bites a lot of people. Zoe returns the jacket. It doesn't fit. Easy, right? Except the store has to process the return, then tell the lender, and the payment schedule can keep running in the meantime.",
         scenes=[R([num(5), ch("zoe", "suspicious", 520), em("📦", 1300, 480, 240, "amber", "RETURN SENT")])]),
    dict(text="So keep paying until the refund actually shows up in your app. If you just stop paying because you sent the box back, that can turn into a late payment on something you don't even own anymore. Keep the receipt, keep the tracking number, and if it drags on, contact the lender, not just the store.",
         scenes=[R([ch("zoe", "concerned", 520), tagel("KEEP PAYING TILL REFUNDED", 1300, 420, "red", True, 50)]),
                 dict(bg="office", els=[em("🧾", 600, 460, 240, "green", "RECEIPT"), em("📮", 1300, 460, 240, "green", "TRACKING #")])]),
    # ---------------- 6
    dict(chapter="6. It can show up on your credit", text="Next. For a long time, these loans mostly didn't show up on credit reports at all. That's changing. Some lenders now report them to credit bureaus, and in 2025 FICO announced credit scores that can include buy now, pay later data. Reporting is still uneven, and it's still changing.",
         scenes=[dict(bg="office", els=[num(6), em("📊", 600, 460, 260), em("👀", 1300, 460, 220, "amber", "NOW IT'S WATCHING")])]),
    dict(text="So assume it can count. On-time payments might help a little, depending on who reports. But a missed one, or a debt that gets sent to collections, can hurt your score for years. And your score matters when you rent your first apartment or finance a car.",
         scenes=[R([ch("zoe", "serious", 520), tagel("ASSUME IT CAN COUNT", 1300, 420, "amber", True)]),
                 dict(bg="plain", els=[em("🏠", 560, 440, 220, "red", "APARTMENT"), em("🚗", 1360, 440, 220, "red", "CAR LOAN")])]),
    dict(text="There's also a weird side effect. Since a lot of these loans don't show up anywhere, the lender approving your fifth plan may have no idea about the first four. In the government's consumer finance study, about sixty-three percent of borrowers had more than one of these loans open at the same time at some point in the year. Nobody's checking your stack. Except you.",
         scenes=[dict(bg="plain", els=[tagel("63% HAD 2+ AT ONCE", 960, 330, "red", True, 90), tagel("CFPB, 2022 DATA", 960, 560, "ink", False, 56)]),
                 R([ch("zoe", "awe", 520), em("🕵️", 1300, 460, 240, "green", "YOU CHECK THE STACK")])]),
    # ---------------- 7
    dict(chapter="7. Pay later, or save first", text="Now meet Sam. Zoe's friend from work, same kind of job, a beanie he refuses to take off indoors. Back in September, Sam started moving fifty dollars from each paycheck into a separate savings account he named \"December.\"",
         scenes=[dict(bg="cafe", els=[num(7), ch("sam", "smile", 560), em("🫙", 1300, 520, 220, "green", "\"DECEMBER\" FUND")])]),
    dict(text="By the start of December, he had three hundred dollars. He spent three hundred dollars on gifts. No schedule, no dates, no fees, no January. His holiday was smaller than Zoe's. That's kind of the point. He bought what he could actually see.",
         scenes=[dict(bg="cafe", els=[ch("sam", "smileBig", 560), em("🎁", 1300, 480, 240, "green", "$300. PAID. DONE.")]),
                 dict(bg="plain", els=[ch("sam", "calm", 460), ch("zoe", "tired", 1460, flip=True), tagel("SAM: $0 OWED", 460, 230, "green"), tagel("ZOE: $820 OWED", 1460, 230, "red")])]),
    dict(text="Meanwhile, on December twelfth, the day Zoe tapped her fifth plan, she still owed eight hundred and twenty dollars. Sam owed nothing. Saving first is basically buy now, pay later, in reverse. Pay earlier, buy later. The fees go to zero, and the stress goes with them.",
         scenes=[dict(bg="board", bgargs=dict(text="SAVE FIRST = PAY LATER IN REVERSE"), els=[]),
                 R([ch("sam", "eyesClosed", 560), em("😌", 1300, 460, 220, "green", "NO JANUARY SURPRISE")], bgargs=dict(extra="couch"))]),
    dict(text="If you do use pay in four, a few guardrails. One plan at a time. Only when the full price is already sitting in your account. Never for things you eat, like groceries or takeout, because you'll still be paying for the burrito long after it's gone. And never to make a payment on another plan.",
         scenes=[R([em("✅", 520, 280, 110, "green"), tagel("ONE PLAN AT A TIME", 1080, 280, "green", False, 50), em("✅", 520, 440, 110, "green"), tagel("FULL PRICE ALREADY SAVED", 1080, 440, "green", False, 50), em("❌", 520, 600, 110, "red"), tagel("NOT FOR FOOD", 1080, 600, "red", False, 50), em("❌", 520, 760, 110, "red"), tagel("NOT TO PAY ANOTHER PLAN", 1080, 760, "red", False, 50)], bgargs=dict(win=False))]),
    # ---------------- honesty check
    dict(text="Want to try Sam's way? Pick a number for next December. Divide it by the paychecks you have left. Three hundred dollars over six paychecks is fifty each. Set it to move automatically on payday, into an account you don't carry a card for. Then forget it exists, which, let's be honest, is a skill most of us already have.",
         scenes=[dict(bg="board", bgargs=dict(text="$300 ÷ 6 PAYCHECKS = $50"), els=[]),
                 dict(bg="cafe", els=[ch("sam", "explaining", 560), em("📲", 1300, 480, 220, "green", "AUTO ON PAYDAY")])]),
    dict(chapter="Honesty check: when it's fine", text="Okay, fairness time, because buy now, pay later isn't evil. Used perfectly, it can be cheaper than the alternative a lot of people actually use: a credit card balance.",
         scenes=[dict(bg="board", bgargs=dict(text="IS IT ACTUALLY BAD?"), els=[])]),
    dict(text="Credit cards that charge interest averaged about twenty-two percent in the Federal Reserve's latest data. If Zoe had put the same twelve hundred dollars on a card at that rate and paid it off over six months, she'd have paid about seventy-nine dollars in interest. On her pay in four plans, paid on time, she'd have paid zero.",
         scenes=[dict(bg="plain", els=[tagel("CARD, 22.36%, 6 MONTHS", 560, 360, "red", False, 54), tagel("≈ $79 INTEREST", 560, 540, "red", True, 64), tagel("PAY IN 4, ON TIME", 1360, 360, "green", False, 54), tagel("$0 INTEREST", 1360, 540, "green", True, 64)])]),
    dict(text="Even with her two fees, thirty-five dollars, Zoe still came out ahead of the card. So the honest answer is: the math on one plan, paid on time, can be fine. The interest was never the problem.",
         scenes=[R([ch("zoe", "calm", 560), tagel("$35 IN FEES < $79", 1300, 400, "amber", True)])]),
    dict(chapter="Honesty check: the real cost", text="The real cost was the eight hundred and forty dollars she wouldn't have spent at full price. Plus three paychecks in a row of being eighty dollars short. Plus the feeling of dreading every other Friday. None of that shows up as an interest rate. All of it is real.",
         scenes=[dict(bg="plain", els=[tagel("$840 SHE WOULDN'T HAVE SPENT", 960, 300, "red", True, 64), tagel("3 PAYCHECKS $80 SHORT", 960, 500, "red", False, 60), tagel("DREADING EVERY OTHER FRIDAY", 960, 700, "red", False, 56)])]),
    dict(text="And here's the catch nobody puts on the checkout screen. Buy now, pay later is easiest to use when you're short on money. Which is exactly when one surprise, a car repair, a smaller paycheck, a sick week, turns a neat little schedule into overdrafts and late fees. LendingTree's survey also found more than half of users said they couldn't make ends meet without it. That's not a shopping tool anymore. That's a warning light.",
         scenes=[R([ch("zoe", "concernedFear", 560), em("🚨", 1300, 460, 240, "red", "WARNING LIGHT")]),
                 dict(bg="plain", els=[tagel("54% SAY THEY NEED IT", 960, 330, "red", True, 84), tagel("TO MAKE ENDS MEET (SURVEY)", 960, 560, "ink", False, 56)])]),
    dict(text="If that sounds like you right now, no shame. It's common. The move is to stop adding new plans, list every payment you already owe with its date, and talk to the lender early if you can't make one. Before it's late, not after.",
         scenes=[R([ch("zoe", "driven", 560), em("📝", 1300, 460, 240, "green", "LIST EVERY DATE")], bgargs=dict(extra="shelf"))]),
    # ---------------- close
    dict(chapter="Back to Zoe", text="So, back to Zoe. Late January. The last payment, sixty dollars for the gifts, clears on the twenty-third. She's done. She deleted the saved card from her shopping apps, which felt weirdly dramatic, like unfollowing an ex.",
         scenes=[R([ch("zoe", "eyesClosed", 560), em("✅", 1300, 460, 240, "green", "LAST PAYMENT: JAN 23")], bgargs=dict(extra="couch")),
                 R([ch("zoe", "smileLOL", 560), em("📱", 1300, 480, 220, "green", "SAVED CARD: DELETED")], bgargs=dict(extra="couch"))]),
    dict(text="Then she copied Sam. Fifty dollars a paycheck into a \"December\" account, starting the next Friday. By next November, that's twenty-two paychecks. Eleven hundred dollars. Almost the same holiday, paid before it happens, with zero dates to remember.",
         scenes=[dict(bg="cafe", els=[ch("zoe", "smile", 460), ch("sam", "smileBig", 1460, flip=True), em("🫙", 960, 560, 200, "green")]),
                 dict(bg="plain", els=[tagel("$50 × 22 PAYCHECKS", 960, 330, "green", False, 76), tagel("= $1,100 BY NOVEMBER", 960, 560, "green", True, 76)])]),
    dict(text="The one-line takeaway: four small payments are still one big price. If you can't afford it once, splitting it doesn't make it cheaper. It just makes it later.",
         scenes=[dict(bg="board", bgargs=dict(text="4 SMALL PAYMENTS = 1 BIG PRICE"), els=[])]),
    dict(text="Next video, we're doing the math on your first apartment: how much rent you can really handle, deposits, renters insurance, and whether a roommate is worth it. If this one saved you from a January surprise, subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("zoe", "smileBig", 320), ch("sam", "smile", 960, flip=True), em("📺", 1560, 470, 260, "green"), tagel("NEXT: APARTMENTS", 1520, 200, "green", True, 52)], bgargs=dict(extra="couch", win=False))]),
]
