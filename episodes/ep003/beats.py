VOICE = ("af_heart", 0.75)
SAY = {"$": "", "FICA": "Fye-kah", "W-4": "W four", "401(k)": "four oh one K", "Y T D": "Y. T. D."}

CAST = {
    "maya": {"seed": "maya", "head": ["bun"], "skinColor": ["d08b5b"], "clothingColor": ["9ddadb"]},
    "jordan": {"seed": "jordan", "head": ["short3"], "skinColor": ["edb98a"], "clothingColor": ["ffcf77"]},
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


# ---- the example, all numbers computed here (2026 federal figures, single filer, one job)
RATE, HOURS, CHECKS = 18, 80, 26
GROSS = RATE * HOURS                                   # 1,440 per paycheck
YEAR = GROSS * CHECKS                                  # 37,440
STD_DED = 16100                                        # 2026 standard deduction, single (Rev. Proc. 2025-32)
TAXABLE = YEAR - STD_DED                               # 21,340
FED_YEAR = 0.10 * 12400 + 0.12 * (TAXABLE - 12400)     # 2,312.80
FED = FED_YEAR / CHECKS                                # 88.95
SS, MED, STATE = GROSS * 0.062, GROSS * 0.0145, GROSS * 0.03   # 89.28, 20.88, 43.20 (state is a made-up 3%)
NET = GROSS - FED - SS - MED - STATE                   # 1,197.69

R = lambda els, **k: dict(bg="room", els=els, **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="Payday, minus a surprise", text="Friday. Payday. Jordan just finished his first two weeks at a full-time job, stocking shelves at a grocery store. Eighteen dollars an hour, forty hours a week. He has done the math in his head roughly four hundred times.",
         scenes=[dict(bg="office", els=[ch("jordan", "driven", 600, flip=True), em("🛒", 1300, 560, 240, "green", "$18 / HOUR")]),
                 R([ch("jordan", "cheeky", 600, flip=True), tagel("$18 × 80 HRS = $1,440", 1320, 330, "green", True, 60)])]),
    dict(text="Eighteen times eighty hours is one thousand, four hundred and forty dollars. He has already spent it. Concert tickets. A new controller. Half of a gaming chair. The other half is a problem for future Jordan.",
         scenes=[R([ch("jordan", "smileBig", 560, flip=True), em("🎟️", 1150, 420, 170), em("🎮", 1550, 420, 170)], bgargs=dict(extra="couch")),
                 R([ch("jordan", "lovingGrin1", 560, flip=True), em("🪑", 1320, 500, 240, "red", "HALF A CHAIR")], bgargs=dict(extra="couch"))]),
    dict(text="Then the deposit hits his account. One thousand, one hundred and ninety-seven dollars and sixty-nine cents. Two hundred and forty-two dollars, just gone. He opens the pay stub. There's a name on it he's never heard of. FICA. And FICA took a hundred and ten dollars. Jordan would like to speak to FICA's manager.",
         scenes=[R([ch("jordan", "fear", 560, flip=True), em("📱", 1300, 460, 220, "red", "DEPOSIT: $1,197.69")]),
                 R([ch("jordan", "rage", 560, flip=True), em("🕵️", 1320, 460, 220, "red", "WHO IS FICA?")])]),
    dict(text="Maya has had a job for a year, and she's seen this movie before. She says the thing every first paycheck needs to hear. The number they offer you is not the number you get. Those are two different numbers, and almost nobody explains the gap.",
         scenes=[dict(bg="hallway", els=[ch("maya", "calm", 480), ch("jordan", "concerned", 1440, flip=True)]),
                 dict(bg="plain", els=[tagel("THE OFFER: $1,440", 560, 420, "green", False, 64), tagel("THE DEPOSIT: $1,198", 1360, 420, "red", True, 64), big("THE GAP NOBODY EXPLAINS", y=760, size=90)])]),
    dict(text="So that's this video. Where the money goes, what every line on your pay stub means, how one form decides how much gets taken, and why a giant tax refund is not the win it looks like.",
         scenes=[dict(bg="board", bgargs=dict(text="WHERE DID $242 GO?"), els=[])]),
    dict(text="Quick honesty note. Maya and Jordan are made up. Composites. The tax numbers are real twenty twenty-six federal figures, sourced in the description, and every calculation can be checked. But it's one simple example: a single person, one job, no other income, and a made-up three percent state tax. Your stub will look different. This channel is education, not financial advice, and definitely not tax advice. For your own situation, check the IRS or a tax professional.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 300), tagel("EXAMPLE: SINGLE, ONE JOB", 1240, 330, "green", True, 54), tagel("STATE TAX: MADE-UP 3%", 1240, 560, "amber", False, 54)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="Seven things to know about your first paycheck. Seven boxes to open. Some of them are even good news.",
         scenes=[dict(bg="board", bgargs=dict(text="7 THINGS"), els=[])]),
    # ---------------- 1
    dict(chapter="1. Gross pay vs net pay", text="First, two words. Gross pay is everything you earned before anything comes out. Net pay is what actually lands in your account. Gross is the menu price. Net is what's left after all the stuff you didn't know was on the bill.",
         scenes=[dict(bg="plain", els=[num(1), tagel("GROSS = WHAT YOU EARNED", 960, 380, "ink", False, 70), tagel("NET = WHAT YOU KEEP", 960, 620, "green", True, 70)]),
                 dict(bg="cafe", els=[ch("maya", "explaining", 560), em("🧾", 1300, 480, 240, "red", "SURPRISE ITEMS")])]),
    dict(text="Jordan's gross for two weeks, one thousand, four hundred and forty. His net, about one thousand, one hundred and ninety-eight. So he keeps about eighty-three cents of every dollar on the offer. In our example, about seventeen percent leaves before he ever sees it.",
         scenes=[dict(bg="plain", els=[tagel("GROSS $1,440", 560, 360, "ink", False, 70), em("➡️", 960, 360, 130), tagel("NET $1,198", 1360, 360, "green", True, 70), big("KEEPS ~83¢ OF EVERY $1", y=720, size=100)])]),
    dict(text="Over a full year, that's thirty-seven thousand, four hundred and forty dollars gross, and about thirty-one thousand, one hundred and forty net. A gap of about six thousand, three hundred dollars. That's not a rounding error. That's a used car.",
         scenes=[dict(bg="board", els=[dict(t="chart", box=(300, 110, 1640, 740), label="Paid so far this year (26 paychecks)", fmt="${v}",
                                            xlabels=["JAN", "APR", "JUL", "OCT", "DEC"],
                                            series=[{"name": "", "color": "amber", "ys": [GROSS * i for i in range(27)], "dy": -25},
                                                    {"name": "", "color": "green", "ys": [round(NET * i, 2) for i in range(27)], "dy": 25}]),
                                       tagel("GROSS", 560, 300, "amber", False, 44), tagel("NET", 560, 400, "green", False, 44)]),
                 dict(bg="outside", els=[ch("jordan", "awe", 520, flip=True), em("🚗", 1300, 680, 260, "red", "$6,300 A YEAR")])]),
    dict(text="And a sneaky one. Jordan gets paid every two weeks. That's twenty-six paychecks a year, not twenty-four. Most months have two paydays, but two months a year have three. Some people budget on two checks a month and treat those third checks like a side quest that pays.",
         scenes=[R([em("📅", 600, 460, 260), tagel("EVERY 2 WEEKS = 26 CHECKS", 1250, 400, "ink", False, 54)], bgargs=dict(extra="shelf")),
                 R([ch("maya", "smileBig", 560), em("🎁", 1300, 480, 220, "green", "2 MONTHS GET 3 CHECKS")])]),
    # ---------------- 2
    dict(chapter="2. Read your pay stub", text="Second. Open the pay stub. Every time, but especially the first one. It looks like a receipt from a store that hates you, but it's really just three sections. What you earned. What got taken out. And what's left.",
         scenes=[dict(bg="office", els=[num(2), ch("jordan", "suspicious", 600, flip=True), em("🧾", 1300, 480, 260, None, "THE PAY STUB")]),
                 dict(bg="board", bgargs=dict(text="EARNED · TAKEN · LEFT"), els=[num(2)])]),
    dict(text="Earned. Your hours, your rate, and your gross. Check these first. Eighty hours at eighteen dollars. If they paid you for seventy-two hours, or at seventeen dollars, that's a mistake, and payroll makes mistakes all the time. It's not personal. It's spreadsheets.",
         scenes=[dict(bg="plain", els=[tagel("80 HRS × $18 = $1,440", 960, 420, "green", True, 80)]),
                 R([ch("jordan", "suspicious", 560, flip=True), em("🔍", 1320, 460, 220, "green", "CHECK HOURS + RATE")])]),
    dict(text="Taken out. In Jordan's example, four lines. Federal income tax withholding, about eighty-nine dollars. Social Security, about eighty-nine dollars. Medicare, about twenty-one. And state income tax, about forty-three, in our made-up state. Total, about two hundred and forty-two dollars.",
         scenes=[dict(bg="plain", els=[tagel(f"FEDERAL TAX  ${FED:,.2f}", 960, 200, "red", False, 54), tagel(f"SOCIAL SECURITY  ${SS:,.2f}", 960, 350, "red", False, 54),
                                       tagel(f"MEDICARE  ${MED:,.2f}", 960, 500, "red", False, 54), tagel(f"STATE (3%)  ${STATE:,.2f}", 960, 650, "red", False, 54),
                                       tagel(f"TOTAL  ${GROSS - NET:,.2f}", 960, 860, "red", True, 70)])]),
    dict(text="Left. Your net pay, about one thousand, one hundred and ninety-eight. You'll also see a column called Y T D. Year to date. The running total since January. It's basically the stat screen for your whole year.",
         scenes=[dict(bg="plain", els=[tagel(f"NET PAY  ${NET:,.2f}", 960, 420, "green", True, 84)]),
                 dict(bg="office", els=[em("📊", 700, 460, 260, "green", "YTD = YEAR TO DATE"), em("🎮", 1400, 460, 200, None, "STAT SCREEN")])]),
    # ---------------- 3
    dict(chapter="3. Meet FICA", text="Third. The mystery guy. FICA isn't a person, which is disappointing, because Jordan had a whole speech ready. It stands for the Federal Insurance Contributions Act, and it's two taxes stapled together. Social Security and Medicare.",
         scenes=[R([num(3), ch("jordan", "rage", 560, flip=True), em("📜", 1320, 460, 220, None, "HIS SPEECH")]),
                 dict(bg="board", bgargs=dict(text="FICA = SOC. SECURITY + MEDICARE"), els=[num(3)])]),
    dict(text="Social Security is six point two percent of your pay. Medicare is one point four five percent. Together, seven point six five percent. On Jordan's fourteen-forty, that's about a hundred and ten dollars. And unlike income tax, there's no standard deduction here. It starts with your very first dollar.",
         scenes=[dict(bg="plain", els=[tagel("6.2% + 1.45% = 7.65%", 960, 340, "ink", False, 84), tagel(f"$1,440 × 7.65% = ${GROSS * 0.0765:,.2f}", 960, 600, "red", True, 72)]),
                 R([ch("jordan", "tired", 600, flip=True), em("1️⃣", 1300, 460, 200, "red", "FROM DOLLAR ONE")])]),
    dict(text="Here's the part almost nobody knows. Your employer pays a matching seven point six five percent on top, out of their own pocket. So Jordan costs the grocery store a bit more than his hourly wage. You never see that half, but it's there.",
         scenes=[dict(bg="office", els=[ch("jordan", "smile", 400, flip=True), ch("boss", "calm", 1520, flip=True), em("✉️", 960, 330, 130, "green"), tagel("EMPLOYER PAYS 7.65% TOO", 960, 140, "green", False, 56)])]),
    dict(text="So what does it buy? Social Security pays retirement, disability and survivor benefits. Medicare is health insurance, mostly for people sixty-five and older. You're paying into a system that's designed to pay you back decades from now. It's the longest preorder in history.",
         scenes=[dict(bg="outside", els=[ch("jordan_old", "smileBig", 560, flip=True), em("🏥", 1300, 520, 220, "green", "BENEFITS LATER")]),
                 dict(bg="plain", els=[em("📦", 960, 430, 300, "green"), big("THE LONGEST PREORDER EVER", y=820, size=90)])]),
    dict(text="A fun fact for much later. The Social Security part stops at a yearly cap. In twenty twenty-six, it only applies to the first one hundred and eighty-four thousand, five hundred dollars you earn. If that's your problem someday, congratulations. Medicare has no cap.",
         scenes=[dict(bg="plain", els=[tagel("SOCIAL SECURITY CAP: $184,500", 960, 360, "ink", False, 66), tagel("MEDICARE: NO CAP", 960, 600, "amber", False, 66)])]),
    # ---------------- 4
    dict(chapter="4. Withholding is a guess", text="Fourth. Federal income tax withholding. This is the line that confuses people most, because it isn't your tax. It's a guess at your tax. Your employer takes a little from each paycheck so that by spring, you've roughly paid your yearly bill.",
         scenes=[dict(bg="office", els=[num(4), em("🎯", 700, 460, 260), tagel("A GUESS, NOT THE BILL", 1300, 460, "amber", True, 60)])]),
    dict(text="Here's the actual bill for Jordan's example, using twenty twenty-six numbers. Yearly pay, thirty-seven thousand, four hundred and forty. First comes the standard deduction. The first sixteen thousand, one hundred dollars isn't taxed at all. That leaves twenty-one thousand, three hundred and forty dollars of taxable income.",
         scenes=[dict(bg="plain", els=[tagel(f"PAY  ${YEAR:,}", 960, 240, "ink", False, 66), tagel(f"− STANDARD DEDUCTION  ${STD_DED:,}", 960, 480, "green", True, 60), tagel(f"= TAXABLE  ${TAXABLE:,}", 960, 720, "amber", False, 66)])]),
    dict(text="Then the brackets. The first twelve thousand, four hundred of taxable income is taxed at ten percent. That's one thousand, two hundred and forty. Everything above that, up to fifty thousand, four hundred, is taxed at twelve percent. For Jordan, that's about one thousand and seventy-three more. Total, about two thousand, three hundred and thirteen dollars for the year.",
         scenes=[dict(bg="board", els=[tagel("FIRST $12,400 × 10% = $1,240", 960, 330, "ink", False, 56), tagel("NEXT $8,940 × 12% = $1,073", 960, 520, "ink", False, 56)]),
                 dict(bg="plain", els=[tagel(f"FEDERAL TAX ≈ ${FED_YEAR:,.0f} A YEAR", 960, 420, "red", True, 76)])]),
    dict(text="Spread across twenty-six paychecks, that's about eighty-nine dollars each. Which is the line on his stub. And as a share of his whole pay, it's only about six percent. Not twenty-two. Not thirty. Six.",
         scenes=[dict(bg="plain", els=[tagel(f"${FED_YEAR:,.0f} ÷ 26 ≈ ${FED:,.0f}", 960, 330, "ink", False, 80), big(f"~{FED_YEAR / YEAR * 100:.0f}% OF HIS PAY", y=650, color="green", size=130)])]),
    dict(text="That's also why the most famous money myth is wrong. A raise can't shrink your paycheck by bumping you into a higher bracket. Only the dollars above the line get the higher rate. Say Jordan gets a one dollar an hour raise. That's about two thousand and eighty more a year, and after taxes in our example, he keeps about one thousand, six hundred and nine of it. More money is more money. We'll do a whole episode on this one.",
         scenes=[dict(bg="plain", els=[em("🪜", 600, 460, 280), tagel("ONLY DOLLARS ABOVE", 1280, 380, "ink", False, 56), tagel("THE LINE PAY MORE", 1280, 520, "ink", False, 56)]),
                 R([ch("jordan", "smileBig", 560, flip=True), tagel("+$2,080 RAISE", 1300, 330, "green", False, 60), tagel("KEEPS ~$1,609", 1300, 520, "green", True, 60)])]),
    # ---------------- 5
    dict(chapter="5. The W-4 sets the guess", text="Fifth. How does your employer know what to guess? You tell them, on a form called the W-4. You fill it out on your first day, somewhere between the parking pass and the video about lifting boxes safely.",
         scenes=[dict(bg="office", els=[num(5), ch("jordan", "tired", 480, flip=True), ch("boss", "smile", 1440, flip=True), em("📝", 960, 380, 180, None, "W-4")])]),
    dict(text="The current W-4 has five steps. For someone like Jordan, single, one job, no kids, no side income, it's mostly step one, name and filing status, and step five, sign it. Steps two through four are for real situations. A second job, a working spouse, kids, or extra income.",
         scenes=[dict(bg="board", bgargs=dict(text="STEP 1 + STEP 5"), els=[num(5)]),
                 dict(bg="plain", els=[tagel("STEP 2: MORE THAN ONE JOB", 960, 260, "amber", False, 56), tagel("STEP 3: KIDS", 960, 440, "ink", False, 56), tagel("STEP 4: OTHER INCOME", 960, 620, "ink", False, 56)])]),
    dict(text="Step two matters more than people think. If you work two jobs at once, each employer withholds as if it's your only job. Each one gives you the whole standard deduction. Then in spring, you find out you only get one. That's how people with two part-time jobs end up owing money.",
         scenes=[R([em("☕", 500, 420, 200, None, "JOB 1"), em("🛒", 1420, 420, 200, None, "JOB 2")]),
                 R([ch("maya", "concerned", 560), em("🧾", 1320, 460, 220, "red", "ONLY ONE DEDUCTION")])]),
    dict(text="Then there's the trap box. Exempt. Some new workers write exempt because someone online said it means bigger paychecks. It does. Then the bill shows up in spring, sometimes with a penalty. Exempt is only for people who owed no federal income tax last year and expect to owe none this year. It's not a cheat code.",
         scenes=[R([ch("jordan", "cheeky", 560, flip=True), em("⚠️", 1320, 460, 220, "red", "\"EXEMPT\"")]),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("🎮", 960, 420, 300, "red"), big("NOT A CHEAT CODE", y=840, color="red", size=110)])]),
    dict(text="And you can change your W-4 any time. New job, second job, big life change. Just ask payroll for a new one. The IRS has a free online tool called the Tax Withholding Estimator that walks you through it.",
         scenes=[dict(bg="office", els=[em("🔁", 600, 460, 220, "green", "UPDATE IT ANYTIME"), em("💻", 1350, 460, 220, "green", "FREE IRS ESTIMATOR")])]),
    # ---------------- 6
    dict(chapter="6. A big refund isn't a bonus", text="Sixth. Every spring, people celebrate their tax refund like they won something. Through early May of twenty twenty-six, the average refund the IRS sent out was about three thousand, two hundred and seventy-six dollars.",
         scenes=[R([num(6), ch("jordan", "smileLOL", 560, flip=True), em("🎉", 1320, 460, 220, "green", "AVG REFUND ~$3,276")])]),
    dict(text="But a refund is your own money coming back. It means too much was withheld all year. You lent the government money at zero percent interest, then threw a party when they paid it back. Spread over a year of paychecks every two weeks, that average refund is about a hundred and twenty-six dollars per check.",
         scenes=[dict(bg="plain", els=[em("🏛️", 600, 440, 260), tagel("0% INTEREST LOAN", 1300, 440, "red", True, 64)]),
                 dict(bg="plain", els=[tagel("$3,276 ÷ 26 ≈ $126 A CHECK", 960, 420, "red", False, 76)])]),
    dict(text="Say Jordan's W-4 was off, and an extra fifty dollars came out of every paycheck. That's one thousand, three hundred dollars by spring. Nice surprise. But that same fifty a check could have built his emergency fund, or paid down a credit card charging over twenty percent.",
         scenes=[R([ch("jordan", "smile", 560, flip=True), tagel("+$50 A CHECK × 26 = $1,300", 1250, 330, "amber", False, 52)]),
                 R([em("🧯", 600, 460, 220, "green", "EMERGENCY FUND"), em("💳", 1320, 460, 220, "red", "20%+ CARD")], bgargs=dict(extra="shelf"))]),
    dict(text="To be fair, some people like a refund as forced savings, and that's a real choice. Owing a big bill is worse. The goal is somewhere near zero. A small refund or a small bill. Not a surprise either way.",
         scenes=[dict(bg="plain", els=[em("⚖️", 960, 440, 320, "green"), big("AIM CLOSE TO ZERO", y=840, color="green", size=100)])]),
    # ---------------- 7
    dict(chapter="7. Pre-tax money costs less", text="Seventh, and this one is good news. Some deductions come out before income tax is figured. A traditional 401(k) contribution is the classic one. Health insurance premiums through work often are too.",
         scenes=[dict(bg="office", els=[num(7), ch("maya", "smile", 560), em("🏦", 1300, 480, 220, "green", "PRE-TAX")])]),
    dict(text="Say Jordan puts fifty dollars a paycheck into his job's traditional 401(k). His take-home doesn't drop by fifty. In our example, it drops by about forty-two fifty. That fifty skips federal income tax at twelve percent, and in our made-up state, the three percent state tax too. Taxes chip in the other seven fifty.",
         scenes=[dict(bg="plain", els=[tagel("PUT IN $50", 560, 360, "ink", False, 70), em("➡️", 960, 360, 130), tagel("TAKE-HOME −$42.50", 1360, 360, "green", True, 64)]),
                 dict(bg="board", bgargs=dict(text="$50 × (12% + 3%) = $7.50"), els=[])]),
    dict(text="A few catches. That money still pays Social Security and Medicare. A handful of states do tax it. And it's for retirement, so taking it out early usually means taxes plus a penalty. But if the job offers a match, that's the free money from episode one. Read your plan's rules.",
         scenes=[R([ch("jordan", "serious", 560, flip=True), tagel("FICA STILL APPLIES", 1300, 330, "amber", False, 54), tagel("EARLY = TAX + PENALTY", 1300, 520, "red", False, 54)]),
                 dict(bg="office", els=[ch("boss", "smile", 1440, flip=True), em("✉️", 700, 440, 220, "green", "MATCH = FREE MONEY")])]),
    # ---------------- honesty check
    dict(chapter="Honesty check: what the example skips", text="Honesty check. Our example is clean on purpose. Real life isn't. State income taxes range from zero in some states to a lot more than three percent in others, and some cities add their own. We used a made-up three percent.",
         scenes=[dict(bg="plain", els=[em("🗺️", 600, 460, 280), tagel("STATE TAX: 0% TO MORE", 1300, 400, "amber", False, 56), tagel("SOME CITIES TOO", 1300, 560, "amber", False, 56)])]),
    dict(text="Withholding isn't perfect, either. Payroll uses IRS formulas that come close, but your real bill depends on your whole year. Start a job in June, or work a ton of overtime one month, and a single paycheck can look weird. The real math happens once, when you file.",
         scenes=[R([ch("maya", "suspicious", 560), em("📆", 1320, 460, 220, None, "REAL MATH: AT FILING")])]),
    dict(text="And the rules change. A recent law added new federal deductions for some tip income and some overtime pay, for twenty twenty-five through twenty twenty-eight. They have limits, they're claimed when you file, and they're income tax deductions, so Social Security and Medicare still apply. If you earn tips or overtime, look up the current rules.",
         scenes=[dict(bg="cafe", els=[ch("maya", "explaining", 560), em("💵", 1300, 460, 200, "green", "TIPS + OVERTIME")]),
                 dict(bg="board", bgargs=dict(text="2025 TO 2028, WITH LIMITS"), els=[])]),
    # ---------------- the mistake
    dict(chapter="The mistake: budgeting from gross", text="Now the most common first-paycheck mistake. Planning your life around the gross number. Jordan's offer works out to three thousand, one hundred and twenty dollars a month. His real take-home is about two thousand, five hundred and ninety-five a month.",
         scenes=[dict(bg="plain", els=[tagel("GROSS: $3,120 / MONTH", 960, 340, "ink", False, 70), tagel(f"NET: ${NET * 26 / 12:,.0f} / MONTH", 960, 580, "green", True, 70)])]),
    dict(text="That's about five hundred and twenty-five dollars a month that never existed. If he signs a lease or a phone plan based on the bigger number, he's spending money that went to taxes before it ever reached him. Budget from net. Always. The deposit is the real number.",
         scenes=[R([ch("jordan", "concernedFear", 560, flip=True), em("👻", 1320, 460, 220, "red", "$525 / MONTH GHOST")]),
                 dict(bg="board", bgargs=dict(text="BUDGET FROM NET"), els=[])]),
    dict(text="In our example, take-home was about eighty-three percent of gross. Yours depends on your state, your W-4, and what you choose to put in before tax. So don't guess. Get the real number from your first stub, and build your plan on that.",
         scenes=[R([ch("maya", "serious", 560), em("🧾", 1320, 460, 220, "green", "USE THE REAL NUMBER")], bgargs=dict(extra="shelf"))]),
    # ---------------- close
    dict(chapter="Back to payday", text="Back to Friday. The concert tickets are bought. The controller is still in his cart. The gaming chair is on hold. Jordan has a new number in his notes app. One thousand, one hundred and ninety-eight. Less fun. Way more real.",
         scenes=[R([ch("jordan", "calm", 560, flip=True), em("📝", 1320, 460, 220, "green", "REAL NUMBER: $1,198")], bgargs=dict(extra="couch", night=True))]),
    dict(text="And FICA? Turns out he's not a thief. He's a very slow preorder for future Jordan. Jordan has decided to forgive him. FICA did not ask.",
         scenes=[R([ch("jordan", "eyesClosed", 560, flip=True), em("🤝", 1320, 460, 220, "green", "FORGIVEN")], bgargs=dict(extra="couch", night=True))]),
    dict(text="Your one move this week. Find your latest pay stub, or your first one when it comes. Check the hours and the rate. Find the four tax lines. Look at your W-4 if anything has changed. And write down your real take-home number. That's the number your whole budget is built on.",
         scenes=[R([em("✅", 560, 300, 130, "green"), tagel("CHECK HOURS + RATE", 1100, 300, "green", False, 48), em("✅", 560, 480, 130, "green"), tagel("FIND THE 4 TAX LINES", 1100, 480, "green", False, 48), em("✅", 560, 660, 130, "green"), tagel("WRITE DOWN YOUR NET", 1100, 660, "green", False, 48)], bgargs=dict(win=False))]),
    dict(text="Next time, we're decoding credit scores. The five things that make up the number, and how to build one from zero without going into debt. Subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("maya", "smileBig", 330), ch("jordan", "smile", 930, flip=True), em("📺", 1580, 420, 280, "green", "NEXT: CREDIT SCORES")], bgargs=dict(extra="couch", win=False))]),
]
