# -*- coding: utf-8 -*-
"""
Content data for the Curefoods website rebuild.
Edit this file to change copy/content, then run `python3 generate.py`.
"""

SITE = {
    "name": "Curefoods",
    "legal_name": "Curefoods India Pvt. Ltd.",
    "domain": "https://curefoods.in",
    "tagline": "India's house of food brands",
    "description": (
        "Curefoods is India's house of food brands, building and scaling "
        "category-defining F&B brands — from healthy meals to biryani, pizza to "
        "desserts — out of 281 cloud kitchens, 99 kiosks and 122 restaurants."
    ),
    "short_description": (
        "India's house of food brands. 281 cloud kitchens, 99 kiosks, "
        "122 restaurants nationwide."
    ),
    "founder": "Ankit Nagori",
    "founded_year": "2020",
    "hq": "Bengaluru, Karnataka, India",
    "stats": [
        {"value": "281", "label": "Cloud kitchens"},
        {"value": "99", "label": "Kiosks"},
        {"value": "122", "label": "Restaurants"},
    ],
    "social": {
        "youtube": "https://www.youtube.com/@the_curefoods",
        "linkedin": "https://in.linkedin.com/company/curefoods",
        "twitter": "https://x.com/the_curefoods/",
    },
    "contact_email": "hello@curefoods.in",
    "support_email": "support@curefoods.in",
    "press_email": "press@curefoods.in",
    "careers_email": "careers@curefoods.in",
}

NAV = [
    {"label": "Our Brands", "href": "/brands.html"},
    {"label": "About Us", "href": "/about.html"},
    {"label": "Newsroom", "href": "/newsroom.html"},
    {"label": "Careers", "href": "/careers.html"},
    {"label": "FAQ", "href": "/faq.html"},
]

# Each brand: slug, name, category, color, short description, long story,
# menu highlights, cities, founded year, faq (brand-specific, feeds FAQPage schema)
BRANDS = [
    {
        "slug": "eatfit",
        "name": "Eatfit",
        "full_name": "Eatfit",
        "category": "Healthy Bowls",
        "color": "#02205F",
        "logo": "/assets/images/logos/eatfit.png",
        "photo": "/assets/images/photos/eatfit-food.jpg",
        "domain": "https://www.eatfit.in/",
        "instagram": "https://www.instagram.com/the_eatfit",
        "swiggy": "https://www.swiggy.com/direct/brand/76139?source=swiggy-direct&subSource=generic",
        "ownly": "https://ownly.food/app/brand/BR112474",
        "tagline": "Not just a meal - It's a Bowl",
        "description": (
            "Eatfit is Curefoods' flagship healthy-eating brand, delivering "
            "calorie-tracked, macro-balanced meals. Our core offerings are built "
            "around two everyday eating needs: healthy meals that perform, and "
            "Indian comfort food that feels like home. At Eatfit, we make food "
            "for real life: balanced, trustworthy and full of flavour, without "
            "making wellness feel like work."
        ),
        "story": (
            "Founded as the first brand under Curefoods in 2020, Eatfit set out to prove "
            "that healthy food could be convenient, affordable and genuinely tasty at scale. "
            "Every meal is nutrition-labelled with calories, protein and macros, and the menu "
            "rotates seasonally with dietitian input."
        ),
        "menu": [
            {"veg": False, "name": "Peri Peri Chicken Rice Bowl", "detail": "420 kcal · 32g protein"},
            {"veg": True, "name": "Paneer Tikka Overload Bowl", "detail": "390 kcal · 24g protein"},
            {"veg": False, "name": "Grilled Chicken Salad", "detail": "310 kcal · 28g protein"},
            {"veg": True, "name": "Quinoa Khichdi", "detail": "340 kcal · 14g protein"},
        ],
        "cities": ["Bengaluru", "Chennai", "Hyderabad", "Coimbatore", "Mysore", "Pune", "Mumbai", "Delhi NCR", "Chandigarh"],
        "founded": "2020",
        "faq": [
            {
                "q": "What makes Eatfit different from a regular food delivery brand?",
                "a": "Every Eatfit dish is nutrition-labelled with exact calories, protein, carbs and fat, "
                     "designed with dietitians so customers can hit fitness goals without home-cooking.",
            },
            {
                "q": "Which cities is Eatfit available in?",
                "a": "Eatfit operates in Bengaluru, Chennai, Hyderabad, Coimbatore, Mysore, Pune, Mumbai, "
                     "Delhi NCR and Chandigarh, with kitchens expanding as Curefoods opens new "
                     "cloud-kitchen clusters.",
            },
            {
                "q": "Is Eatfit good for weight loss?",
                "a": "Eatfit portions and labels every meal with exact calories, protein, carbs and fat, "
                     "which makes it easier to track intake toward a weight or fitness goal. As with any "
                     "meal plan, results depend on overall diet and activity, not any single meal.",
            },
            {
                "q": "Does Eatfit have both vegetarian and non-vegetarian meals?",
                "a": "Yes — Eatfit's menu spans both, from grilled chicken and Peri Peri chicken rice "
                     "bowls to paneer and quinoa khichdi options, all nutrition-labelled the same way.",
            },
            {
                "q": "Can I order Eatfit as a one-time meal or only as a subscription?",
                "a": "Eatfit meals can be ordered as a one-time meal through online platforms — Swiggy, "
                     "Zomato and Ownly. We no longer offer subscription meals.",
            },
            {
                "q": "How do I report an issue with my Eatfit order?",
                "a": "You can report an order issue in the Eatfit app under Orders, by emailing "
                     "hello@eatfit.in, or via Eatfit's WhatsApp support.",
            },
        ],
    },
    {
        "slug": "sharief-bhai",
        "name": "Sharief Bhai Biryani",
        "full_name": "Sharief Bhai Biryani",
        "category": "Biryani, Mandi, Shawarma & More",
        "color": "#B8330F",
        "logo": "/assets/images/logos/sharief-bhai.png",
        "photo": "/assets/images/photos/sharief-bhai-store.jpg",
        "domain": "https://www.shariefbhai.com",
        "instagram": "https://www.instagram.com/shariefbhai_biryani/",
        "swiggy": "https://www.swiggy.com/direct/brand/469102?source=swiggy-direct&subSource=instagram",
        "zomato": "https://link.zomato.com/xqzv/6",
        "ownly": "https://ownly.food/app/brand/BR112583",
        "tagline": "Old-city biryani and Arabian mandi, done right.",
        "description": (
            "Sharief Bhai Biryani was born from a deep respect for Dakhni Muslim household "
            "cuisine — the kind of food prepared with care for a dawat, served "
            "generously, and shared with pride. The rich, slow-cooked flavours of "
            "the Deccan — biryanis layered with fragrant Zeeraka Samba rice, paya "
            "simmered through the night, kebabs charred over open flame — these "
            "were traditions too precious to remain behind closed doors."
        ),
        "story": (
            "Sharief Bhai was built to capture the soul of Bengaluru's Mosque Road biryani "
            "culture — slow-cooked dum biryani, mandi and ghee rice — and take it city-wide "
            "without losing the recipe. The brand runs a growing lineup of ghee rice SKUs "
            "alongside its core biryani and mandi range, and operates a mix of delivery-only "
            "kitchens and dine-in flagship stores. Its sibling brand, Roz Shawarma, spun out "
            "to focus purely on shawarma and rolls for a faster, lighter occasion."
        ),
        "menu": [
            {"veg": False, "name": "Hyderabadi Chicken Dum Biryani", "detail": "Signature slow-dum biryani"},
            {"veg": False, "name": "Chicken Mandi", "detail": "Arabian-style rice & smoked chicken"},
            {"veg": True, "name": "Ghee Rice Combo", "detail": "Multiple ghee rice variants"},
            {"veg": False, "name": "Seekh Kebab Platter", "detail": "Char-grilled kebabs"},
        ],
        "cities": ["Bengaluru", "Chennai", "Coimbatore", "Mysore", "Mangalore", "Manipal", "Tumkur", "Hassan", "Puducherry", "Hosur", "Palakkad"],
        "store_count": "54",
        "founded": "2021",
        "flagship": "Mosque Road, Frazer Town, Bengaluru",
        "faq": [
            {
                "q": "Where is Sharief Bhai's flagship store?",
                "a": "Sharief Bhai's flagship dine-in store is on Mosque Road in Frazer Town, Bengaluru — "
                     "the city's historic biryani and old-city food street.",
            },
            {
                "q": "Is Sharief Bhai available outside Karnataka?",
                "a": "Sharief Bhai runs 54 stores across 11 cities in Karnataka (Bengaluru, Mysore, "
                     "Mangalore, Manipal, Tumkur, Hassan), Tamil Nadu (Chennai, Coimbatore, Hosur), "
                     "Puducherry and Palakkad — it does not currently have stores in Hyderabad or "
                     "the rest of Telangana.",
            },
            {
                "q": "What is the difference between Sharief Bhai and Roz Shawarma?",
                "a": "Roz Shawarma is Sharief Bhai's sibling brand focused only on shawarma and rolls, "
                     "sharing kitchens but running a lighter, faster menu for quick-bite occasions.",
            },
            {
                "q": "Is Sharief Bhai's meat halal?",
                "a": "Yes — Sharief Bhai uses 100% halal meat across all its outlets.",
            },
            {
                "q": "Does Sharief Bhai have vegetarian options?",
                "a": "Yes — alongside its biryani and mandi range, Sharief Bhai serves vegetarian dishes "
                     "such as ghee rice, soya chaap biryani and paneer-based items.",
            },
            {
                "q": "Is Sharief Bhai available outside India?",
                "a": "Sharief Bhai opened its first international outlet at BurJuman Mall in Dubai in "
                     "November 2024, marking the brand's expansion into the UAE alongside its home "
                     "market in India.",
            },
            {
                "q": "What type of biryani does Sharief Bhai serve?",
                "a": "Sharief Bhai serves slow-cooked, dum-style biryani made with aromatic rice, "
                     "carefully marinated meat and a blend of spices for a rich and flavourful taste.",
            },
            {
                "q": "What are the best-selling or must-try dishes at Sharief Bhai?",
                "a": "The Har-dil-Azeez biryani may reign supreme, but every dish carries the same "
                     "purpose: to make every meal feel like an occasion.",
            },
            {
                "q": "Is Sharief Bhai available for dine-in and delivery?",
                "a": "Yes. Sharief Bhai serves customers through both dine-in outlets and online "
                     "food delivery, depending on the location.",
            },
            {
                "q": "Can I order Sharief Bhai for parties or large gatherings?",
                "a": "Yes. Sharief Bhai can be a great choice for family gatherings, celebrations "
                     "and group meals. Customers can explore available bulk-ordering options based "
                     "on their location.",
            },
            {
                "q": "What makes Sharief Bhai's biryani unique?",
                "a": "Sharief Bhai biryani is known for its authentic Dakhni flavours, traditional "
                     "dum-style cooking, rich aroma, and generous portions.",
            },
            {
                "q": "What is Dakhni cuisine?",
                "a": "Dakhni cuisine is a rich blend of Mughlai and South Indian influences, known "
                     "for slow-cooked dishes, aromatic spices, soulful gravies, biryanis, kebabs and "
                     "festive recipes.",
            },
            {
                "q": "Is Sharief Bhai's biryani spicy?",
                "a": "Sharief Bhai biryani is made with balanced spices — rich and aromatic, but "
                     "not overpowering.",
            },
            {
                "q": "Does Sharief Bhai offer Bucket Biryani packs?",
                "a": "Yes — Bucket Biryani packs are available and are designed for get-togethers, "
                     "family meals and group celebrations.",
            },
            {
                "q": "What is the Dakhni Thaal at Sharief Bhai?",
                "a": "The Dakhni Thaal is a dine-in experience with 11 items in a single thali, "
                     "serving up to 4 people.",
            },
            {
                "q": "Does Sharief Bhai run any offers or discounts?",
                "a": "Yes, Sharief Bhai regularly runs offers across its outlets and delivery "
                     "platforms.",
            },
            {
                "q": "Does Sharief Bhai have seasonal or limited-time dishes?",
                "a": "Yes, Sharief Bhai introduces exclusive dishes during festive seasons and "
                     "special occasions.",
            },
            {
                "q": "What hygiene and safety measures does Sharief Bhai follow?",
                "a": "Sharief Bhai follows strict hygiene protocols across outlets, using fresh "
                     "ingredients, maintaining clean kitchens, and running regular quality checks.",
            },
            {
                "q": "What awards has Sharief Bhai won?",
                "a": "Sharief Bhai has won Best in Biryani by Swiggy (2025), Best Biryani "
                     "Restaurant by Restaurant India (2025), and Best Biryani by EazyDiner (2023).",
            },
            {
                "q": "How can I place an order directly with Sharief Bhai?",
                "a": "You can call Sharief Bhai's customer care to order directly, or order "
                     "through Ownly and leading food delivery platforms.",
            },
            {
                "q": "How can I contact Sharief Bhai for feedback or support?",
                "a": "You can email hello@shariefbhai.com or use the feedback form on "
                     "shariefbhai.com.",
            },
            {
                "q": "Does Sharief Bhai cater to corporate clients?",
                "a": "Yes, Sharief Bhai offers corporate food booking and catering, and has "
                     "served 500+ corporate clients.",
            },
        ],
    },
    {
        "slug": "olio",
        "name": "OLIO",
        "full_name": "OLIO",
        "category": "Pizza & Italian",
        "color": "#02311E",
        "logo": "/assets/images/logos/olio.png",
        "logo_bg": "#F9F1DD",
        "photo": "/assets/images/photos/olio-food.jpg",
        "domain": "https://www.oliopizza.in",
        "instagram": "https://www.instagram.com/oliopizza.in",
        "swiggy": "https://sds.swig.gy/LU5bKT5Tk6n",
        "zomato": "https://link.zomato.com/xqzv/hbyayexg",
        "ownly": "https://ownly.food/app/brand/BR112479",
        "tagline": "Asli Cheese | Smoky Crust",
        "description": (
            "OLIO is a young, delivery-first pizza brand known for its smoky charred "
            "crust, stretchy real cheese and bold, craveable toppings."
        ),
        "story": (
            "Built for spontaneous cravings, sharing and high-energy food moments, OLIO "
            "puts pizza first. Its pizzas pair hand-stretched dough with a crispy, "
            "charred smoky crust, natural stretchy cheese, signature tomato sauce and "
            "bold toppings. With 200+ locations across 40+ cities, OLIO brings a "
            "playful, accessible pizza experience across its growing network."
        ),
        "menu": [
            {"veg": True, "name": "Alfredo Pasta", "detail": "Creamy white sauce pasta"},
            {"veg": True, "name": "Arrabbiata Penne", "detail": "Spicy tomato-basil pasta"},
            {"veg": True, "name": "Farmhouse Pizza", "detail": "Classic veg-loaded pizza"},
            {"veg": True, "name": "Garlic Bread Bites", "detail": "Side"},
        ],
        "cities": [
            "Ahmedabad", "Aurangabad", "Bengaluru", "Chandigarh", "Chennai", "Coimbatore",
            "Delhi", "Dharwad", "Faridabad", "Gurgaon", "Guwahati", "Hubli", "Hyderabad",
            "Jaipur", "Kochi", "Kolkata", "Lucknow", "Ludhiana", "Mumbai", "Nagpur",
            "Nashik", "Noida", "Pune", "Salem", "Surat", "Vadodara",
        ],
        "store_count": "200+",
        "founded": "2021",
        "faq": [
            {
                "q": "Which cities is OLIO available in?",
                "a": "OLIO Pizza is expanding rapidly across India — currently live in Ahmedabad, "
                     "Aurangabad, Bengaluru, Chandigarh, Chennai, Coimbatore, Delhi, Dharwad, "
                     "Faridabad, Gurgaon, Guwahati, Hubli, Hyderabad, Jaipur, Kochi, Kolkata, "
                     "Lucknow, Ludhiana, Mumbai, Nagpur, Nashik, Noida, Pune, Salem, Surat, "
                     "Vadodara and more.",
            },
            {
                "q": "What makes OLIO Pizza different from other pizza brands?",
                "a": "OLIO serves smoky pizzas made with hand-stretched dough, premium ingredients, "
                     "bold toppings and a signature crust.",
            },
            {
                "q": "How can I order OLIO Pizza online?",
                "a": "You can order OLIO Pizza on Swiggy, Zomato, Ownly, Toing or any other food "
                     "delivery app.",
            },
            {
                "q": "Does OLIO offer late-night pizza delivery?",
                "a": "Yes! Most OLIO outlets deliver till 3AM. City-wise timings vary — check your "
                     "neighbourhood OLIO Pizza store on Swiggy or Zomato for the exact timings.",
            },
            {
                "q": "Can I customize my pizza toppings at OLIO?",
                "a": "You can choose from veg, non-veg, cheese burst, and multi-grain base when "
                     "ordering from OLIO Pizza.",
            },
            {
                "q": "What are OLIO's most popular pizzas?",
                "a": "Some of our crowd favourites include the Margherita, Veg Overload, Peri "
                     "Peri Chicken, Deluxe Veggie and Paneer Red-Hot with a smoky crust.",
            },
            {
                "q": "Do you offer Jain or vegan pizza options?",
                "a": "Select locations offer Jain-friendly and vegan-friendly options.",
            },
            {
                "q": "Are your bases hand-stretched and fresh?",
                "a": "Always. Every pizza is made from hand-stretched dough, proofed in-house, "
                     "and made fresh for every order.",
            },
            {
                "q": "Is OLIO Pizza vegetarian-friendly?",
                "a": "Yes, we offer a wide range of 100% vegetarian pizzas, garlic breads and sides.",
            },
            {
                "q": "What else can I order from OLIO?",
                "a": "Along with pizzas, OLIO menus can include pastas, garlic breads and sides, "
                     "snacks, beverages and desserts, depending on the outlet.",
            },
            {
                "q": "What is OLIO Woodfired Pizza?",
                "a": "OLIO Woodfired is the brand's crowd-pleasing range of smoky, loaded pizzas "
                     "made for sharing, featuring a charred crust with vegetarian and "
                     "non-vegetarian options.",
            },
            {
                "q": "What is the OLIO 99 Slice?",
                "a": "The OLIO 99 Slice is a giant 24 cm single pizza slice made for one person, "
                     "designed for quick meals, campus breaks, late-night cravings and "
                     "grab-and-go occasions.",
            },
            {
                "q": "Which OLIO range should I choose?",
                "a": "Choose OLIO Woodfired for a complete smoky pizza made for sharing, or the "
                     "OLIO 99 Slice for one giant 24 cm slice designed for a quick solo meal.",
            },
            {
                "q": "Can I order OLIO Pizza for a group or party?",
                "a": "Yes, OLIO Woodfired pizzas, sides and combos are suited to group orders, "
                     "though menu choices and serving sizes vary by kitchen.",
            },
            {
                "q": "Do OLIO menus and prices vary by city?",
                "a": "Yes, pizza flavours, combos, prices, offers, kitchen hours and delivery "
                     "availability can vary by city and ordering platform, so the live Swiggy, "
                     "Zomato or Ownly menu is the current source for a given address.",
            },
        ],
    },
    {
        "slug": "arambam",
        "name": "Arambam",
        "full_name": "Arambam",
        "category": "Flavours of South India",
        "color": "#137e73",
        "logo": "/assets/images/logos/arambam.webp",
        "logo_bg": "#4D4D24",
        "photo": "/assets/images/photos/arambam-food.jpg",
        "domain": "https://www.arambam.com",
        "instagram": "https://www.instagram.com/arambamofficial",
        "zomato": "https://zomato.onelink.me/xqzv/7ei4gtxv?brand_id=922&ref_id=5620",
        "ownly": "https://ownly.food/app/brand/BR112491",
        "tagline": "Flavours of South - wholesome South Indian, built on millets.",
        "description": (
            "Arambam is Curefoods' celebrity-backed South Indian brand, bringing the "
            "comforting flavours of the South together with the goodness of millets, "
            "offering regional favourites from across five South Indian states on "
            "one menu."
        ),
        "story": (
            "Arambam launched in partnership with actor Rakul Preet Singh, positioned around "
            "the nutritional case for millets over rice and wheat. Run by Curefoods' Millet "
            "Express subsidiary, it later entered an 18-month master franchise agreement with "
            "EAT360 to accelerate expansion beyond its Bengaluru and Mumbai launch markets."
        ),
        "menu": [
            {"veg": True, "name": "Ragi Mudde Combo", "detail": "Karnataka-style millet ball with sambar"},
            {"veg": True, "name": "Millet Bisi Bele Bath", "detail": "Millet-based one-pot rice"},
            {"veg": True, "name": "Andhra Millet Thali", "detail": "5-states-in-1-plate format"},
            {"veg": True, "name": "Jowar Dosa", "detail": "Multi-millet batter"},
        ],
        "cities": ["Bengaluru", "Chennai", "Hyderabad", "Vizag", "Delhi", "Gurugram", "Noida", "Mumbai", "Pune", "Bhopal", "Ujjain", "Coimbatore"],
        "founded": "2024",
        "ambassador": "Rakul Preet Singh (brand partner)",
        "faq": [
            {
                "q": "What does 'Flavours of South' mean for Arambam?",
                "a": "'Flavours of South' is Arambam's celebration of South Indian cuisine — "
                     "bringing together the diverse regional flavours of the South with "
                     "millet-forward dishes, all under one menu.",
            },
            {
                "q": "Is Arambam the same company as Millet Express?",
                "a": "Arambam is run by Curefoods' Millet Express subsidiary, which also operates the "
                     "separate Millet Express brand; the two share ownership but run distinct menus and storefronts.",
            },
            {
                "q": "Why does Arambam use millets instead of rice or wheat?",
                "a": "Arambam brings the diverse and comforting Flavours of South to one menu, "
                     "combining traditional South Indian favourites with millet-forward dishes. "
                     "It's a celebration of familiar regional flavours with a modern, "
                     "millet-focused approach.",
            },
            {
                "q": "Which cities is Arambam available in?",
                "a": "Arambam launched its first restaurant in Hyderabad in April 2024 and has "
                     "since grown its presence across 12 cities in India — Bengaluru, Chennai, "
                     "Hyderabad, Vizag, Delhi, Gurugram, Noida, Mumbai, Pune, Bhopal, Ujjain, "
                     "and Coimbatore.",
            },
            {
                "q": "Does Arambam offer catering or group orders?",
                "a": "You can check with your nearest Arambam outlet for catering and "
                     "bulk-order options.",
            },
            {
                "q": "What kind of food does Arambam serve?",
                "a": "Arambam serves a variety of South Indian dishes inspired by regional "
                     "flavours, including breakfast favourites, rice-based dishes, tiffins, "
                     "snacks, beverages, and millet-forward creations.",
            },
            {
                "q": "Does Arambam offer franchise opportunities, and what's the investment required?",
                "a": "Yes — Arambam offers two franchise tiers: a Unit Franchise starting at "
                     "₹20-25 lakhs, and a Master Franchise starting at ₹60 lakhs onwards.",
            },
            {
                "q": "Do I need prior restaurant experience to open an Arambam franchise?",
                "a": "No, prior food and beverage experience is optional — Arambam's franchise "
                     "enquiry process asks about industry background but does not require it, "
                     "only interest in the sector and sufficient capital for the chosen tier.",
            },
            {
                "q": "How can I contact Arambam directly?",
                "a": "You can reach Arambam through the 'Get In Touch' contact section on "
                     "arambam.com.",
            },
            {
                "q": "Who launched Arambam, and what's the brand's origin story?",
                "a": "Arambam was launched in April 2024 in Hyderabad by actor Rakul Preet Singh "
                     "in partnership with Curefoods, positioned as a millet-based South Indian "
                     "restaurant.",
            },
        ],
    },
    {
        "slug": "krispy-kreme",
        "name": "Krispy Kreme",
        "full_name": "Krispy Kreme India",
        "category": "Doughnuts & Coffee",
        "color": "#046A38",
        "logo": "/assets/images/logos/krispy-kreme.png",
        "photo": "/assets/images/photos/krispy-kreme-food.jpg",
        "domain": "https://www.krispykremeindia.in",
        "instagram": "https://www.instagram.com/krispykreme_ind/",
        "swiggy": "https://sds.swig.gy/8PcCzQskjZc",
        "zomato": "https://zomato.onelink.me/xqzv/7ei4gtxv?brand_id=917&ref_id=5601",
        "ownly": "https://ownly.food/app/brand/BR112481",
        "tagline": "Made fresh Daily",
        "description": (
            "Krispy Kreme is a global doughnut and coffee brand operated by Curefoods "
            "in India with presence across 10 cities and 150+ locations."
        ),
        "story": (
            "Unlike Curefoods' home-grown brands, Krispy Kreme is an international master-"
            "franchise partnership — Curefoods operates the India business (stores, kitchens "
            "and delivery) under Krispy Kreme's global brand standards and recipes, betting "
            "that a globally trusted name accelerates trust and ticket size faster than a "
            "new brand could alone."
        ),
        "menu": [
            {"veg": True, "name": "Original Glazed Dozen", "detail": "The signature glazed doughnut"},
            {"veg": True, "name": "Chocolate Iced Kreme Filled", "detail": "Filled doughnut"},
            {"veg": True, "name": "Assorted Doughnut Box", "detail": "Mixed selection"},
            {"veg": True, "name": "Kreme Coffee", "detail": "Hot & cold coffee range"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Delhi NCR", "Jaipur", "Chandigarh", "Pune"],
        "store_count": "150+",
        "founded": "2022 (Curefoods master franchise; global brand since 1937)",
        "faq": [
            {
                "q": "Is Krispy Kreme a Curefoods-owned brand or a franchise?",
                "a": "Krispy Kreme is a global brand. Curefoods operates it in India as the "
                     "exclusive master franchisee, running local stores, kitchens and delivery "
                     "under Krispy Kreme's international recipes and brand standards, rather "
                     "than owning the underlying intellectual property.",
            },
            {
                "q": "When did Krispy Kreme first come to India?",
                "a": "Krispy Kreme first opened in India in Bengaluru in January 2013 under an "
                     "earlier operator. In 2025, Curefoods became the brand's exclusive master "
                     "franchisee and has led its expansion across India since.",
            },
            {
                "q": "Are Krispy Kreme doughnuts in India vegetarian or eggless?",
                "a": "Krispy Kreme's doughnuts in India are made with an eggless recipe, adapted "
                     "specifically for the vegetarian and egg-free dietary preferences common "
                     "among Indian consumers.",
            },
            {
                "q": "Which cities is Krispy Kreme available in?",
                "a": "Krispy Kreme runs 150+ stores across Bengaluru, Hyderabad, Chennai, Delhi NCR, "
                     "Jaipur, Chandigarh, and Pune under Curefoods.",
            },
            {
                "q": "What does Krispy Kreme India offer beyond doughnuts?",
                "a": "Alongside its signature doughnuts, Krispy Kreme India serves a coffee range, "
                     "milkshakes and chillers, seasonal desserts and a curated savoury range across "
                     "its cafe format stores, giving guests a full dessert, snacks and beverage "
                     "experience. Krispy Kreme India also provides a wide variety of chocolate "
                     "doughnuts.",
            },
            {
                "q": "Are Krispy Kreme doughnuts in India made fresh locally, or shipped from one central kitchen?",
                "a": "Krispy Kreme operates dedicated production units for each city cluster, and "
                     "doughnuts are supplied fresh to nearby stores daily rather than shipped from "
                     "a single central facility.",
            },
            {
                "q": "What is the Hot Light experience at Krispy Kreme stores?",
                "a": "At select Krispy Kreme theatre shops, guests can watch doughnuts being made "
                     "and glazed in real time under the brand's signature Hot Light, a "
                     "theatre-style experience that has been part of Krispy Kreme's identity "
                     "globally.",
            },
            {
                "q": "Where can I find a Krispy Kreme store or order near me?",
                "a": "Guests can locate their nearest Krispy Kreme store or place an order for "
                     "delivery through krispykremeindia.in, Swiggy or Zomato, depending on the "
                     "city.",
            },
            {
                "q": "Does Krispy Kreme India do corporate or birthday party orders?",
                "a": "Yes, Krispy Kreme India offers corporate and birthday order services for "
                     "occasions such as office parties, meetings, school events and family "
                     "gatherings, bookable with guest-count tiers from under 50 to over 200.",
            },
            {
                "q": "Has Krispy Kreme India won any awards?",
                "a": "Yes, Krispy Kreme has received awards in India related to product, "
                     "branding and innovation.",
            },
            {
                "q": "When did Krispy Kreme open its Chennai store?",
                "a": "Krispy Kreme launched its first factory outlet in Chennai at Express "
                     "Avenue on 25 July 2014.",
            },
            {
                "q": "Did Krispy Kreme ever have a store in Mumbai?",
                "a": "Krispy Kreme opened an outlet at Hiranandani Gardens, Powai, Mumbai, on "
                     "17 October 2014, as part of its early India expansion beyond Bengaluru.",
            },
        ],
    },
    {
        "slug": "nomad-pizza",
        "name": "Nomad Pizza",
        "full_name": "Nomad Pizza",
        "category": "Gourmet Pizza",
        "color": "#c84d27",
        "logo": "/assets/images/logos/nomad-pizza.png",
        "photo": "/assets/images/photos/nomad-pizza-food.jpg",
        "domain": "https://www.nomadpizza.in/",
        "instagram": "https://www.instagram.com/nomadpizzaofficial",
        "swiggy": "https://www.swiggy.com/direct/brand/251919?source=swiggy-direct&subSource=generic",
        "zomato": "https://link.zomato.com/xqzv/rshare?id=7823556130563a9f",
        "ownly": "https://ownly.food/app/brand/BR112488",
        "tagline": "Food Inspired by Travel",
        "description": (
            "Nomad Pizza brings artisanal, hand-stretched pizzas with globally inspired "
            "toppings to Curefoods' delivery network — crafted for the premium everyday "
            "pizza experience."
        ),
        "story": (
            "Born in Delhi in 2019, Nomad Pizza was built on the idea that food is a form "
            "of exploration. Inspired by flavours from around the world, we bring global "
            "food experiences to your doorstep. Pizza is at our heart, but we go beyond "
            "pizza with rice bowls, Panuzzos, pastas, Mexican favourites, a dedicated "
            "Protein category, and more. With 75+ outlets across 19 cities, we continue "
            "to innovate while staying true to our philosophy: Food Inspired by Travel."
        ),
        "menu": [
            {"veg": True, "name": "Peri Peri Paneer Pizza", "detail": "Hand-stretched, wood-fired base"},
            {"veg": False, "name": "Korean BBQ Chicken Pizza", "detail": "Globally-inspired topping"},
            {"veg": True, "name": "Classic Margherita", "detail": "San Marzano-style tomato base"},
            {"veg": False, "name": "Nomad Meat Feast", "detail": "Four-meat loaded pizza"},
        ],
        "cities": ["Delhi NCR", "Mumbai", "Bangalore", "Ahmedabad", "Chandigarh", "Jaipur", "Dehradun", "Indore", "Goa", "Hyderabad"],
        "store_count": "75+",
        "founded": "2021",
        "faq": [
            {
                "q": "What makes Nomad Pizza different from other pizza delivery brands?",
                "a": "Nomad Pizza stands out because it's not just another pizza delivery brand — "
                     "it brings pizzas inspired by different regions of the world, with fresh "
                     "dough, distinctive pizza styles, and quality ingredients. The idea is "
                     "simple: \"Food Inspired by Travel.\"",
            },
            {
                "q": "Who founded Nomad Pizza?",
                "a": "Nomad Pizza was founded by Amit Ajwani in Delhi in 2019, before Curefoods "
                     "acquired the brand in October 2021.",
            },
            {
                "q": "Which cities is Nomad Pizza available in?",
                "a": "Nomad Pizza is currently available across 19+ cities in India, including "
                     "Delhi NCR, Mumbai, Bangalore, Ahmedabad, Chandigarh, Jaipur, Dehradun, "
                     "Indore, Goa, Hyderabad, and more.",
            },
            {
                "q": "How can I order from Nomad Pizza?",
                "a": "You can order directly through the Nomad Pizza website, via Zomato and "
                     "Swiggy, or dine in and take away at any outlet.",
            },
            {
                "q": "Can I schedule my order for a later time?",
                "a": "Yes, you can pre-order for a later time through the website or partner "
                     "apps, depending on availability.",
            },
            {
                "q": "Does Nomad Pizza use fresh ingredients?",
                "a": "The dough is made fresh every day, and Nomad Pizza uses high-quality "
                     "cheeses, sauces and toppings with no frozen bases or shortcuts.",
            },
            {
                "q": "What kind of cheese does Nomad Pizza use?",
                "a": "Nomad Pizza uses real mozzarella, burrata, feta and other premium cheeses.",
            },
            {
                "q": "Does Nomad Pizza offer gluten-free options?",
                "a": "Gluten-free bases are not currently offered, though the brand is exploring "
                     "this based on demand.",
            },
            {
                "q": "Can I customize my pizza's toppings or sauces?",
                "a": "Basic changes to toppings and sauces can be made while ordering; for "
                     "specific dietary needs, customers can speak directly with the outlet team.",
            },
            {
                "q": "Is allergen information available?",
                "a": "Yes, allergen information is available at the outlet and can be requested "
                     "before ordering.",
            },
            {
                "q": "Can I dine in at Nomad Pizza outlets?",
                "a": "Yes, all outlets offer dine-in seating with a warm, vibrant atmosphere "
                     "suited to a casual meal.",
            },
            {
                "q": "Are Nomad Pizza outlets pet-friendly?",
                "a": "Some outlets are pet-friendly, but customers should check with the "
                     "specific location before visiting.",
            },
            {
                "q": "Does Nomad Pizza host private events or parties?",
                "a": "Select outlets can host private gatherings, tastings and events.",
            },
            {
                "q": "Are there discounts or a loyalty program at Nomad Pizza?",
                "a": "Customers can follow Nomad Pizza on Instagram or subscribe to the "
                     "newsletter for current offers and deals.",
            },
            {
                "q": "Is there a first-time order discount at Nomad Pizza?",
                "a": "First-time users ordering through the Nomad Pizza website may get a "
                     "special discount, listed on the homepage when active.",
            },
            {
                "q": "How can businesses collaborate or partner with Nomad Pizza?",
                "a": "Collaboration proposals can be sent via the contact page, email, or "
                     "Instagram DM.",
            },
            {
                "q": "What is Nomad Pizza's refund or complaint policy?",
                "a": "Customers with issues are asked to contact customer service immediately, "
                     "and the brand aims for a fair and quick resolution.",
            },
            {
                "q": "How can I contact Nomad Pizza customer support?",
                "a": "You can use the website contact form, call the toll-free number "
                     "1800-890-2120, or DM @nomadpizzas on Instagram.",
            },
            {
                "q": "What are Nomad Pizza's operating hours?",
                "a": "Outlets operate all days from 12:00 to 23:00.",
            },
        ],
    },
    {
        "slug": "cakezone",
        "name": "CakeZone",
        "full_name": "CakeZone",
        "category": "Cakes & Celebrations",
        "color": "#4b3593",
        "logo": "/assets/images/logos/cakezone.svg",
        "logo_bg": "#4b3593",
        "photo": "/assets/images/photos/cakezone-food.jpg",
        "domain": "https://cakezone.com/",
        "instagram": "https://www.instagram.com/cakezone.patisserie",
        "swiggy": "https://www.swiggy.com/direct/brand/7003?source=swiggy-direct&subSource=instagram",
        "zomato": "https://zomato.onelink.me/xqzv/7ei4gtxv?brand_id=659&ref_id=5599",
        "ownly": "https://ownly.food/app/brand/BR112492",
        "tagline": "Every moment is a cake moment.",
        "description": (
            "CakeZone is a leading dessert brand in India, bringing irresistible cakes "
            "and desserts to customers across 60+ cities through 200+ outlets. With a "
            "passion for great taste, quality ingredients, and delightful experiences, "
            "CakeZone makes every celebration a little sweeter."
        ),
        "story": (
            "CakeZone was brought into Curefoods to own the celebrations occasion — cakes, "
            "customised messages, and add-on gifting — with a delivery promise built around "
            "urgency: same-day and midnight slots for last-minute celebrations."
        ),
        "menu": [
            {"veg": True, "name": "Truffle Cake", "detail": "Half kg / 1 kg"},
            {"veg": True, "name": "Red Velvet Cake", "detail": "Half kg / 1 kg"},
            {"veg": True, "name": "Photo Cake", "detail": "Customisable"},
            {"veg": True, "name": "Pull-Me-Up Cake", "detail": "Layered surprise cake"},
        ],
        "cities": ["Bengaluru", "Hyderabad", "Chennai", "Mumbai", "Delhi NCR", "Pune", "Kolkata", "Ahmedabad", "Chandigarh", "Jaipur", "Coimbatore", "Indore"],
        "store_count": "200+",
        "founded": "2020 (acquired by Curefoods)",
        "faq": [
            {
                "q": "Does CakeZone deliver at midnight?",
                "a": "Yes — CakeZone offers midnight and same-day delivery slots designed for "
                     "last-minute birthday and anniversary celebrations.",
            },
            {
                "q": "Does CakeZone offer eggless cakes?",
                "a": "Yes — CakeZone carries a full menu of 100% eggless cakes across its "
                     "flavours, not a limited add-on selection.",
            },
            {
                "q": "How fast can CakeZone deliver a cake?",
                "a": "Beyond same-day and midnight slots, CakeZone offers express delivery "
                     "within 60 minutes in select areas.",
            },
            {
                "q": "Can I personalize a CakeZone cake with a name or message?",
                "a": "Yes — CakeZone lets customers add a name or message at checkout on select "
                     "cakes for personalization.",
            },
            {
                "q": "Where does CakeZone deliver?",
                "a": "CakeZone is live in most Indian cities including Bengaluru, Hyderabad, "
                     "Mumbai, Pune, Chennai, Delhi, Kolkata and Ahmedabad, among others. You can "
                     "find your nearest outlet on Swiggy or Zomato.",
            },
            {
                "q": "How do I order from CakeZone?",
                "a": "You can order online via Swiggy or Zomato, or use Instamart or Blinkit "
                     "for quick deliveries.",
            },
            {
                "q": "What kind of cakes can I get from CakeZone?",
                "a": "The menu features premium cakes, jar cakes, cheesecakes and Indian fusion "
                     "cakes — from chocolate truffle, red velvet and black forest to photo "
                     "cakes, bento cakes and celebration combos.",
            },
            {
                "q": "Are DIY cake kits available at CakeZone?",
                "a": "Yes, CakeZone offers seasonally available DIY Bento Cake Kits that let you "
                     "decorate and gift cakes your own way, ideal for birthdays, kids or "
                     "creative celebrations, subject to availability.",
            },
            {
                "q": "Does CakeZone offer gift-wrapped or festive packaging?",
                "a": "Yes, CakeZone cakes come in packaging designed for celebrations, whether "
                     "for birthdays, anniversaries or the festive season.",
            },
            {
                "q": "Does CakeZone have physical stores?",
                "a": "CakeZone is a delivery-first desserts brand with no dine-in; you can enjoy "
                     "freshly made cakes at home by ordering through Swiggy or Zomato.",
            },
        ],
    },
    {
        "slug": "frozen-bottle",
        "name": "Frozen Bottle",
        "full_name": "Frozen Bottle",
        "category": "Milkshake, Dessert & Ice-Cream",
        "color": "#EB1256",
        "logo": "/assets/images/logos/frozen-bottle.png",
        "photo": "/assets/images/photos/frozen-bottle-food.jpg",
        "domain": "https://frozenbottle.com",
        "domain_cta": "Know more on Frozenbottle.com",
        "instagram": "https://www.instagram.com/frozen_bottle",
        "swiggy": "https://www.swiggy.com/direct/brand/5655?source=swiggy-direct&subSource=generic",
        "ownly": "https://ownly.food/app/brand/BR113086",
        "tagline": "100% veg, 100% eggless — Your Chill Zone",
        "description": (
            "Frozen Bottle is Curefoods' cold-dessert brand, serving thick milkshakes, "
            "ice-cream sundae jars, boba and Belgian waffles that are 100% vegetarian and "
            "100% eggless."
        ),
        "story": (
            "Frozen Bottle launched in 2017 as a 100% vegetarian, 100% eggless dessert brand — "
            "thick milkshakes, ice-cream sundae jars, boba and Belgian waffles. Its own promise, "
            "#servingmemories, is the pitch: a dessert destination people remember, not just "
            "another delivery order."
        ),
        "menu": [
            {"veg": True, "name": "Signature Milkshake", "detail": "Thick, jar-served milkshake"},
            {"veg": True, "name": "Belgian Choco Chunk Sundae Jar", "detail": "Ice cream sundae jar"},
            {"veg": True, "name": "Gudbud Sundae Jar", "detail": "Layered ice cream sundae"},
            {"veg": True, "name": "Belgian Waffles", "detail": "Served with ice cream"},
        ],
        "cities": ["Bengaluru", "Mumbai", "Hyderabad", "Pune", "Chennai", "Gurugram", "Kerala"],
        "founded": "2017",
        "faq": [
            {
                "q": "Is Frozen Bottle vegetarian?",
                "a": "Yes — Frozen Bottle's entire menu, from milkshakes to ice-cream sundae "
                     "jars, is 100% vegetarian.",
            },
            {
                "q": "Are Frozen Bottle's desserts eggless?",
                "a": "Yes — all Frozen Bottle products are 100% eggless.",
            },
            {
                "q": "What does Frozen Bottle sell besides milkshakes?",
                "a": "Beyond its signature thick milkshakes, Frozen Bottle serves ice-cream "
                     "sundae jars, boba and bubble teas, cold coffee and Belgian waffles.",
            },
            {
                "q": "Which cities is Frozen Bottle available in?",
                "a": "Frozen Bottle has outlets across Bengaluru, Mumbai, Hyderabad, Pune, "
                     "Chennai, Gurugram and Kerala, with Bengaluru as its largest market.",
            },
            {
                "q": "Are there delivery charges on Frozen Bottle orders?",
                "a": "Yes, Frozen Bottle charges a nominal delivery fee calculated by distance, "
                     "which is subject to change based on current offers.",
            },
            {
                "q": "What delivery options does Frozen Bottle offer?",
                "a": "Frozen Bottle offers both doorstep delivery and store pickup.",
            },
            {
                "q": "What should I do if my Frozen Bottle order arrives damaged?",
                "a": "Contact Frozen Bottle within 1 hour via WhatsApp with your order number, "
                     "a description of the issue, and a photo of the damaged item.",
            },
            {
                "q": "What payment methods does Frozen Bottle accept?",
                "a": "Frozen Bottle accepts debit card, credit card, net banking, UPI, wallets, "
                     "and cash on delivery.",
            },
            {
                "q": "How should a Frozen Bottle cake be stored?",
                "a": "Store the product between 0°C and 5°C.",
            },
            {
                "q": "Can I cancel or modify my Frozen Bottle order?",
                "a": "Cancellations must be requested at least 24 hours before the scheduled "
                     "delivery slot; same-day delivery orders cannot be cancelled.",
            },
            {
                "q": "Can I order a customized cake from Frozen Bottle?",
                "a": "Yes, customers can place customized cake orders by contacting Frozen "
                     "Bottle directly to discuss requirements.",
            },
            {
                "q": "Does Frozen Bottle offer gluten-free options?",
                "a": "No, Frozen Bottle does not currently offer gluten-free products.",
            },
            {
                "q": "Does Frozen Bottle offer vegan desserts?",
                "a": "Yes, Frozen Bottle has vegan options available — customers should reach "
                     "out to customize their order.",
            },
            {
                "q": "Can I include a gift note or message with my Frozen Bottle order?",
                "a": "Yes, gift notes or messages can be added at the time of placing the order.",
            },
            {
                "q": "Can I place a same-day delivery order with Frozen Bottle?",
                "a": "Yes, orders can be placed and delivered on the same day, subject to slot "
                     "availability.",
            },
            {
                "q": "How do I get in touch about a Frozen Bottle franchise opportunity?",
                "a": "Franchise enquiries can be sent to franchise@frozenbottle.in.",
            },
            {
                "q": "What are Frozen Bottle's customer care hours?",
                "a": "General customer care is available Monday to Friday, 10 AM to 6 PM.",
            },
        ],
    },
]

# Site-wide FAQ (in addition to per-brand FAQs), feeds the /faq.html hub — the
# single richest page for AEO / LLM citation.
SITE_FAQ = [
    {
        "q": "What is Curefoods?",
        "a": "Curefoods is a Bengaluru-headquartered house of food brands, founded in 2020 by "
             "Ankit Nagori. It builds and scales multiple F&B brands — spanning healthy meals, "
             "biryani, pizza, desserts and celebration cakes — out of a shared network of "
             "cloud kitchens and dine-in stores across India.",
    },
    {
        "q": "How many brands does Curefoods own?",
        "a": "Curefoods' published brand portfolio includes Eatfit, Sharief Bhai Biryani, "
             "OLIO, Arambam, Nomad Pizza, CakeZone and Frozen Bottle, plus master-franchise "
             "partner Krispy Kreme.",
    },
    {
        "q": "What is a 'house of brands' model, and why does Curefoods use it?",
        "a": "A house-of-brands model runs several distinct, independently-branded products from "
             "shared infrastructure — in Curefoods' case, shared cloud kitchens, supply chain and "
             "delivery operations. It lets one kitchen serve several occasions (health food, "
             "biryani, dessert) to the same customer without diluting any single brand's identity.",
    },
    {
        "q": "How many kitchens and stores does Curefoods operate?",
        "a": "As of March 31, 2025, Curefoods runs 281 cloud kitchens, 99 kiosks and 122 "
             "restaurants across India.",
    },
    {
        "q": "Who founded Curefoods and when?",
        "a": "Curefoods was founded in 2020 by Ankit Nagori, former co-founder of Cure.fit "
             "(Cult.fit) and former Chief Business Officer of Flipkart, who set out to apply the same operating rigor to "
             "the food-brands business.",
    },
    {
        "q": "How can I order from Curefoods brands?",
        "a": "Every Curefoods brand is listed on major food delivery platforms (Swiggy, Zomato) "
             "under its own name — search the brand name directly, e.g. 'Eatfit' or 'Sharief "
             "Bhai' — and select brands also operate dedicated apps and dine-in stores.",
    },
    {
        "q": "Is Curefoods the same company as Rebel Foods?",
        "a": "No. Curefoods and Rebel Foods are separate, competing Indian cloud-kitchen "
             "companies that both use a house-of-brands model. Rebel Foods owns brands like "
             "Faasos, Behrouz Biryani and Oven Story; Curefoods owns Eatfit, Sharief Bhai, "
             "CakeZone and the brands listed on this site.",
    },
    {
        "q": "Does Curefoods have physical, dine-in stores or only delivery kitchens?",
        "a": "Both. Most Curefoods brands operate delivery-only cloud kitchens, but several — "
             "including Sharief Bhai's Mosque Road flagship and Krispy Kreme's dine-in cafés — "
             "also run dine-in and walk-in retail formats.",
    },
    {
        "q": "How do I apply for a job at Curefoods?",
        "a": "Open roles across all Curefoods brands are listed on the Careers page "
             "(curefoods.in/careers.html); applications can also be sent to careers@curefoods.in.",
    },
    {
        "q": "How can franchise or partnership enquiries reach Curefoods?",
        "a": "Franchise and partnership enquiries can be sent to hello@curefoods.in.",
    },
    {
        "q": "Are Curefoods' kitchens FSSAI-licensed and hygienic?",
        "a": "Yes. Every food business operating in India, including cloud kitchens listed on Swiggy "
             "or Zomato, is required to hold a valid FSSAI licence, and Curefoods' kitchens operate "
             "under that same regulatory requirement.",
    },
    {
        "q": "What should I do if my order from a Curefoods brand has a problem?",
        "a": "For orders placed through Swiggy or Zomato, use that platform's order-help or refund flow "
             "first, since they process the payment and delivery. For orders placed directly with a "
             "brand (its own app, website or phone line), contact that brand's listed support channel, "
             "or reach Curefoods at support@curefoods.in.",
    },
    {
        "q": "Do Curefoods brands offer vegetarian and eggless options?",
        "a": "Yes, across the portfolio — CakeZone runs a 100% eggless cake menu, Krispy Kreme India "
             "uses an eggless doughnut recipe, and Eatfit, Sharief Bhai and Arambam all carry dedicated "
             "vegetarian dishes alongside non-vegetarian ones.",
    },
    {
        "q": "Can I track my order from a Curefoods brand in real time?",
        "a": "Orders placed via Swiggy or Zomato are tracked inside those apps. Brands with their own "
             "ordering channels, such as Sharief Bhai and Krispy Kreme India, offer tracking through "
             "their own app or website as well.",
    },
]

VALUES = [
    {"title": "Kitchen-first economics", "text": "Every brand is designed around shared kitchen infrastructure, so unit economics work before marketing spend does."},
    {"title": "Category depth over breadth", "text": "Each brand owns one occasion — health, biryani, dessert, celebration — built for depth in that category rather than breadth across categories."},
    {"title": "Data-run, fast to the door", "text": "Menu, pricing and kitchen placement are driven by order-level data, and kitchen density is built to shrink delivery time without shrinking food quality."},
]

CORE_PURPOSE = {
    "eyebrow": "Core Purpose",
    "title": "Create Iconic Food Brands",
    "paragraphs": [
        "Food is not just a necessity. It is a daily part of how people live, feel, and connect.",
        "Every meal is a moment.",
        "And over time, these moments build trust... and habit.",
        "At Curefoods, our role is not just to serve food, but to build brands that customers choose, remember, and come back to.",
        "We are here to create iconic food brands that customers remember, trust and love for years to come.",
    ],
}

CORE_VALUES = [
    {"title": "Love for Food", "icon": "/assets/images/values/value-love-for-food.png"},
    {"title": "Do More with Less", "icon": "/assets/images/values/value-do-more-with-less.png"},
    {"title": "Act Like an Owner", "icon": "/assets/images/values/value-act-like-owner.png"},
    {"title": "Pursuit of Excellence", "icon": "/assets/images/values/value-pursuit-excellence.png"},
]

# Pulled verbatim from curefoods.in/about ("We serve happiness to your plate
# across India" stats block) — not inferred or estimated.
FACILITY_STATS = {
    "as_of": "March 31, 2025",
    "items": [
        {"label": "Cloud Kitchens", "value": "281"},
        {"label": "Kiosks", "value": "99"},
        {"label": "Restaurants", "value": "122"},
    ],
}

# Real third-party press coverage — verified live before adding, not written by Curefoods.
# Thumbnails are each article's own og:image, pulled directly from its source page.
NEWS_MENTIONS = [
    {
        "title": "Curefoods acquires South West India operations for Krispy Kreme",
        "source": "ET HospitalityWorld",
        "photo": "/assets/images/photos/krispy-kreme-food.jpg",
        "url": "https://hospitality.economictimes.indiatimes.com/news/restaurants/curefoods-acquires-south-west-india-operations-for-krispy-kreme/116871846",
    },
    {
        "title": "Curefoods is no longer just Eatfit. It wants to eat Domino's",
        "source": "The Ken",
        "photo": "/assets/images/photos/news/the-ken-domino.jpg",
        "url": "https://the-ken.com/story/curefoods-is-no-longer-just-eatfit-it-wants-to-eat-dominos/",
    },
    {
        "title": "Experience Dakhni cuisine at the new Sharief Bhai flagship store in Bengaluru",
        "source": "ET HospitalityWorld",
        "photo": "/assets/images/photos/sharief-bhai-store.jpg",
        "url": "https://hospitality.economictimes.indiatimes.com/news/restaurants/experience-dakhni-cuisine-at-the-new-sharief-bhai-flagship-store-in-bengaluru/121689522",
    },
    {
        "title": "Best Spots To Visit In Bangalore's Famed Food Destination Frazer Town",
        "source": "Travel + Leisure Asia",
        "photo": "/assets/images/photos/news/travel-leisure-frazer-town.jpg",
        "url": "https://www.travelandleisureasia.com/in/dining/food/best-food-spots-in-frazer-town-in-bangalore/",
    },
    {
        "title": "Gosht Biryani, Paya Soup And Gurda Kaleji Fry: This Restaurant's Muslim Delicacies Are Just Like Dadi Makes",
        "source": "LBB, Bengaluru",
        "photo": "/assets/images/photos/news/lbb-sharief-bhai.jpg",
        "url": "https://lbb.in/bangalore/sharief-bhai-koramangala/",
    },
    {
        "title": "IPL 2026: Rajasthan Royals strengthen commercial lineup with Olio Pizza and MobiKwik partnerships",
        "source": "SportsMint Media",
        "photo": "/assets/images/photos/news/sportsmint-olio-rr.jpg",
        "url": "https://sportsmintmedia.com/ipl-2026-rajasthan-royals-strengthen-commercial-lineup-with-olio-pizza-and-mobikwik-partnerships/",
    },
    {
        "title": "Inside Curefoods' strategy against quick food delivery and its bet on Krispy Kreme and other brands",
        "source": "YourStory",
        "photo": "/assets/images/photos/news/curefoods-brand-tile.jpg",
        "url": "https://yourstory.com/2026/03/curefood-strategy-against-quick-food-delivery-bet-on-krispy-kreme",
    },
    {
        "title": "Curefoods widens playbook with chicken, coffee and ice cream ahead of IPO",
        "source": "ET Retail",
        "photo": "/assets/images/photos/curefoods-mascot.jpg",
        "url": "https://retail.economictimes.indiatimes.com/news/food-entertainment/food-services/curefoods-widens-playbook-with-chicken-coffee-and-ice-cream-ahead-of-ipo/129067916",
    },
    {
        "title": "Here's how Ankit Nagori plans to scale Curefoods",
        "source": "Business Today",
        "photo": "/assets/images/photos/news/businesstoday-ankit-nagori.jpg",
        "url": "https://www.businesstoday.in/latest/corporate/story/heres-how-ankit-nagori-plans-to-scale-curefoods-526760-2026-04-21",
    },
    {
        "title": "Curefoods takes on quick food delivery; a motivational AI fitness coach",
        "source": "YourStory",
        "photo": "/assets/images/photos/news/yourstory-daily-capsule.jpg",
        "url": "https://yourstory.com/2026/03/daily-capsule-curefoods-takes-on-quick-food-delivery",
    },
    {
        "title": "CureFoods and Hyperpure Create Automated Procurement System for 500+ Outlets",
        "source": "Entrepreneur India",
        "photo": "/assets/images/photos/news/entrepreneurindia-hyperpure.jpg",
        "url": "https://entrepreneurindia.com/blog/en/news/curefoods-and-hyperpure-create-automated-procurement-system-for-500-outlets.58882",
    },
    {
        "title": "Curefoods bets on premium, Gen Z demand; expands into new categories to drive growth",
        "source": "BusinessLine",
        "photo": "/assets/images/photos/news/businessline-krispy-kreme.jpg",
        "url": "https://www.thehindubusinessline.com/companies/curefoods-bets-on-premium-gen-z-demand-expands-into-new-categories-to-drive-growth/article70874384.ece",
    },
    {
        "title": "From cloud kitchens to cafes: Curefoods charts its next growth chapter",
        "source": "Fortune India",
        "photo": "/assets/images/photos/news/fortuneindia-growth.jpg",
        "url": "https://www.fortuneindia.com/startups-news/from-cloud-kitchens-to-cafes-curefoods-charts-its-next-growth-chapter/140444",
    },
    {
        "title": "India's coolest start-ups: How Ankit Nagori turned Curefoods into a formidable brand",
        "source": "Business Today",
        "photo": "/assets/images/photos/news/curefoods-brand-tile.jpg",
        "url": "https://www.businesstoday.in/magazine/corporate/story/indias-coolest-start-ups-how-ankit-nagori-turned-curefoods-into-a-formidable-brand-412622-2024-01-10",
    },
    {
        "title": "Ankit Nagori — CEO of Curefoods on Building India's Cloud Kitchen Empire",
        "source": "Franchise India",
        "photo": "/assets/images/photos/news/curefoods-brand-tile.jpg",
        "url": "https://www.franchiseindia.com/insights/en/interview/ankit-nagori-ceo-of-curefoods-on-building-indias-cloud-kitchen-empire.57613",
    },
    {
        "title": "Ankit Nagori: The Digital Foodpreneur",
        "source": "Entrepreneur India",
        "photo": "/assets/images/photos/news/entrepreneur-ankit-digital-foodpreneur.jpg",
        "url": "https://india.entrepreneur.com/entrepreneurs/ankit-nagori-the-digital-foodpreneur/450738",
    },
    {
        "title": "Our Flagship Brand Eatfit Enjoys A Customer Loyalty Rate Of 70%: Curefoods' Ankit Nagori",
        "source": "Inc42",
        "photo": "/assets/images/photos/news/inc42-eatfit-loyalty.jpg",
        "url": "https://inc42.com/buzz/our-flagship-brand-eatfit-enjoys-a-customer-loyalty-rate-of-70-curefoods-ankit-nagori/",
    },
    {
        "title": "Curefoods Acquires 5 More Food Brands To Amplify Its Footprint In 2022",
        "source": "Entrepreneur India",
        "photo": "/assets/images/photos/news/entrepreneur-5-brands-2022.jpg",
        "url": "https://india.entrepreneur.com/news-and-trends/curefoods-acquires-5-more-food-brands-to-amplify-its/411539",
    },
    {
        "title": "Curefoods becomes exclusive franchisee for Krispy Kreme India after acquiring New Delhi stores",
        "source": "World Coffee Portal",
        "photo": "/assets/images/photos/news/worldcoffeeportal-kk-franchise.jpg",
        "url": "https://www.worldcoffeeportal.com/news/curefoods-secures-pan-india-rights-to-operate-us-chain-krispy-kreme/",
    },
    {
        "title": "Krispy Kreme Debuts in Chandigarh with New Store at CP67 Mall",
        "source": "Franchise India",
        "photo": "/assets/images/photos/news/franchiseindia-kk-chandigarh.jpg",
        "url": "https://www.franchiseindia.com/insights/en/news/krispy-kreme-debuts-in-chandigarh-with-new-store-at-cp67-mall.59038",
    },
    {
        "title": "Krispy Kreme Launches First Jaipur Outlet, Marking its Entry into Rajasthan",
        "source": "Entrepreneur India",
        "photo": "/assets/images/photos/news/franchiseindia-kk-jaipur.jpg",
        "url": "https://www.entrepreneurindia.com/blog/en/news/krispy-kreme-launches-first-jaipur-outlet-marking-its-entry-into-rajasthan.58177",
    },
    {
        "title": "Curefoods' Olio Pizza launches 200th outlet with new kiosk in Calangute, Goa",
        "source": "IndiaRetailing",
        "photo": "/assets/images/photos/news/nuffoods-olio-goa.jpg",
        "url": "https://www.indiaretailing.com/2025/07/03/curefoods-olio-pizza-calangute-goa/",
    },
    {
        "title": "Sharief Bhai brings authentic biryani to the UAE with new restaurant at BurJuman",
        "source": "Khaleej Times",
        "photo": "/assets/images/photos/news/khaleejtimes-shariefbhai-dubai.jpg",
        "url": "https://www.khaleejtimes.com/kt-network/sharief-bhai-brings-authentic-biryani-to-the-uae-with-new-restaurant-at-burjuman",
    },
    {
        "title": "Rakul Preet Singh and Curefoods Join Hands to Launch Arambam",
        "source": "Entrepreneur India",
        "photo": "/assets/images/photos/news/entrepreneur-arambam-launch.jpg",
        "url": "https://india.entrepreneur.com/news-and-trends/rakul-preet-singh-and-curefoods-join-hands-to-launch-arambam/472904",
    },
]
