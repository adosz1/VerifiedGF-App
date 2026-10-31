import json

restaurants = [
  # ─── MIDLANDS & BURTON (10 Venues) ───
  {
    "id": 0, "name": "The Trentside Tavern", "type": "Gastropub & Grill", "city": "Burton upon Trent", "region": "midlands",
    "address": "27 Riverside Walk, Burton upon Trent, DE14 1RS", "shortLoc": "Burton upon Trent · 0.4 mi", "distance": "0.4 mi",
    "phone": "01283 742 881", "web": "trentsidetavern.co.uk", "hours": "Tue–Sun 12:00–22:00", "closed": "Closed Mondays",
    "duration": "3:42", "art": "🍳", "bg": "radial-gradient(circle at center, #1E293B, #0F172A)",
    "mapX": 395, "mapY": 390, "categories": ["midlands", "dedicated", "fine"],
    "badges": [{"text": "✓ 100% Dedicated Kitchen", "cls": "badge-verified-green"}, {"text": "✓ Dedicated Fryer", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "100% Gluten-Free Facility", "desc": "Zero gluten allowed on premises. No wheat flour enters the building."},
      {"title": "Dedicated Fish & Chips Fryer", "desc": "Separate oil tank tested weekly for gluten ppm count."},
      {"title": "Colour-Coded Allergen Tools", "desc": "All utensils comply with strict blue-handled allergy prep standards."}
    ],
    "menu": [
      {"section": "Starters", "items": [{"name": "Crispy Salt & Pepper Squid", "desc": "Rice flour dusting, lime aioli", "price": "£8.50"}, {"name": "Pan-Seared Scallops", "desc": "Cauliflower purée, crispy pancetta", "price": "£10.50"}]},
      {"section": "Mains", "items": [{"name": "Beer-Battered Haddock & Chips", "desc": "GF golden ale batter, hand-cut chips, peas", "price": "£16.50"}, {"name": "8oz Dry-Aged Ribeye Steak", "desc": "Triple-cooked chips, GF peppercorn sauce", "price": "£27.00"}]},
      {"section": "Desserts", "items": [{"name": "Warm Chocolate Fondant", "desc": "Vanilla bean ice cream, berry coulis", "price": "£7.50"}]}
    ]
  },
  {
    "id": 1, "name": "The Grain & Blossom", "type": "Artisan Bakery & Café", "city": "Burton upon Trent", "region": "midlands",
    "address": "14 High Street, Burton upon Trent, DE14 1JQ", "shortLoc": "Burton upon Trent · 0.8 mi", "distance": "0.8 mi",
    "phone": "01283 511 204", "web": "grainandblossom.co.uk", "hours": "Mon–Sat 08:00–17:00", "closed": "Closed Sundays",
    "duration": "2:17", "art": "☕", "bg": "radial-gradient(circle at center, #312E81, #1E1B4B)",
    "mapX": 398, "mapY": 394, "categories": ["midlands", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF Bakery", "cls": "badge-verified-green"}, {"text": "✓ Dedicated Ovens", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Flour Dust Free Environment", "desc": "No wheat, barley, or rye ever enters the bakery."},
      {"title": "Dedicated Deck Ovens", "desc": "Ovens calibrated solely for gluten-free sourdough and pastries."}
    ],
    "menu": [
      {"section": "Brunch", "items": [{"name": "Full Trentside Breakfast", "desc": "GF sausage, bacon, eggs, GF sourdough toast", "price": "£11.50"}, {"name": "Smashed Avo & Feta", "desc": "Toasted house sourdough, chilli flakes", "price": "£9.50"}]},
      {"section": "Bakery", "items": [{"name": "Butter Croissant", "desc": "100% GF lamination, baked fresh at 6am", "price": "£3.60"}, {"name": "Pain au Chocolat", "desc": "Belgian dark chocolate batons", "price": "£3.80"}]}
    ]
  },
  {
    "id": 2, "name": "Sakura Modern Japanese", "type": "Modern Japanese & Robata", "city": "Burton upon Trent", "region": "midlands",
    "address": "8 Orchard Street, Burton upon Trent, DE14 2PP", "shortLoc": "Burton upon Trent · 1.2 mi", "distance": "1.2 mi",
    "phone": "01283 648 322", "web": "sakurabt.co.uk", "hours": "Wed–Sun 17:30–22:30", "closed": "Closed Mon–Tue",
    "duration": "4:05", "art": "🥢", "bg": "radial-gradient(circle at center, #881337, #4C0519)",
    "mapX": 392, "mapY": 398, "categories": ["midlands", "asian", "dedicated"],
    "badges": [{"text": "✓ Certified GF Tamari Only", "cls": "badge-verified-green"}, {"text": "✓ Separate Tempura Fryer", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Zero Wheat Soy Sauce", "desc": "Kitchen exclusively stocks certified gluten-free tamari."},
      {"title": "Rice Flour Tempura", "desc": "Dedicated fryer uses 100% potato & rice starches."}
    ],
    "menu": [
      {"section": "Sushi", "items": [{"name": "Salmon Nigiri (4)", "desc": "Scottish salmon, GF tamari glaze", "price": "£9.50"}, {"name": "Dragon Maki Roll (8)", "desc": "Prawn tempura, avocado, GF eel sauce", "price": "£13.50"}]},
      {"section": "Mains", "items": [{"name": "Chicken Katsu Curry", "desc": "Crispy GF panko chicken, aromatic curry, rice", "price": "£16.00"}]}
    ]
  },
  {
    "id": 3, "name": "Spice Sanctuary", "type": "Indian Dining & Tandoor", "city": "Burton upon Trent", "region": "midlands",
    "address": "42 Union Street, Burton upon Trent, DE14 1AA", "shortLoc": "Burton upon Trent · 0.6 mi", "distance": "0.6 mi",
    "phone": "01283 583 100", "web": "spicesanctuary.co.uk", "hours": "Tue–Sun 12:00–22:30", "closed": "Closed Mondays",
    "duration": "3:28", "art": "🍛", "bg": "radial-gradient(circle at center, #7C2D12, #431407)",
    "mapX": 402, "mapY": 392, "categories": ["midlands", "asian", "dedicated"],
    "badges": [{"text": "✓ Single-Source Spices", "cls": "badge-verified-green"}, {"text": "✓ Dedicated Tandoor", "cls": "badge-verified-green"}, {"text": "✓ 100% GF Menu", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Milled-to-Order Spices", "desc": "Whole spices milled in certified GF premises to avoid transit contamination."},
      {"title": "GF Naan in Dedicated Oven", "desc": "Clay tandoor used exclusively for coeliac-safe doughs."}
    ],
    "menu": [
      {"section": "Curries", "items": [{"name": "Lamb Rogan Josh", "desc": "Slow-cooked shoulder, saffron basmati", "price": "£16.50"}, {"name": "Butter Chicken", "desc": "Old Delhi creamy tomato sauce, rice", "price": "£15.50"}]},
      {"section": "Breads", "items": [{"name": "GF Garlic & Coriander Naan", "desc": "Tapioca & chickpea blend, baked fresh", "price": "£3.80"}]}
    ]
  },
  {
    "id": 4, "name": "Pura Pasta", "type": "Italian Trattoria & Pizzeria", "city": "Burton upon Trent", "region": "midlands",
    "address": "19 Station Street, Burton upon Trent, DE14 1BT", "shortLoc": "Burton upon Trent · 0.3 mi", "distance": "0.3 mi",
    "phone": "01283 490 555", "web": "purapastabt.co.uk", "hours": "Mon–Sun 11:30–22:00", "closed": "Open 7 Days",
    "duration": "2:54", "art": "🍝", "bg": "radial-gradient(circle at center, #14532D, #052E16)",
    "mapX": 396, "mapY": 386, "categories": ["midlands", "fine", "dedicated"],
    "badges": [{"text": "✓ Fresh GF Pasta Daily", "cls": "badge-verified-green"}, {"text": "✓ Dedicated Stone Oven", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Hand-Rolled GF Pasta", "desc": "Made daily with corn, rice, and egg yolk. No dry box pasta used."},
      {"title": "Zero Wheat Flour in Building", "desc": "Airborne flour contamination is physically impossible."}
    ],
    "menu": [
      {"section": "Handmade Pasta", "items": [{"name": "Beef Ragù Pappardelle", "desc": "12-hour Chianti braised beef, Parmigiano", "price": "£16.50"}, {"name": "Lobster & Crab Linguine", "desc": "Chilli, garlic, white wine emulsion", "price": "£22.00"}]},
      {"section": "Pizza", "items": [{"name": "Margherita D.O.P.", "desc": "San Marzano tomatoes, Fior di Latte", "price": "£13.50"}]}
    ]
  },
  {
    "id": 5, "name": "Libre Kitchen", "type": "Corn Mexican Street Food", "city": "Burton upon Trent", "region": "midlands",
    "address": "55 Horninglow Street, Burton upon Trent, DE13 0PJ", "shortLoc": "Burton upon Trent · 1.5 mi", "distance": "1.5 mi",
    "phone": "01283 712 999", "web": "librekitchen.co.uk", "hours": "Mon–Sat 11:00–21:00", "closed": "Closed Sundays",
    "duration": "2:35", "art": "🌮", "bg": "radial-gradient(circle at center, #854D0E, #422006)",
    "mapX": 408, "mapY": 402, "categories": ["midlands", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% Nixtamal Corn", "cls": "badge-verified-green"}, {"text": "✓ Dedicated Tortilla Fryer", "cls": "badge-verified-green"}, {"text": "✓ Takeaway Sealed", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Corn Tortillas Only", "desc": "Wheat flour tortillas are forbidden on premises."},
      {"title": "Tamper-Evident Seals", "desc": "Takeaway bags sealed with coeliac-safe inspection tape."}
    ],
    "menu": [
      {"section": "Tacos", "items": [{"name": "Beef Birria Quesatacos (3)", "desc": "Slow-cooked beef, melted Oaxaca, consommé dip", "price": "£12.50"}, {"name": "Baja Crispy Fish Tacos (3)", "desc": "GF batter, chipotle crema, lime slaw", "price": "£11.80"}]}
    ]
  },
  {
    "id": 6, "name": "Petite Maison", "type": "Patisserie & Afternoon Tea", "city": "Burton upon Trent", "region": "midlands",
    "address": "3 George Street, Burton upon Trent, DE14 1EB", "shortLoc": "Burton upon Trent · 0.9 mi", "distance": "0.9 mi",
    "phone": "01283 602 411", "web": "petitemaisonbt.co.uk", "hours": "Wed–Sun 09:00–17:00", "closed": "Closed Mon–Tue",
    "duration": "3:10", "art": "🧁", "bg": "radial-gradient(circle at center, #701A75, #4A044E)",
    "mapX": 390, "mapY": 393, "categories": ["midlands", "cafe", "fine"],
    "badges": [{"text": "✓ 100% GF Patisserie", "cls": "badge-verified-green"}, {"text": "✓ Dedicated High Tea Prep", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "French Technique, 0% Gluten", "desc": "Choux, macarons, and sponges baked with almond and rice flours."},
      {"title": "Strict Certified Butter & Creams", "desc": "All dairy certified free of grain thickeners."}
    ],
    "menu": [
      {"section": "Afternoon Tea", "items": [{"name": "Traditional Afternoon Tea", "desc": "4 sandwiches, 2 warm scones, 4 mini pastries, tea", "price": "£28.00"}]},
      {"section": "Patisserie", "items": [{"name": "Opera Gateau", "desc": "Almond sponge, coffee buttercream, dark chocolate", "price": "£5.80"}]}
    ]
  },
  {
    "id": 7, "name": "Bee Gluten Free", "type": "Artisan Bakery & Delicatessen", "city": "Birmingham", "region": "midlands",
    "address": "South Birmingham Hub, B30 3DY", "shortLoc": "Birmingham · 24 mi", "distance": "24 mi",
    "phone": "0121 459 9200", "web": "beeglutenfree.co.uk", "hours": "Tue–Sat 09:00–16:00", "closed": "Closed Sun–Mon",
    "duration": "2:40", "art": "🐝", "bg": "radial-gradient(circle at center, #CA8A04, #713F12)",
    "mapX": 380, "mapY": 420, "categories": ["midlands", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% Dedicated Facility", "cls": "badge-verified-green"}, {"text": "✓ Savoury Pies & Bakes", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "100% Dedicated Midlands Kitchen", "desc": "Full allergy certification. Caters for severe coeliac disease."}
    ],
    "menu": [
      {"section": "Savoury Bakes", "items": [{"name": "Steak & Ale Pie", "desc": "GF pastry, tender beef in rich GF ale gravy", "price": "£6.50"}, {"name": "Traditional Cornish Pasty", "desc": "Flaky GF shortcrust, beef, swede, potato", "price": "£5.80"}]}
    ]
  },
  {
    "id": 8, "name": "The Farmhouse at Mackworth", "type": "Gastropub Dining", "city": "Derby", "region": "midlands",
    "address": "Ashbourne Road, Mackworth, Derby, DE22 4LY", "shortLoc": "Derby · 11 mi", "distance": "11 mi",
    "phone": "01332 824 324", "web": "thefarmhouseatmackworth.com", "hours": "Mon–Sun 12:00–22:00", "closed": "Open 7 Days",
    "duration": "3:15", "art": "🏡", "bg": "radial-gradient(circle at center, #15803D, #14532D)",
    "mapX": 410, "mapY": 370, "categories": ["midlands", "fine", "dedicated"],
    "badges": [{"text": "✓ Coeliac UK Accredited", "cls": "badge-certified"}, {"text": "✓ Dedicated GF Station", "cls": "badge-verified-green"}, {"text": "✓ Verified GF Fryer", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "Coeliac UK Accredited Partner", "desc": "Independent kitchen audits verifying allergen procedures."}
    ],
    "menu": [
      {"section": "Mains", "items": [{"name": "Pan-Fried Sea Bass", "desc": "Crushed new potatoes, samphire, white wine sauce", "price": "£21.50"}, {"name": "Sunday Roast (GF)", "desc": "Roast sirloin, GF Yorkshire pudding, roast potatoes, gravy", "price": "£19.50"}]}
    ]
  },
  {
    "id": 9, "name": "No 12 Plantbased & GF", "type": "Fine Dining Tasting Menus", "city": "Nottingham", "region": "midlands",
    "address": "Eldon Chambers, Wheeler Gate, Nottingham, NG1 2NS", "shortLoc": "Nottingham · 26 mi", "distance": "26 mi",
    "phone": "0115 958 7990", "web": "no12restaurant.co.uk", "hours": "Wed–Sat 17:30–22:00", "closed": "Closed Sun–Tue",
    "duration": "4:12", "art": "🌿", "bg": "radial-gradient(circle at center, #0F766E, #134E4A)",
    "mapX": 435, "mapY": 375, "categories": ["midlands", "fine", "dedicated"],
    "badges": [{"text": "✓ 100% GF Tasting Menus", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe Certified", "cls": "badge-certified"}, {"text": "✓ Michelin Guide Listed", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "7-Course Coeliac Tasting", "desc": "Entire tasting experience is 100% coeliac-safe by default."}
    ],
    "menu": [
      {"section": "Tasting Menu Highlights", "items": [{"name": "Charred King Oyster Mushroom", "desc": "Truffled potato mousseline, mushroom jus", "price": "£14.00"}, {"name": "Smoked Beetroot Tartare", "desc": "Caper emulsion, GF seeded crackers", "price": "£12.00"}]}
    ]
  },

  # ─── LONDON (16 Venues) ───
  {
    "id": 10, "name": "Niche Gluten-free Dining", "type": "100% GF British Comfort Dining", "city": "London", "region": "london",
    "address": "197-199 Rosebery Ave, Islington, London, EC1R 4TJ", "shortLoc": "Islington, London", "distance": "London Central",
    "phone": "020 7837 5048", "web": "nicherestaurants.co.uk", "hours": "Mon–Sun 12:00–22:00", "closed": "Open 7 Days",
    "duration": "3:55", "art": "🇬🇧", "bg": "radial-gradient(circle at center, #1E3A8A, #0F172A)",
    "mapX": 472, "mapY": 490, "categories": ["london", "dedicated", "fine"],
    "badges": [{"text": "✓ London's 1st 100% GF", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Certified", "cls": "badge-certified"}, {"text": "✓ Peanut & Sesame Free", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "100% Gluten-Free Since Day One", "desc": "Pioneering Coeliac UK accredited venue in London. Zero gluten in kitchen."}
    ],
    "menu": [
      {"section": "Comfort Classics", "items": [{"name": "Southern Fried Chicken", "desc": "GF spiced coating, skin-on fries, house slaw", "price": "£18.50"}, {"name": "Niche Beef & Ale Pie", "desc": "Rich braised beef in GF pastry, mash, gravy", "price": "£19.50"}, {"name": "Parmesan & Truffle Doughnut Balls", "desc": "Savory GF choux balls, garlic dip", "price": "£8.50"}]}
    ]
  },
  {
    "id": 11, "name": "Paladar", "type": "100% GF Latin American Dining", "city": "London", "region": "london",
    "address": "4-5 London Rd, Southwark, London, SE1 6JZ", "shortLoc": "Elephant & Castle, London", "distance": "London SE1",
    "phone": "020 7186 5555", "web": "paladarlondon.com", "hours": "Tue–Sun 12:00–22:30", "closed": "Closed Mondays",
    "duration": "4:15", "art": "🥑", "bg": "radial-gradient(circle at center, #B91C1C, #450A0A)",
    "mapX": 475, "mapY": 498, "categories": ["london", "asian", "dedicated", "fine"],
    "badges": [{"text": "✓ 100% GF Latin Kitchen", "cls": "badge-verified-green"}, {"text": "✓ 100% Corn & Cassava", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Naturally Gluten-Free Tradition", "desc": "Entire menu based on corn, cassava, and plantain. Zero wheat allowed."}
    ],
    "menu": [
      {"section": "Small Plates & Sharing", "items": [{"name": "Crispy Cassava Croquettes", "desc": "Guava salsa, creamy queso blanco", "price": "£9.00"}, {"name": "Roast Pork Carnitas", "desc": "Black bean purée, grilled pineapple salsa", "price": "£16.50"}, {"name": "100% GF Cinnamon Churros", "desc": "Dulce de leche & spicy chocolate dips", "price": "£8.50"}]}
    ]
  },
  {
    "id": 12, "name": "Utter Waffle", "type": "100% GF Waffle House & Brunch", "city": "London", "region": "london",
    "address": "119 Dulwich Rd, Herne Hill, London, SE24 0NG", "shortLoc": "Herne Hill, London", "distance": "London South",
    "phone": "020 7737 4555", "web": "utterwaffle.co.uk", "hours": "Wed–Sun 09:00–16:00", "closed": "Closed Mon–Tue",
    "duration": "2:50", "art": "🧇", "bg": "radial-gradient(circle at center, #EA580C, #7C2D12)",
    "mapX": 471, "mapY": 508, "categories": ["london", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF Waffle Kitchen", "cls": "badge-verified-green"}, {"text": "✓ Multi-Award Winning", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Society Loved", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Zero Wheat Waffle Irons", "desc": "All waffle irons dedicated 100% to coeliac-safe proprietary waffle recipe."}
    ],
    "menu": [
      {"section": "Savoury Stuffed Waffles", "items": [{"name": "The James Bland", "desc": "Waffle stuffed with smoked bacon, topped with fried chicken & maple", "price": "£14.50"}, {"name": "Waffle Eggs Royale", "desc": "Smoked salmon, poached eggs, hollandaise", "price": "£13.50"}]}
    ]
  },
  {
    "id": 13, "name": "Après Food Co.", "type": "Wholesome Organic Dining", "city": "London", "region": "london",
    "address": "72 St John St, Clerkenwell, London, EC1M 4DT", "shortLoc": "Clerkenwell, London", "distance": "London Central",
    "phone": "020 7686 8888", "web": "apresfood.com", "hours": "Mon–Sat 10:00–21:00", "closed": "Closed Sundays",
    "duration": "3:20", "art": "🥗", "bg": "radial-gradient(circle at center, #047857, #064E3B)",
    "mapX": 474, "mapY": 488, "categories": ["london", "fine", "dedicated"],
    "badges": [{"text": "✓ 100% GF & Refined Sugar Free", "cls": "badge-verified-green"}, {"text": "✓ Nutritional Chef Led", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Clean Certified Ingredients", "desc": "Nutritional therapist approved kitchen free of refined sugars and gluten."}
    ],
    "menu": [
      {"section": "Mains", "items": [{"name": "12-Hour Slow Cooked Lamb", "desc": "Sweet potato mash, seasonal greens, rosemary jus", "price": "£22.00"}, {"name": "Artisanal GF Sourdough Pizza", "desc": "San Marzano, Buffalo mozzarella, Parma ham", "price": "£16.50"}]}
    ]
  },
  {
    "id": 14, "name": "Indigo at One Aldwych", "type": "Luxury Hotel Dining (100% GF)", "city": "London", "region": "london",
    "address": "1 Aldwych, Covent Garden, London, WC2B 4BZ", "shortLoc": "Covent Garden, London", "distance": "London West End",
    "phone": "020 7300 1070", "web": "onealdwych.com/indigo", "hours": "Tue–Sun 12:00–22:30", "closed": "Closed Mondays",
    "duration": "4:40", "art": "🍷", "bg": "radial-gradient(circle at center, #4C1D95, #2E1065)",
    "mapX": 473, "mapY": 492, "categories": ["london", "fine", "dedicated"],
    "badges": [{"text": "✓ 100% GF & Dairy Free", "cls": "badge-verified-green"}, {"text": "✓ Executive Chef Led", "cls": "badge-verified-green"}, {"text": "✓ 5-Star Hotel Kitchen", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Entirely Gluten & Dairy Free", "desc": "Renowned luxury restaurant where every single dish is certified coeliac-safe."}
    ],
    "menu": [
      {"section": "Fine Dining", "items": [{"name": "Diver-Caught Scallops", "desc": "Pea purée, crispy shallots, bacon crumb", "price": "£19.00"}, {"name": "Dry-Aged Beef Fillet", "desc": "Caramelised onion purée, truffle potato terrine", "price": "£38.00"}]}
    ]
  },
  {
    "id": 15, "name": "Los Mochis", "type": "Mexican & Japanese Fusion", "city": "London", "region": "london",
    "address": "2-4 Farmer St, Notting Hill, London, W8 7SN", "shortLoc": "Notting Hill, London", "distance": "London West",
    "phone": "020 7229 5555", "web": "losmochis.co.uk", "hours": "Mon–Sun 12:00–23:00", "closed": "Open 7 Days",
    "duration": "3:50", "art": "🌮", "bg": "radial-gradient(circle at center, #BE123C, #4C0519)",
    "mapX": 462, "mapY": 491, "categories": ["london", "asian", "dedicated", "fine"],
    "badges": [{"text": "✓ 100% Gluten-Free Menu", "cls": "badge-verified-green"}, {"text": "✓ Zero Wheat Anywhere", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Accredited", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Full Fusion Without Gluten", "desc": "Mexican street food meets Japanese maki. Not a grain of gluten in the kitchen."}
    ],
    "menu": [
      {"section": "Tacos & Maki", "items": [{"name": "Truffle Guacamole", "desc": "Fresh corn chips, shaved black truffle", "price": "£12.50"}, {"name": "Wagyu Carne Asada Tacos (2)", "desc": "A5 wagyu, smoked habanero, pickled onion", "price": "£18.00"}]}
    ]
  },
  {
    "id": 16, "name": "Station 26", "type": "French & British Bistro", "city": "London", "region": "london",
    "address": "Brixton Village, Coldharbour Ln, London, SW9 8PS", "shortLoc": "Brixton, London", "distance": "London SW9",
    "phone": "020 7733 8826", "web": "station26.co.uk", "hours": "Tue–Sun 12:00–22:00", "closed": "Closed Mondays",
    "duration": "3:05", "art": "🥩", "bg": "radial-gradient(circle at center, #0284C7, #082F49)",
    "mapX": 472, "mapY": 505, "categories": ["london", "fine", "dedicated"],
    "badges": [{"text": "✓ 100% Dedicated Bistro", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Haven", "cls": "badge-verified-green"}, {"text": "✓ Homemade GF Breads", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Boutique Dedicated Kitchen", "desc": "Popular Brixton Village hotspot with zero gluten on site."}
    ],
    "menu": [
      {"section": "Bistro Mains", "items": [{"name": "Steak Frites", "desc": "Aged ribeye steak, GF hand-cut fries, béarnaise sauce", "price": "£21.50"}, {"name": "Confit Duck Leg", "desc": "Dauphinoise potatoes, red wine reduction", "price": "£19.50"}]}
    ]
  },
  {
    "id": 17, "name": "Manna Dew", "type": "French Patisserie & Bakery", "city": "London", "region": "london",
    "address": "169 Battersea High St, London, SW11 3JS", "shortLoc": "Battersea, London", "distance": "London SW11",
    "phone": "020 3633 4488", "web": "mannadew.co.uk", "hours": "Tue–Sat 09:00–17:00", "closed": "Closed Sun–Mon",
    "duration": "2:30", "art": "🥐", "bg": "radial-gradient(circle at center, #D97706, #78350F)",
    "mapX": 468, "mapY": 501, "categories": ["london", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% Dedicated Pastry Hub", "cls": "badge-verified-green"}, {"text": "✓ Award-Winning Croissants", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Artisan French Lamination", "desc": "Pioneered the UK's first authentic flaky gluten-free butter croissants."}
    ],
    "menu": [
      {"section": "Laminated Pastries", "items": [{"name": "Classic Butter Croissant", "desc": "100% GF butter pastry, 24 flaky layers", "price": "£3.80"}, {"name": "Almond Frangipane Croissant", "desc": "Toasted flaked almonds, rich filling", "price": "£4.50"}]}
    ]
  },
  {
    "id": 18, "name": "Copains London", "type": "Parisian Bakery & Café", "city": "London", "region": "london",
    "address": "40 Long Acre, Covent Garden, London, WC2E 9JT", "shortLoc": "Covent Garden, London", "distance": "London Central",
    "phone": "020 7497 2200", "web": "copains-paris.com", "hours": "Mon–Sun 08:30–18:30", "closed": "Open 7 Days",
    "duration": "2:45", "art": "🥖", "bg": "radial-gradient(circle at center, #4338CA, #1E1B4B)",
    "mapX": 473, "mapY": 491, "categories": ["london", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% Gluten-Free Bakery", "cls": "badge-verified-green"}, {"text": "✓ Paris Born Concept", "cls": "badge-verified-green"}, {"text": "✓ Artisanal Baguettes", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Dedicated French Craft", "desc": "Baking fresh daily with corn, rice, and buckwheat flours. Zero wheat."}
    ],
    "menu": [
      {"section": "Fresh Bakes", "items": [{"name": "Traditional French Baguette", "desc": "Crispy crust, chewy crumb, 100% GF", "price": "£3.50"}, {"name": "Tarte au Citron Meringuée", "desc": "Tangy lemon curd, torched meringue", "price": "£5.20"}]}
    ]
  },
  {
    "id": 19, "name": "Cookies and Scream", "type": "Retro Bakery & Dessert Bar", "city": "London", "region": "london",
    "address": "130 Holloway Rd, London, N7 8JE", "shortLoc": "Holloway, London", "distance": "London North",
    "phone": "020 7700 3322", "web": "cookiesandscream.com", "hours": "Wed–Sun 12:00–18:00", "closed": "Closed Mon–Tue",
    "duration": "2:10", "art": "🍪", "bg": "radial-gradient(circle at center, #9333EA, #3B0764)",
    "mapX": 472, "mapY": 482, "categories": ["london", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF & Vegan", "cls": "badge-verified-green"}, {"text": "✓ Cult Coeliac Destination", "cls": "badge-verified-green"}, {"text": "✓ Made From Scratch", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Vegan & Coeliac Haven", "desc": "Dedicated bakery kitchen operating without gluten, dairy, or eggs."}
    ],
    "menu": [
      {"section": "Scream Treats", "items": [{"name": "The Scream Shake", "desc": "Thick milkshake blended with warm brownie", "price": "£6.50"}, {"name": "Choc Fudge Cookie Pie", "desc": "Thick cookie pie with molten centre", "price": "£4.50"}]}
    ]
  },
  {
    "id": 20, "name": "Wicked Fish", "type": "100% GF Chipper & Seafood", "city": "London", "region": "london",
    "address": "Spitalfields & Hackney, London, E1 6EW", "shortLoc": "Spitalfields, London", "distance": "London East",
    "phone": "020 7247 1100", "web": "wickedfish.co.uk", "hours": "Tue–Sun 11:30–21:30", "closed": "Closed Mondays",
    "duration": "3:10", "art": "🐟", "bg": "radial-gradient(circle at center, #0284C7, #0C4A6E)",
    "mapX": 477, "mapY": 489, "categories": ["london", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% GF Fryers", "cls": "badge-verified-green"}, {"text": "✓ Sustainable Cod & Haddock", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Approved", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Zero Wheat in Frying Oil", "desc": "All batter made with rice flour and sparkling soda water."}
    ],
    "menu": [
      {"section": "Seafood Classics", "items": [{"name": "Atlantic Cod & Chips", "desc": "Golden light GF batter, beef dripping chips", "price": "£15.50"}, {"name": "GF Battered Sausage", "desc": "Butcher's pork sausage in crispy batter", "price": "£5.00"}]}
    ]
  },
  {
    "id": 21, "name": "Near & Far", "type": "Californian Bar & Kitchen", "city": "London", "region": "london",
    "address": "48 Chalk Farm Rd, Camden, London, NW1 8AJ", "shortLoc": "Camden, London", "distance": "London NW1",
    "phone": "020 7485 5566", "web": "nearandfarlondon.com", "hours": "Wed–Sun 16:00–23:00", "closed": "Closed Mon–Tue",
    "duration": "3:30", "art": "🌴", "bg": "radial-gradient(circle at center, #DB2777, #831843)",
    "mapX": 469, "mapY": 486, "categories": ["london", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% Gluten-Free Food", "cls": "badge-verified-green"}, {"text": "✓ Palm Springs Aesthetic", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "100% Coeliac-Safe Street Food", "desc": "Full kitchen menu is strictly gluten-free."}
    ],
    "menu": [
      {"section": "Street Bites", "items": [{"name": "Loaded Corn Nachos", "desc": "Melted cheese, salsa fresca, jalapenos, sour cream", "price": "£10.50"}, {"name": "Crispy Buttermilk Chicken Strips", "desc": "GF batter, honey mustard dip", "price": "£9.00"}]}
    ]
  },
  {
    "id": 22, "name": "Vida Bakery", "type": "Rainbow Bakery & Tearoom", "city": "London", "region": "london",
    "address": "139 Brick Ln, London, E1 6SB", "shortLoc": "Brick Lane, London", "distance": "London East",
    "phone": "020 7739 1222", "web": "vidabakery.co.uk", "hours": "Thu–Sun 11:00–18:00", "closed": "Closed Mon–Wed",
    "duration": "2:25", "art": "🍰", "bg": "radial-gradient(circle at center, #F43F5E, #881337)",
    "mapX": 478, "mapY": 490, "categories": ["london", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF & Dairy Free", "cls": "badge-verified-green"}, {"text": "✓ Custom Celebration Cakes", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Whimsical Allergy Safe Bakery", "desc": "Free of gluten, dairy, and eggs in dedicated facility."}
    ],
    "menu": [
      {"section": "Sweet Treats", "items": [{"name": "Rainbow Cake Slice", "desc": "Multi-coloured vanilla sponge, buttercream", "price": "£6.00"}, {"name": "Salted Caramel Cupcake", "desc": "Moist chocolate sponge, caramel drizzle", "price": "£3.80"}]}
    ]
  },
  {
    "id": 23, "name": "Grom Gelato", "type": "100% GF Italian Gelateria", "city": "London", "region": "london",
    "address": "16 Piccadilly, London, W1J 0DE", "shortLoc": "Piccadilly, London", "distance": "London Central",
    "phone": "020 7434 0000", "web": "grom.it", "hours": "Mon–Sun 11:00–23:00", "closed": "Open 7 Days",
    "duration": "2:00", "art": "🍨", "bg": "radial-gradient(circle at center, #0284C7, #075985)",
    "mapX": 472, "mapY": 493, "categories": ["london", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF Cones & Gelato", "cls": "badge-verified-green"}, {"text": "✓ Italian Coeliac Society (AIC)", "cls": "badge-certified"}, {"text": "✓ Zero Cross Contact", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "Certified Gluten-Free Gelateria", "desc": "All biscuits, waffle cones, and flavours are certified GF by Italian Coeliac Society."}
    ],
    "menu": [
      {"section": "Gelato & Cones", "items": [{"name": "Crispy Waffle Cone (Double Scoop)", "desc": "Pistachio & Crema di Grom in GF baked cone", "price": "£6.50"}, {"name": "Hot Chocolate Affogato", "desc": "Vanilla gelato drowned in hot Italian chocolate", "price": "£5.50"}]}
    ]
  },
  {
    "id": 24, "name": "Leadbelly's Bar & Kitchen", "type": "Modern British Bar & Grill", "city": "London", "region": "london",
    "address": "Montreal House, Deal Porter Way, London, SE16 7AQ", "shortLoc": "Canada Water, London", "distance": "London SE16",
    "phone": "020 7231 8444", "web": "leadbellysbar.co.uk", "hours": "Mon–Sun 12:00–22:30", "closed": "Open 7 Days",
    "duration": "3:40", "art": "🍔", "bg": "radial-gradient(circle at center, #374151, #111827)",
    "mapX": 479, "mapY": 497, "categories": ["london", "fine", "dedicated"],
    "badges": [{"text": "✓ Coeliac UK Accredited", "cls": "badge-certified"}, {"text": "✓ 98% Menu Gluten Free", "cls": "badge-verified-green"}, {"text": "✓ Dedicated Fryers", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "Accredited Coeliac Kitchen", "desc": "Rigorous kitchen controls inspected by Coeliac UK team."}
    ],
    "menu": [
      {"section": "Pub Classics", "items": [{"name": "Leadbelly's Bacon Cheeseburger", "desc": "GF brioche bun, double beef patty, fries", "price": "£16.50"}, {"name": "Crispy Calamari", "desc": "GF flour coating, garlic mayonnaise", "price": "£8.50"}]}
    ]
  },
  {
    "id": 25, "name": "The Bach", "type": "Kiwi Brunch & Specialty Coffee", "city": "London", "region": "london",
    "address": "12 Broadway Market, London, E8 4QJ", "shortLoc": "Broadway Market, London", "distance": "London East",
    "phone": "020 7254 3333", "web": "wearethebach.com", "hours": "Mon–Sun 08:30–16:30", "closed": "Open 7 Days",
    "duration": "2:35", "art": "🥝", "bg": "radial-gradient(circle at center, #15803D, #052E16)",
    "mapX": 478, "mapY": 486, "categories": ["london", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF Kitchen", "cls": "badge-verified-green"}, {"text": "✓ New Zealand Style", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "All-Day Coeliac Safe Brunch", "desc": "Everything made in-house using certified gluten-free grain alternatives."}
    ],
    "menu": [
      {"section": "Kiwi Brunch", "items": [{"name": "Sweet Corn Fritters", "desc": "Avocado, chilli jam, grilled halloumi", "price": "£13.50"}, {"name": "Toasted Banana Bread", "desc": "Espresso butter, maple walnuts", "price": "£5.50"}]}
    ]
  },

  # ─── MANCHESTER & THE NORTH (10 Venues) ───
  {
    "id": 26, "name": "Off The Wheaten Track", "type": "Deli & Tearoom", "city": "Manchester", "region": "north",
    "address": "8 Oxford Rd, Altrincham, Greater Manchester, WA14 2DY", "shortLoc": "Altrincham, Manchester", "distance": "Manchester Area",
    "phone": "0161 941 2444", "web": "offthewheatentrackdeli.com", "hours": "Tue–Sat 09:30–16:30", "closed": "Closed Sun–Mon",
    "duration": "3:25", "art": "🥧", "bg": "radial-gradient(circle at center, #B45309, #78350F)",
    "mapX": 365, "mapY": 340, "categories": ["north", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% Dedicated Deli", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Accredited", "cls": "badge-certified"}, {"text": "✓ Traditional British Bakes", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "Pioneer Coeliac Tearoom", "desc": "Award-winning north-west hub where everything is guaranteed 100% gluten-free."}
    ],
    "menu": [
      {"section": "Deli Specialities", "items": [{"name": "Traditional Afternoon Tea", "desc": "GF finger sandwiches, fresh scones, cakes, tea", "price": "£24.00"}, {"name": "Steak & Onion Suet Pudding", "desc": "Tender beef in GF suet crust, gravy, chips", "price": "£14.50"}]}
    ]
  },
  {
    "id": 27, "name": "The Remedy Kitchen", "type": "Holistic Healthy Kitchen", "city": "Manchester", "region": "north",
    "address": "19 Royal Exchange Arcade, Manchester, M2 7EA", "shortLoc": "Manchester Centre", "distance": "Manchester Central",
    "phone": "0161 832 9900", "web": "theremedykitchen.co.uk", "hours": "Mon–Sun 09:00–17:00", "closed": "Open 7 Days",
    "duration": "3:00", "art": "🥑", "bg": "radial-gradient(circle at center, #047857, #064E3B)",
    "mapX": 368, "mapY": 335, "categories": ["north", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% Gluten-Free", "cls": "badge-verified-green"}, {"text": "✓ Dairy & Refined Sugar Free", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Zero Allergen Compromise", "desc": "Dedicated kitchen designed specifically for digestive wellness and coeliac disease."}
    ],
    "menu": [
      {"section": "Bowls & Brunch", "items": [{"name": "Buckwheat Protein Pancakes", "desc": "Berry compote, coconut yoghurt, maple", "price": "£11.50"}, {"name": "Teriyaki Salmon Nourish Bowl", "desc": "GF teriyaki, quinoa, edamame, avocado", "price": "£14.50"}]}
    ]
  },
  {
    "id": 28, "name": "Mia’s Arepas", "type": "Venezuelan Street Food", "city": "Manchester", "region": "north",
    "address": "Escape to Freight Island, Baring St, Manchester, M1 2PZ", "shortLoc": "Freight Island, Manchester", "distance": "Manchester M1",
    "phone": "0161 507 9999", "web": "miasarepas.co.uk", "hours": "Wed–Sun 12:00–22:00", "closed": "Closed Mon–Tue",
    "duration": "2:30", "art": "🫓", "bg": "radial-gradient(circle at center, #EA580C, #9A3412)",
    "mapX": 370, "mapY": 338, "categories": ["north", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% GF Corn Kitchen", "cls": "badge-verified-green"}, {"text": "✓ Halal Certified", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Pure Pre-Cooked Cornmeal", "desc": "Arepas grilled fresh on dedicated plates. Zero wheat on premises."}
    ],
    "menu": [
      {"section": "Arepas", "items": [{"name": "La Pabellón", "desc": "Shredded beef, black beans, fried plantain, queso", "price": "£10.50"}, {"name": "Reina Pepiada", "desc": "Shredded chicken, avocado, lime mayo", "price": "£9.80"}]}
    ]
  },
  {
    "id": 29, "name": "Pico’s Tacos", "type": "Mexican Taqueria", "city": "Manchester", "region": "north",
    "address": "Mackie Mayor, 1 Eagle St, Manchester, M4 5BU", "shortLoc": "Northern Quarter, Manchester", "distance": "Manchester M4",
    "phone": "0161 834 8888", "web": "picostacos.co.uk", "hours": "Tue–Sun 11:30–21:30", "closed": "Closed Mondays",
    "duration": "2:40", "art": "🌮", "bg": "radial-gradient(circle at center, #B91C1C, #7F1D1D)",
    "mapX": 372, "mapY": 334, "categories": ["north", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% GF Taqueria", "cls": "badge-verified-green"}, {"text": "✓ Freshly Pressed Corn", "cls": "badge-verified-green"}, {"text": "✓ Dedicated Prep", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Masa Harina Certified", "desc": "Entire taco menu is naturally gluten-free without risk of cross-contamination."}
    ],
    "menu": [
      {"section": "Tacos (3)", "items": [{"name": "Pork Carnitas", "desc": "Slow-braised pork, salsa verde, coriander", "price": "£11.00"}, {"name": "Grilled Fish Tacos", "desc": "Chilli marinated cod, pickled cabbage, crema", "price": "£12.00"}]}
    ]
  },
  {
    "id": 30, "name": "The Oxford Place", "type": "Fine Dining Restaurant", "city": "Leeds", "region": "north",
    "address": "2 Oxford Pl, Leeds, LS1 3AX", "shortLoc": "Leeds City Centre", "distance": "Leeds Central",
    "phone": "0113 234 1200", "web": "theoxfordplace.uk", "hours": "Tue–Sat 12:00–21:30", "closed": "Closed Sun–Mon",
    "duration": "4:20", "art": "🥩", "bg": "radial-gradient(circle at center, #1E293B, #0F172A)",
    "mapX": 405, "mapY": 315, "categories": ["north", "fine", "dedicated"],
    "badges": [{"text": "✓ 100% GF Fine Dining", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Certified", "cls": "badge-certified"}, {"text": "✓ Yorkshire's Best GF", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "Leeds' 1st Dedicated GF Restaurant", "desc": "Coeliac family-owned destination delivering high-end culinary dining."}
    ],
    "menu": [
      {"section": "Mains", "items": [{"name": "Yorkshire Beef Fillet", "desc": "Dauphinoise potatoes, carrot purée, red wine jus", "price": "£29.50"}, {"name": "Slow-Braised Pork Belly", "desc": "Crispy crackling, celeriac mash, apple compote", "price": "£22.00"}]}
    ]
  },
  {
    "id": 31, "name": "Wildcraft Bakery", "type": "Artisan Bakery & Café", "city": "Leeds", "region": "north",
    "address": "Unit 5, Penneys Walk, Meanwood, Leeds, LS6 2HG", "shortLoc": "Meanwood, Leeds", "distance": "Leeds North",
    "phone": "0113 274 7799", "web": "wildcraftbakery.com", "hours": "Wed–Sat 09:30–16:00", "closed": "Closed Sun–Tue",
    "duration": "3:00", "art": "🍞", "bg": "radial-gradient(circle at center, #9A3412, #431407)",
    "mapX": 403, "mapY": 310, "categories": ["north", "cafe", "dedicated"],
    "badges": [{"text": "✓ Award-Winning GF Bakery", "cls": "badge-verified-green"}, {"text": "✓ 100% Dedicated Building", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Nationally Acclaimed Breads", "desc": "Winner of multiple British Baker awards for gluten-free loaves and brioche."}
    ],
    "menu": [
      {"section": "Fresh Loaves & Sweet", "items": [{"name": "Wild Artisan Sourdough", "desc": "Deep crust, naturally fermented GF loaf", "price": "£5.20"}, {"name": "Filled Brioche Doughnuts", "desc": "Custard or raspberry jam filling", "price": "£3.80"}]}
    ]
  },
  {
    "id": 32, "name": "Casa Leeds", "type": "Colombian & Latin Kitchen", "city": "Leeds", "region": "north",
    "address": "6 Grand Arcade, Leeds, LS1 6PG", "shortLoc": "Grand Arcade, Leeds", "distance": "Leeds Central",
    "phone": "0113 244 5599", "web": "casaleeds.co.uk", "hours": "Tue–Sun 12:00–22:00", "closed": "Closed Mondays",
    "duration": "3:15", "art": "🫔", "bg": "radial-gradient(circle at center, #DC2626, #7F1D1D)",
    "mapX": 407, "mapY": 316, "categories": ["north", "asian", "dedicated"],
    "badges": [{"text": "✓ 100% Gluten-Free Food", "cls": "badge-verified-green"}, {"text": "✓ Tapas & Empanadas", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "100% Corn-Based Kitchen", "desc": "Traditional Colombian recipes prepared without wheat."}
    ],
    "menu": [
      {"section": "Tapas", "items": [{"name": "Crispy Beef Empanadas (3)", "desc": "Yellow corn pastry, spicy aji dip", "price": "£8.50"}, {"name": "Slow-Cooked Pork Arepa", "desc": "Stuffed corn bread, avocado, melted cheese", "price": "£9.80"}]}
    ]
  },
  {
    "id": 33, "name": "Pig & Potato", "type": "Hearty Comfort Food", "city": "York", "region": "north",
    "address": "Shambles Market, York, YO1 7LA", "shortLoc": "The Shambles, York", "distance": "York Central",
    "phone": "01904 622 300", "web": "pigandpotatoyork.co.uk", "hours": "Tue–Sun 10:00–17:00", "closed": "Closed Mondays",
    "duration": "2:50", "art": "🥔", "bg": "radial-gradient(circle at center, #CA8A04, #713F12)",
    "mapX": 425, "mapY": 305, "categories": ["north", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% Dedicated Kitchen", "cls": "badge-verified-green"}, {"text": "✓ Local Yorkshire Produce", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Approved", "cls": "badge-certified"}],
    "protocols": [
      {"title": "York's Dedicated Coeliac Spot", "desc": "Fish pies, sausages, and mash made in 100% safe environment."}
    ],
    "menu": [
      {"section": "Plates", "items": [{"name": "Yorkshire Sausage & Mash", "desc": "GF pork sausages, buttery mash, onion gravy", "price": "£12.50"}, {"name": "Smoked Haddock Fish Pie", "desc": "Creamy leek sauce, cheddar potato mash lid", "price": "£13.50"}]}
    ]
  },
  {
    "id": 34, "name": "The Nakery", "type": "Raw Bakery & Dessert Bar", "city": "Liverpool", "region": "north",
    "address": "44 Berry St, Liverpool, L1 4JQ", "shortLoc": "Berry St, Liverpool", "distance": "Liverpool Central",
    "phone": "0151 709 5555", "web": "thenakery.co.uk", "hours": "Wed–Sun 11:00–18:00", "closed": "Closed Mon–Tue",
    "duration": "2:15", "art": "🧁", "bg": "radial-gradient(circle at center, #EC4899, #831843)",
    "mapX": 350, "mapY": 342, "categories": ["north", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF & Plant Based", "cls": "badge-verified-green"}, {"text": "✓ No Refined Sugars", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Friendly", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Nutrient Dense Sweets", "desc": "Handcrafted treats prepared in a strictly wheat-free facility."}
    ],
    "menu": [
      {"section": "Desserts", "items": [{"name": "Peanut Butter Fudge Slice", "desc": "Raw cacao base, creamy peanut butter core", "price": "£4.50"}, {"name": "Raspberry White Choc Cake", "desc": "Almond flour sponge, cashew cream", "price": "£4.80"}]}
    ]
  },
  {
    "id": 35, "name": "Sweet Mandarin", "type": "Cantonese Certified Dining", "city": "Manchester", "region": "north",
    "address": "19 Copperas St, Northern Quarter, Manchester, M4 1HS", "shortLoc": "Northern Quarter, Manchester", "distance": "Manchester M4",
    "phone": "0161 832 8848", "web": "sweetmandarin.com", "hours": "Wed–Sun 17:00–22:30", "closed": "Closed Mon–Tue",
    "duration": "4:00", "art": "🥡", "bg": "radial-gradient(circle at center, #DC2626, #450A0A)",
    "mapX": 371, "mapY": 333, "categories": ["north", "asian", "dedicated"],
    "badges": [{"text": "✓ Coeliac UK Accredited", "cls": "badge-certified"}, {"text": "✓ Certified GF Soy Sauce", "cls": "badge-verified-green"}, {"text": "✓ Dedicated GF Woks", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "Dedicated Chinese Wok Station", "desc": "Twin chefs developed famous Coeliac UK certified sauces."}
    ],
    "menu": [
      {"section": "Chinese Classics", "items": [{"name": "Sweet & Sour Crispy Chicken", "desc": "Rice flour batter, tangy sauce, fried rice", "price": "£15.50"}, {"name": "GF Steamed Dim Sum Platter", "desc": "Har gau prawn dumplings, chicken rolls", "price": "£11.50"}]}
    ]
  },

  # ─── SOUTH & WEST ENGLAND (8 Venues) ───
  {
    "id": 36, "name": "Fisk & Frite", "type": "GF Seafood & Friterie", "city": "Bristol", "region": "south",
    "address": "St Werburghs, Bristol, BS2 9XG", "shortLoc": "St Werburghs, Bristol", "distance": "Bristol Central",
    "phone": "0117 955 8800", "web": "fiskandfrite.co.uk", "hours": "Thu–Sun 12:00–21:00", "closed": "Closed Mon–Wed",
    "duration": "3:00", "art": "🍟", "bg": "radial-gradient(circle at center, #0284C7, #075985)",
    "mapX": 375, "mapY": 490, "categories": ["south", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% GF & Nut Free", "cls": "badge-verified-green"}, {"text": "✓ Belgian Style Frites", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Dedicated Seafood Fryers", "desc": "Double cooked frites and local fish in strictly wheat-free oil."}
    ],
    "menu": [
      {"section": "Mains", "items": [{"name": "Crispy Haddock & Double Frites", "desc": "GF batter, homemade tartare, lemon", "price": "£15.00"}, {"name": "Cornish Moules Frites", "desc": "White wine garlic cream broth, fries", "price": "£16.50"}]}
    ]
  },
  {
    "id": 37, "name": "Dos Dedos", "type": "Mexican Taqueria & Mezcal Bar", "city": "Bath", "region": "south",
    "address": "Edgar Mews, Bath, BA1 2EF", "shortLoc": "Edgar Mews, Bath", "distance": "Bath Central",
    "phone": "01225 448 833", "web": "dosdedos.co.uk", "hours": "Tue–Sun 16:00–23:00", "closed": "Closed Mondays",
    "duration": "3:10", "art": "🌮", "bg": "radial-gradient(circle at center, #D97706, #78350F)",
    "mapX": 382, "mapY": 495, "categories": ["south", "asian", "dedicated"],
    "badges": [{"text": "✓ 100% Gluten-Free Menu", "cls": "badge-verified-green"}, {"text": "✓ Masa Corn Tacos", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "100% GF Mexican Bar", "desc": "Every single taco, chip, and salsa is guaranteed free from wheat."}
    ],
    "menu": [
      {"section": "Tacos (3)", "items": [{"name": "Pork Carnitas", "desc": "Chicharron, coriander, habanero salsa", "price": "£11.50"}, {"name": "Queso Fundido & Chips", "desc": "Baked cheese, chorizo, fresh corn chips", "price": "£9.00"}]}
    ]
  },
  {
    "id": 38, "name": "Nook", "type": "Aussie Brunch & Poke Bar", "city": "Bath", "region": "south",
    "address": "High St, Bath, BA1 5AQ", "shortLoc": "High St, Bath", "distance": "Bath Central",
    "phone": "01225 334 455", "web": "nookbath.co.uk", "hours": "Mon–Sun 08:30–16:00", "closed": "Open 7 Days",
    "duration": "2:30", "art": "🥗", "bg": "radial-gradient(circle at center, #059669, #064E3B)",
    "mapX": 384, "mapY": 497, "categories": ["south", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% Gluten-Free Café", "cls": "badge-verified-green"}, {"text": "✓ Hawaiian Poke Bowls", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Clean Eating Brunch", "desc": "Entire menu is 100% gluten-free and crafted from whole foods."}
    ],
    "menu": [
      {"section": "Bowls", "items": [{"name": "Ahi Tuna Poke Bowl", "desc": "Sashimi tuna, brown rice, edamame, GF ponzu", "price": "£13.50"}, {"name": "Zucchini Corn Fritters", "desc": "Poached egg, avocado salsa, bacon", "price": "£12.50"}]}
    ]
  },
  {
    "id": 39, "name": "Casa Azul", "type": "Authentic Mexican Kitchen", "city": "Brighton", "region": "south",
    "address": "Open Market, Marshalls Row, Brighton, BN1 4JU", "shortLoc": "The Open Market, Brighton", "distance": "Brighton Central",
    "phone": "01273 695 500", "web": "casaazulbrighton.co.uk", "hours": "Wed–Sun 11:30–17:00", "closed": "Closed Mon–Tue",
    "duration": "2:45", "art": "🌶️", "bg": "radial-gradient(circle at center, #E11D48, #881337)",
    "mapX": 465, "mapY": 542, "categories": ["south", "asian", "dedicated"],
    "badges": [{"text": "✓ 100% GF Mexican Food", "cls": "badge-verified-green"}, {"text": "✓ Homemade Masa Tortillas", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Open Market Safe Hub", "desc": "Strictly gluten-free kitchen in Brighton's vibrant open market."}
    ],
    "menu": [
      {"section": "Mexican Favourites", "items": [{"name": "Chicken Tinga Tacos (3)", "desc": "Chipotle shredded chicken, sour cream", "price": "£10.50"}, {"name": "Slow-Cooked Tamales", "desc": "Steamed masa leaf, salsa verde", "price": "£7.50"}]}
    ]
  },
  {
    "id": 40, "name": "Halisco", "type": "Contemporary Mexican Bistro", "city": "Brighton", "region": "south",
    "address": "64 Preston St, Brighton, BN1 2HE", "shortLoc": "Preston St, Brighton", "distance": "Brighton Seafront",
    "phone": "01273 326 655", "web": "halisco.co.uk", "hours": "Tue–Sun 12:00–22:00", "closed": "Closed Mondays",
    "duration": "3:20", "art": "🍹", "bg": "radial-gradient(circle at center, #7C3AED, #3B0764)",
    "mapX": 463, "mapY": 544, "categories": ["south", "fine", "dedicated"],
    "badges": [{"text": "✓ 100% Dedicated Menu", "cls": "badge-verified-green"}, {"text": "✓ Seafront Dining", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "100% Verified By Management", "desc": "Full menu certified coeliac-safe by executive chefs."}
    ],
    "menu": [
      {"section": "Plates", "items": [{"name": "Crispy Fish Tacos (3)", "desc": "Beer-battered cod (GF ale), lime crema", "price": "£12.00"}, {"name": "GF Cinnamon Sugar Churros", "desc": "Salted caramel dip", "price": "£6.50"}]}
    ]
  },
  {
    "id": 41, "name": "Nano Fish and Chips", "type": "Traditional Chip Shop", "city": "Brighton", "region": "south",
    "address": "15 St James's St, Kemptown, Brighton, BN2 1RF", "shortLoc": "Kemptown, Brighton", "distance": "Brighton East",
    "phone": "01273 681 122", "web": "nanofishandchips.co.uk", "hours": "Mon–Sun 12:00–21:30", "closed": "Open 7 Days",
    "duration": "2:30", "art": "🐟", "bg": "radial-gradient(circle at center, #0284C7, #0369A1)",
    "mapX": 467, "mapY": 545, "categories": ["south", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% GF Transitioned", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Society Backed", "cls": "badge-certified"}, {"text": "✓ Dedicated Fry Tanks", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "Fully Converted GF Chipper", "desc": "Transitioned to a strictly 100% gluten-free kitchen in full coeliac partnership."}
    ],
    "menu": [
      {"section": "Fish & Chips", "items": [{"name": "Large Cod & Chips", "desc": "Crispy golden GF batter, chunky chips", "price": "£14.50"}, {"name": "Curry Sauce & Mushy Peas", "desc": "Homemade 100% GF recipe", "price": "£2.50"}]}
    ]
  },
  {
    "id": 42, "name": "Wolfies of Hove", "type": "Seafood & Fish Bar", "city": "Brighton & Hove", "region": "south",
    "address": "90 Goldstone Villas, Hove, BN3 3RU", "shortLoc": "Goldstone Villas, Hove", "distance": "Hove Station",
    "phone": "01273 911 119", "web": "wolfieshove.co.uk", "hours": "Tue–Sat 12:00–21:00", "closed": "Closed Sun–Mon",
    "duration": "3:00", "art": "🍟", "bg": "radial-gradient(circle at center, #1E40AF, #172554)",
    "mapX": 460, "mapY": 543, "categories": ["south", "takeaway", "dedicated"],
    "badges": [{"text": "✓ Dedicated GF Batter", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Accredited", "cls": "badge-certified"}, {"text": "✓ Sustainable Catch", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "Coeliac Society Favorite", "desc": "Dedicated fryers used solely for coeliac-safe orders."}
    ],
    "menu": [
      {"section": "Seafood", "items": [{"name": "Haddock in Light GF Batter", "desc": "Skinless haddock, twice cooked chips", "price": "£15.00"}]}
    ]
  },
  {
    "id": 43, "name": "The Catch Fish & Chip Bar", "type": "Coastal Fish & Chips", "city": "Cornwall", "region": "south",
    "address": "Harbour Way, Padstow, Cornwall, PL28 8BL", "shortLoc": "Padstow, Cornwall", "distance": "Cornwall Coast",
    "phone": "01841 532 200", "web": "thecatchcornwall.co.uk", "hours": "Wed–Sun 12:00–20:30", "closed": "Closed Mon–Tue",
    "duration": "2:40", "art": "⛵", "bg": "radial-gradient(circle at center, #0D9488, #115E59)",
    "mapX": 250, "mapY": 570, "categories": ["south", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% Dedicated Oil Tanks", "cls": "badge-verified-green"}, {"text": "✓ Cornish Day-Boat Fish", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Coastal Coeliac Safe", "desc": "100% separate filtration and fryer bank for gluten-free fish."}
    ],
    "menu": [
      {"section": "Cornish Catch", "items": [{"name": "Cornish Plaice & Chips", "desc": "Local caught plaice, GF batter, lemon", "price": "£16.00"}]}
    ]
  },

  # ─── SCOTLAND & NORTHERN (8 Venues) ───
  {
    "id": 44, "name": "Sugar Daddy’s Bakery", "type": "All-American Bakery", "city": "Edinburgh", "region": "scotland",
    "address": "8 Roseneath St, Marchmont, Edinburgh, EH9 1JH", "shortLoc": "Marchmont, Edinburgh", "distance": "Edinburgh South",
    "phone": "0131 229 9988", "web": "sugardaddysedinburgh.com", "hours": "Wed–Sun 10:00–17:00", "closed": "Closed Mon–Tue",
    "duration": "2:30", "art": "🧁", "bg": "radial-gradient(circle at center, #D946EF, #701A75)",
    "mapX": 350, "mapY": 185, "categories": ["scotland", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF Bakery", "cls": "badge-verified-green"}, {"text": "✓ Scotland's Most Famous GF", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "100% Gluten-Free Building", "desc": "Iconic Edinburgh bakery where no wheat ever enters."}
    ],
    "menu": [
      {"section": "Cakes & Bakes", "items": [{"name": "Giant NYC Cookie", "desc": "Chocolate chip & walnut molten centre", "price": "£4.20"}, {"name": "Red Velvet Cupcake", "desc": "Cream cheese frosting, velvet sponge", "price": "£3.80"}]}
    ]
  },
  {
    "id": 45, "name": "Tupiniquim", "type": "Brazilian Street Crêperie", "city": "Edinburgh", "region": "scotland",
    "address": "Green Police Box, Lauriston Pl, Edinburgh, EH3 9AU", "shortLoc": "The Meadows, Edinburgh", "distance": "Edinburgh Central",
    "phone": "0131 229 9900", "web": "tupiniquim.co.uk", "hours": "Mon–Sat 10:30–18:00", "closed": "Closed Sundays",
    "duration": "2:20", "art": "🥞", "bg": "radial-gradient(circle at center, #16A34A, #14532D)",
    "mapX": 352, "mapY": 188, "categories": ["scotland", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% GF Crêpes & Galettes", "cls": "badge-verified-green"}, {"text": "✓ Tapioca & Buckwheat", "cls": "badge-verified-green"}, {"text": "✓ Famous Green Box", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Naturally Wheat Free", "desc": "Manioc starch and buckwheat galettes made to order."}
    ],
    "menu": [
      {"section": "Crêpes", "items": [{"name": "Picanha Beef Galette", "desc": "Brazilian pulled beef, cheese, chimichurri", "price": "£8.50"}, {"name": "Nutella & Banana Crêpe", "desc": "Flambéed banana, toasted almonds", "price": "£7.00"}]}
    ]
  },
  {
    "id": 46, "name": "Confelicity", "type": "Café & Fresh Breads", "city": "Edinburgh", "region": "scotland",
    "address": "28 Bruntsfield Pl, Edinburgh, EH10 4HN", "shortLoc": "Bruntsfield, Edinburgh", "distance": "Edinburgh West",
    "phone": "0131 447 7788", "web": "confelicityedinburgh.com", "hours": "Wed–Sun 09:00–16:00", "closed": "Closed Mon–Tue",
    "duration": "2:40", "art": "🍞", "bg": "radial-gradient(circle at center, #F59E0B, #78350F)",
    "mapX": 348, "mapY": 189, "categories": ["scotland", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF Bakery Kitchen", "cls": "badge-verified-green"}, {"text": "✓ Swedish Cinnamon Buns", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Warm Artisan Bakes", "desc": "Dedicated bakery producing baguettes and cinnamon rolls daily."}
    ],
    "menu": [
      {"section": "Bakes", "items": [{"name": "Swedish Kanelbulle", "desc": "Spiced cinnamon & cardamom bun", "price": "£3.80"}, {"name": "Ham & Emmental Baguette", "desc": "Warm GF baguette, Dijon mustard", "price": "£7.50"}]}
    ]
  },
  {
    "id": 47, "name": "Ciccetta’s", "type": "Gelato & Belgian Waffles", "city": "Edinburgh", "region": "scotland",
    "address": "Commercial St, Leith, Edinburgh, EH6 6LX", "shortLoc": "Leith, Edinburgh", "distance": "Edinburgh Port",
    "phone": "0131 554 4400", "web": "ciccettas.co.uk", "hours": "Mon–Sun 12:00–20:00", "closed": "Open 7 Days",
    "duration": "2:10", "art": "🍨", "bg": "radial-gradient(circle at center, #06B6D4, #164E63)",
    "mapX": 355, "mapY": 180, "categories": ["scotland", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF Gelateria", "cls": "badge-verified-green"}, {"text": "✓ GF Waffle Cones", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Dedicated Waffle Cones", "desc": "No cross-contact from wheat cones or baked goods."}
    ],
    "menu": [
      {"section": "Waffles & Gelato", "items": [{"name": "Belgian Sugar Waffle", "desc": "Warm GF waffle, Fior di latte gelato", "price": "£7.50"}]}
    ]
  },
  {
    "id": 48, "name": "Dyno Dough", "type": "Stone-Baked GF Pizza", "city": "Edinburgh", "region": "scotland",
    "address": "Cowgate, Old Town, Edinburgh, EH1 1JR", "shortLoc": "Old Town, Edinburgh", "distance": "Edinburgh Central",
    "phone": "0131 220 5500", "web": "dynodough.co.uk", "hours": "Tue–Sun 16:00–23:00", "closed": "Closed Mondays",
    "duration": "3:10", "art": "🍕", "bg": "radial-gradient(circle at center, #B91C1C, #450A0A)",
    "mapX": 353, "mapY": 186, "categories": ["scotland", "takeaway", "dedicated"],
    "badges": [{"text": "✓ 100% GF Pizzeria", "cls": "badge-verified-green"}, {"text": "✓ Neapolitan Crust", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Safe", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Stone Oven Coeliac Haven", "desc": "Pizza dough formulated without gluten or deglutinated wheat starch."}
    ],
    "menu": [
      {"section": "Pizza", "items": [{"name": "Spicy Pepperoni & Hot Honey", "desc": "Tomato, mozzarella, artisan pepperoni, honey", "price": "£14.50"}]}
    ]
  },
  {
    "id": 49, "name": "Bodega Taqueria", "type": "Mexican Canteen", "city": "Edinburgh", "region": "scotland",
    "address": "Leith Walk, Edinburgh, EH6 5HB", "shortLoc": "Leith Walk, Edinburgh", "distance": "Edinburgh Leith",
    "phone": "0131 555 3300", "web": "ilovebodega.com", "hours": "Tue–Sun 17:00–22:00", "closed": "Closed Mondays",
    "duration": "3:00", "art": "🌮", "bg": "radial-gradient(circle at center, #E11D48, #4C0519)",
    "mapX": 354, "mapY": 183, "categories": ["scotland", "asian", "dedicated"],
    "badges": [{"text": "✓ 100% GF Taqueria", "cls": "badge-verified-green"}, {"text": "✓ Nixtamal Corn", "cls": "badge-verified-green"}, {"text": "✓ Coeliac Approved", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Masa Corn Tortillas Only", "desc": "Zero flour tortillas in inventory."}
    ],
    "menu": [
      {"section": "Tacos (2)", "items": [{"name": "Slow-Braised Pork Carnitas", "desc": "Salsa de arbol, coriander, white onion", "price": "£9.50"}]}
    ]
  },
  {
    "id": 50, "name": "Dakhin", "type": "South Indian Cuisine", "city": "Glasgow", "region": "scotland",
    "address": "89 Candleriggs, Merchant City, Glasgow, G1 1NP", "shortLoc": "Merchant City, Glasgow", "distance": "Glasgow Central",
    "phone": "0141 553 2585", "web": "dakhin.com", "hours": "Tue–Sun 12:00–22:30", "closed": "Closed Mondays",
    "duration": "3:45", "art": "🍛", "bg": "radial-gradient(circle at center, #9A3412, #431407)",
    "mapX": 315, "mapY": 188, "categories": ["scotland", "asian", "dedicated"],
    "badges": [{"text": "✓ 100% Gluten-Free Menu", "cls": "badge-verified-green"}, {"text": "✓ Scotland's 1st 100% GF Indian", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Certified", "cls": "badge-certified"}],
    "protocols": [
      {"title": "Naturally Wheat Free Cuisine", "desc": "South Indian dosas and curries made with rice and lentil doughs."}
    ],
    "menu": [
      {"section": "Dosas & Curries", "items": [{"name": "Masala Dosa", "desc": "Crispy rice & lentil crêpe, spiced potato, sambar", "price": "£12.50"}, {"name": "Meen Kulambu", "desc": "Monkfish curry, tamarind, coconut, curry leaves", "price": "£17.50"}]}
    ]
  },
  {
    "id": 51, "name": "Wild Flours Bakery", "type": "Traditional Scottish Bakery", "city": "Glasgow", "region": "scotland",
    "address": "Giffnock, Glasgow, G46 6QL", "shortLoc": "South Glasgow", "distance": "Glasgow South",
    "phone": "0141 638 8800", "web": "wildfloursbakery.co.uk", "hours": "Wed–Sat 09:30–16:30", "closed": "Closed Sun–Tue",
    "duration": "2:40", "art": "🥧", "bg": "radial-gradient(circle at center, #1E3A8A, #0F172A)",
    "mapX": 314, "mapY": 194, "categories": ["scotland", "cafe", "dedicated"],
    "badges": [{"text": "✓ 100% GF Scottish Bakes", "cls": "badge-verified-green"}, {"text": "✓ Coeliac UK Accredited", "cls": "badge-certified"}, {"text": "✓ Morning Rolls & Scones", "cls": "badge-verified-green"}],
    "protocols": [
      {"title": "Scotland's Dedicated Morning Rolls", "desc": "Fresh soft Scottish rolls without any gluten cross-contamination."}
    ],
    "menu": [
      {"section": "Scottish Bakes", "items": [{"name": "Traditional Scottish Morning Rolls (2)", "desc": "Soft, floury, coeliac-safe rolls", "price": "£3.00"}, {"name": "Empire Biscuit", "desc": "Shortbread biscuits, jam, glacé cherry", "price": "£3.20"}]}
    ]
  }
]

print(f"Generated {len(restaurants)} restaurants successfully!")
with open("c:/Users/kovia/Desktop/VerifiedGF-App/restaurants_data.json", "w", encoding="utf-8") as f:
    json.dump(restaurants, f, indent=2)
