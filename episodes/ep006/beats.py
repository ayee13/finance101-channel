VOICE = ("af_heart", 0.75)
SAY = {"$": "", "401(k)": "four oh one K", "401(K)": "four oh one K", "IRAs": "I.R.A.s", "IRA": "I.R.A.", "IRS": "I.R.S.", "HR": "H.R."}

CAST = {
    "maya": {"seed": "maya", "head": ["bun"], "skinColor": ["d08b5b"], "clothingColor": ["9ddadb"]},
    "jordan": {"seed": "jordan", "head": ["short3"], "skinColor": ["edb98a"], "clothingColor": ["ffcf77"]},
    "jordan_old": {"seed": "jordan", "head": ["grayShort"], "skinColor": ["edb98a"], "clothingColor": ["ffcf77"], "accessories": ["glasses2"]},
    "hr": {"seed": "hr", "head": ["long"], "skinColor": ["ae5d29"], "clothingColor": ["8fa7df"], "accessories": ["glasses"]},
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


# ---- the examples, all numbers computed here (made-up people and pay, real 2026 tax rules)
def fv(pay, r, months, start=0.0):
    b = start
    for _ in range(months):
        b = b * (1 + r / 12) + pay
    return b


PAY = 18 * 40 * 52                    # Jordan: $18/hr full time = $37,440 a year (same job as ep003)
OWN = PAY * 0.06 / 12                 # 6% = $187.20 a month
MATCH = OWN * 0.5                     # 50% match up to 6% = $93.60 a month, $1,123.20 a year
STD = 16100                           # 2026 standard deduction, single (IRS Rev. Proc. 2025-32)
J_TAXABLE = PAY - STD                 # 21,340 -> top bracket 12% (10% to 12,400, 12% to 50,400)
TAKEHOME_DROP = OWN * 0.88            # ~$164.74 a month (federal income tax only, traditional side)
SKIP1 = fv(MATCH, .07, 12) * (1 + .07 / 12) ** 540   # one year of skipped match, 19->65: ~$26,800
MATCH_ALL = fv(MATCH, .07, 552)       # match only, 19->65: ~$381,800
MATCH_29 = fv(MATCH, .07, 432)        # match only, 29->65: ~$181,900
MAYA_PAY = 22000                      # Maya: taxable 5,900, all at 10%, federal income tax $590
MAYA_ROTH = fv(100, .07, 552)         # $100/mo Roth IRA 19->65: ~$407,900 (put in $55,200)
MAYA_FEE = fv(100, .06, 552)          # same after a 1% yearly fee: ~$293,800
F = (1 + .07 / 12) ** 552             # $1,000 grows ~24.8x in 46 years at 7% -> $24,795
# traditional, taxed 22% later: $19,340; Roth, taxed 12% now: $21,820; traditional at 12% later: $21,820; at 10%: $22,316
# 5% check: SKIP1 ~$10,900; MATCH_ALL ~$200,500; MAYA_ROTH ~$214,200

R = lambda els, **k: dict(bg="room", els=els, **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="The box Jordan skipped", text="Monday morning, a break room that smells like burnt coffee. Jordan has just hit ninety days at the grocery store. Same job, same eighteen dollars an hour. And today, HR hands him a folder that says \"Benefits Enrollment\" in a font that has never been fun.",
         scenes=[dict(bg="office", els=[ch("jordan", "tired", 520, flip=True), em("☕", 1250, 560, 180, None, "DAY 90")]),
                 dict(bg="office", els=[ch("jordan", "suspicious", 480, flip=True), ch("hr", "explaining", 1440), em("📁", 960, 400, 180, None, "BENEFITS")])]),
    dict(text="Page four. A box. \"Percent of pay you'd like to contribute to the 401(k).\" Jordan writes a zero. Retirement, he reasons, is a problem for a guy named Old Jordan. Old Jordan sounds like he has it handled.",
         scenes=[dict(bg="plain", els=[em("📝", 700, 450, 260), tagel("CONTRIBUTE: 0%", 1300, 450, "red", True, 72)]),
                 R([ch("jordan", "cheeky", 560, flip=True), em("👴", 1320, 480, 220, None, "OLD JORDAN'S PROBLEM")])]),
    dict(text="Across town, Maya fixes bikes part time, about twenty-two thousand a year. Her job has no retirement plan at all. No folder. No box. So on a Sunday night, she opened one herself, an account called a Roth IRA, and set up a hundred dollars a month.",
         scenes=[R([ch("maya", "driven", 560), em("🚲", 1320, 560, 240, None, "NO PLAN AT WORK")], bgargs=dict(extra="shelf")),
                 R([ch("maya", "smile", 560), em("💻", 1320, 480, 220, "green", "ROTH IRA: $100/MO")], bgargs=dict(night=True))]),
    dict(text="Here's the twist. Jordan's job was offering him free money. For every dollar he put in, up to six percent of his pay, the store would add fifty cents. That zero he wrote? It turned down about one thousand, one hundred and twenty-three dollars a year. For doing nothing.",
         scenes=[dict(bg="plain", els=[tagel("YOU PUT IN $1", 560, 400, "green", False, 66), tagel("THEY ADD $0.50", 1360, 400, "green", True, 66)]),
                 R([ch("jordan", "awe", 560, flip=True), em("🎁", 1320, 480, 220, "red", "-$1,123 A YEAR")])]),
    dict(text="One person had the better deal and skipped it. The other had no deal and built her own. So today: Roth IRA versus 401(k). What they are, tax now versus tax later, and the order a lot of people use to fill them.",
         scenes=[dict(bg="board", bgargs=dict(text="ROTH IRA VS 401(K)"), els=[])]),
    dict(text="Quick honesty note. Maya and Jordan are made up. Composites. Their pay and their accounts are examples, but the tax rules and limits are real, for twenty twenty-six. And this channel is education, not financial advice. It's how the accounts work, not a plan for your specific life.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 320), tagel("EXAMPLES, REAL RULES", 560, 700, "green", True)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="One more thing before we start. A retirement account is not a weird investment. It's a container. A backpack with tax rules sewn into it. What goes inside, like the index funds from episode two, is a separate choice. Seven moves. Let's open the backpack.",
         scenes=[dict(bg="plain", els=[em("🎒", 960, 440, 320, "green"), big("A CONTAINER, NOT AN INVESTMENT", y=860, size=80)]),
                 dict(bg="board", bgargs=dict(text="7 MOVES"), els=[])]),
    # ---------------- move 1
    dict(chapter="1. Never skip the match", text="Move one. If your job offers a match, that's the first thing to understand, before Roth, before anything. A match is your employer adding money when you add money. Fifty cents per dollar, up to six percent of pay, is a common setup. Yours might be different, so read the plan.",
         scenes=[dict(bg="office", els=[num(1), ch("hr", "explaining", 520), em("✉️", 1300, 460, 220, "green", "50% UP TO 6%")])]),
    dict(text="Jordan makes about thirty-seven thousand, four hundred and forty a year. Six percent of that is a hundred and eighty-seven dollars and twenty cents a month. Put that in, and the store adds ninety-three sixty. Every month. That's an instant fifty percent on your money, before any investing even happens. No game hands out bonus XP like that.",
         scenes=[dict(bg="plain", els=[tagel("JORDAN: $187.20 / MO", 960, 330, "green", False, 66), tagel("STORE ADDS: $93.60 / MO", 960, 560, "green", True, 66)]),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("⭐", 960, 420, 300, "green"), big("+50% BONUS XP", y=800, color="green", size=100)])]),
    dict(text="So what did that zero really cost? One year of skipped match is about eleven hundred dollars. Left invested from nineteen to sixty-five at an assumed seven percent a year, that one year grows to about twenty-six thousand, eight hundred. One year. One box.",
         scenes=[dict(bg="plain", els=[tagel("1 YEAR OF MATCH: $1,123", 960, 300, "red", False, 64), em("⬇️", 960, 490, 110), tagel("~$26,800 AT 65", 960, 690, "red", True, 64)]),
                 dict(bg="board", bgargs=dict(text="ASSUMED 7% A YEAR, NOT A PROMISE"), els=[])]),
    dict(text="And if he takes the match every month from nineteen to sixty-five, just the store's half, the money he never earned, grows to about three hundred and eighty-two thousand dollars, in future dollars. Wait until twenty-nine to start, and the store's half comes to about one eighty-two. Ten years of \"later\" costs about two hundred thousand dollars of free money.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(560, 120, 1760, 760), items=[("Match from 19", MATCH_ALL, "green"), ("Match from 29", MATCH_29, "red")]), ch("jordan", "concerned", 300, h=560, flip=True)]),
                 R([ch("jordan_old", "rage", 560, flip=True), em("🧾", 1320, 480, 220, "red", "LATER = -$200K")])]),
    dict(text="And here's the part that makes it easier. If Jordan puts his hundred and eighty-seven into the traditional side of the plan, it comes out before federal income tax. So his take-home pay doesn't drop by a hundred and eighty-seven. It drops by about a hundred and sixty-five. Taxes chip in the rest.",
         scenes=[R([ch("jordan", "smile", 560, flip=True), tagel("-$187 IN THE PLAN", 1320, 350, "green", False, 56), tagel("-$165 TAKE-HOME", 1320, 560, "green", True, 56)])]),
    # ---------------- move 2
    dict(chapter="2. Tax now or tax later", text="Move two. The big difference between these accounts isn't the name. It's when you pay tax. Traditional accounts, like a traditional 401(k), skip the tax now. You pay it later, when you take the money out in retirement.",
         scenes=[dict(bg="office", els=[num(2), em("⏰", 700, 460, 240, None, "TRADITIONAL"), tagel("TAX LATER", 1300, 460, "amber", True, 72)])]),
    dict(text="Roth accounts flip it. You pay the tax now, on money you've already been taxed on. Then, if you follow the rules, the money comes out tax-free in retirement. Including all the growth. Decades of growth, and the IRS doesn't get a slice.",
         scenes=[dict(bg="office", els=[em("🧾", 700, 460, 240, "green", "ROTH"), tagel("TAX NOW, NOT LATER", 1320, 460, "green", True, 64)]),
                 dict(bg="plain", els=[em("🍕", 960, 420, 300, "green"), big("THE GROWTH IS ALL YOURS", y=820, color="green", size=90)])]),
    dict(text="So which wins? Let's run one thousand dollars of pay through both. Seven percent a year, forty-six years, nineteen to sixty-five. Money at that rate grows about twenty-four point eight times. So one thousand dollars becomes about twenty-four thousand, eight hundred.",
         scenes=[dict(bg="board", bgargs=dict(text="$1,000 x 24.8 = $24,795"), els=[])]),
    dict(text="Traditional: the whole thousand goes in, grows to twenty-four eight, and then gets taxed when Jordan takes it out. Roth: Jordan pays his twelve percent first, so eight hundred and eighty goes in, and grows to about twenty-one thousand, eight hundred. Tax-free.",
         scenes=[dict(bg="plain", els=[tagel("TRADITIONAL: $1,000 IN", 560, 360, "amber", False, 54), tagel("→ $24,795, TAXED LATER", 560, 540, "amber", False, 54),
                                          tagel("ROTH: $880 IN", 1400, 360, "green", False, 54), tagel("→ $21,820, TAX-FREE", 1400, 540, "green", True, 54)])]),
    dict(text="Now the magic trick. If Jordan's tax rate in retirement is also twelve percent, the traditional account leaves him with exactly twenty-one thousand, eight hundred too. To the dollar. It's the same math in a different order. Like multiplying three times five or five times three.",
         scenes=[dict(bg="board", bgargs=dict(text="SAME RATE = SAME RESULT"), els=[]),
                 dict(bg="plain", els=[big("3 × 5 = 5 × 3", y=460, color="green", size=150)])]),
    dict(text="So the whole question comes down to one thing. Is your tax rate higher now, or later? If it's higher later, say twenty-two percent, the traditional one shrinks to about nineteen thousand, three hundred, and Roth wins by about twenty-five hundred. If it's lower later, say ten percent, traditional wins, at about twenty-two thousand, three hundred.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("Roth (12% now)", 21820, "green"), ("Trad, 22% later", 19340, "red"), ("Trad, 10% later", 22316, "amber")])])]),
    # ---------------- move 3
    dict(chapter="3. Why 19 is Roth season", text="Move three. That's why people your age hear \"Roth\" so often. At nineteen, your tax rate is probably about as low as it will ever be. Not because of a loophole. Because you're at the bottom of the income ladder, and the bottom rungs are taxed the least.",
         scenes=[dict(bg="outside", els=[num(3), ch("maya", "smileBig", 560), em("🪜", 1320, 480, 260, "green", "BOTTOM RUNGS")])]),
    dict(text="In twenty twenty-six, a single person's first sixteen thousand, one hundred dollars of income is covered by the standard deduction. No federal income tax on that part. After that, the next twelve thousand, four hundred is taxed at ten percent. Then twelve percent, up to fifty thousand, four hundred of taxable income.",
         scenes=[dict(bg="plain", els=[tagel("FIRST $16,100: 0%", 960, 260, "green", True, 64), tagel("NEXT $12,400: 10%", 960, 480, "green", False, 64), tagel("THEN 12%, THEN MORE", 960, 700, "amber", False, 64)])]),
    dict(text="Maya makes twenty-two thousand. Subtract the sixteen thousand one hundred, and only five thousand, nine hundred is taxable, all of it at ten percent. Her whole federal income tax bill for the year: about five hundred and ninety dollars. Her top rate is the lowest bracket there is.",
         scenes=[R([ch("maya", "explaining", 560), tagel("$22,000 - $16,100", 1320, 330, "ink", False, 56), tagel("= $5,900 AT 10%", 1320, 520, "green", True, 56)], bgargs=dict(extra="shelf"))]),
    dict(text="So for Maya, paying tax now is cheap. Ten cents on the dollar, and then the growth is hers forever. And if your income is below the standard deduction, like a summer job, you might owe zero federal income tax on it. Roth money then goes in with no income tax, and can come out with none. That's about as good as the rules get.",
         scenes=[R([ch("maya", "smileLOL", 560), em("🏷️", 1320, 480, 220, "green", "TAX ON SALE: 10%")]),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("🆓", 960, 420, 300, "green"), big("0% IN, 0% OUT", y=820, color="green", size=110)])]),
    dict(text="A hundred a month in Maya's Roth IRA from nineteen to sixty-five, at an assumed seven percent, comes to about four hundred and eight thousand. She'd put in fifty-five thousand, two hundred of it. Follow the rules, and none of that four hundred and eight is taxed on the way out.",
         scenes=[dict(bg="plain", els=[tagel("PUT IN: $55,200", 560, 420, "ink", False, 64), tagel("AT 65: ~$407,900", 1360, 420, "green", True, 64)]),
                 dict(bg="board", bgargs=dict(text="FUTURE DOLLARS, ASSUMED 7%"), els=[])]),
    # ---------------- move 4
    dict(chapter="4. Know the rules", text="Move four. The rules, in plain English. A 401(k) comes through a job. You can only get one if your employer offers it, and many smaller jobs don't. An IRA is an individual retirement account. You open it yourself, at a bank or brokerage, no employer needed.",
         scenes=[dict(bg="office", els=[num(4), em("🏢", 560, 460, 240, None, "401(K): VIA A JOB"), em("🙋", 1360, 460, 240, "green", "IRA: YOU OPEN IT")])]),
    dict(text="But there's a catch. To put money in an IRA, you need earned income. Pay from a job, tips, or self-employment. Birthday money doesn't count. And you can't put in more than you earned that year. Mowing lawns for two thousand dollars means two thousand is the cap.",
         scenes=[R([ch("jordan", "suspicious", 560, flip=True), em("🎂", 1320, 480, 220, "red", "BIRTHDAY CASH: NO")]),
                 dict(bg="outside", els=[ch("maya", "calm", 560), em("💼", 1320, 560, 220, "green", "PAY OR TIPS: YES")])]),
    dict(text="The limits for twenty twenty-six: up to seven thousand, five hundred a year across all your IRAs. Up to twenty-four thousand, five hundred of your own money in a 401(k). And you have until the tax deadline, April fifteenth, twenty twenty-seven, to make twenty twenty-six IRA contributions.",
         scenes=[dict(bg="plain", els=[tagel("IRA: $7,500 / YEAR", 960, 260, "green", False, 66), tagel("401(K): $24,500 / YEAR", 960, 480, "green", False, 66), tagel("2026 IRA: BY 4/15/27", 960, 700, "amber", True, 58)])]),
    dict(text="Those limits are way above what most nineteen-year-olds can save, and that's fine. Nobody is grading you against the max. Most of the limits also tend to go up every year or so with inflation. And Roth IRAs have an income cap, but it starts around a hundred and fifty-three thousand for a single person. Not a problem you have yet.",
         scenes=[R([ch("maya", "smileLOL", 560), em("📏", 1320, 480, 220, None, "THE MAX IS NOT THE GOAL")])]),
    dict(text="One more. Lots of 401(k) plans now have a Roth option too, called a Roth 401(k). Same tax-now idea, inside your work plan. Some plans still put the match on the traditional side, even if you pick Roth. Still free money. Just taxed later.",
         scenes=[dict(bg="office", els=[ch("hr", "smile", 520), em("🔀", 1300, 460, 220, "green", "ROTH 401(K)")])]),
    # ---------------- move 5
    dict(chapter="5. The Roth escape hatch", text="Move five. The question every nineteen-year-old asks: what if I need it before I'm old? Fair. Sixty-five is basically a different character.",
         scenes=[R([num(5), ch("jordan", "concernedFear", 560, flip=True), em("👴", 1320, 480, 220, None, "65 = NEW CHARACTER")])]),
    dict(text="Here's a rule that surprises people. With a Roth IRA, the money you put in, your contributions, can generally come back out at any time, with no tax and no penalty. After three years, Maya has put in three thousand, six hundred, and the account is worth about three thousand, nine hundred and ninety. She can take the thirty-six hundred back out.",
         scenes=[dict(bg="plain", els=[tagel("PUT IN: $3,600", 560, 420, "green", True, 64), tagel("GROWTH: ~$393", 1360, 420, "amber", False, 64)]),
                 R([ch("maya", "calm", 560), em("🚪", 1320, 480, 220, "green", "CONTRIBUTIONS: ANYTIME")])]),
    dict(text="The growth is different. Take the earnings out early, generally before fifty-nine and a half, or within five years of your first Roth contribution, and you can owe tax plus a ten percent penalty. There are exceptions, but the default is: contributions, flexible. Growth, locked.",
         scenes=[dict(bg="plain", els=[em("🔓", 600, 440, 240, "green", "CONTRIBUTIONS"), em("🔒", 1320, 440, 240, "red", "GROWTH: LOCKED")])]),
    dict(text="A 401(k) is stricter. Pull five thousand dollars out of a traditional one at twenty-two, and you'll generally owe a ten percent penalty, five hundred dollars, plus income tax. At a twelve percent rate, another six hundred. Five thousand out, about thirty-nine hundred in your pocket, before any state tax.",
         scenes=[R([ch("jordan", "fear", 560, flip=True), tagel("$5,000 OUT", 1320, 280, "ink", False, 56), tagel("-$500 PENALTY", 1320, 450, "red", False, 56), tagel("-$600 TAX = $3,900", 1320, 620, "red", True, 56)])]),
    dict(text="But don't treat the Roth escape hatch like a savings account. Every dollar you pull out loses its tax-free future, and you can't just put it back later beyond your yearly limit. That's what the emergency fund from last episode is for. The Roth is the backup to the backup.",
         scenes=[R([ch("maya", "serious", 560), em("🧯", 1320, 480, 220, "green", "EMERGENCY FUND FIRST")], bgargs=dict(extra="shelf"))]),
    # ---------------- move 6
    dict(chapter="6. Buy something inside it", text="Move six, and this is the mistake that catches a lot of people. Opening the account is not the same as investing. Money you move into an IRA often lands as cash, and just sits there, waiting for instructions.",
         scenes=[R([num(6), ch("jordan", "cheeky", 560, flip=True), em("🎒", 1320, 480, 220, "red", "BACKPACK, NO SNACKS")])]),
    dict(text="It's like buying a season pass and never riding anything. Maya's hundred a month earning a tiny cash rate for forty-six years is a very different story from the same money in a diversified investment. So log in and check. Is it invested, or is it just parked?",
         scenes=[dict(bg="outside", els=[ch("maya", "suspicious", 560), em("🎢", 1320, 460, 260, "red", "PASS, NO RIDES")]),
                 dict(bg="board", bgargs=dict(text="INVESTED OR JUST PARKED?"), els=[])]),
    dict(text="In a 401(k), the menu is set by the plan. Many plans have a target-date fund, which picks a mix for the year you'd retire and gets more careful over time. Or a total market index fund. The same idea as episode two: own a little of everything, keep costs low.",
         scenes=[dict(bg="office", els=[ch("hr", "explaining", 520), em("📋", 1300, 460, 220, "green", "THE PLAN MENU")]),
                 dict(bg="plain", els=[em("🧺", 960, 440, 300, "green"), big("A LITTLE OF EVERYTHING", y=820, color="green", size=96)])]),
    dict(text="And look at the yearly fee for anything you pick. Maya's hundred a month at seven percent becomes about four hundred and eight thousand. Knock one percent off for fees, and it's about two hundred and ninety-four. That one percent costs her roughly a hundred and fourteen thousand dollars.",
         scenes=[dict(bg="plain", els=[tagel("AT 7%: ~$407,900", 560, 420, "green", False, 62), tagel("AT 6%: ~$293,800", 1360, 420, "red", True, 62)]),
                 R([ch("maya", "rage", 560), em("👹", 1320, 480, 220, "red", "THE 1% TOOK $114K")])]),
    # ---------------- move 7
    dict(chapter="7. A common order to fill them", text="Move seven. So which one first? There's no single right answer, but a lot of people use an order like this one. Think of it as a checklist, not a law.",
         scenes=[dict(bg="board", bgargs=dict(text="A COMMON ORDER"), els=[num(7)])]),
    dict(text="Step one, a starter emergency fund, so surprises don't go on a card. Step two, put in enough to get the full employer match, if there is one. Step three, pay off high-interest debt, like a credit card at twenty-two percent. Step four, a Roth IRA. Step five, go back and add more to the 401(k).",
         scenes=[R([tagel("1. STARTER CASH CUSHION", 960, 200, "green", False, 50), tagel("2. GET THE FULL MATCH", 960, 340, "green", True, 50), tagel("3. KILL HIGH-RATE DEBT", 960, 480, "red", False, 50),
                    tagel("4. ROTH IRA", 960, 620, "green", False, 50), tagel("5. MORE 401(K)", 960, 760, "green", False, 50)], bgargs=dict(win=False))]),
    dict(text="Notice the match sits at step two, before even the debt. That's because a fifty percent instant return is hard to beat. And there's a newer one coming. Starting with contributions for twenty twenty-seven, a federal Saver's Match can add up to a thousand dollars a year for savers with lower incomes. It has its own rules, including that full-time students and dependents generally don't qualify, so check IRS dot gov.",
         scenes=[R([ch("jordan", "driven", 560, flip=True), em("🥈", 1320, 480, 220, "green", "MATCH = STEP 2")]),
                 dict(bg="office", els=[em("🏛️", 700, 460, 240, "green"), tagel("SAVER'S MATCH, 2027", 1300, 400, "green", True, 56), tagel("CHECK IF YOU QUALIFY", 1300, 600, "amber", False, 50)])]),
    # ---------------- honesty check
    dict(chapter="Honesty check: when Roth loses", text="Honesty check. Roth is not automatically better. It's a bet that your tax rate later will be at least as high as now. Sometimes that bet loses.",
         scenes=[dict(bg="board", bgargs=dict(text="THE CATCH"), els=[])]),
    dict(text="If you end up with a lower income in retirement, traditional can come out ahead, like the ten percent example. If you're already in a higher bracket, the tax break today may be worth more. And nobody knows what tax rates will be in forty years. Congress changes the rules. That's also why some people split it, some Roth, some traditional, so they're not betting everything on one guess.",
         scenes=[dict(bg="plain", els=[em("🔮", 560, 440, 260, None, "TAXES IN 40 YEARS?"), em("⚖️", 1380, 440, 260, "green", "SPLIT THE BET")])]),
    dict(text="Second catch: returns. We used seven percent. At five percent, Maya's Roth reaches about two hundred and fourteen thousand instead of four oh eight. Jordan's one skipped year of match costs about eleven thousand instead of twenty-seven. Smaller. Still not nothing. The direction holds. The exact numbers never come with a promise.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("Maya at 7%", MAYA_ROTH, "green"), ("Maya at 5%", fv(100, .05, 552), "amber")])]),
                 dict(bg="plain", els=[tagel("1 YEAR, AT 7%: $26.8K", 960, 360, "red", False, 60), tagel("1 YEAR, AT 5%: $10.9K", 960, 580, "red", True, 60)])]),
    dict(text="Third catch: vesting. Your own contributions are always yours. But the employer's match can come with a schedule, where you only keep all of it after a few years on the job. Leave after one year, and you might keep only part of the match, or none. Look up your plan's vesting schedule before you plan a dramatic exit.",
         scenes=[dict(bg="office", els=[ch("jordan", "concerned", 520, flip=True), em("⏳", 1300, 460, 220, "red", "VESTING SCHEDULE")])]),
    dict(text="And one more. These are future dollars. With prices rising, four hundred thousand at sixty-five won't buy what four hundred thousand buys today. Still way more than the zero in Jordan's box. Just the honest version.",
         scenes=[R([ch("maya", "solemn", 560), tagel("FUTURE DOLLARS", 1320, 420, "amber", True, 64)])]),
    # ---------------- close
    dict(chapter="Back to the break room", text="So, back to the break room. Jordan asked HR for a new form. He crossed out the zero and wrote a six. His take-home dropped about a hundred and sixty-five a month, and his account now grows by about two hundred and eighty dollars a month, counting the store's half.",
         scenes=[dict(bg="office", els=[ch("jordan", "driven", 480, flip=True, glow="green"), ch("hr", "smileBig", 1440), em("📝", 960, 400, 180, "green", "0% → 6%")])]),
    dict(text="Maya kept her hundred a month in the Roth, and finally clicked the button that actually invests it. She says it was the most boring thirty seconds of her year. Which, for money, is a compliment.",
         scenes=[R([ch("maya", "eyesClosed", 560), em("✅", 1320, 480, 220, "green", "ACTUALLY INVESTED")], bgargs=dict(extra="couch"))]),
    dict(text="Here's the one-line version. Take the free money first, and at nineteen, paying tax now is usually cheap.",
         scenes=[dict(bg="plain", els=[big("FREE MONEY FIRST", y=400, color="green", size=120), big("TAX IS CHEAP AT 19", y=600, size=100)])]),
    dict(text="Your move this week. Find out if your job has a retirement plan and a match, and what percent gets the full match. If there's no plan, look up how a Roth IRA works at a bank or brokerage. And if you already have an account, log in and check that the money is invested, not parked.",
         scenes=[R([em("✅", 560, 300, 130, "green"), tagel("ASK ABOUT A MATCH", 1100, 300, "green", False, 48), em("✅", 560, 480, 130, "green"), tagel("NO PLAN? LEARN ROTH IRA", 1100, 480, "green", False, 48), em("✅", 560, 660, 130, "green"), tagel("INVESTED, NOT PARKED", 1100, 660, "green", False, 48)], bgargs=dict(win=False))]),
    dict(text="Next time: budgeting that doesn't suck. Fifty, thirty, twenty, versus zero-based, versus paying yourself first. Subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("maya", "smileBig", 330), ch("jordan", "smile", 930, flip=True), em("📺", 1500, 400, 240, "green"), tagel("NEXT: BUDGETING", 1500, 700, "green", False, 48)], bgargs=dict(extra="couch", win=False))]),
]
