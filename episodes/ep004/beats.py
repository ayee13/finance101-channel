VOICE = ("af_heart", 0.75)
SAY = {"$": "", "APR": "A.P.R.", "AnnualCreditReport.com": "Annual Credit Report dot com", "VantageScore": "Vantage Score"}

CAST = {
    "maya": {"seed": "maya", "head": ["bun"], "skinColor": ["d08b5b"], "clothingColor": ["9ddadb"]},
    "jordan": {"seed": "jordan", "head": ["short3"], "skinColor": ["edb98a"], "clothingColor": ["ffcf77"]},
    "clerk": {"seed": "clerk", "head": ["noHair2"], "skinColor": ["ae5d29"], "clothingColor": ["8fa7df"]},
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


# ---- the examples, all numbers computed here
LIMIT, CONCERT = 500, 400
UTIL_BAD = CONCERT / LIMIT                      # 0.80
UTIL_OK = 50 / LIMIT                            # 0.10
CARD_APR = 0.2215                               # Fed G.19, May 2026, accounts assessed interest
INT_MONTH = CONCERT * CARD_APR / 12             # 7.38
INT_YEAR = CONCERT * ((1 + CARD_APR / 12) ** 12 - 1)   # 98.17
SECURED, SUB = 200, 20                          # made-up secured card deposit and one subscription
UTIL_SEC = SUB / SECURED                        # 0.10


def pmt(p, r, n):
    i = r / 12
    return p * i / (1 - (1 + i) ** -n)


LOAN, MONTHS = 15000, 60                        # used car, 5 years
PRIME, SUBP = 0.0877, 0.1942                    # Experian Q1 2026 used-car averages (VantageScore 4.0)
PAY_P, PAY_S = pmt(LOAN, PRIME, MONTHS), pmt(LOAN, SUBP, MONTHS)        # 309.70, 392.58
INT_P, INT_S = PAY_P * MONTHS - LOAN, PAY_S * MONTHS - LOAN             # 3,582, 8,555
GAP = INT_S - INT_P                                                     # 4,973

R = lambda els, **k: dict(bg="room", els=els, **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="The deposit nobody expected", text="Maya is nineteen, and she just signed for her first studio apartment. Tiny. One window. A radiator that sounds like it's thinking. She's thrilled. Step one of adulthood: put the internet and the electric bill in her own name.",
         scenes=[R([ch("maya", "smileBig", 560), em("🔑", 1320, 460, 220, "green", "FIRST PLACE")], bgargs=dict(extra="shelf")),
                 R([ch("maya", "driven", 560), em("💡", 1150, 420, 170), em("📶", 1550, 420, 170)])]),
    dict(text="Maya is good with money. She has never owed anyone a single dollar. No credit card. No loans. She pays cash, she splits the bill to the cent, and she has never once been late on anything. So she's expecting a gold star.",
         scenes=[dict(bg="cafe", els=[ch("maya", "smile", 560), em("💵", 1320, 460, 220, "green", "NEVER OWED A DOLLAR")]),
                 R([ch("maya", "lovingGrin1", 560), em("⭐", 1320, 440, 240, "green", "GOLD STAR?")])]),
    dict(text="Instead, the electric company says it can't find a credit score for her. No score, no history. So before they'll turn on her lights, they'd like a security deposit. In our example, three hundred dollars.",
         scenes=[dict(bg="office", els=[ch("maya", "concerned", 480), ch("clerk", "explaining", 1440, flip=True), em("🖥️", 960, 400, 170, "red", "NO SCORE FOUND")]),
                 R([ch("maya", "fear", 560), em("🧾", 1320, 460, 220, "red", "DEPOSIT: $300")])]),
    dict(text="Her friend Jordan, same age, moved out the same month. Jordan has, let's say, a more relaxed relationship with money. But Jordan got a student credit card at eighteen, put one small bill on it, and paid it off every month. Jordan's deposit? Zero.",
         scenes=[R([ch("jordan", "cheeky", 560, flip=True), em("💳", 1320, 460, 220, "green", "1 SMALL BILL, PAID")], bgargs=dict(extra="couch")),
                 dict(bg="plain", els=[tagel("MAYA: $300 DEPOSIT", 560, 420, "red", True, 60), tagel("JORDAN: $0", 1360, 420, "green", True, 60)])]),
    dict(text="So the person who has never owed a dollar looks riskier than the person who uses a credit card. That feels backwards. It's not a bug. It's how the system reads you. And once you see how it works, building a good score from zero, without ever paying a cent of interest, is very doable.",
         scenes=[dict(bg="plain", els=[em("🤔", 960, 440, 340), big("WAIT. THAT'S BACKWARDS?", y=860, size=100)]),
                 dict(bg="board", bgargs=dict(text="NO DEBT ≠ GOOD CREDIT"), els=[])]),
    dict(text="Quick honesty note. Maya and Jordan are made up. Composites. Deposits, rules and scores vary by company and by state, and the dollar amounts here are examples. The facts about how scores work are sourced in the description. And this channel is education, not financial advice. It's how the system works, not a plan for your specific life.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 300), tagel("EXAMPLES, NOT QUOTES", 1240, 330, "green", True, 54), tagel("RULES VARY BY COMPANY", 1240, 560, "amber", False, 54)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="Seven things to know about credit scores. What the number is, the five ingredients inside it, and how to start one from nothing. Let's open the box.",
         scenes=[dict(bg="board", bgargs=dict(text="7 THINGS"), els=[])]),
    # ---------------- 1
    dict(chapter="1. A score answers one question", text="First. A credit score is not a grade on you as a person. It answers one narrow question. If someone lends you money, how likely are you to pay it back on time? That's it. It's a prediction, made by a computer, from your past behavior.",
         scenes=[dict(bg="plain", els=[num(1), em("❓", 600, 460, 280), tagel("WILL YOU PAY ON TIME?", 1280, 460, "ink", False, 60)]),
                 dict(bg="office", els=[ch("maya", "suspicious", 560), em("🤖", 1320, 460, 220, None, "A PREDICTION")])]),
    dict(text="The most common scores run from three hundred to eight hundred and fifty. Higher means lower risk to a lender. The national average FICO score, the most widely used kind, was seven hundred and fourteen in FICO's latest report.",
         scenes=[dict(bg="plain", els=[tagel("300", 360, 420, "red", False, 90), em("➡️", 960, 420, 160), tagel("850", 1560, 420, "green", True, 90), big("AVERAGE FICO: 714", y=780, size=110)])]),
    dict(text="And here's a thing that confuses everyone. You don't have one score. You have dozens. The raw material is your credit report, a record kept by three big credit bureaus. Then different scoring models, mostly FICO and VantageScore, each in several versions, turn that report into a number. Like the same gameplay footage, scored by different judges.",
         scenes=[dict(bg="office", els=[em("📄", 400, 420, 180, None, "BUREAU 1"), em("📄", 960, 420, 180, None, "BUREAU 2"), em("📄", 1520, 420, 180, None, "BUREAU 3")]),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("🎮", 960, 420, 300, "green"), big("SAME GAME, DIFFERENT JUDGES", y=840, color="green", size=90)])]),
    dict(text="So if your banking app says seven twenty and a lender sees six ninety, nobody is lying. They're reading different versions. What matters is the stuff underneath, and that stuff is the same everywhere.",
         scenes=[R([ch("jordan", "suspicious", 560, flip=True), tagel("APP: 720", 1300, 330, "ink", False, 60), tagel("LENDER: 690", 1300, 520, "amber", False, 60)])]),
    # ---------------- the five ingredients
    dict(text="FICO publishes the recipe, roughly. Five ingredients. Payment history, about thirty-five percent. Amounts owed, about thirty. Length of credit history, about fifteen. New credit, about ten. And credit mix, about ten. The next four chapters walk through them, biggest first.",
         scenes=[dict(bg="plain", els=[tagel("PAYMENT HISTORY  35%", 960, 170, "green", True, 56), tagel("AMOUNTS OWED  30%", 960, 350, "green", False, 56), tagel("LENGTH OF HISTORY  15%", 960, 530, "ink", False, 56),
                                       tagel("NEW CREDIT  10%", 960, 710, "ink", False, 56), tagel("CREDIT MIX  10%", 960, 890, "ink", False, 56)])]),
    # ---------------- 2
    dict(chapter="2. Pay on time, every time", text="Second. The biggest ingredient, about thirty-five percent, is payment history. Did you pay what you owed, when you owed it? Lenders found that your track record is the best predictor of your future. Which is also true of literally every group project you've ever been in.",
         scenes=[R([num(2), ch("maya", "explaining", 560), em("📅", 1320, 460, 220, "green", "ON TIME = 35%")]),
                 dict(bg="cafe", els=[ch("jordan", "tired", 560, flip=True), em("📚", 1320, 460, 220, None, "GROUP PROJECT")])]),
    dict(text="Here's the good news. Being a day or two late usually doesn't show up on your report. Lenders generally report a payment as late once it's thirty days past due. You'll probably still owe a late fee, but your score isn't ruined because you forgot over a weekend.",
         scenes=[dict(bg="plain", els=[tagel("1 DAY LATE: A FEE", 960, 340, "amber", False, 70), tagel("30 DAYS LATE: ON YOUR REPORT", 960, 600, "red", True, 64)])]),
    dict(text="The bad news. Once a thirty-day late payment lands on your report, it can stay there for up to seven years. It hurts most when it's new, and fades with time. But seven years is a long time to carry around one forgotten bill. It's like a bad screenshot in the group chat. It never fully goes away.",
         scenes=[R([ch("jordan", "concernedFear", 560, flip=True), em("📸", 1320, 460, 220, "red", "UP TO 7 YEARS")]),
                 dict(bg="board", bgargs=dict(text="NEW = HURTS MOST, THEN FADES"), els=[])]),
    dict(text="So the single best move in all of credit is boring. Turn on autopay. At least for the minimum payment, so you're never thirty days late by accident. Better yet, for the full statement balance, which we'll get to. Set it once, and your future self never has to remember.",
         scenes=[R([ch("maya", "calm", 560), em("🔁", 1320, 460, 220, "green", "AUTOPAY: ON")], bgargs=dict(extra="couch"))]),
    # ---------------- 3
    dict(chapter="3. Use a little, not a lot", text="Third. About thirty percent is amounts owed. For credit cards, the big piece is something called utilization. It's a fancy word for a simple fraction. How much of your credit limit are you using?",
         scenes=[dict(bg="board", bgargs=dict(text="BALANCE ÷ LIMIT"), els=[num(3)])]),
    dict(text="Jordan's card has a five-hundred-dollar limit. He buys concert tickets for four hundred. When his statement comes out, it shows a four-hundred-dollar balance. Four hundred divided by five hundred is eighty percent. To a scoring model, eighty percent looks like someone who is running out of room.",
         scenes=[R([ch("jordan", "smileBig", 560, flip=True), em("🎟️", 1320, 460, 220, None, "$400 TICKETS")]),
                 dict(bg="plain", els=[tagel(f"$400 ÷ $500 = {UTIL_BAD:.0%}", 960, 420, "red", True, 90)])]),
    dict(text="Here's the twist. Jordan pays the whole four hundred off right after the statement arrives. No interest. Totally responsible. But the card company already reported the eighty percent balance to the bureaus. The score sees the snapshot, not the happy ending.",
         scenes=[R([ch("jordan", "rage", 560, flip=True), em("📸", 1320, 460, 220, "red", "SNAPSHOT: 80%")]),
                 dict(bg="board", bgargs=dict(text="SNAPSHOT, NOT HAPPY ENDING"), els=[])]),
    dict(text="The fix is easy. Use a small slice of your limit, or pay most of it before the statement date, so the reported number is low. A common rule of thumb is to stay under thirty percent, and people with the highest scores tend to use well under ten. Fifty dollars on a five-hundred-dollar limit is ten percent.",
         scenes=[dict(bg="plain", els=[tagel("UNDER 30%: GOOD", 960, 300, "green", False, 70), tagel(f"UNDER 10%: GREAT  ($50 / $500)", 960, 560, "green", True, 64)]),
                 R([ch("maya", "smile", 560), em("📆", 1320, 460, 220, "green", "PAY BEFORE STATEMENT")])]),
    dict(text="And a nice detail. In most common scores, utilization has no long memory. Pay the balance down, wait for the next report, and that part of your score can bounce back in about a month. A late payment sticks around for years. A high balance is more like a bad hair day.",
         scenes=[R([ch("jordan", "smileLOL", 560, flip=True), em("💇", 1320, 460, 220, "green", "BOUNCES BACK")])]),
    # ---------------- 4
    dict(chapter="4. Time is an ingredient", text="Fourth. About fifteen percent is the length of your credit history. How old is your oldest account, and how old are your accounts on average? This is the one ingredient you can't rush. You can't speedrun time.",
         scenes=[dict(bg="plain", els=[num(4), em("⏳", 960, 440, 320, "green"), big("YOU CAN'T SPEEDRUN TIME", y=860, size=100)])]),
    dict(text="Which is exactly why starting at eighteen or nineteen is such an unfair advantage. A card Maya opens at nineteen is ten years old when she's twenty-nine. That's the same idea as compound interest from episode one. The clock does the work, if you start it.",
         scenes=[R([ch("maya", "driven", 560), tagel("OPENED AT 19", 1300, 330, "green", False, 60), tagel("10 YEARS OLD AT 29", 1300, 520, "green", True, 60)])]),
    dict(text="Two classic mistakes here. Mistake one: closing your oldest card because you don't use it. If it has no yearly fee, it's often better to keep it open with one tiny charge every few months. Closing it can shrink your available credit, which pushes up your utilization, and over time it can shorten your history.",
         scenes=[R([ch("jordan", "cheeky", 560, flip=True), em("✂️", 1320, 460, 220, "red", "CUTTING THE OLDEST")]),
                 dict(bg="plain", els=[tagel("NO FEE? KEEP IT OPEN", 960, 360, "green", True, 70), tagel("ONE TINY CHARGE NOW + THEN", 960, 600, "ink", False, 60)])]),
    dict(text="Mistake two: opening a bunch of new accounts at once. If Jordan has one card that's two years old, and opens a new one, his average age drops from twenty-four months to twelve. Instantly. Which brings us to the next ingredient.",
         scenes=[dict(bg="plain", els=[tagel("1 CARD: 24 MONTHS", 960, 300, "green", False, 64), em("⬇️", 960, 480, 110), tagel("2 CARDS: AVERAGE 12 MONTHS", 960, 680, "red", True, 64)])]),
    # ---------------- 5
    dict(chapter="5. New credit and the mix", text="Fifth. The last two ingredients, about ten percent each. New credit is about how many accounts you've opened lately, and how many times you've applied. When you apply for a card or a loan, the lender pulls your report. That's called a hard inquiry.",
         scenes=[dict(bg="office", els=[num(5), ch("jordan", "serious", 560, flip=True), em("🔍", 1320, 460, 220, "amber", "HARD INQUIRY")])]),
    dict(text="A hard inquiry usually knocks a few points off, it stays on your report for about two years, and FICO only counts it for one. Not a disaster. But ten applications in a month looks like someone who suddenly needs a lot of money. It's the credit version of texting someone eleven times in a row.",
         scenes=[dict(bg="plain", els=[tagel("A FEW POINTS", 560, 360, "amber", False, 64), tagel("FICO COUNTS 1 YEAR", 1360, 360, "amber", False, 60), big("DON'T APPLY FOR EVERYTHING", y=720, size=96)]),
                 R([ch("jordan", "concerned", 560, flip=True), em("📱", 1320, 460, 220, "red", "11 MESSAGES SENT")])]),
    dict(text="And the myth to kill. Checking your own score does not hurt it. When you look, that's a soft inquiry. Same for most preapproval offers in the mail. Check it as often as you want. It's like checking your own stats. It doesn't change the score.",
         scenes=[R([ch("maya", "smileBig", 560), em("👀", 1320, 460, 220, "green", "CHECKING YOURS: SAFE")], bgargs=dict(extra="couch"))]),
    dict(text="Credit mix is having different types of credit. Cards, which are revolving, and loans with fixed payments, like a car loan or student loan. It's only about ten percent, and it is never, ever a reason to take out a loan you don't need. Nobody should finance a car for the vibes of a better mix.",
         scenes=[dict(bg="plain", els=[em("💳", 560, 420, 200, None, "REVOLVING"), em("🚗", 1360, 420, 200, None, "INSTALLMENT")]),
                 dict(bg="outside", els=[ch("maya", "suspicious", 560), em("🚙", 1320, 640, 240, "red", "NOT FOR THE VIBES")])]),
    # ---------------- 6
    dict(chapter="6. Start from zero without debt", text="Sixth. Back to Maya, who has no score at all. She's not alone. In the government's consumer bureau estimate, about seven million American adults had no credit record at all, and about one in ten more had a record too thin to score.",
         scenes=[R([num(6), ch("maya", "concerned", 560), em("👻", 1320, 460, 220, None, "CREDIT INVISIBLE")]),
                 dict(bg="plain", els=[tagel("~7 MILLION: NO RECORD", 960, 360, "ink", False, 66), tagel("~1 IN 10: TOO THIN", 960, 600, "amber", False, 66)])]),
    dict(text="To get a FICO score, you generally need at least one account that's been open six months or more, and something reported in the last six months. So the goal isn't to borrow. The goal is to have one account, used a tiny bit, paid on time, for six months. Credit is not the same thing as debt. Debt is what happens if you don't pay it off.",
         scenes=[dict(bg="board", bgargs=dict(text="1 ACCOUNT × 6 MONTHS"), els=[num(6)]),
                 dict(bg="plain", els=[tagel("CREDIT: A TOOL", 560, 420, "green", True, 70), tagel("DEBT: UNPAID TOOL", 1360, 420, "red", False, 70)])]),
    dict(text="Option one: a secured card. You give the bank a deposit, say two hundred dollars, and that becomes your limit. You put one small bill on it, like a twenty-dollar subscription, and set autopay for the full statement balance. That's ten percent utilization, zero interest, and a clean on-time payment every month.",
         scenes=[R([ch("maya", "driven", 560), em("🏦", 1320, 460, 220, "green", "DEPOSIT = $200 LIMIT")]),
                 dict(bg="plain", els=[tagel(f"$20 ÷ $200 = {UTIL_SEC:.0%}", 960, 300, "green", False, 74), tagel("AUTOPAY FULL BALANCE", 960, 520, "green", True, 66), tagel("INTEREST PAID: $0", 960, 740, "green", False, 66)])]),
    dict(text="Check two things first. That the card reports to all three bureaus, otherwise it's building nothing. And the fees. Some secured cards have no yearly fee, some charge one. Many let you graduate to a regular card later and get your deposit back.",
         scenes=[R([ch("maya", "suspicious", 560), tagel("REPORTS TO ALL 3?", 1300, 330, "amber", False, 60), tagel("YEARLY FEE?", 1300, 520, "amber", False, 60)])]),
    dict(text="Option two: become an authorized user. A parent or someone you trust adds you to their card, and its history can show up on your report. This only helps if they pay on time and keep the balance low. If they miss payments, their mistake can land on your report too. Choose your teammate carefully.",
         scenes=[R([ch("maya", "smile", 560), em("💳", 1150, 420, 170), em("🤝", 1550, 420, 170), tagel("AUTHORIZED USER", 1350, 680, "green", True, 56)]),
                 R([ch("jordan", "concerned", 560, flip=True), em("⚠️", 1320, 460, 220, "red", "THEIR LATE = YOURS")])]),
    dict(text="Option three: other routes that can help. A student card with a low limit. A credit-builder loan from a bank or credit union, where you pay into a locked savings account and get the money at the end. That one is technically a loan, so read the interest and fees. And some services report your rent or phone bill, though not every score counts them.",
         scenes=[dict(bg="plain", els=[tagel("STUDENT CARD", 960, 220, "ink", False, 62), tagel("CREDIT-BUILDER LOAN", 960, 420, "amber", False, 62), tagel("RENT REPORTING", 960, 620, "ink", False, 62)]),
                 dict(bg="board", bgargs=dict(text="READ THE FEES FIRST"), els=[])]),
    # ---------------- 7
    dict(chapter="7. Read your reports for free", text="Seventh. Your credit report is the source code of your score, and you can read it for free. The official site is AnnualCreditReport.com. You can get a free report from each of the three bureaus every week. Not a lookalike site. That exact one.",
         scenes=[dict(bg="office", els=[num(7), ch("maya", "explaining", 560), em("💻", 1320, 460, 220, "green", "FREE, WEEKLY")]),
                 dict(bg="plain", els=[big("ANNUALCREDITREPORT.COM", y=420, color="green", size=110), tagel("THE OFFICIAL ONE", 960, 700, "green", True, 60)])]),
    dict(text="Look for things that aren't yours. An account you never opened. A late payment that wasn't late. A wrong address. Mistakes happen, and you have the right to dispute them with the bureau. It's free, and the bureau has to look into it.",
         scenes=[R([ch("maya", "suspicious", 560), em("🔍", 1320, 460, 220, "red", "NOT MINE?")]),
                 dict(bg="board", bgargs=dict(text="DISPUTE = FREE"), els=[])]),
    dict(text="And one more free power move. A credit freeze. Since twenty eighteen, federal law lets you freeze your report at each bureau for free. Then nobody can open new credit in your name, including scammers. You can unfreeze it when you apply for something. It's two-factor authentication for your identity.",
         scenes=[R([ch("jordan", "smileBig", 560, flip=True), em("🧊", 1320, 460, 220, "green", "FREEZE: FREE")]),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("🔐", 960, 420, 300, "green"), big("2FA FOR YOUR IDENTITY", y=840, color="green", size=100)])]),
    # ---------------- honesty check
    dict(chapter="Honesty check: why it matters in dollars", text="Honesty check. Does this number actually matter, or is it just a high score for nerds? Let's put a price on it with real average rates.",
         scenes=[dict(bg="board", bgargs=dict(text="WHAT'S A SCORE WORTH?"), els=[])]),
    dict(text="Say you finance a fifteen-thousand-dollar used car over five years. Credit bureau data from early twenty twenty-six put average used-car rates around eight point eight percent for borrowers with prime scores, and about nineteen point four percent for subprime.",
         scenes=[dict(bg="outside", els=[ch("jordan", "calm", 520, flip=True), em("🚗", 1300, 680, 260, None, "$15,000, 5 YEARS")]),
                 dict(bg="plain", els=[tagel("PRIME: ~8.8%", 560, 420, "green", True, 70), tagel("SUBPRIME: ~19.4%", 1360, 420, "red", True, 70)])]),
    dict(text=f"At prime, the payment is about three hundred and ten dollars a month, and the total interest is about three thousand, five hundred and eighty. At subprime, about three hundred and ninety-three a month, and about eight thousand, five hundred and fifty in interest. Same car. Same driver. About five thousand dollars apart.",
         scenes=[dict(bg="plain", els=[tagel(f"PRIME: ${PAY_P:,.0f}/MO", 560, 300, "green", False, 60), tagel(f"INTEREST ${INT_P:,.0f}", 560, 480, "green", True, 60),
                                       tagel(f"SUBPRIME: ${PAY_S:,.0f}/MO", 1360, 300, "red", False, 60), tagel(f"INTEREST ${INT_S:,.0f}", 1360, 480, "red", True, 60),
                                       big(f"GAP: ABOUT ${GAP:,.0f}", y=800, color="red", size=120)])]),
    dict(text="And that's one loan. Scores can also affect apartment applications, security deposits like Maya's, some insurance prices in many states, and much bigger loans later. Those rate tiers use one scoring model, and your real offer depends on the lender. But the direction is always the same.",
         scenes=[R([ch("maya", "serious", 560), tagel("APARTMENTS", 1300, 260, "ink", False, 54), tagel("DEPOSITS", 1300, 430, "ink", False, 54), tagel("BIG LOANS LATER", 1300, 600, "ink", False, 54)])]),
    dict(text="Now the other half of the honesty check. A credit score measures how you handle borrowing. Nothing else. It doesn't include your income, your savings, or your investments. Someone with an eight hundred score can be broke, and someone with no score can be doing great. It's a tool for borrowing. Not a scoreboard for your life.",
         scenes=[dict(bg="plain", els=[tagel("NOT IN YOUR SCORE:", 960, 200, "ink", False, 62), tagel("INCOME", 560, 440, "amber", False, 60), tagel("SAVINGS", 1360, 440, "amber", False, 60), big("A TOOL, NOT A SCOREBOARD", y=760, size=100)])]),
    # ---------------- the mistake
    dict(chapter="The myth: carrying a balance helps", text="Now the most expensive myth in this whole topic. Somebody, somewhere, will tell you to carry a small balance on your card, because it builds credit. It doesn't. The score sees that you used the card and paid on time. It does not give bonus points for paying interest.",
         scenes=[R([ch("jordan", "suspicious", 560, flip=True), em("🗣️", 1320, 460, 220, "red", "\"CARRY A BALANCE\"")]),
                 dict(bg="board", bgargs=dict(text="INTEREST ≠ BONUS POINTS"), els=[])]),
    dict(text="Say Jordan leaves that four hundred dollars on his card instead, at about twenty-two percent, the average rate on cards charging interest in the Federal Reserve's data. That's about seven dollars and thirty-eight cents in interest the first month. Leave it for a year and it's about ninety-eight dollars, paid for absolutely nothing.",
         scenes=[dict(bg="plain", els=[tagel(f"$400 × 22.15% ÷ 12 ≈ ${INT_MONTH:.2f}", 960, 360, "red", False, 66), tagel(f"1 YEAR ≈ ${INT_YEAR:.0f} FOR NOTHING", 960, 600, "red", True, 66)]),
                 R([ch("jordan", "rage", 560, flip=True), em("🔥", 1320, 460, 220, "red", "$98 IN FLAMES")])]),
    dict(text="So the rule is simple. Pay the full statement balance every month. Not the minimum. Not most of it. All of it. Card companies make their money from people who don't. Your job is to be their least profitable customer.",
         scenes=[dict(bg="plain", els=[em("😇", 960, 420, 300, "green"), big("BE THEIR LEAST PROFITABLE CUSTOMER", y=840, color="green", size=82)])]),
    dict(text="One more trap, and it's a big one. Co-signing. If a friend asks you to co-sign their loan or their lease, you're not vouching for them. You're promising to pay if they don't, and their late payments can show up on your report. Love your friends. Don't co-sign for them casually.",
         scenes=[dict(bg="hallway", els=[ch("maya", "concernedFear", 480), ch("jordan", "smileBig", 1440, flip=True), em("✍️", 960, 400, 180, "red", "CO-SIGN?")])]),
    # ---------------- close
    dict(chapter="Back to the deposit", text="Back to Maya's studio. She paid the three-hundred-dollar deposit. Annoying. Then she opened a secured card with a two-hundred-dollar deposit, put her twenty-dollar music subscription on it, and set autopay for the full balance.",
         scenes=[R([ch("maya", "tired", 560), em("🧾", 1320, 460, 220, "red", "$300 DEPOSIT, PAID")], bgargs=dict(night=True)),
                 R([ch("maya", "driven", 560), em("🎧", 1320, 460, 220, "green", "$20 ON AUTOPAY")], bgargs=dict(night=True))]),
    dict(text="Six months later, she has a score. A year later, it's a good one. She has paid exactly zero dollars in interest. She is still, technically, a person who has never owed anyone a dollar past the due date. The system just finally noticed.",
         scenes=[R([ch("maya", "smileLOL", 560, glow="green"), em("📈", 1320, 460, 220, "green", "SCORE: UNLOCKED")], bgargs=dict(extra="couch"))]),
    dict(text="Your one move this week. Pull your free credit reports from AnnualCreditReport.com and check them for anything that isn't yours. If you have a card, turn on autopay for the full statement balance. If you have nothing yet, look into one starter account, and read the fees. Credit isn't debt. It's a track record. Start the clock.",
         scenes=[R([em("✅", 560, 300, 130, "green"), tagel("PULL YOUR FREE REPORTS", 1100, 300, "green", False, 48), em("✅", 560, 480, 130, "green"), tagel("AUTOPAY FULL BALANCE", 1100, 480, "green", False, 48), em("✅", 560, 660, 130, "green"), tagel("ONE STARTER ACCOUNT", 1100, 660, "green", False, 48)], bgargs=dict(win=False))]),
    dict(text="Next time, the emergency fund. Why your first goal is a thousand dollars, then three months, and where that money should actually live. Subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("maya", "smileBig", 330), ch("jordan", "smile", 930, flip=True), em("📺", 1500, 400, 240, "green"), tagel("NEXT: EMERGENCY FUND", 1500, 700, "green", False, 48)], bgargs=dict(extra="couch", win=False))]),
]
