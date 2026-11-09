VOICE = ("af_heart", 0.75)
SAY = {"$": "", "401(k)": "four oh one K", "50/30/20": "fifty, thirty, twenty"}

CAST = {
    "maya": {"seed": "maya", "head": ["bun"], "skinColor": ["d08b5b"], "clothingColor": ["9ddadb"]},
    "jordan": {"seed": "jordan", "head": ["short3"], "skinColor": ["edb98a"], "clothingColor": ["ffcf77"]},
    "theo": {"seed": "theo", "head": ["afro"], "skinColor": ["694d3d"], "clothingColor": ["f9a8d4"]},
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


# ---- the example, all numbers computed here (made-up budget; pay from ep003 and ep006)
GROSS_MO = 18 * 40 * 52 / 12          # $3,120 a month before anything comes out
TAKE = 2400                            # about what lands after taxes and his 6% 401(k) (ep003 + ep006: ~$2,430)
GAP = GROSS_MO - TAKE                  # $720 a month that was never his to spend
RENT_30 = 0.30 * GROSS_MO              # $936: the old "30% of gross" rent rule
N, WNT, SV = TAKE * .5, TAKE * .3, TAKE * .2   # 50/30/20 -> $1,200 / $720 / $480
NEEDS = dict(rent=800, utilities=80, phone=50, groceries=300, insurance=150, gas=120)   # $1,500 = 62.5%
IRREG = dict(holidays=300, birthdays=240, car_repair=600, registration=120, phone=360)  # $1,620 a year -> $135 a month
WANTS = dict(subs=35, eating_out=180, fun=150, clothes=60, buffer=100)                  # $525
SAVE = 240                              # 10%, moved on payday: $2,880 in a year
# zero-based check: 1,500 + 240 + 135 + 525 = 2,400
LEAK = 6.50 * 365                       # $6.50 a day = $2,372.50 a year
SUBS = 5 * 12.99                        # five $12.99 subscriptions = $64.95 a month, $779.40 a year

R = lambda els, **k: dict(bg="room", els=els, **k)

BEATS = [
    # ---------------- cold open
    dict(chapter="The 40-tab spreadsheet", text="The first of the month. Jordan has made a budget. Not a little budget. A spreadsheet with forty categories, color coded, with a separate line for gum. He calls it his masterpiece. His roommate Theo calls it a lot.",
         scenes=[R([ch("jordan", "driven", 560, flip=True), em("💻", 1300, 520, 240, "green", "40 CATEGORIES")], bgargs=dict(extra="shelf")),
                 R([ch("theo", "suspicious", 560), em("🍬", 1300, 520, 200, None, "A LINE FOR GUM")], bgargs=dict(extra="couch"))]),
    dict(text="Day four, he logs every coffee. Day six, he logs most of them. Day nine, a friend's birthday dinner happens, nobody planned for it, and the spreadsheet quietly dies. Nobody holds a funeral.",
         scenes=[dict(bg="plain", els=[tagel("DAY 4: LOGS IT ALL", 960, 260, "green", False, 60), tagel("DAY 6: LOGS SOME", 960, 480, "amber", False, 60), tagel("DAY 9: GONE", 960, 700, "red", True, 60)]),
                 dict(bg="cafe", els=[ch("jordan", "tired", 520, flip=True), em("🎂", 1300, 520, 220, "red", "NOT IN THE PLAN")])]),
    dict(text="Down the hall, Maya's budget is three numbers on a sticky note. Bills. Savings. Everything else. That's it. No app. No color coding. Her handwriting is honestly not great.",
         scenes=[dict(bg="hallway", els=[ch("maya", "calm", 480), em("🗒️", 1300, 470, 240, "green", "3 NUMBERS")])]),
    dict(text="The twenty-eighth of the month. Jordan checks his account and has thirty-eight dollars and a feeling. Maya has already moved two hundred and forty dollars into savings, and she still has money left for pizza. The one with the fancy budget is the one who's broke.",
         scenes=[R([ch("jordan", "concernedFear", 560, flip=True), em("📱", 1300, 480, 220, "red", "$38 LEFT")], bgargs=dict(night=True)),
                 R([ch("maya", "smileLOL", 560), em("🍕", 1300, 480, 220, "green", "SAVED $240. PIZZA OK")], bgargs=dict(night=True))]),
    dict(text="So what happened? Jordan isn't lazy, and he's not bad at math. His budget failed for one boring reason, and it's the same reason most budgets fail. By the end of this video you'll know what it is, and three ways to build a budget that actually survives a month.",
         scenes=[dict(bg="board", bgargs=dict(text="WHY BUDGETS FAIL"), els=[]),
                 dict(bg="plain", els=[tagel("50/30/20", 400, 450, "green", False, 64), tagel("ZERO-BASED", 960, 650, "amber", False, 64), tagel("PAY YOURSELF FIRST", 1450, 450, "green", False, 56)])]),
    dict(text="Quick honesty note. Maya, Jordan and Theo are made up. Composites. The budgets are examples with made-up prices, and yours will look different, because your rent is not their rent. This channel is education, not financial advice. It's a way to think about money, not a plan for your specific life.",
         scenes=[dict(bg="office", els=[em("📋", 560, 430, 300), tagel("MADE-UP PRICES", 1240, 330, "amber", False, 56), tagel("YOUR NUMBERS DIFFER", 1240, 560, "amber", False, 56)]),
                 dict(bg="plain", bgargs=dict(color=(254, 243, 199)), els=[big("EDUCATION", y=380, size=150), big("NOT FINANCIAL ADVICE", y=560, color="red", size=120)])]),
    dict(text="First, the word budget. Most people hear it and think of a diet. Something you're bad at, that ends with you eating a whole pizza at midnight out of spite. A budget is not that. A budget is just a plan for money you already have, made before the money decides for you. Seven moves. Let's go.",
         scenes=[R([ch("jordan", "rage", 560, flip=True), em("🥗", 1300, 500, 220, "red", "BUDGET = DIET?")]),
                 dict(bg="board", bgargs=dict(text="7 MOVES"), els=[])]),
    # ---------------- 1
    dict(chapter="1. Budget the money you actually get", text="Move one. Start with the right number. Jordan makes eighteen dollars an hour, full time. That's about three thousand, one hundred and twenty dollars a month. And that's the number he built his masterpiece on.",
         scenes=[dict(bg="office", els=[num(1), ch("jordan", "smileBig", 560, flip=True), tagel("$18/HR = $3,120/MO", 1320, 330, "amber", False, 60)])]),
    dict(text="But remember episode three? Taxes come out first. And since episode six, he also puts six percent into his 401(k). What actually lands in his account is about two thousand, four hundred a month. His spreadsheet was spending seven hundred and twenty dollars a month that never existed.",
         scenes=[dict(bg="plain", els=[tagel("ON PAPER: $3,120", 560, 400, "amber", False, 66), tagel("IN THE BANK: $2,400", 1360, 400, "green", True, 66), big("$720 THAT NEVER EXISTED", y=780, color="red", size=90)]),
                 R([ch("jordan", "awe", 560, flip=True), em("👻", 1300, 480, 220, "red", "GHOST MONEY")])]),
    dict(text="So rule one. Your budget starts with take-home pay. The amount that actually hits your account. If your hours change a lot, start with a low month, not a great one. Plan with the money you have, not the money you wish you had.",
         scenes=[R([ch("maya", "explaining", 560), em("🏦", 1300, 500, 220, "green", "TAKE-HOME ONLY")], bgargs=dict(extra="shelf"))]),
    dict(text="One more step before you plan anything. Look back. Open your last month of bank and card statements and sort every charge into a few rough piles. It takes about twenty minutes, it is mildly horrifying, and it's the most useful twenty minutes in this whole video. You can't plan a month you've never actually looked at.",
         scenes=[R([ch("jordan", "concernedFear", 560, flip=True), em("🧾", 1300, 480, 220, "amber", "LAST 30 DAYS")], bgargs=dict(extra="shelf")),
                 dict(bg="plain", els=[tagel("LOOK BACK FIRST", 960, 380, "green", True, 72), tagel("THEN PLAN", 960, 600, "ink", False, 72)])]),
    # ---------------- 2
    dict(chapter="2. The one boring reason budgets fail", text="Move two, and this is the big one. Here's why Jordan's budget died on day nine. He built it for an average month. And an average month doesn't exist.",
         scenes=[dict(bg="board", bgargs=dict(text="THE AVERAGE MONTH ISN'T REAL"), els=[num(2)])]),
    dict(text="Every month has something weird in it. A birthday. A car registration. A phone that falls in a lake. The holidays, which, fun fact, are coming whether you budgeted for them or not. These aren't surprises. They happen every year. They just don't happen every month, so they never make it onto the list.",
         scenes=[R([em("🎂", 420, 420, 180, "red"), em("🚗", 820, 420, 180, "red"), em("📱", 1220, 420, 180, "red"), em("🎁", 1600, 420, 180, "red"), tagel("NOT SURPRISES. JUST NOT MONTHLY.", 960, 760, "red", True, 56)])]),
    dict(text="So let's count Jordan's. Holiday gifts, three hundred a year. Birthdays, two forty. Car repairs, six hundred. Registration, a hundred and twenty. Saving for a new phone, three sixty. That's one thousand, six hundred and twenty dollars a year that his monthly budget pretended wasn't coming.",
         scenes=[dict(bg="plain", els=[tagel("HOLIDAYS $300", 560, 250, "red", False, 56), tagel("BIRTHDAYS $240", 1360, 250, "red", False, 56), tagel("CAR REPAIRS $600", 560, 450, "red", False, 56), tagel("REGISTRATION $120", 1360, 450, "red", False, 56), tagel("NEW PHONE $360", 960, 650, "red", False, 56)]),
                 dict(bg="board", bgargs=dict(text="$1,620 A YEAR"), els=[])]),
    dict(text="Divide by twelve, and it's a hundred and thirty-five dollars a month. That's the fix. It's called a sinking fund. A separate pot of money for the stuff you know is coming. Every month a little goes in, and when the birthday shows up, the money is already sitting there, wearing a party hat.",
         scenes=[dict(bg="board", bgargs=dict(text="$1,620 ÷ 12 = $135 / MONTH"), els=[]),
                 R([ch("maya", "smileBig", 560), em("🫙", 1300, 520, 240, "green", "SINKING FUND")], bgargs=dict(extra="shelf"))]),
    dict(text="It's November, so here's the timely version. If you'll spend three hundred dollars on gifts this year and you start saving in January next time, that's twenty-five dollars a month. Way easier than three hundred dollars in one December panic, which is basically the final boss of the year.",
         scenes=[dict(bg="outside", els=[ch("jordan", "concerned", 560, flip=True), em("🎄", 1300, 520, 240, "red", "DECEMBER PANIC")]),
                 dict(bg="plain", els=[tagel("$300 ÷ 12 = $25 / MONTH", 960, 420, "green", True, 72)])]),
    # ---------------- 3
    dict(chapter="3. Method one: 50/30/20", text="Okay. Now you have the right number and you know about the weird months. Time to pick a method. Method one is the famous one, the fifty, thirty, twenty rule. It was popularized in a book back in two thousand five, and it's still around because it's simple.",
         scenes=[dict(bg="board", bgargs=dict(text="50 / 30 / 20"), els=[num(3)])]),
    dict(text="You split your take-home pay into three buckets. Fifty percent for needs: rent, groceries, utilities, insurance, getting to work. Thirty percent for wants: eating out, games, concerts. Twenty percent for savings and paying down debt.",
         scenes=[dict(bg="plain", els=[em("🏠", 400, 400, 200, "amber", "50% NEEDS"), em("🎮", 960, 400, 200, None, "30% WANTS"), em("🐷", 1520, 400, 200, "green", "20% SAVINGS")])]),
    dict(text="On Jordan's two thousand, four hundred, that's twelve hundred for needs, seven twenty for wants, and four eighty for savings. Three numbers. You could fit it on a sticky note. Possibly Maya's sticky note.",
         scenes=[dict(bg="plain", els=[tagel("NEEDS: $1,200", 960, 250, "amber", False, 72), tagel("WANTS: $720", 960, 470, "ink", False, 72), tagel("SAVINGS: $480", 960, 690, "green", True, 72)])]),
    dict(text="Here's the good part. It doesn't care if you spend your wants money on concerts or on sneakers. It just asks you to keep the buckets roughly the right size. Hold that thought, though, because we'll stress-test this one later, and it has a weak spot.",
         scenes=[R([ch("theo", "smile", 560), em("👟", 1300, 520, 220, "green", "WANTS = YOUR CALL")], bgargs=dict(extra="couch"))]),
    # ---------------- 4
    dict(chapter="4. Method two: zero-based", text="Method two is zero-based budgeting. Before the month starts, you give every single dollar a job, until the money left without a job is zero. Not zero in your account. Zero dollars unassigned.",
         scenes=[dict(bg="board", bgargs=dict(text="EVERY DOLLAR GETS A JOB"), els=[num(4)]),
                 dict(bg="plain", els=[tagel("NOT $0 IN THE BANK", 960, 380, "red", False, 70), tagel("$0 WITHOUT A JOB", 960, 600, "green", True, 70)])]),
    dict(text="Here's Jordan's, done properly. Needs: rent eight hundred, utilities eighty, phone fifty, groceries three hundred, car insurance one fifty, gas one twenty. That's fifteen hundred. Savings, two forty. Sinking fund, one thirty-five. That leaves five hundred and twenty-five for wants.",
         scenes=[dict(bg="plain", els=[tagel("RENT $800", 560, 230, "amber", False, 56), tagel("GROCERIES $300", 1360, 230, "amber", False, 56), tagel("INSURANCE $150", 560, 430, "amber", False, 56), tagel("GAS $120", 1360, 430, "amber", False, 56), tagel("UTILITIES $80", 560, 630, "amber", False, 56), tagel("PHONE $50", 1360, 630, "amber", False, 56), tagel("NEEDS = $1,500", 960, 840, "amber", True, 60)]),
                 dict(bg="plain", els=[tagel("NEEDS $1,500", 960, 250, "amber", False, 66), tagel("SAVINGS $240", 560, 500, "green", True, 60), tagel("SINKING $135", 1360, 500, "green", True, 60), tagel("WANTS $525", 960, 750, "ink", False, 66)])]),
    dict(text="And the wants get jobs too. Eating out, one eighty. Fun, one fifty. Clothes, sixty. Subscriptions, thirty-five. And a hundred dollar buffer for whatever life throws at him. Add it all up, and it hits exactly two thousand, four hundred. Every dollar employed. Full employment. The economy of Jordan is booming.",
         scenes=[dict(bg="plain", els=[tagel("EATING OUT $180", 560, 250, "ink", False, 56), tagel("FUN $150", 1360, 250, "ink", False, 56), tagel("CLOTHES $60", 560, 450, "ink", False, 56), tagel("SUBSCRIPTIONS $35", 1360, 450, "ink", False, 56), tagel("BUFFER $100", 960, 650, "green", True, 56)]),
                 R([ch("jordan", "smileLOL", 560, flip=True), tagel("TOTAL: $2,400. LEFT: $0", 1320, 330, "green", True, 54)])]),
    dict(text="The upside: you know exactly where everything goes. The downside: it takes more time, and it's easy to overdo it. Remember the line for gum? Zero-based works best with ten to fifteen categories, not forty. You're running a budget, not a museum.",
         scenes=[dict(bg="office", els=[ch("maya", "cheeky", 560), em("🏛️", 1300, 480, 220, "red", "NOT A MUSEUM")])]),
    # ---------------- 5
    dict(chapter="5. Method three: pay yourself first", text="Method three is Maya's. Pay yourself first. On payday, before rent, before pizza, before anything, a set amount moves automatically to savings. Then the bills get paid. Then whatever is left, she spends however she wants. No guilt. No tracking every coffee.",
         scenes=[R([num(5), ch("maya", "eyesClosed", 560), em("📲", 1300, 480, 220, "green", "PAYDAY: AUTO-SAVE")], bgargs=dict(extra="couch")),
                 dict(bg="plain", els=[tagel("1. SAVE", 960, 280, "green", True, 70), tagel("2. BILLS", 960, 500, "amber", False, 70), tagel("3. SPEND THE REST", 960, 720, "ink", False, 70)])]),
    dict(text="Why does this work? Because savings that come last usually turn into zero. There's always a reason. A sale. A drop. A friend's trip. If the money leaves before you see it, you just live on what's left, and honestly, most people adjust in about a month.",
         scenes=[R([ch("jordan", "cheeky", 560, flip=True), em("🛍️", 1300, 500, 220, "red", "SAVE WHAT'S LEFT = $0")])]),
    dict(text="Maya saves two hundred and forty a month. That's ten percent of two thousand, four hundred. In one year, that's two thousand, eight hundred and eighty dollars, before any interest, and she never once had to decide to do it. The decision happened one time, on one boring Sunday.",
         scenes=[dict(bg="plain", els=[tagel("$240 × 12", 560, 420, "green", False, 72), em("➡️", 960, 420, 140), tagel("$2,880 A YEAR", 1360, 420, "green", True, 72)]),
                 R([ch("maya", "smile", 560), em("🛋️", 1300, 520, 220, "green", "DECIDED ONCE")], bgargs=dict(extra="shelf"))]),
    dict(text="So which method is best? Honestly, the one you'll still be doing in March. If you like control, zero-based. If you want simple, fifty thirty twenty. If you hate tracking, pay yourself first. You can even mix them. Maya does pay yourself first, and uses fifty thirty twenty as a quick check.",
         scenes=[dict(bg="board", bgargs=dict(text="BEST = THE ONE YOU KEEP"), els=[]),
                 dict(bg="plain", els=[tagel("LIKE CONTROL? ZERO-BASED", 960, 280, "amber", False, 56), tagel("WANT SIMPLE? 50/30/20", 960, 500, "violet", False, 56), tagel("HATE TRACKING? PAY YOU FIRST", 960, 720, "green", False, 56)])]),
    # ---------------- 6
    dict(chapter="6. Budget fun on purpose", text="Move six sounds backwards. Put fun in the budget on purpose. A budget with zero fun is like a game with no save points. You will rage quit. Usually right around day nine.",
         scenes=[dict(bg="plain", bgargs=dict(color=(30, 41, 59)), els=[num(6), em("🎮", 960, 420, 300, "red"), big("NO SAVE POINTS = RAGE QUIT", y=840, color="red", size=80)])]),
    dict(text="Fun money is what makes the rest stick. When Jordan's friend has a birthday dinner, he doesn't blow up the plan, because dinner already has a line. One fifty for fun. Spend it, enjoy it, done.",
         scenes=[dict(bg="cafe", els=[ch("jordan", "smileBig", 520, flip=True), ch("theo", "smileLOL", 1420), em("🍝", 960, 500, 180, "green", "ALREADY BUDGETED")])]),
    dict(text="The fun you didn't plan is where money leaks. Six dollars and fifty cents a day on delivery fees and snacks doesn't feel like anything. Over a year, it's two thousand, three hundred and seventy-two dollars. Five streaming and app subscriptions at twelve ninety-nine each: about sixty-five a month, seven hundred and seventy-nine a year.",
         scenes=[dict(bg="plain", els=[tagel("$6.50 A DAY", 560, 380, "red", False, 70), em("➡️", 960, 380, 140), tagel("$2,372 A YEAR", 1360, 380, "red", True, 70)]),
                 dict(bg="room", els=[em("📺", 420, 420, 160, "red"), em("🎵", 760, 420, 160, "red"), em("🎮", 1100, 420, 160, "red"), em("☁️", 1440, 420, 160, "red"), tagel("5 × $12.99 = $779 / YEAR", 960, 760, "red", True, 60)])]),
    dict(text="None of that is evil. It's just money nobody decided to spend. The goal isn't to stop having fun. It's to pick your fun, instead of letting autopay pick it for you.",
         scenes=[R([ch("maya", "explaining", 560), tagel("PICK YOUR FUN", 1300, 380, "green", True, 64)])]),
    # ---------------- 7
    dict(chapter="7. Check it, don't quit it", text="Move seven. Every budget breaks. That's not failure. That's information. The trick is a ten-minute check once a week. Look at what you spent, compare it to the plan, and adjust.",
         scenes=[R([num(7), ch("jordan", "serious", 560, flip=True), em("⏱️", 1300, 480, 220, "green", "10 MIN A WEEK")], bgargs=dict(extra="shelf"))]),
    dict(text="Blew past your eating out line? Fine. Move forty dollars from clothes, or from the buffer. You're not cheating. That's literally what the buffer is for. The only real mistake is the one Jordan made on day nine, which was deciding the whole thing was ruined and walking away.",
         scenes=[dict(bg="plain", els=[tagel("CLOTHES -$40", 560, 420, "red", False, 64), em("➡️", 960, 420, 140), tagel("EATING OUT +$40", 1360, 420, "green", True, 64)]),
                 dict(bg="cafe", els=[ch("jordan", "solemn", 520, flip=True), em("🚪", 1300, 520, 220, "red", "WALKING AWAY")])]),
    dict(text="Think of it like GPS. You miss a turn, it doesn't tell you to sell the car. It says rerouting, and keeps going. Your budget should be just as calm about it as that voice is.",
         scenes=[dict(bg="outside", els=[em("🧭", 960, 440, 280, "green"), big("REROUTING...", y=820, color="green", size=100)])]),
    # ---------------- honesty check
    dict(chapter="Honesty check: when 50% isn't enough", text="Now the honesty check. Remember fifty thirty twenty's weak spot? Look at Jordan's needs. Fifteen hundred dollars. The rule says needs should be twelve hundred. He's three hundred over, and he lives with a roommate.",
         scenes=[dict(bg="plain", els=[ch("jordan", "concerned", 360, h=560, flip=True), tagel("RULE: $1,200 (50%)", 1180, 330, "green", False, 60), tagel("JORDAN: $1,500 (62.5%)", 1180, 560, "red", True, 60)])]),
    dict(text="That's normal. In the Bureau of Labor Statistics spending survey, housing alone takes about a third of what the average household spends. When you're young and earning less, rent can eat a bigger slice. For a lot of people starting out, needs land closer to sixty percent.",
         scenes=[dict(bg="office", els=[em("🏠", 560, 460, 280, "amber", "HOUSING ≈ 1/3 OF SPENDING"), tagel("STARTING OUT: ~60% NEEDS", 1360, 330, "amber", False, 52)])]),
    dict(text="So don't treat fifty thirty twenty like a law. Treat it like a starting point. Jordan's real split is roughly sixty-two, twenty-two, sixteen. Needs, sixty-two and a half percent. Wants, about twenty-two. Savings plus the sinking fund, about sixteen. That's okay. The direction matters more than hitting the exact numbers.",
         scenes=[dict(bg="plain", els=[tagel("NEEDS $1,500 ≈ 62%", 960, 250, "amber", False, 66), tagel("WANTS $525 ≈ 22%", 960, 470, "ink", False, 66), tagel("SAVE + SINK $375 ≈ 16%", 960, 690, "green", True, 66)]),
                 dict(bg="board", bgargs=dict(text="A STARTING POINT, NOT A LAW"), els=[])]),
    dict(text="And here's the catch nobody mentions. The fastest way to free up money is usually not skipping lattes. It's the big three: housing, transportation and food. Ten dollars a month saved on coffee is nice. Two hundred a month saved by picking a cheaper place or a roommate is a different game.",
         scenes=[dict(bg="plain", els=[em("🏠", 420, 420, 200, "green"), em("🚗", 960, 420, 200, "green"), em("🛒", 1500, 420, 200, "green"), tagel("THE BIG THREE", 960, 760, "green", True, 70)]),
                 dict(bg="plain", els=[tagel("COFFEE: -$10/MO", 560, 420, "ink", False, 64), tagel("ROOMMATE: -$200/MO", 1360, 420, "green", True, 64)])]),
    dict(chapter="Honesty check: the common mistakes", text="Two more mistakes worth naming. One, the old rule says keep rent under thirty percent of your gross pay. For Jordan, that's nine hundred and thirty-six. But take-home pay is smaller than gross, so even rent that passes that test can squeeze everything else. Always check rent against take-home too.",
         scenes=[dict(bg="hallway", els=[ch("theo", "suspicious", 480), tagel("30% OF GROSS = $936", 1300, 330, "amber", False, 56), tagel("CHECK TAKE-HOME TOO", 1300, 560, "red", True, 56)])]),
    dict(text="Two, if your income jumps around, from tips, gigs or changing hours, budget on your lowest normal month. When a big month comes, the extra goes to the sinking fund or savings first. That way a slow month is annoying, not a crisis.",
         scenes=[dict(bg="plain", els=[dict(t="chart", series=[{"name": "Pay", "color": "amber", "ys": [1900, 2600, 2100, 2800, 2000, 2500]}, {"name": "Plan", "color": "green", "ys": [1900] * 6, "dy": 30}], xlabels=["JAN", "FEB", "MAR", "APR", "MAY", "JUN"], label="Made-up example", fmt="${v}", box=(300, 140, 1640, 740))])]),
    dict(text="And if all of this still feels like too much, start with just one thing. Pick a number, any number, and move it to savings on payday. Even twenty dollars. A budget that's imperfect but alive beats a perfect one that died on day nine.",
         scenes=[R([ch("maya", "smile", 560), em("🌱", 1300, 500, 220, "green", "START WITH $20")], bgargs=dict(extra="shelf"))]),
    # ---------------- close
    dict(chapter="Back to the 28th", text="So, back to the twenty-eighth. Next month. Jordan deleted thirty of his forty categories, including gum. He set up a two-hundred-forty-dollar transfer on payday and a sinking fund called Weird Stuff.",
         scenes=[R([ch("jordan", "driven", 560, flip=True), em("🗑️", 1250, 520, 200, "green", "40 → 10 CATEGORIES")], bgargs=dict(night=True)),
                 R([ch("jordan", "smile", 560, flip=True), em("🫙", 1300, 520, 220, "green", "WEIRD STUFF FUND")], bgargs=dict(night=True))]),
    dict(text="Theo's birthday happened again. Dinner was already in the plan. On the twenty-eighth, Jordan has money left, and for the first time, he knows exactly why.",
         scenes=[dict(bg="cafe", els=[ch("jordan", "smileLOL", 520, flip=True), ch("theo", "smileBig", 1420), em("🎉", 960, 440, 200, "green")])]),
    dict(text="Here's the one-line version. A budget fails when it's built for a perfect month, so build yours for a real one.",
         scenes=[dict(bg="board", bgargs=dict(text="BUILD IT FOR A REAL MONTH"), els=[])]),
    dict(text="Your move this week. Find your real take-home pay. List the things that happen every year but not every month, and divide by twelve. Then pick one method and set up one automatic transfer on payday. That's it. Ten minutes.",
         scenes=[R([em("✅", 560, 300, 130, "green"), tagel("FIND YOUR TAKE-HOME", 1100, 300, "green", False, 50), em("✅", 560, 480, 130, "green"), tagel("YEARLY STUFF ÷ 12", 1100, 480, "green", False, 50), em("✅", 560, 660, 130, "green"), tagel("1 AUTO-TRANSFER", 1100, 660, "green", False, 50)], bgargs=dict(win=False))]),
    dict(text="Next time: student loans, before you sign. Subsidized versus unsubsidized, interest that starts earlier than you'd think, and the total cost nobody shows you. Subscribe so you don't miss it. Education, not advice. See you there.",
         scenes=[R([ch("maya", "smileBig", 280), ch("jordan", "smile", 800, flip=True), em("📺", 1490, 420, 280, "green", "NEXT: STUDENT LOANS")], bgargs=dict(extra="couch", win=False))]),
]
