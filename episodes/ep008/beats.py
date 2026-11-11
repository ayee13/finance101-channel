VOICE = ("af_heart", 0.75)
SAY = {"$": "", "FAFSA": "faff-suh", "Mario Kart": "Mario Kart"}

CAST = {
    "theo": {"seed": "theo", "head": ["afro"], "skinColor": ["694d3d"], "clothingColor": ["f9a8d4"]},
    "ava": {"seed": "ava", "head": ["longCurly"], "skinColor": ["ae5d29"], "clothingColor": ["a7f3d0"]},
    "aid": {"seed": "aid", "head": ["mediumStraight"], "skinColor": ["edb98a"], "clothingColor": ["c4b5fd"], "accessories": ["glasses"]},
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


# ---- the example, every number computed here
RATE = 0.0652                          # 2026-27 undergrad Direct Loan rate, assumed for all four years
FEE = 0.01057                          # Direct Loan fee, loans first disbursed Oct 1 2026 - Sep 30 2027
SUB = [3500, 4500, 5500, 5500]         # dependent undergrad subsidized maximums, years 1-4
UNSUB = [2000, 2000, 2000, 2000]       # the rest of the $5,500 / $6,500 / $7,500 / $7,500 annual limits
YRS = [4.5, 3.5, 2.5, 1.5]             # years from each fall disbursement to the end of the 6-month grace period


def pmt(p, r, n):
    i = r / 12
    return p * i / (1 - (1 + i) ** -n)


THEO_BORROW = sum(SUB) + sum(UNSUB)                            # $27,000
THEO_INT = sum(u * RATE * y for u, y in zip(UNSUB, YRS))       # $1,564.80 of unpaid interest added
THEO_BAL = THEO_BORROW + THEO_INT                              # $28,564.80 -> over $25,000, so 15-year tier
THEO_PMT = pmt(THEO_BAL, RATE, 180)                            # $249.14 a month
THEO_TOTAL = THEO_PMT * 180                                    # $44,845.96
AVA_BORROW = sum(SUB) + 4 * 1000                               # $23,000 ($1,000 a year in scholarships)
AVA_INT_PAID = sum(1000 * RATE * y for y in YRS)               # $782.40 paid while in school
AVA_PMT = pmt(AVA_BORROW, RATE, 120)                           # $261.39 a month, 10-year tier
AVA_TOTAL = AVA_PMT * 120 + AVA_INT_PAID                       # $32,149.74
GAP = THEO_TOTAL - AVA_TOTAL                                   # $12,696.23
PER_1K = pmt(1000, RATE, 120)                                  # $11.36 a month per $1,000, 10 years
FEE_5500 = 5500 * FEE                                          # $58.13
ONE_5500 = 5500 * RATE * 4.5                                   # $1,613.70 on a first-year $5,500 unsubsidized loan
PRIV = pmt(27000, 0.12, 120)                                   # $387.37 a month at an example 12%
assert round(THEO_TOTAL) == 44846 and round(AVA_TOTAL) == 32150 and round(GAP) == 12696

R = lambda els, **k: dict(bg="room", els=els, **k)
K = lambda els, **k: dict(bg="room", els=els, bgargs=dict(extra="shelf"), **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="Four minutes in August", text="August. A kitchen table. Theo is eighteen, starts college in three weeks, and has a laptop open to his financial aid page. There's a big green button that says accept all. He reads none of it. He clicks it. Total time, four minutes. Faster than a Netflix intro you forgot to skip.",
         scenes=[R([ch("theo", "smileBig", 560), em("💻", 1300, 520, 240, "green", "ACCEPT ALL")]),
                 R([ch("theo", "eyesClosed", 560), em("⏱️", 1300, 500, 220, None, "4 MINUTES")])]),
    dict(text="Across town, Ava is at the same kind of table, for the same school, the same major, the same loans on offer. She takes about two hours. She has a notepad. She has questions. Her little brother asks if she's okay.",
         scenes=[K([ch("ava", "suspicious", 560), em("🗒️", 1300, 520, 220, "green", "2 HOURS. QUESTIONS.")]),
                 K([ch("ava", "explaining", 560), em("🧐", 1300, 480, 200, None, "\"ARE YOU OKAY?\"")])]),
    dict(text="Fast forward. Both graduate. Both start repaying at the same federal rate. And here's the weird part. Theo's monthly payment is smaller than Ava's. About two hundred and forty-nine dollars a month for Theo. About two hundred and sixty-one for Ava.",
         scenes=[dict(bg="plain", els=[ch("theo", "smile", 420), ch("ava", "calm", 1500, flip=True), tagel("THEO: $249 / MONTH", 420, 230, "green"), tagel("AVA: $261 / MONTH", 1500, 230, "amber")])]),
    dict(text="So Theo wins, right? Not even close. By the time they're done, Theo will have paid back about forty-four thousand, eight hundred dollars. Ava, about thirty-two thousand, one hundred. Same school. Same rate. A gap of almost twelve thousand, seven hundred dollars. And most of it was decided at a kitchen table, years before either of them saw a bill.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("Theo pays back", round(THEO_TOTAL), "red"), ("Ava pays back", round(AVA_TOTAL), "green")])]),
                 dict(bg="board", bgargs=dict(text="GAP: ~$12,700"), els=[])]),
    dict(text="Quick honesty note before we go on. Theo and Ava are made up. Composites. The rules and the math are real, and every number is shown, but it's an example, not your situation. And this channel is education, not financial advice. Your school, your aid offer and your family's money are all different, so use this as a way to read your own paperwork, not as a plan.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 320), tagel("EXAMPLE, NOT YOUR PLAN", 560, 700, "green", True)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="Student loans are weird. They're the only big loan most people sign at eighteen, with no income, and with no idea what the monthly payment will be. Nobody would buy a car that way. So, seven things to understand before you sign. Ava found all of them. Theo found them later, which is the expensive way.",
         scenes=[R([ch("theo", "concerned", 560), em("🚗", 1300, 560, 240, "red", "NO ONE BUYS A CAR LIKE THIS")]),
                 dict(bg="board", bgargs=dict(text="7 THINGS BEFORE YOU SIGN"), els=[])]),
    # ---------------- 1
    dict(chapter="1. Free money first", text="Number one. Loans are the last money in, not the first. Before you borrow a dollar, you go after the money you never pay back. Grants, which are need-based aid. Scholarships. Work-study. And the door to most of it is one form, the FAFSA.",
         scenes=[dict(bg="office", els=[num(1), em("🎁", 700, 470, 240, "green", "GRANTS"), em("🏅", 1250, 470, 220, "green", "SCHOLARSHIPS")]),
                 dict(bg="board", bgargs=dict(text="FREE MONEY → THEN LOANS"), els=[num(1)])]),
    dict(text="If you're starting school next fall, the FAFSA for that year is already open. It went live in late September this year, the earliest launch ever. Some state and school aid runs out, so earlier is usually better. And yes, you need it even for most federal loans, so skipping it doesn't skip the loans, it just skips the free stuff.",
         scenes=[dict(bg="room", els=[em("📢", 960, 450, 300, "green", "2027-28 FAFSA: OPEN NOW")]),
                 R([ch("ava", "driven", 560), em("📝", 1300, 520, 220, "green", "FILED EARLY")])]),
    dict(text="Ava filed early and applied for small local scholarships. Boring ones. A credit union essay. A community award nobody else bothered with. They added up to a thousand dollars a year. Theo didn't apply for anything, because he assumed scholarships are only for genius kids and athletes. They are also, it turns out, for people who fill out the form.",
         scenes=[K([ch("ava", "smileLOL", 560), em("✉️", 1300, 500, 220, "green", "+$1,000 A YEAR")]),
                 R([ch("theo", "cheeky", 560), em("🏈", 1300, 520, 200, None, "\"ONLY FOR ATHLETES\"")])]),
    dict(text="Over four years, that's four thousand dollars Ava never has to borrow. Which, as we'll see, is worth a lot more than four thousand dollars.",
         scenes=[dict(bg="plain", els=[tagel("$1,000 x 4 YEARS", 960, 380, "green", False, 80), tagel("= $4,000 NOT BORROWED", 960, 600, "green", True, 80)])]),
    # ---------------- 2
    dict(chapter="2. Subsidized vs unsubsidized", text="Number two. Read the names on your aid offer, because two loans with almost the same name behave very differently. Federal Direct Subsidized, and Federal Direct Unsubsidized. One extra syllable. Big difference.",
         scenes=[dict(bg="office", els=[num(2), tagel("SUBSIDIZED", 560, 620, "green", True, 64), tagel("UNSUBSIDIZED", 1360, 620, "red", True, 64)])]),
    dict(text="Subsidized means the government pays the interest while you're in school at least half time, and for six months after you leave. Your balance just sits there. It's based on financial need, and it has lower limits. For a dependent student, up to three thousand, five hundred the first year, then four thousand, five hundred, then five thousand, five hundred.",
         scenes=[K([ch("ava", "calm", 560), em("🛡️", 1300, 480, 220, "green", "INTEREST PAID FOR YOU")]),
                 dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("Year 1", 3500, "green"), ("Year 2", 4500, "green"), ("Years 3-4", 5500, "green")])])]),
    dict(text="Unsubsidized means nobody pays it for you. Interest starts on the day the money goes out, even while you're sitting in a lecture about something else entirely. The total federal limit for a dependent first-year student is five thousand, five hundred. Then six thousand, five hundred. Then seven thousand, five hundred. Up to thirty-one thousand total.",
         scenes=[R([ch("theo", "concernedFear", 560), em("⏲️", 1300, 500, 220, "red", "INTEREST: DAY ONE")]),
                 dict(bg="board", bgargs=dict(text="$5,500 / $6,500 / $7,500"), els=[])]),
    dict(text="In our example, Theo and Ava both qualify for the full subsidized amount. Theo takes the max every year: twenty-seven thousand over four years, eight thousand of it unsubsidized. Ava's scholarships replace a thousand a year of the unsubsidized part. So she borrows twenty-three thousand, and only four thousand of it builds interest while she's in school.",
         scenes=[dict(bg="plain", els=[ch("theo", "smile", 420), ch("ava", "calm", 1500, flip=True), tagel("THEO: $27,000", 420, 230, "red"), tagel("AVA: $23,000", 1500, 230, "green")]),
                 dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("Theo: unsubsidized", 8000, "red"), ("Ava: unsubsidized", 4000, "green")])])]),
    # ---------------- 3
    dict(chapter="3. The interest starts early", text="Number three. The part almost nobody explains. The federal rate for new undergraduate loans this school year is six point five two percent, fixed. We'll assume that rate all four years, which is a simplification, because the rate is reset every July for new loans.",
         scenes=[dict(bg="board", bgargs=dict(text="6.52% FIXED (2026-27)"), els=[num(3)]),
                 dict(bg="office", els=[em("📆", 960, 450, 280, None, "NEW RATE EVERY JULY")])]),
    dict(text="Take one unsubsidized loan of five thousand, five hundred dollars, the first-year max. Four years of school plus a six-month grace period is four and a half years of interest before your first payment. That's about one thousand, six hundred and fourteen dollars. Then, in most cases, that unpaid interest gets added to your balance. That's called capitalization. Now you owe about seven thousand, one hundred and fourteen, and you pay interest on the interest.",
         scenes=[dict(bg="plain", els=[tagel("$5,500 BORROWED", 560, 380, "ink", False, 66), em("➡️", 960, 380, 140), tagel("$7,114 OWED", 1360, 380, "red", True, 66)]),
                 dict(bg="board", bgargs=dict(text="INTEREST ON THE INTEREST"), els=[])]),
    dict(text="It's like a Mario Kart race where the blue shell launches before the race starts. You haven't even crossed the line, and you're already behind.",
         scenes=[dict(bg="outside", els=[ch("theo", "fear", 560), em("🏎️", 1300, 640, 220, None), em("🐚", 1400, 330, 180, "red", "BEFORE THE START")])]),
    dict(text="For Theo's eight thousand dollars of unsubsidized loans, the interest that piles up before repayment comes to about one thousand, five hundred and sixty-five dollars. He finds out about it when his first statement shows a balance bigger than what he borrowed.",
         scenes=[R([ch("theo", "awe", 560), em("🧾", 1300, 480, 240, "red", "OWES $28,565")], bgargs=dict(night=True))]),
    # ---------------- 4
    dict(chapter="4. Pay the interest while you're in school", text="Number four is Ava's quiet trick. You're allowed to pay the interest while you're still in school. You don't have to. But if you do, it never gets added to the balance.",
         scenes=[K([num(4), ch("ava", "driven", 560), em("📲", 1300, 500, 220, "green", "PAY THE INTEREST")])]),
    dict(text="Here's what that cost Ava. On her first thousand-dollar loan, the interest is about five dollars and forty-three cents a month. Each year adds another loan, so by senior year it's about twenty-one seventy-three a month. Over the whole four and a half years, about seven hundred and eighty-two dollars in total. That's a part-time shift or two a semester.",
         scenes=[dict(bg="plain", els=[dict(t="chart", series=[{"name": "Ava", "color": "green", "ys": [5.43, 10.87, 16.30, 21.73]}], xlabels=["YEAR 1", "YEAR 2", "YEAR 3", "YEAR 4"], label="Interest per month, 6.52%", fmt="${v}", box=(300, 140, 1640, 740))]),
                 dict(bg="cafe", els=[ch("ava", "smile", 560), em("☕", 1300, 520, 220, "green", "$782 OVER 4.5 YEARS")])]),
    dict(text="So when Ava graduates, she owes exactly what she borrowed. Twenty-three thousand dollars. Not a penny of interest on top. Even ten or twenty dollars a month toward the interest helps, if paying all of it isn't possible.",
         scenes=[K([ch("ava", "smileLOL", 560), tagel("OWES $23,000. FLAT.", 1300, 380, "green", True, 64)])]),
    # ---------------- 5
    dict(chapter="5. The fee and the real number", text="Number five. Federal student loans have a fee, taken out before the money even reaches your school. For loans first sent out between October of this year and the end of next September, it's one point zero five seven percent.",
         scenes=[dict(bg="office", els=[num(5), em("✂️", 960, 460, 260, "red", "FEE: 1.057%")])]),
    dict(text="On a five-thousand, five-hundred-dollar loan, that's about fifty-eight dollars. So about five thousand, four hundred and forty-two dollars shows up. But you owe the full five thousand, five hundred, plus interest. Small, but it's the kind of thing that's always in the paperwork and never in the brochure.",
         scenes=[dict(bg="plain", els=[tagel("YOU GET: $5,442", 960, 360, "amber", False, 76), tagel("YOU OWE: $5,500", 960, 580, "red", True, 76)])]),
    dict(text="Here's a shortcut worth remembering. At six point five two percent, every thousand dollars you borrow costs about eleven dollars and thirty-six cents a month for ten years. About thirteen hundred and sixty-four dollars back in total. So before you accept a loan, divide by a thousand and multiply by eleven. Now you know the monthly bill, roughly, before you sign.",
         scenes=[dict(bg="board", bgargs=dict(text="$1,000 ≈ $11.36 / MONTH"), els=[]),
                 K([ch("ava", "explaining", 560), em("🧮", 1300, 500, 220, "green", "÷ 1,000 x 11")])]),
    # ---------------- 6
    dict(chapter="6. Borrow less than you're offered", text="Number six. The amount on your aid offer is a maximum, not a recommendation. You can accept part of a loan. You can type in a smaller number. The big green accept all button is a menu with one item highlighted.",
         scenes=[R([num(6), ch("theo", "suspicious", 560), em("🍽️", 1300, 500, 220, None, "IT'S A MENU")])]),
    dict(text="One common guideline: try to keep your total student debt below what you expect to earn in your first year after school. It's a rough rule, not a law, and it depends hugely on your field. But it's a sanity check. If the loans would be bigger than the first salary, that's worth a conversation with the financial aid office before you sign.",
         scenes=[dict(bg="plain", els=[tagel("KEEP TOTAL DEBT", 960, 340, "amber", False, 70), tagel("UNDER 1ST-YEAR PAY", 960, 580, "green", True, 70)]),
                 dict(bg="office", els=[ch("ava", "explaining", 520), ch("aid", "smile", 1400, flip=True), em("💬", 960, 400, 180, "green")])]),
    dict(text="Also worth knowing: you can usually say yes to a loan in the fall and borrow less in the spring, or turn down future years. Every year is a new decision. You're not signing up for four years at once, even if it feels that way.",
         scenes=[dict(bg="board", bgargs=dict(text="EVERY YEAR = NEW DECISION"), els=[])]),
    # ---------------- 7
    dict(chapter="7. Know your payment before you sign", text="Number seven. And this is where Theo's smaller payment comes from. For federal loans first made on or after July first, twenty twenty-six, there are two repayment plans. A standard plan with fixed payments, and an income-based plan called the Repayment Assistance Plan.",
         scenes=[dict(bg="office", els=[num(7), tagel("STANDARD: FIXED", 560, 620, "ink", False, 60), tagel("RAP: INCOME-BASED", 1360, 620, "ink", False, 60)])]),
    dict(text="The new standard plan sets how long you pay by how much you owe when repayment starts. Under twenty-five thousand dollars, ten years. Twenty-five thousand up to fifty thousand, fifteen years. Bigger balances, twenty or twenty-five years.",
         scenes=[dict(bg="plain", els=[tagel("UNDER $25K: 10 YRS", 960, 260, "green", False, 66), tagel("$25K-$50K: 15 YRS", 960, 470, "amber", False, 66), tagel("BIGGER: 20-25 YRS", 960, 680, "red", False, 66)])]),
    dict(text="Theo owes about twenty-eight thousand, five hundred and sixty-five. That's over the line, so he gets fifteen years, at about two hundred and forty-nine a month. Ava owes twenty-three thousand. Under the line. Ten years, at about two hundred and sixty-one a month.",
         scenes=[dict(bg="plain", els=[ch("theo", "smile", 420), ch("ava", "calm", 1500, flip=True), tagel("$28,565 → 15 YEARS", 420, 230, "red"), tagel("$23,000 → 10 YEARS", 1500, 230, "green")])]),
    dict(text="A smaller payment, spread over five more years, means five more years of interest. Theo pays about forty-four thousand, eight hundred and forty-six in total. Ava pays about thirty-one thousand, three hundred and sixty-seven, plus the seven hundred and eighty-two she paid in school. About thirty-two thousand, one hundred and fifty. That's the twelve thousand, seven hundred dollar gap. Theo also makes his last payment at thirty-seven. Ava, at thirty-two.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("Theo: 15 years", round(THEO_TOTAL), "red"), ("Ava: 10 years", round(AVA_TOTAL), "green")])]),
                 R([ch("theo", "tired", 560), em("🎂", 1300, 500, 220, "red", "LAST PAYMENT AT 37")])]),
    dict(text="The lesson isn't that low payments are bad. Sometimes a lower payment is exactly what keeps you afloat. The lesson is to look at the total, not just the monthly number. The monthly number is the one designed to look friendly.",
         scenes=[dict(bg="board", bgargs=dict(text="READ THE TOTAL, NOT THE MONTHLY"), els=[])]),
    # ---------------- honesty check 1
    dict(chapter="Honesty check: private loans", text="Honesty check, part one. Private student loans. These come from banks and other lenders, not the government, and they're a different animal. Rates depend on your credit, which at eighteen usually means a parent co-signs. That makes them legally on the hook too.",
         scenes=[dict(bg="office", els=[em("🏦", 640, 460, 260), em("✍️", 1280, 460, 220, "red", "CO-SIGNER = ON THE HOOK")])]),
    dict(text="Advertised private rates this year ran from about two percent for borrowers with excellent credit to around eighteen percent at the high end, and some are variable, meaning they can rise later. At an example twelve percent, the same twenty-seven thousand over ten years costs about three hundred and eighty-seven dollars a month.",
         scenes=[dict(bg="plain", els=[tagel("PRIVATE: ~2% TO ~18%", 960, 330, "amber", False, 72), tagel("VARIABLE CAN RISE", 960, 560, "red", True, 72)]),
                 R([ch("theo", "concernedFear", 560), em("💳", 1300, 500, 220, "red", "$387 / MONTH AT 12%")])]),
    dict(text="Private loans also usually don't come with income-based plans, and many have fewer options if you lose a job. That's why the common order is free money first, federal loans second, and private loans only to fill a real gap after that.",
         scenes=[dict(bg="board", bgargs=dict(text="FREE → FEDERAL → PRIVATE"), els=[])]),
    # ---------------- honesty check 2
    dict(chapter="Honesty check: the catches", text="Honesty check, part two. The catches nobody puts on the brochure. First, student loans are very hard to get rid of in bankruptcy. For most people, they stay until they're paid. This is not a loan you can walk away from like a gym membership.",
         scenes=[dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("⛓️", 960, 440, 300, "red", "HARD TO ESCAPE")])]),
    dict(text="Second, the income-based plan is a real safety net. Under the Repayment Assistance Plan, the payment is based on your income, with a ten-dollar minimum. But a lower payment usually means a longer road, and the rules have changed a lot in the last few years. They could change again. Check studentaid dot gov for the current version, not a video, including this one.",
         scenes=[R([ch("ava", "serious", 560), em("🪂", 1300, 480, 220, "green", "SAFETY NET, NOT FREE")]),
                 dict(bg="office", els=[em("🔎", 960, 440, 260, None, "CHECK STUDENTAID.GOV")])]),
    dict(text="Third, Theo isn't stuck. Federal loans have no penalty for paying early. If he pays three hundred and twenty-five a month instead of two forty-nine, he's done in about ten years, and saves around six thousand dollars of interest. The plan sets the minimum, not the maximum.",
         scenes=[R([ch("theo", "driven", 560, glow="green"), em("🚀", 1300, 480, 220, "green", "PAY EARLY, NO PENALTY")])]),
    dict(text="And fourth, the biggest catch of all: a loan is only a good deal if the thing it pays for is. School can be a great investment. It can also be four years and twenty-seven thousand dollars toward something you didn't want. Picking a school and a path you'll actually finish matters more than any interest rate in this video.",
         scenes=[dict(bg="outside", els=[ch("ava", "solemn", 560), em("🎓", 1300, 480, 240, "green", "FINISH WHAT YOU START")])]),
    # ---------------- mistakes
    dict(chapter="Common mistakes", text="Three quick mistakes to avoid. One: treating a refund check as free money. If your loans are bigger than your bill, the extra comes back to you, and it's very tempting. It's still borrowed. Some students send it right back to pay down the loan.",
         scenes=[R([ch("theo", "lovingGrin1", 560), em("💸", 1300, 500, 220, "red", "REFUND = STILL A LOAN")])]),
    dict(text="Two: not knowing who your loan servicer is. That's the company that sends your bills. Find it in your account on studentaid dot gov, because a missed first bill can hurt your credit, and the bill shows up long after you've stopped thinking about it. Three: never paying anyone to apply for aid or fix your loans. The FAFSA is free. Federal repayment changes are free.",
         scenes=[dict(bg="office", els=[em("📬", 520, 460, 240, "green", "KNOW YOUR SERVICER"), em("🚫", 1400, 460, 240, "red", "NEVER PAY FOR FAFSA")])]),
    # ---------------- close
    dict(chapter="Back to the kitchen table", text="So, back to the kitchen table. Theo didn't do anything crazy. He clicked one button and skipped a few forms. That's it. That's the whole twelve thousand, seven hundred dollars.",
         scenes=[R([ch("theo", "concerned", 560), em("💻", 1300, 520, 220, "red", "ACCEPT ALL")], bgargs=dict(night=True))]),
    dict(text="And Ava isn't a math genius. She just asked three questions. What's free? What builds interest? And what's the total? The monthly payment tells you if you can afford it. The total tells you what it costs.",
         scenes=[K([ch("ava", "smileBig", 560, glow="green"), em("🗒️", 1300, 500, 220, "green", "3 QUESTIONS")])]),
    dict(text="Your move this week, if school is in your future. Open the FAFSA if you haven't. Find one small scholarship to apply for. And when an aid offer shows up, write down the total you'd owe, not just the monthly. Ten minutes of reading can be worth more than most part-time jobs.",
         scenes=[R([em("✅", 560, 300, 130, "green"), tagel("FILE THE FAFSA", 1100, 300, "green", False, 50), em("✅", 560, 480, 130, "green"), tagel("1 SCHOLARSHIP", 1100, 480, "green", False, 50), em("✅", 560, 660, 130, "green"), tagel("WRITE THE TOTAL", 1100, 660, "green", False, 50)], bgargs=dict(win=False))]),
    dict(text="Next time: the real cost of your first car. Depreciation, insurance, and the loan length trap that makes a car look cheap. Subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("ava", "smileBig", 240, h=560), ch("theo", "smile", 900, h=560, flip=True), em("📺", 1490, 420, 280, "green", "NEXT: YOUR FIRST CAR")], bgargs=dict(extra="couch", win=False))]),
]
