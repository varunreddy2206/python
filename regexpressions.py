# import re 

# xyz=r'[a-z]'
# text="the trustees have approved the following updated policy document"

# match=re.findall(xyz,text)

# print(match)

# x=r'[A-Z,a-z]'
# text="Divakar Labbe"

# match=re.findall(x,text)
# print(match)

###################################################

# import re

# # v=r'[0-9]'
# # v=r'[^aet ]'

# v=r'xyw+e*z'

# text="xyz xywz xyez"

# match=re.findall(v,text)
# print(match)

# xyz=r'varun'

# x="my name is varun"

# match=re.match(xyz,x)

# if match:
#     print("match found",match.group())
# else:
#     print("no match found")

##################################################

# import re

# mob='+91-9866541755'
# xyz=r'^\+?\d{1,3}[-\s]?\d{10}$'

# if re.match(xyz,mob):
#     print("valid no.")

# else:
#     print("invalid")

##################################################

# import re

# x="varunredd$@gmail.com"

# xyz=r'^[A-Za-z0-9!$#]+@[a-z]+\.[a-z]{2,3}$'

# if re.match(xyz,x):
#     print("valid email")

# else:
#     print("invalid email")

####################################################

# import re

# password='Varun@2206#123'

# xyz=r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%&])[A-Za-z\d@$!%]{10,}'

# if re.match(xyz,password):
#     print("strong password")

# else:
#     print("weak password")

########################################################

# import re

# emails = [
#     'John123@example-domain.com',
#     'A.User@sub.mail-server.co.uk',
#     'jane@example.com',
#     'P.Name@company.org',
#     'X1@sub-example.com',
#     'user@domain.c'
# ]

# pattern = r'^[A-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'

# for email in emails:
#     if re.match(pattern, email):
#         print(f"{email} -> Valid")
#     else:
#         print(f"{email} -> Invalid")

##################################################

# import re

# numbers = [
#     '9876543210',
#     '8123456789',
#     '+91-9876543210',
#     '+91 9876543210',
#     '919876543210',
#     '6123456789',
#     '1234567890'
# ]

# pattern = r'^(\+91[\-\s]?|91[\-\s]?)?[789]\d{9}$'

# for number in numbers:
#     if re.match(pattern, number):
#         print(f"{number} -> Valid")
#     else:
#         print(f"{number} -> Invalid")

####################################################

# import re
# text1='''Live ScoresScheduleArchivesNewsAll Stories  Premium Editorials Latest NewsTopicsSpotlightOpinionsSpecialsStats & AnalysisInterviewsLive BlogsHarsha BhogleSeries  India tour of Australia, 2024-25 SA20, 2025 ICC Champions Trophy, 2025 West Indies tour of Pakistan, 2025 Big Bash League 2024-25 Sri Lanka tour of New Zealand, 2024-25 Vijay Hazare Trophy 2024-25 Bangladesh Premier League, 2024-25 Ireland Womens tour of India, 2025 All Series »Teams   Test Teams India Afghanistan Ireland Pakistan Australia Sri Lanka Bangladesh England West Indies South Africa Zimbabwe New Zealand   Associate Malaysia Nepal Germany Namibia Denmark Singapore Papua New Guinea Kuwait Vanuatu Jersey Oman Fiji   More... Videos  All Videos Categories Playlists   RankingsICC Rankings - MenICC Rankings - Women More World Test Championship World Cup Super League Auction Tracker Photos Mobile AppsCareersContact Us  {{premiumScreenName}}     My Account Sign Out MATCHESMLS vs SYS - Ings BreakSEC vs MICT - PreviewRAJ vs TN - LiveHAR vs BEN - LiveWEL vs CD - CD WonAllLive NowTodayINTERNATIONALPakistan v West Indies, 2025Pakistan A vs West Indies2-day Warm-up MatchSL tour of NZ 2024-25New Zealand vs Sri Lanka2nd ODINew Zealand vs Sri Lanka3rd ODISouth Africa vs Pakistan,2024-25South Africa vs Pakistan2nd TestT20 LEAGUESA20Sunrisers Eastern Cape vs MI Cape Town1st MatchDurban Super Giants vs Pretoria Capitals2nd MatchBBL 2024-25Perth Scorchers vs Melbourne Renegades26th MatchSydney Thunder vs Hobart Hurricanes27th MatchMelbourne Stars vs Sydney Sixers28th MatchHobart Hurricanes vs Sydney Thunder29th MatchSydney Sixers vs Perth Scorchers30th MatchAdelaide Strikers vs Brisbane Heat31st MatchBPL, 2024-25Dhaka Capitals vs Rangpur Riders11th MatchSylhet Strikers vs Fortune Barishal12th MatchFortune Barishal vs Rangpur Riders  LIVE13th MatchDhaka Capitals vs Chittagong Kings14th MatchDurbar Rajshahi vs Khulna Tigers15th MatchDhaka Capitals vs Sylhet Strikers16th MatchSuper Smash 2024-25Wellington vs Central Districts10th MatchCanterbury vs Auckland11th MatchDOMESTICVijay Hazare TrophyRajasthan vs Tamil Nadu  LIVE2nd Preliminary quarter finalHaryana vs Bengal  LIVE1st Preliminary quarter finalTBC vs TBC4th Preliminary quarter finalTBC vs TBC3rd Preliminary quarter finalWOMENIndia Women v Ireland Women, 2025India Women vs Ireland Women1st ODI (ICC Championship Match)   Unable to resolve the request Unfortunately the page you requested was not found. Some of the possible reasons could be:  The page you were looking for might no longer exist. Please try the options below. There was a temporary problem. Please make sure you refresh/reload the page your were on before this one.  To navigate to the page you were looking for, please try any one of the following  Home - To return to cricbuzz Homepage. Live Cricket Score - For the scores of the current matches. Cricket Schedule - For Cricket Schedule of upcoming International, domestic and T20 Series etc. Cricket Match Archives - For Scorecards, Commentary and Results of all international cricket matches. Latest Cricket News - News from the World of Cricket. Cricket Photo 
# Gallery - For Latest Photos from around the cricketing world.  Search on cricbuzz   To navigate to the page you were looking for, please try any one of the following:  MATCHESBangladesh Premier League, 2024-25 14th Match, SylhetDHCPCKThu, 09 Jan 12:30 GMTBangladesh Premier League, 2024-25 13th Match, SylhetBRSALRGRThu, 09 Jan 07:30 GMTSA20, 2025 1st Match, GqeberhaSECMICTThu, 09 Jan 15:30 GMTBig Bash League 2024-25 28th Match, MelbourneMLSSYSThu, 09 Jan 08:15 GMTVijay Hazare Trophy 2024-25 2nd Preliminary quarter final, VadodaraRAJTNThu, 09 Jan 03:30 GMTMore Matches    LATEST NEWS   Steve Smith to lead Australia in Sri Lanka8h ago   Optimism around Shami's return; Akash Deep ruled out for a month17h ago  Guptill retires from international cricket18h ago  SA20 aims to be IPL's biggest little brother20h ago  NZ demolish SL despite Theekshana's hattrick23h ago  More News       LATEST PHOTOS   Australia vs India, 5th Test, Day 3Sun, Jan 05 2025  Australia vs India, 5th Test, Day 1Fri, Jan 03 2025  Australia vs India, 4th Test, Day 5Mon, Dec 30 2024  Australia vs India, 4th Test, Day 4Sun, Dec 29 2024  Australia vs India, 4th Test, Day 3Sat, Dec 28 2024  Australia vs India, 4th Test, Day 2Fri, Dec 27 2024  More Photos '''


# pattern=r'\bIndia\b'
# match=re.findall(pattern,text1)
# print(match)

######################################

import re 

txt='''Skip to



Main content





      Keyboard shortcuts






Search

alt
+
/







Cart

shift
+
alt
+
c







Home

shift
+
alt
+
h







Orders

shift
+
alt
+
o





Show/hide shortcuts, shift, alt, z

Show/Hide shortcuts

shift
+
alt
+
z

















.in









                   Delivering to Mumbai 400001


                   Update location





















All


Select the department you want to search in

All Categories
Alexa Skills
Amazon Devices
Amazon Fashion
Amazon Fresh
Amazon Fresh Meat
Amazon Pharmacy
Appliances
Apps & Games
Audible Audiobooks
Baby
Beauty
Books
Car & Motorbike
Clothing & Accessories
Collectibles
Computers & Accessories
Deals
Electronics
Furniture
Garden & Outdoors
Gift Cards
Grocery & Gourmet Foods
Health & Personal Care
Home & Kitchen
Industrial & Scientific
Jewellery
Kindle Store
Luggage & Bags
Luxury Beauty
Movies & TV Shows
MP3 Music
Music
Musical Instruments
Office Products
Pet Supplies
Prime Video
Shoes & Handbags
Software
Sports, Fitness & Outdoors
Subscribe & Save
Tools & Home Improvement
Toys & Games
Under ₹500
Video Games
Watches













Search Amazon.in

























EN





Hello, sign in
Account & Lists



Returns
& Orders










        Cart













All










Fresh
MX Player
Sell
Best Sellers
Mobiles
Today's Deals
Prime
Customer Service
 Electronics
Home & Kitchen
Amazon Pay
New Releases
Fashion
Computers
Car & Motorbike
Books
Toys & Games
Sports, Fitness & Outdoors
Beauty & Personal Care
Gift Cards
Home Improvement
Custom Products
Health, Household & Personal Care
Grocery & Gourmet Foods
Video Games
Baby
Pet Supplies
Audible
Gift Ideas
AmazonBasics
Subscribe & Save
Kindle eBooks


























      Audible Membership





      New & Trending






      Categories






      More to Explore


















































Amazon BestsellersOur most popular products based on sales.  Updated frequently.











Bestsellers in Audible Books & Originals#1Atomic Habits: Tiny Changes, Remarkable ResultsJames Clear4.6 out of 5 stars 100,089Audible Audiobook1 offer from ₹820.00#2The Psychology of Money: Timeless Lessons on Wealth, Greed, and HappinessMorgan Housel4.6 out of 5 stars 69,054Audible Audiobook1 offer from ₹668.00#3How to Talk to Anyone: 92 Little Tricks for Big Success in RelationshipsLeil Lowndes4.4 out of 5 stars 14,367Audible Audiobook1 offer from ₹844.00#4Dopamine Detox: A Short Guide to Remove Distractions and Get Your Brain to Do Hard Things (Productivity Series, Book 1)Thibaut Meurisse4.4 out of 5 stars 12,343Audible Audiobook1 offer from ₹233.00#5Ikigai: The Japanese Secret to a Long and Happy LifeHéctor García4.6 out of 5 stars 56,983Audible Audiobook1 offer from ₹615.00#6Nexus: A Brief History of Information Networks from the Stone Age to AIYuval Noah Harari4.5 out of 5 stars 3,468Audible Audiobook1 offer from ₹1,230.00#7Thinking, 
Fast and SlowDaniel Kahneman4.5 out of 5 stars 31,295Audible Audiobook1 offer from ₹957.00#8The Courage to Be Disliked : How to Free Yourself, Change Your Life and Achieve Real HappinessFumitake Koga4.6 out of 5 stars 15,819Audible Audiobook1 offer from ₹1,063.00#9Rich Dad Poor Dad: What the Rich Teach Their Kids About Money - That the Poor and Middle Class Do Not!Robert T. Kiyosaki4.5 out of 5 stars 18,175Audible Audiobook1 offer from ₹844.00#10SapiensYuval Noah Harari4.7 out of 5 stars 121,189Audible Audiobook1 offer from ₹957.00#11The Let Them Theory: A Life-Changing Tool That Millions of People Can’t Stop Talking AboutMel Robbins4.7 out of 5 stars 903Audible Audiobook1 offer from ₹1,171.00#12Autobiography of a YogiParamahansa Yogananda4.6 out of 5 stars 11,449Audible Audiobook1 offer from ₹1,126.00#13The 5 AM ClubRobin Sharma4.5 out of 5 stars 34,289Audible Audiobook1 offer from ₹759.00#14The Subtle Art of Not Giving a F*ck: A Counterintuitive Approach to Living a Good LifeMark Manson4.5 out of 5 stars 147,287Audible Audiobook1 offer from ₹1,181.00#15The Intelligent Investor Rev Ed.Benjamin Graham4.5 out of 5 stars 47,316Audible Audiobook1 offer from ₹2,082.00#16The Compound Effect: Multiply Your Success One Simple Step at a TimeDarren Hardy4.6 out of 5 stars 18,923Audible Audiobook1 offer from ₹608.00#17The Hard Thing About Hard Things: Building a Business When There Are No Easy AnswersBen Horowitz4.6 out of 5 stars 14,403Audible Audiobook1 offer from ₹1,350.00#1811 Rules for Life: Secrets to Level UpChetan Bhagat4.6 out of 5 stars 1,480Audible Audiobook1 offer from ₹69.00#19The Diary of a CEO: The 33 Laws of Business and LifeSteven Bartlett4.5 out of 5 stars 2,602Audible Audiobook1 offer from ₹1,093.00#20Harry Potter and the Philosopher's Stone, Book 1J.K. Rowling4.7 out of 5 stars 119,502Audible Audiobook1 offer from ₹999.00#21The Almanack of Naval Ravikant: A Guide to Wealth and HappinessEric Jorgenson4.6 out of 5 stars 19,792Audible Audiobook1 offer from ₹586.00#22Never Split the Difference: Negotiating as if Your Life Depended on ItChris Voss4.6 out of 5 stars 44,064Audible Audiobook1 offer from ₹820.00#23The Power of Your Subconscious MindJoseph Murphy3.9 out of 5 stars 23Audible Audiobook1 offer from ₹267.00#24The Fyodor Dostoyevsky Complete Collection: The Brothers Karamazov; Crime and Punishment; The Idiot; Notes from the Underground; The Demons; Novellas; Complete Short Stories; Essays; and LettersFyodor DostoyevskyAudible Audiobook1 offer from ₹5,694.00#25You Are the Placebo: Making 
Your Mind MatterAdam Boyce4.6 out of 5 stars 8,192Audible Audiobook1 offer from ₹836.00#26The Nvidia Way: Jensen Huang and the Making of a Tech GiantTae Kim4.6 out of 5 stars 214Audible Audiobook1 offer from ₹820.00#27Norwegian WoodHaruki Murakami4.5 out of 5 stars 19,819Audible Audiobook1 offer from ₹888.00#28Becoming Supernatural: How Common People Are Doing the UncommonAdam Boyce4.7 out of 5 stars 20,528Audible Audiobook1 offer from ₹938.00#29Clear Thinking: Turning Ordinary Moments into Extraordinary ResultsShane Parrish4.5 out of 5 stars 1,936Audible Audiobook1 offer from ₹957.00#30The Golden Road: How Ancient India Transformed the WorldWilliam Dalrymple4.6 out of 5 stars 487Audible Audiobook1 offer from ₹683.00#31Start with Why: How Great Leaders Inspire Everyone to Take ActionSimon Sinek4.5 out of 5 stars 23,916Audible Audiobook1 offer from ₹888.00#32Zero to OnePeter Thiel4.5 out of 5 stars 31,845Audible Audiobook1 offer from ₹615.00#33Focus on What Matters: A Collection of Stoic Letters on Living WellDarius Foroux4.5 out of 5 stars 641Audible Audiobook1 offer from ₹754.00#34Life's Amazing Secrets: How to Find Balance and Purpose in Your LifeGaur Gopal Das4.6 out of 5 stars 24,053Audible Audiobook1 offer from ₹1,005.00#35Think and Grow RichNapoleon Hill4.4 out of 5 stars 79,437Audible Audiobook1 offer from ₹166.00#36The Mountain Is You: Transforming Self-Sabotage into Self-MasteryBrianna Wiest4.3 out 
of 5 stars 20,754Audible Audiobook1 offer from ₹668.00#37The Power of Now: A Guide to Spiritual EnlightenmentEckhart Tolle4.5 out of 5 stars 60,260Audible Audiobook1 offer from ₹656.00#38Let's Talk Money: You've Worked Hard for It, Now Make It Work for YouMonika Halan4.6 out of 5 stars 4,161Audible Audiobook1 offer from ₹371.00#39Gunahon ka Devta (Hindi Edition)धर्मवीर भारतीAudible Audiobook1 offer from ₹210.00#40Inner Engineering: A Yogi's Guide to JoySadhguru4.6 out of 5
 stars 21,857Audible Audiobook1 offer from ₹879.00#41Make Epic MoneyAnkur Warikoo4.4 out of 5 stars 801Audible Audiobook1 offer from ₹879.00#4212 Rules for Life: An Antidote to ChaosJordan B. Peterson4.5 out of 5 stars 77,228Audible Audiobook1 offer from ₹957.00#43The Alchemist: A Fable About Following Your DreamPaulo Coelho4.6 out of 5 stars 45,512Audible Audiobook1 offer from ₹1,181.00#44Project Hail MaryAndy Weir4.7 out of 5 stars 131,413Audible Audiobook1 offer from ₹1,003.00#45Feel-Good Productivity: How to Do More of What Matters to YouAli Abdaal4.5 out of 5 stars 2,699Audible Audiobook1 offer from ₹957.00#46Harry Potter and the Goblet of Fire, Book 4J.K. Rowling4.7 out of 5 stars 77,036Audible Audiobook1 offer from ₹1,599.00#47The 48 Laws of PowerRobert Greene3.9 out of 5 stars 10Audible Audiobook1 offer from ₹773.00#48Men Are from Mars, Women Are from Venus: The Classic Guide to Understanding the Opposite SexJohn Gray4.5 out of 5 stars 14,913Audible Audiobook1 offer from ₹1,519.00#49Hitchhiker's Guide to the GalaxyDouglas Adams4.4 out of 5 stars 23,975Audible Audiobook1 offer from ₹323.00#50Harry Potter and the Chamber of Secrets, Book 2J.K. Rowling4.7 out of 5 stars 96,944Audible Audiobook1 offer from ₹999.00←Previous page12Next page→Hot New Releasesin Audible Books & OriginalsMovers and Shakersin Audible Books & OriginalsMost Wished Forin Audible Books & Originals









 Any Department






















                    Your recently viewed items and featured recommendations         View or edit your browsing history     After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.         Your recently viewed items and featured recommendations      ›    View or edit your browsing history     After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.




    Back to top






Get to Know Us


About Amazon


Careers


Press Releases


Amazon Science





Connect with Us


Facebook


Twitter


Instagram





Make Money with Us


Sell on Amazon


Sell under Amazon Accelerator


Protect and Build Your Brand


Amazon Global Selling


Supply to Amazon


Become an Affiliate


Fulfilment by Amazon


Advertise Your Products


Amazon Pay on Merchants





Let Us Help You


Your Account


Returns Centre


Recalls and Product Safety Alerts


100% Purchase Protection


Amazon App Download


Help

















English



India






AbeBooksBooks, art& collectibles
Amazon Web ServicesScalable CloudComputing Services
AudibleDownloadAudio Books
IMDbMovies, TV& Celebrities
 

ShopbopDesignerFashion Brands

Amazon BusinessEverything ForYour Business
Prime Now 2-Hour Deliveryon Everyday Items
Amazon Prime Music100 million songs, ad-freeOver 15 million podcast episodes



Conditions of Use & Sale Privacy Notice Interest-Based Ads © 1996-2025, Amazon.com, Inc. or its affiliates

'''

# pattern=r'\d{0,4}\d+(\D)'
# match=re.findall(pattern,txt)
# print(match)


# def even_num(number):
#       if number%2==0:
#             return True
#       else:
#             return False

# result=even_num(7)
# print(result)

# def add_number(a,b):
#       return a+b

# result=add_number(3,3)
# print(result)



