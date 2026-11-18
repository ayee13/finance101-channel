VOICE = ("af_heart", 0.75)
SAY = {"$": "", "3x": "three times"}

CAST = {
    "eli": {"seed": "eli", "head": ["pomp"], "skinColor": ["d08b5b"], "clothingColor": ["fdba74"]},
    "rosa": {"seed": "rosa", "head": ["long"], "skinColor": ["edb98a"], "clothingColor": ["a5b4fc"]},
    "manager": {"seed": "manager", "head": ["noHair2"], "skinColor": ["ae5d29"], "clothingColor": ["8fa7df"], "accessories": ["glasses"]},
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
WAGE = 18.50
GROSS = WAGE * 40 * 52                      # $38,480 a year before taxes
GM = GROSS / 12                             # $3,206.67 a month before taxes
TAKE_HOME = 2600                            # assumed take-home per month after taxes (varies by state)
RULE30 = GM * 0.30                          # $962
MAX3X = GM / 3                              # $1,068.89: highest rent that passes a "3x the rent" income check
STUDIO = 1150                               # Eli's studio, assumed
UTIL_ALONE, NET_ALONE, INS = 110, 60, 14    # utilities, internet (assumed), renters insurance (~$14, III via Bankrate)
ELI = STUDIO + UTIL_ALONE + NET_ALONE + INS          # $1,334 a month
TWO_BED = 1500                              # Rosa's 2-bedroom, split with a roommate
ROSA = TWO_BED // 2 + UTIL_ALONE // 2 + NET_ALONE // 2 + INS   # $849 a month
MOVE_ELI = STUDIO + STUDIO + 50 + 150 + 600          # first month, deposit, application, truck, basics = $3,100
MOVE_ROSA = 750 + 750 + 50 + 75 + 300                # $1,925
NEW = 1400 // 2 + UTIL_ALONE // 2 + NET_ALONE // 2 + INS   # Eli's later plan: $1,400 2-bed with a coworker -> $799
MOVE_NEW = 700 + 700 + 50 + 75 + 600                 # $2,125, saved at $425 a month for 5 months
assert GROSS == 38480 and round(GM, 2) == 3206.67 and round(RULE30) == 962 and round(MAX3X, 2) == 1068.89
assert ELI == 1334 and ROSA == 849 and ELI - ROSA == 485 and (ELI - ROSA) * 12 == 5820
assert round(ELI / GM * 100) == 42 and round(ELI / TAKE_HOME * 100) == 51 and round(STUDIO / GM * 100) == 36
assert MOVE_ELI == 3100 and MOVE_ROSA == 1925 and NEW == 799 and MOVE_NEW == 2125 and MOVE_NEW / 5 == 425
assert STUDIO * 3 * 12 - GROSS == 2920 and round(STUDIO * 0.05 * 12) == 690 and TAKE_HOME - ELI == 1266

R = lambda els, **k: dict(bg="room", els=els, **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="Same paycheck, two leases", text="Saturday morning. Eli is twenty, works full time at a bike shop, eighteen fifty an hour. He just toured a studio apartment. Hardwood floors. A window that looks at a different window. Eleven hundred and fifty dollars a month. He's already picked a spot for the gaming chair.",
         scenes=[dict(bg="hallway", els=[ch("eli", "smileBig", 620), em("🔑", 1300, 520, 200, "green", "STUDIO: $1,150")]),
                 R([ch("eli", "lovingGrin1", 560), em("🪑", 1300, 600, 220, None, "CHAIR GOES HERE")], bgargs=dict(extra="shelf"))]),
    dict(text="Across town, his friend Rosa, also twenty, also eighteen fifty an hour, is signing for a two-bedroom with a roommate. It's older. The kitchen has one working burner and a mysterious smell. Her half is seven fifty.",
         scenes=[R([ch("rosa", "smile", 560), em("🏠", 1300, 480, 220, "green", "HER HALF: $750")]),
                 R([ch("rosa", "suspicious", 560), em("🍳", 1300, 520, 200, "red", "1 WORKING BURNER")])]),
    dict(text="Here's the surprise. Eli's rent is eleven fifty. But the check he needs before he gets the keys is about thirty-one hundred dollars. And once he's in, his real monthly housing bill eats about half of everything he takes home. Same paycheck as Rosa. Very different year.",
         scenes=[dict(bg="plain", els=[tagel("RENT: $1,150", 560, 380, "ink", False, 72), tagel("KEYS: ~$3,100", 1360, 380, "red", True, 72)]),
                 R([ch("eli", "awe", 560), em("🧾", 1300, 460, 260, "red", "HALF HIS TAKE-HOME")])]),
    dict(text="So today, the honest math on your first apartment. Not which one is prettiest. What it actually costs to get in, to stay in, and to not be broke while you live there.",
         scenes=[dict(bg="plain", els=[em("🏢", 960, 440, 340), big("GET IN. STAY IN. NOT BROKE.", y=860, size=86)])]),
    dict(text="Quick honesty note. Eli and Rosa are made up. Composites. The rent and insurance figures come from real sources, and every number is calculated on screen, but your city, your pay and your lease will be different. And this channel is education, not financial advice. It's arithmetic, not a plan for your life.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 320), tagel("EXAMPLE, NOT A PROMISE", 560, 700, "green", True)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="Seven moves. A couple of them will save you thousands. One of them will save you from a very awkward phone call with a parent. Let's start with the rule everybody quotes and almost nobody runs.",
         scenes=[dict(bg="board", bgargs=dict(text="7 MOVES"), els=[])]),
    # ---------------- 1
    dict(chapter="1. Run the 30% rule", text="The thirty percent rule says: spend no more than thirty percent of your income on housing. It started as a government rule for public housing decades ago, and it stuck. Researchers still use it. If you pay more than thirty percent, you count as cost burdened.",
         scenes=[dict(bg="board", bgargs=dict(text="HOUSING ≤ 30% OF INCOME"), els=[num(1)]),
                 dict(bg="office", els=[num(1), em("🏛️", 600, 460, 260), tagel("OVER 30% = COST BURDENED", 1250, 460, "red", False, 50)])]),
    dict(text="Let's run it for Eli. Eighteen fifty an hour, forty hours a week, fifty-two weeks. That's thirty-eight thousand, four hundred and eighty dollars a year before taxes. About three thousand, two hundred and seven a month. Thirty percent of that is nine hundred and sixty-two dollars.",
         scenes=[dict(bg="plain", els=[tagel("$18.50 × 40 × 52", 960, 280, "ink", False, 72), tagel("= $38,480 A YEAR", 960, 470, "ink", False, 72), tagel("= $3,207 A MONTH", 960, 660, "ink", False, 72)]),
                 R([ch("eli", "serious", 560), tagel("30% = $962", 1300, 420, "amber", True, 76)])]),
    dict(text="His studio is eleven fifty. That's about thirty-six percent, before a single light switch gets flipped. He's over the line, and he hasn't even unpacked the gaming chair.",
         scenes=[R([ch("eli", "concerned", 560), tagel("$1,150 = 36%", 1300, 360, "red", True, 76), tagel("THE LINE: $962", 1300, 560, "amber", False, 56)])]),
    dict(text="And Eli is not some rare case. Harvard's housing center counted a record twenty-two point seven million renter households paying more than thirty percent in 2024. That's about half of all renters. It's so common it barely feels like a warning anymore. It still is one.",
         scenes=[dict(bg="plain", els=[tagel("22.7 MILLION", 960, 320, "red", True, 100), tagel("~HALF OF ALL RENTERS (2024)", 960, 560, "ink", False, 56)])]),
    dict(text="Notice that the rule uses income before taxes. Eli doesn't get that. After taxes he takes home about twenty-six hundred a month, in our example. Hold on to that number. It's about to get uncomfortable.",
         scenes=[R([ch("eli", "suspicious", 560), tagel("BEFORE TAXES: $3,207", 1300, 360, "ink", False, 54), tagel("TAKE-HOME: ~$2,600", 1300, 540, "amber", True, 54)])]),
    # ---------------- 2
    dict(chapter="2. Pass the landlord's 3x test", text="Here's the rule you'll actually run into. A lot of landlords want your monthly income before taxes to be at least three times the rent. Some say forty times the rent per year. Same idea. It's their version of the thirty percent rule, except they enforce it.",
         scenes=[dict(bg="office", els=[num(2), ch("manager", "serious", 600), em("📄", 1300, 460, 220, "amber", "INCOME ≥ 3x RENT")])]),
    dict(text="Three times eleven fifty is thirty-four fifty a month. That's forty-one thousand, four hundred a year. Eli makes thirty-eight thousand, four eighty. He's short by about twenty-nine hundred dollars of yearly income. The application comes back: approved, if you add a cosigner.",
         scenes=[dict(bg="plain", els=[tagel("NEEDS: $41,400 / YR", 560, 380, "red", False, 60), tagel("HAS: $38,480 / YR", 1360, 380, "amber", False, 60)]),
                 dict(bg="office", els=[ch("eli", "concernedFear", 560), em("✉️", 1300, 460, 220, "red", "NEEDS A COSIGNER")])]),
    dict(text="That's the awkward phone call. A cosigner, sometimes called a guarantor, is usually a parent who signs saying they'll pay if you don't. That's not a formality. If Eli misses rent, it's their money and their credit on the line. It's like borrowing someone's account in a game, except if you lose, they lose too.",
         scenes=[R([ch("eli", "tired", 560), em("📞", 1300, 460, 220, "red", "HI MOM. SO...")]),
                 dict(bg="plain", els=[em("🎮", 700, 440, 240), tagel("THEIR ACCOUNT. YOUR PLAY.", 1250, 440, "red", True, 54)])]),
    dict(text="Flip the test around and it tells you your own ceiling. Divide your monthly income by three. For Eli, that's about a thousand and sixty-nine. That's the most he can rent alone without asking anyone for help. Try that before you tour, not after you fall in love with the window.",
         scenes=[dict(bg="board", bgargs=dict(text="$3,207 ÷ 3 = $1,069 MAX"), els=[]),
                 R([ch("eli", "explaining", 560), tagel("DIVIDE BEFORE YOU TOUR", 1300, 420, "green", True)])]),
    # ---------------- 3
    dict(chapter="3. Add up the real monthly bill", text="Next. Rent is the price on the listing. It is not what living there costs. The listing is like the base price of a game. The real cost is the base game plus every pack you didn't know you'd need.",
         scenes=[dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[num(3), em("🎮", 700, 440, 240), em("➕", 1060, 440, 140), em("📦", 1380, 440, 240, "red", "THE DLC")])]),
    dict(text="For Eli's studio: electric and gas, about a hundred and ten a month in our example. Internet, sixty. Renters insurance, about fourteen. Rent plus all that is thirteen hundred and thirty-four dollars a month. And that's before parking, laundry, or a pet fee, if the building has them.",
         scenes=[R([em("💡", 330, 360, 150, None, "UTILITIES $110"), em("📶", 960, 360, 150, None, "INTERNET $60"), em("🛡️", 1590, 360, 150, None, "INSURANCE $14")]),
                 dict(bg="plain", els=[tagel("$1,150 + $110 + $60 + $14", 960, 330, "ink", False, 64), tagel("= $1,334 A MONTH", 960, 540, "red", True, 84)])]),
    dict(text="Thirteen thirty-four is about forty-two percent of Eli's income before taxes. Out of his twenty-six hundred take-home, it's fifty-one percent. Half his money, gone on the first of the month, before food, his phone, his bus pass, or literally anything fun.",
         scenes=[dict(bg="plain", els=[tagel("42% OF GROSS", 560, 400, "red", False, 70), tagel("51% OF TAKE-HOME", 1360, 400, "red", True, 70)]),
                 R([ch("eli", "fear", 560), tagel("$2,600 − $1,334 = $1,266", 1300, 420, "amber", False, 50)])]),
    dict(text="Remember the fifty thirty twenty budget from a few episodes ago? Fifty percent of take-home for all your needs. Eli's housing alone already ate the whole needs bucket. Everything else he needs has to come out of the fun money or the savings. That's how good people end up with a credit card balance.",
         scenes=[dict(bg="board", bgargs=dict(text="NEEDS BUCKET: $1,300"), els=[]),
                 R([ch("eli", "concerned", 560), em("🪣", 1300, 480, 240, "red", "BUCKET: ALREADY FULL")])]),
    dict(text="So when you look at a place, ask the landlord or a current tenant: what do utilities usually run here in winter and summer? Some buildings include water or heat. Some don't. That one question can be worth a hundred dollars a month.",
         scenes=[dict(bg="hallway", els=[ch("rosa", "explaining", 560), em("❓", 1300, 460, 220, "green", "UTILITIES IN WINTER?")])]),
    # ---------------- 4
    dict(chapter="4. Save the move-in cash first", text="Now, the check to get the keys. This is the number that blindsides almost everyone. Most places want the first month's rent up front. Plus a security deposit, often about one month's rent. Plus an application fee.",
         scenes=[dict(bg="office", els=[num(4), ch("manager", "smile", 1400, flip=True), em("🔑", 700, 460, 240, "amber", "KEYS: NOT FREE")])]),
    dict(text="For Eli: eleven fifty for the first month. Eleven fifty for the deposit. Fifty to apply. About a hundred and fifty for a moving truck and pizza for the friends who carry the couch. And around six hundred for the stuff an empty apartment doesn't come with. A mattress. A shower curtain. Toilet paper, which you will forget.",
         scenes=[dict(bg="plain", els=[tagel("FIRST MONTH  $1,150", 960, 220, "ink", False, 56), tagel("DEPOSIT  $1,150", 960, 350, "ink", False, 56), tagel("APPLICATION  $50", 960, 480, "ink", False, 56), tagel("TRUCK + PIZZA  $150", 960, 610, "ink", False, 56), tagel("MATTRESS, ETC.  $600", 960, 740, "ink", False, 56)]),
                 R([em("🛏️", 560, 480, 220), em("🚿", 960, 480, 200), em("🧻", 1360, 480, 200, "red", "YOU WILL FORGET")])]),
    dict(text="Total: about thirty-one hundred dollars. Before he's slept there one night. Rosa, splitting a two-bedroom and bringing her old bed, needed about nineteen twenty-five. Still a lot. But twelve hundred less.",
         scenes=[dict(bg="plain", els=[ch("eli", "awe", 420, h=560), ch("rosa", "calm", 1500, h=560, flip=True), tagel("ELI: $3,100", 420, 200, "red", True), tagel("ROSA: $1,925", 1500, 200, "amber")])]),
    dict(text="Here's the trap. If you put move-in costs on a credit card, you start your new life paying interest on your toilet paper. Save the move-in cash first. If you need thirty-one hundred dollars and you can save five hundred a month, that's about six months. Set the move date from the savings, not from the listing.",
         scenes=[R([ch("eli", "concernedFear", 560), em("💳", 1300, 460, 220, "red", "INTEREST ON TP")]),
                 dict(bg="board", bgargs=dict(text="SAVINGS SETS THE MOVE DATE"), els=[])]),
    dict(text="One more thing about that deposit. It's your money. You can get it back. On move-in day, walk through with your phone and take photos and video of every scratch, stain and dent, with timestamps. Send them to the landlord. Future you, moving out, will want that evidence.",
         scenes=[dict(bg="hallway", els=[ch("rosa", "driven", 560), em("📸", 1300, 460, 220, "green", "PHOTO EVERY SCRATCH")])]),
    # ---------------- 5
    dict(chapter="5. Get renters insurance", text="Fast one, and it's the cheapest thing in this whole video. Your landlord's insurance covers the building. It does not cover your stuff. If there's a fire, a pipe bursts, or someone breaks in, your laptop is your problem.",
         scenes=[R([num(5), em("🏢", 600, 460, 240, "amber", "BUILDING: COVERED"), em("💻", 1300, 460, 220, "red", "YOUR STUFF: NOT")])]),
    dict(text="Renters insurance covers your things, and usually liability too, like if your overflowing bathtub floods the neighbor below. The national average is around fourteen dollars a month, according to the Insurance Information Institute. That's about a hundred and sixty-eight dollars a year. About what one streaming subscription costs.",
         scenes=[R([ch("rosa", "smile", 560), em("🛡️", 1300, 460, 240, "green", "~$14 A MONTH")]),
                 dict(bg="plain", els=[em("🛁", 600, 440, 240, "red"), tagel("FLOODED THE NEIGHBOR?", 1300, 440, "red", False, 54)])]),
    dict(text="Example. A break-in. Laptop, bike and clothes, three thousand dollars to replace. Say Rosa's policy has a five hundred dollar deductible, the part you pay first. Insurance pays the other twenty-five hundred. Check whether your policy pays what it costs to replace things, or only what your used stuff was worth. That difference is real.",
         scenes=[dict(bg="plain", els=[tagel("LOSS: $3,000", 560, 330, "red", False, 66), tagel("YOU PAY: $500", 560, 520, "amber", False, 66), tagel("POLICY PAYS: $2,500", 1360, 420, "green", True, 66)])]),
    # ---------------- 6
    dict(chapter="6. Do the roommate math", text="Now the big lever. Roommates. Rosa's half of a fifteen hundred dollar two-bedroom is seven fifty. Split utilities and internet, add her own insurance, and her real monthly bill is eight hundred and forty-nine dollars.",
         scenes=[R([num(6), ch("rosa", "smileBig", 560), tagel("$750 + $55 + $30 + $14", 1300, 360, "ink", False, 48), tagel("= $849", 1300, 520, "green", True, 76)])]),
    dict(text="Eli's is thirteen thirty-four. The difference is four hundred and eighty-five dollars a month. That's fifty-eight hundred and twenty dollars a year. Rosa's housing is about thirty-three percent of her take-home. Eli's is fifty-one. Same job. Same pay. One working burner.",
         scenes=[dict(bg="plain", els=[ch("eli", "tired", 420, h=560), ch("rosa", "smileLOL", 1500, h=560, flip=True), tagel("$1,334", 420, 200, "red", True), tagel("$849", 1500, 200, "green", True)]),
                 dict(bg="plain", els=[tagel("$485 A MONTH", 960, 340, "green", False, 84), tagel("= $5,820 A YEAR", 960, 560, "green", True, 84)])]),
    dict(text="But a roommate is a money relationship, not just a vibe. Before you sign, talk about the boring stuff out loud. Who pays the landlord? How do you split utilities? What happens with guests, dishes and the thermostat? Put it in a short written agreement. It feels weird. Not doing it is weirder, later.",
         scenes=[R([ch("rosa", "explaining", 520), em("📝", 1300, 460, 220, "green", "ROOMMATE AGREEMENT")]),
                 dict(bg="board", bgargs=dict(text="DISHES. GUESTS. THERMOSTAT."), els=[])]),
    dict(text="And here's the catch nobody explains. If both your names are on one lease, many leases make each of you responsible for the whole rent, not just your half. If your roommate leaves in month four, the landlord can come to you for all fifteen hundred. So pick a roommate the way you'd pick a co-op partner for a really long campaign. Reliable beats fun.",
         scenes=[R([ch("rosa", "concernedFear", 560), em("🧾", 1300, 460, 240, "red", "ROOMMATE LEFT: $1,500")]),
                 dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[em("🤝", 960, 420, 300, "green"), big("RELIABLE BEATS FUN", y=820, color="green", size=90)])]),
    # ---------------- 7
    dict(chapter="7. Read the lease before you sign", text="Last move. The lease. It's long, it's boring, and it's the part that costs people the most money later. Look for three things.",
         scenes=[dict(bg="office", els=[num(7), ch("eli", "suspicious", 560), em("📜", 1300, 460, 240, "amber", "READ ALL OF IT")])]),
    dict(text="One: what happens if you leave early. Some leases charge a fee, like two months of rent. For Eli, that's twenty-three hundred dollars to get out. Two: renewal. Rent can go up when the lease renews. A five percent bump on eleven fifty is fifty-seven dollars and fifty cents more a month, or six hundred and ninety a year.",
         scenes=[dict(bg="plain", els=[tagel("LEAVE EARLY: $2,300", 560, 400, "red", True, 60), tagel("+5% RENEWAL: +$690/YR", 1360, 400, "red", False, 52)])]),
    dict(text="Three: who fixes what, and how fast. Who handles a broken heater in January? What about pests? Ask how to submit repair requests, and keep every request in writing. Texts and emails, not just hallway conversations.",
         scenes=[R([ch("eli", "explaining", 560), em("🔧", 1300, 460, 220, "green", "REPAIRS IN WRITING")])]),
    dict(text="And a timing tip, since it's November. Rents tend to soften in the colder months, because fewer people move. Apartment List's national median slipped in September, the start of the off-season. That can make winter a decent time to ask about a lower rent, a waived fee, or a free month. The worst they can say is no.",
         scenes=[dict(bg="outside", els=[em("❄️", 600, 400, 240, "green"), tagel("OFF-SEASON = ASK", 1250, 400, "green", True, 64)]),
                 dict(bg="office", els=[ch("rosa", "cheeky", 560), ch("manager", "calm", 1400, flip=True), em("💬", 960, 360, 160, "green")])]),
    # ---------------- honesty check
    dict(chapter="Honesty check: the 30% rule is rough", text="Now, fairness time. The thirty percent rule is a rough guide, not a law of physics. The national median rent on Apartment List was about thirteen hundred and eighty-eight dollars in September. In a lot of cities, people starting out simply can't hit thirty percent alone. Nobody's failing a test there. The math is just hard.",
         scenes=[dict(bg="board", bgargs=dict(text="30% = A GUIDE, NOT A LAW"), els=[]),
                 dict(bg="plain", els=[tagel("MEDIAN RENT: ~$1,388", 960, 330, "amber", True, 80), tagel("APARTMENT LIST, SEPT 2026", 960, 560, "ink", False, 54)])]),
    dict(text="It also cuts the other way. Thirty percent of income before taxes can still be too much if you have a car payment or student loans. Some people run it on take-home pay instead. For Eli, thirty percent of twenty-six hundred is seven eighty. That's a stricter line, and a safer one.",
         scenes=[R([ch("eli", "serious", 560), tagel("30% OF TAKE-HOME: $780", 1300, 420, "green", True, 52)])]),
    dict(text="So use the rule as a question, not a verdict. If housing is over thirty percent, what gives? Roommates, a cheaper area, a longer commute, or more time at home while you save. Each one has a cost. A longer commute costs gas and hours. Living at home costs some independence. Only you can price those. But you should price them on purpose.",
         scenes=[dict(bg="plain", els=[em("🧑‍🤝‍🧑", 330, 420, 180, None, "ROOMMATES"), em("🗺️", 960, 420, 180, None, "CHEAPER AREA"), em("🏡", 1590, 420, 180, None, "HOME LONGER")])]),
    dict(chapter="Honesty check: the hidden costs", text="And the catch nobody mentions. The first year in a new place always costs more than the spreadsheet. The vacuum. The trash can. The extension cord. The pot, because Rosa's one working burner needs something to work on. Plan an extra cushion for the first few months. Then build your emergency fund back up.",
         scenes=[R([em("🧹", 420, 460, 180), em("🗑️", 820, 460, 180), em("🔌", 1220, 460, 180), em("🍲", 1620, 460, 180, "red", "+ CUSHION")]),
                 R([ch("rosa", "smileLOL", 560), em("🔥", 1300, 500, 200, "amber", "1 BURNER, 1 POT")])]),
    # ---------------- close
    dict(chapter="Back to Eli and Rosa", text="So, back to Eli. He didn't take the studio. He did the three-times math, felt it in his stomach, and didn't make the phone call. Instead, he found a coworker looking to split a fourteen hundred dollar two-bedroom. His real monthly bill: seven ninety-nine. About thirty-one percent of his take-home.",
         scenes=[R([ch("eli", "calm", 560), em("🤝", 1300, 460, 220, "green", "SPLIT A $1,400 2-BED")]),
                 dict(bg="plain", els=[tagel("$1,334 → $799", 960, 340, "green", True, 90), tagel("51% → 31% OF TAKE-HOME", 960, 560, "green", False, 64)])]),
    dict(text="His move-in cash dropped to about twenty-one twenty-five. He saved four twenty-five a month for five months, and moved in with the money already in the bank. No cosigner. No credit card. And yes, the gaming chair fits. Barely.",
         scenes=[dict(bg="board", bgargs=dict(text="$425 × 5 MONTHS = $2,125"), els=[]),
                 R([ch("eli", "smileLOL", 560), em("🪑", 1300, 600, 220, "green", "IT FITS. BARELY.")], bgargs=dict(extra="couch"))]),
    dict(text="The one-line takeaway: rent is the price, but move-in is the cover charge, and the monthly bill is everything else. Count all three before you fall in love with the window.",
         scenes=[dict(bg="board", bgargs=dict(text="RENT + MOVE-IN + EVERYTHING ELSE"), els=[])]),
    dict(text="Next video: taxes for your first job. Why a raise can't actually lower your take-home pay, and why a big refund isn't free money. If this one saved you from a thirty-one hundred dollar surprise, subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("eli", "smileBig", 320), ch("rosa", "smile", 960, flip=True), em("📺", 1560, 470, 260, "green"), tagel("NEXT: FIRST-JOB TAXES", 1500, 200, "green", True, 48)], bgargs=dict(extra="couch", win=False))]),
]
