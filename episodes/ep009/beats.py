VOICE = ("af_heart", 0.75)
SAY = {"$": "", "APR": "A P R", "GTA": "G T A", "20/4/10": "twenty, four, ten"}

CAST = {
    "leo": {"seed": "leo", "head": ["flatTop"], "skinColor": ["edb98a"], "clothingColor": ["93c5fd"]},
    "nia": {"seed": "nia", "head": ["bantuKnots"], "skinColor": ["694d3d"], "clothingColor": ["fca5a5"]},
    "dealer": {"seed": "dealer", "head": ["shaved2"], "skinColor": ["d08b5b"], "clothingColor": ["e5e7eb"], "facialHair": ["goatee1"]},
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
def pmt(p, r, n):
    i = r / 12
    return p * i / (1 - (1 + i) ** -n)


def bal(p, r, n, k):
    i = r / 12
    return p * (1 + i) ** k - pmt(p, r, n) * ((1 + i) ** k - 1) / i


TAXFEE = 0.08                       # assumed sales tax + fees, varies a lot by state
NEW_APR, USED_APR = 0.070, 0.106    # Edmunds Q3 2026 averages
L_LOAN = 32000 * (1 + TAXFEE) - 1000    # Leo: $32,000 new, $1,000 down -> $33,560
N_LOAN = 16000 * (1 + TAXFEE) - 3000    # Nia: $16,000 four-year-old used, $3,000 down -> $14,280
L84, L60 = pmt(L_LOAN, NEW_APR, 84), pmt(L_LOAN, NEW_APR, 60)   # $506.51, $664.53
N48 = pmt(N_LOAN, USED_APR, 48)                                  # $366.31
L84_INT, L60_INT = L84 * 84 - L_LOAN, L60 * 60 - L_LOAN          # $8,987, $6,312
N48_INT = N48 * 48 - N_LOAN                                      # $3,303
# depreciation assumption: new loses 20% in year 1 then 15% a year; used loses 10% a year
LV = [32000 * 0.8 * 0.85 ** (y - 1) if y else 32000 for y in range(8)]
NV = [16000 * 0.9 ** y for y in range(8)]
LB = [bal(L_LOAN, NEW_APR, 84, 12 * y) for y in range(8)]
INS = 5939 / 12                     # Bankrate 2026 avg, 19-year-old, own full-coverage policy: $495 a month
INS_FAM = 4304 / 12                 # same, on a parent's policy: $359 a month
L_RUN, N_RUN = 220, 280             # assumed gas, maintenance, registration (older car = more repairs)
L_ALL, N_ALL = L84 + INS + L_RUN, N48 + INS + N_RUN               # $1,221 vs $1,141 a month
L7 = 1000 + L84 * 84 + (INS + L_RUN) * 84                          # $103,600 out of pocket over 7 years
N7 = 3000 + N48 * 48 + (INS + N_RUN) * 84                          # $85,676
GAP = (L7 - LV[7]) - (N7 - NV[7])                                  # $15,922 after subtracting what each car is still worth
FREED = N48 * 36                                                   # $13,187 Nia keeps in years 5 to 7
assert round(L84) == 507 and round(N48) == 366 and round(GAP) == 15922 and round(LV[1] - LB[1]) == -4109

R = lambda els, **k: dict(bg="room", els=els, **k)
LOT = lambda els, **k: dict(bg="outside", els=els, **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="Same paycheck, two sets of keys", text="Saturday morning. A car dealership with too many balloons. Leo is twenty, three months into his first full-time job, and he is sitting in a brand new compact SUV that still smells like plastic and optimism.",
         scenes=[LOT([em("🎈", 400, 260, 160), em("🎈", 1560, 300, 140), em("🚙", 960, 700, 300)]),
                 LOT([ch("leo", "smileBig", 560), em("🚙", 1320, 680, 300, None, "NEW. SHINY.")])]),
    dict(text="Across town, Nia is also twenty, at the same kind of job, for the same pay. She's buying a four-year-old sedan with a dent in the back door. She has named the dent. The dent is called Gerald.",
         scenes=[LOT([ch("nia", "cheeky", 560), em("🚗", 1320, 680, 300, "4 YEARS OLD")]),
                 LOT([ch("nia", "smileLOL", 560), em("🩹", 1320, 480, 200, None, "THIS IS GERALD")])]),
    dict(text="Here's the thing. Their monthly payments aren't that far apart. Leo's is about five hundred and seven dollars. Nia's is about three hundred and sixty-six. A difference of about a hundred and forty dollars. Roughly a streaming bundle and a few takeout nights.",
         scenes=[dict(bg="plain", els=[ch("leo", "smile", 420), ch("nia", "calm", 1500, flip=True), tagel("LEO: $507 / MONTH", 420, 230, "amber"), tagel("NIA: $366 / MONTH", 1500, 230, "green")])]),
    dict(text="But seven years from now, after you count everything the car really costs, Leo will have spent about sixteen thousand dollars more than Nia. For basically the same commute. Same road. Same traffic. Same playlist.",
         scenes=[dict(bg="board", bgargs=dict(text="7 YEARS LATER: ~$16,000"), els=[]),
                 dict(bg="outside", els=[ch("leo", "awe", 560), em("🧾", 1320, 480, 240, "red", "+$16,000")])]),
    dict(text="Quick honesty note. Leo and Nia are made up. Composites. The averages come from real sources, and every number is calculated on screen, but it's an example, not your situation. Prices, rates and insurance swing a lot by state and by driver. And this channel is education, not financial advice. Use this to read your own deal, not as a plan.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 320), tagel("EXAMPLE, NOT YOUR DEAL", 560, 700, "green", True)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="A car is usually the second biggest thing people your age buy, right after college. And it's the only one where someone hands you free coffee while you sign. So, seven things to understand about the real cost of your first car. Leo learned them in the fine print. Nia learned them before.",
         scenes=[R([ch("leo", "lovingGrin1", 560), em("☕", 1320, 500, 220, None, "FREE COFFEE")]),
                 dict(bg="board", bgargs=dict(text="7 THINGS BEFORE YOU SIGN"), els=[])]),
    # ---------------- 1
    dict(chapter="1. Price the car, not the payment", text="Number one. The first question at the dealership is almost always the same. So, what monthly payment are you looking for? It sounds friendly. It's actually the most expensive question in the building.",
         scenes=[dict(bg="office", els=[num(1), ch("dealer", "smileBig", 1400, flip=True), em("💬", 620, 420, 220, "red", "\"WHAT MONTHLY?\"")])]),
    dict(text="Because almost any car fits almost any monthly payment. You just make the loan longer. Leo said five hundred. Twenty minutes later, there was a car that fit five hundred. Funny how that works.",
         scenes=[dict(bg="office", els=[ch("leo", "smile", 520), ch("dealer", "cheeky", 1400, flip=True), tagel("\"$500 IS FINE\"", 960, 260, "red")])]),
    dict(text="Nia asked a different question. What's the out-the-door price? That's the full number, with tax, title, registration and dealer fees. In our example, fees and taxes add about eight percent. Leo's thirty-two thousand dollar car is really about thirty-four thousand, five hundred and sixty. Nia's sixteen thousand dollar car, about seventeen thousand, two hundred and eighty.",
         scenes=[R([ch("nia", "explaining", 560), em("🏷️", 1320, 480, 220, "green", "OUT-THE-DOOR PRICE?")], bgargs=dict(extra="shelf")),
                 dict(bg="plain", els=[tagel("LEO: $32,000 → $34,560", 960, 360, "amber", False, 66), tagel("NIA: $16,000 → $17,280", 960, 580, "green", False, 66)])]),
    dict(text="For context, the average new vehicle in America sold for about fifty-one thousand dollars last month, a record. So Leo isn't even being wild. He's buying below average. That's how quietly this stuff adds up.",
         scenes=[dict(bg="board", bgargs=dict(text="AVG NEW CAR: $51,109"), els=[]),
                 LOT([ch("leo", "suspicious", 560), em("📊", 1320, 480, 220, None, "BELOW AVERAGE (!)")])]),
    dict(text="Then she did the boring, powerful thing. She emailed three sellers and asked each one for an out-the-door price, in writing. Same car, three answers, about a thousand dollars apart. It took one evening. It's the closest thing to a cheat code this video has.",
         scenes=[R([ch("nia", "smile", 560), em("📧", 1320, 480, 220, "green", "3 WRITTEN QUOTES")], bgargs=dict(extra="shelf"))]),
    # ---------------- 2
    dict(chapter="2. The 84-month stretch", text="Number two. Leo puts a thousand down and borrows thirty-three thousand, five hundred and sixty. The average rate for a new car loan last quarter was about seven percent. Over five years, his payment would be about six hundred and sixty-five a month. Too high. So the loan gets stretched to seven years. Eighty-four months. Now it's about five hundred and seven.",
         scenes=[dict(bg="office", els=[num(2), em("📄", 700, 460, 240), tagel("7% APR (Q3 AVG)", 1320, 460, "amber", False, 60)]),
                 dict(bg="plain", els=[tagel("60 MONTHS: $665", 960, 360, "amber", False, 72), tagel("84 MONTHS: $507", 960, 580, "green", False, 72)])]),
    dict(text="Feels like a win. A hundred and fifty-eight dollars a month, gone. But look at the interest. Five years: about six thousand, three hundred. Seven years: about nine thousand. The longer loan costs about two thousand, seven hundred more. Smaller bite, bigger meal.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("5-year interest", round(L60_INT), "amber"), ("7-year interest", round(L84_INT), "red")])]),
                 R([ch("leo", "concerned", 560), em("🍔", 1320, 500, 220, "red", "+$2,675 INTEREST")])]),
    dict(text="And Leo is not alone. Last quarter, about one in four new car loans was eighty-four months or longer. A record. The average new car payment hit about seven hundred and eighty-seven dollars a month. That's not a car payment. That's a second rent.",
         scenes=[dict(bg="board", bgargs=dict(text="1 IN 4 LOANS: 84+ MONTHS"), els=[]),
                 dict(bg="room", els=[em("🏠", 700, 460, 240), em("🚙", 1300, 500, 260, "red", "$787 = SECOND RENT")])]),
    dict(text="Seven years is a long time. Seven years ago, you were probably in middle school, and your biggest monthly commitment was a game's battle pass. A seven-year loan means you're still paying for this car when it's old enough to be in second grade.",
         scenes=[R([ch("leo", "tired", 560), em("🎮", 1320, 480, 220, None, "BATTLE PASS ERA")], bgargs=dict(extra="couch")),
                 dict(bg="plain", els=[em("🚙", 700, 460, 260, "red"), em("🎒", 1250, 460, 220), tagel("STILL PAYING AT AGE 7", 960, 760, "red")])]),
    # ---------------- 3
    dict(chapter="3. Depreciation, the invisible bill", text="Number three. The biggest cost of owning a car doesn't come with a bill. It's depreciation. The car slowly becomes worth less. AAA's latest yearly study found it's the biggest single cost of owning a new car, about four thousand, four hundred dollars a year on average.",
         scenes=[LOT([num(3), em("🚙", 960, 620, 280, "red"), em("📉", 1400, 330, 200, "red", "DEPRECIATION")]),
                 dict(bg="board", bgargs=dict(text="AAA: ~$4,422 / YEAR"), els=[])]),
    dict(text="New cars drop fastest at the start. For our example, we'll assume Leo's car loses twenty percent in year one, then fifteen percent a year. That's a rough rule of thumb, not a law. Nia's car already did its big drop with its first owner. We'll assume hers loses ten percent a year.",
         scenes=[dict(bg="plain", els=[dict(t="chart", series=[{"name": "Leo's car", "color": "red", "ys": [round(v) for v in LV]}, {"name": "Nia's car", "color": "green", "ys": [round(v) for v in NV], "dy": 30}], xlabels=["NOW", "1", "2", "3", "4", "5", "6", "7"], label="Car value (assumed), years", box=(240, 120, 1680, 760))])]),
    dict(text="Now put Leo's loan on top of that. After one year, he still owes about twenty-nine thousand, seven hundred. The car is worth about twenty-five thousand, six hundred. He owes about four thousand dollars more than the car is worth. That's called being upside down, or underwater.",
         scenes=[dict(bg="plain", els=[dict(t="chart", series=[{"name": "Owed", "color": "red", "ys": [round(v) for v in LB]}, {"name": "Worth", "color": "amber", "ys": [round(v) for v in LV], "dy": 30}], xlabels=["NOW", "1", "2", "3", "4", "5", "6", "7"], label="Leo: loan vs car value", box=(240, 120, 1680, 760))]),
                 R([ch("leo", "concernedFear", 560), em("🌊", 1320, 480, 220, "red", "UNDERWATER: -$4,109")])]),
    dict(text="In our example he stays underwater for about four years. Which is fine, until it isn't. If the car gets totaled, or he needs to sell it, the money from the car doesn't cover the loan. He'd owe the difference on a car he no longer has. It's like a GTA heist where the getaway car explodes and you still owe for the car.",
         scenes=[LOT([ch("leo", "fear", 560), em("💥", 1320, 520, 240, "red", "STILL OWES THE LOAN")])]),
    dict(text="And here's the trap that makes it worse. Say Leo trades this car in after two years, while he's still underwater. The dealer can roll the leftover loan into his next loan. Now he's paying for one and a half cars, and only driving one. That's how some people end up underwater for a decade.",
         scenes=[dict(bg="office", els=[ch("dealer", "smileBig", 1400, flip=True), em("🔄", 600, 460, 240, "red", "ROLLED INTO NEXT LOAN")]),
                 LOT([em("🚙", 700, 640, 260, "red"), em("➕", 1060, 600, 120), em("🚗", 1400, 660, 160, "red", "HALF A CAR")])]),
    # ---------------- 4
    dict(chapter="4. Insurance is the plot twist", text="Number four. Insurance. This is where a lot of twenty-year-olds get blindsided, because young drivers pay the most. If you finance a car, the lender will usually require full coverage, which covers damage to the car too, not just the other person.",
         scenes=[R([num(4), ch("nia", "concerned", 560), em("🛡️", 1320, 480, 220, "red", "FULL COVERAGE")])]),
    dict(text="Bankrate's averages for a nineteen-year-old with full coverage this year: about five thousand, nine hundred dollars a year on their own policy. About four hundred and ninety-five dollars a month. That's almost as much as Leo's car payment. On a parent's policy, the average is about four thousand, three hundred a year.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("Own policy", 5939, "red"), ("On a parent's policy", 4304, "amber")])]),
                 R([ch("leo", "awe", 560), em("🛡️", 1320, 480, 220, "red", "$495 / MONTH")])]),
    dict(text="So before you shop for a car, shop for insurance. Get quotes on the exact cars you're considering, because a sporty model can cost a lot more to insure than a boring one. Ask about good student discounts, and what a higher deductible would do to the price. And if you still live at home, ask whether staying on a family policy is an option. This part isn't about the car at all. It's about one phone call.",
         scenes=[R([ch("nia", "driven", 560), em("📞", 1320, 480, 220, "green", "QUOTE FIRST")], bgargs=dict(extra="shelf")),
                 R([em("✅", 560, 300, 120, "green"), tagel("QUOTE THE EXACT CAR", 1100, 300, "green", False, 50), em("✅", 560, 480, 120, "green"), tagel("ASK ABOUT DISCOUNTS", 1100, 480, "green", False, 50), em("✅", 560, 660, 120, "green"), tagel("COMPARE DEDUCTIBLES", 1100, 660, "green", False, 50)], bgargs=dict(win=False))]),
    # ---------------- 5
    dict(chapter="5. Add up the real monthly number", text="Number five. Add it all up, because the payment is only the first line. In our example, both of them pay the same four hundred and ninety-five a month for insurance. Gas, maintenance and registration, we'll assume two hundred and twenty for Leo, and two hundred and eighty for Nia, because older cars need more repairs.",
         scenes=[dict(bg="board", bgargs=dict(text="PAYMENT IS LINE ONE"), els=[num(5)]),
                 dict(bg="plain", els=[tagel("INSURANCE: $495", 960, 260, "red", False, 64), tagel("LEO GAS + UPKEEP: $220", 960, 470, "amber", False, 64), tagel("NIA GAS + UPKEEP: $280", 960, 680, "amber", False, 64)])]),
    dict(text="Leo's real number is about twelve hundred and twenty-one dollars a month. Nia's is about eleven hundred and forty-one. Only about eighty dollars apart. Surprise. Both are huge. A car isn't a payment. It's a monthly subscription with a steering wheel.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("Leo, all-in", round(L_ALL), "red"), ("Nia, all-in", round(N_ALL), "amber")])]),
                 R([ch("nia", "solemn", 560), em("🚗", 1320, 520, 240, "red", "SUBSCRIPTION + WHEEL")])]),
    dict(text="AAA's yearly study puts the average cost of owning and running a new car at about twelve thousand, nine hundred dollars a year. About a thousand and seventy-two a month. So if your budget only has room for the payment, it doesn't have room for the car.",
         scenes=[dict(bg="board", bgargs=dict(text="AAA: $12,863 / YEAR"), els=[]),
                 R([ch("leo", "serious", 560), tagel("ROOM FOR THE PAYMENT", 1300, 330, "red", False, 50), tagel("≠ ROOM FOR THE CAR", 1300, 500, "red", True, 50)])]),
    # ---------------- 6
    dict(chapter="6. Buy used like a detective", text="Number six. If used cars are often the better deal, how do you avoid buying someone else's problem? You go full detective. Not dramatic detective. Clipboard detective.",
         scenes=[LOT([num(6), ch("nia", "suspicious", 560), em("🔍", 1320, 480, 220, "green", "CLIPBOARD DETECTIVE")])]),
    dict(text="First, a vehicle history report, using the car's VIN, to check for accidents, flood damage or a salvage title. Second, a pre-purchase inspection by an independent mechanic you choose, not one the seller picks. It costs money. It costs a lot less than one surprise transmission.",
         scenes=[dict(bg="office", els=[em("📄", 620, 440, 240, "green", "HISTORY REPORT"), em("🔧", 1320, 440, 240, "green", "YOUR MECHANIC")]),
                 dict(bg="outside", els=[ch("nia", "smile", 520), em("🚗", 1250, 680, 260), em("🔧", 1520, 440, 160, "green")])]),
    dict(text="Third, get your loan approved before you walk in. A credit union or your bank can pre-approve you, so you know your rate and your limit. Then the dealer has to beat that rate, instead of building one around you. Nia showed up with a pre-approval. Leo showed up with vibes.",
         scenes=[R([ch("nia", "driven", 560), em("✉️", 1320, 480, 220, "green", "PRE-APPROVED")], bgargs=dict(extra="shelf")),
                 R([ch("leo", "cheeky", 560), em("✨", 1320, 480, 220, "red", "VIBES")])]),
    dict(text="One more. Watch for add-ons in the finance office. Extended warranties, paint protection, extra packages. Some can be useful, but they're optional, they're negotiable, and when they're rolled into the loan, you pay interest on them for years. Ask for the price of each one, alone, in writing.",
         scenes=[dict(bg="office", els=[ch("dealer", "smileLOL", 1400, flip=True), em("🧴", 420, 420, 180, "red", "PAINT PROTECTION"), em("📜", 900, 380, 150, "red")])]),
    # ---------------- 7
    dict(chapter="7. Pay it off, then keep driving", text="Number seven is where Nia quietly wins. Her loan is four years. Her payment is about three hundred and sixty-six, and her total interest is about three thousand, three hundred. When the loan ends, she does the most powerful thing you can do with a car. Nothing. She keeps driving it.",
         scenes=[LOT([num(7), ch("nia", "eyesClosed", 560), em("🚗", 1320, 680, 260, "green", "PAID OFF")])]),
    dict(text="For the next three years, she sends that same three hundred and sixty-six dollars a month to savings instead. That's about thirteen thousand, two hundred dollars, before any interest. Meanwhile, Leo is still making payments on a car that's now worth less than ten thousand.",
         scenes=[dict(bg="plain", els=[tagel("$366 x 36 MONTHS", 960, 360, "green", False, 76), tagel("≈ $13,187 SAVED", 960, 580, "green", True, 76)]),
                 R([ch("leo", "tired", 560), em("🧾", 1320, 480, 220, "red", "PAYMENT 70 OF 84")], bgargs=dict(night=True))]),
    dict(text="Add up all seven years. Leo spends about a hundred and three thousand, six hundred, and has a car worth about nine thousand, seven hundred. Nia spends about eighty-five thousand, seven hundred, and has a car worth about seven thousand, seven hundred. Subtract what each car is still worth, and the gap is about fifteen thousand, nine hundred dollars. That's the sixteen thousand from the start.",
         scenes=[dict(bg="plain", els=[dict(t="bars", box=(260, 120, 1660, 760), items=[("Leo: spent minus car", round(L7 - LV[7]), "red"), ("Nia: spent minus car", round(N7 - NV[7]), "green")])]),
                 dict(bg="board", bgargs=dict(text="GAP: ~$15,900"), els=[])]),
    # ---------------- honesty check
    dict(chapter="Honesty check: used isn't free", text="Honesty check. Used is not automatically cheaper, and this example is generous to Nia in a few ways. Her loan rate is higher, ten point six percent, the average for used car loans last quarter. Older cars break more. And if she'd skipped the inspection, one bad repair could wipe out a year of savings.",
         scenes=[dict(bg="board", bgargs=dict(text="USED APR: 10.6% (Q3 AVG)"), els=[]),
                 LOT([ch("nia", "concerned", 560), em("🔥", 1320, 520, 220, "red", "ONE BAD REPAIR")])]),
    dict(text="And rates for someone your age with a short credit history are often higher than these averages. A higher rate shrinks every gap in this video, and can flip some of them. So compare the full cost of the exact loans you're offered, not our example.",
         scenes=[R([ch("leo", "serious", 560), tagel("YOUR RATE ≠ AVERAGE", 1300, 400, "red", True, 54)])]),
    dict(text="There are also real reasons people buy new. A full warranty. Newer safety features. Sometimes a low promotional rate, though those usually need strong credit. New isn't wrong. It's just more expensive than the payment makes it look.",
         scenes=[LOT([ch("leo", "calm", 560), em("🛡️", 1200, 460, 180, "green", "WARRANTY"), em("🦺", 1560, 640, 150, "green")])]),
    dict(chapter="Honesty check: the 20/4/10 rule", text="One common rule of thumb is called twenty, four, ten. Put twenty percent down. Borrow for no more than four years. And keep total car costs under ten percent of your income before taxes.",
         scenes=[dict(bg="board", bgargs=dict(text="20% DOWN / 4 YRS / 10%"), els=[])]),
    dict(text="Here's the uncomfortable part. If you earn forty thousand a year, ten percent is about three hundred and thirty-three a month. Insurance alone for a nineteen-year-old can be more than that. So at twenty, almost nobody fits this rule. That doesn't mean the rule is broken. It means a car is a bigger financial decision at your age than anyone makes it sound.",
         scenes=[dict(bg="plain", els=[tagel("10% OF $40K ≈ $333/MO", 960, 360, "amber", False, 70), tagel("INSURANCE ALONE: $495", 960, 580, "red", True, 70)]),
                 R([ch("nia", "solemn", 560), em("🤔", 1320, 480, 200, None, "BIGGER THAN IT LOOKS")])]),
    dict(text="So use it as a direction. Bigger down payment. Shorter loan. Cheaper car to insure. And ask the bigger question too. Could a bike, transit, or one more year on the family car get you there? Sometimes the best car deal is the car you don't buy yet.",
         scenes=[dict(bg="outside", els=[em("🚲", 500, 560, 220, "green", "BIKE"), em("🚌", 960, 560, 240, "green", "TRANSIT"), em("🏠", 1420, 560, 220, "green", "FAMILY CAR")])]),
    # ---------------- close
    dict(chapter="Back to the lot", text="So, back to that Saturday. Same job. Same pay. Two sets of keys. The difference between Leo and Nia was not luck, or some secret dealer trick. It was three questions. What's the out-the-door price? What does it cost to insure? And what's the total I'll pay, not the monthly?",
         scenes=[LOT([ch("leo", "calm", 480), ch("nia", "smile", 1440, flip=True), em("🔑", 960, 520, 160)]),
                 R([em("❓", 560, 300, 120, "green"), tagel("OUT-THE-DOOR PRICE", 1100, 300, "green", False, 50), em("❓", 560, 480, 120, "green"), tagel("INSURANCE QUOTE", 1100, 480, "green", False, 50), em("❓", 560, 660, 120, "green"), tagel("TOTAL, NOT MONTHLY", 1100, 660, "green", False, 50)], bgargs=dict(win=False))]),
    dict(text="And for the Leos watching. You're not stuck. You can refinance if your credit improves, pay a little extra toward the principal each month, and keep the car long after the last payment. The worst part of the deal is the beginning. You get to write the ending.",
         scenes=[LOT([ch("leo", "driven", 960, glow="green"), em("🛣️", 1450, 520, 200, "green", "WRITE THE ENDING")])]),
    dict(text="The one-line takeaway: never shop by the monthly payment. Shop by the total. If you're car shopping this winter, with all the year-end sale signs, run these numbers before the balloons get to you.",
         scenes=[dict(bg="board", bgargs=dict(text="SHOP THE TOTAL, NOT THE MONTHLY"), els=[])]),
    dict(text="Next video, we're looking at buy now, pay later, and how those little four-payment splits quietly add up, just in time for holiday shopping. If this one saved you from a seven-year loan, subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("nia", "smileBig", 330), ch("leo", "smile", 930, flip=True), em("📺", 1580, 420, 280, "green", "NEXT: PAY LATER")], bgargs=dict(extra="couch", win=False))]),
]
