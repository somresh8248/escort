import os
import re
from scratch_universal import apply_universal_updates, read_file, write_file

def update_about():
    html = read_file('about.html')
    html = apply_universal_updates(html)
    
    # Team section in about.html: Change Dentist to Ayurvedic specialists
    html = html.replace('<h5>Our Doctor</h5>', '<h5>Our Specialists</h5>')
    html = html.replace('<h2>Best Expert Dentist</h2>', '<h2>Expert Ayurvedic Vaidyas & Therapists</h2>')
    
    html = re.sub(
        r'<h4><a href="team-single\.html">Howard Holmes</a></h4>\s*<p>Dentist</p>',
        '<h4><a href="team-single.html">Dr. Rajesh Sharma</a></h4>\n                                    <p>Chief Ayurvedic Physician</p>',
        html
    )
    html = re.sub(
        r'<h4><a href="team-single\.html">Ella Thompson</a></h4>\s*<p>Dentist</p>',
        '<h4><a href="team-single.html">Priya Nair</a></h4>\n                                    <p>Senior Skin & Facial Esthetician</p>',
        html
    )
    html = re.sub(
        r'<h4><a href="team-single\.html">Vincent Cooper</a></h4>\s*<p>Dentist</p>',
        '<h4><a href="team-single.html">Dr. Ananya Iyer</a></h4>\n                                    <p>Panchakarma & Wellness Specialist</p>',
        html
    )
    html = re.sub(
        r'<h4><a href="team-single\.html">Danielle Bryant</a></h4>\s*<p>Dentist</p>',
        '<h4><a href="team-single.html">Arjun Verma</a></h4>\n                                    <p>Master Abhyanga & Body Therapist</p>',
        html
    )
    
    # FAQ accordion in about.html
    faq_replacements = [
        ("Vivamus rhoncus ante a ipsum imperdiet ?", 
         "What should I expect during an Ayurvedic Dosha consultation?",
         "Every session begins with a personalized consultation where our certified Ayurvedic vaidyas assess your unique Prakriti (body constitution) and current imbalances (Vata, Pitta, and Kapha) to tailor treatments and herbal oils specifically for you."),
        ("Integer id dolor at nisi laoreet iaculis vitae ?",
         "What makes authentic Kerala Abhyanga massage unique?",
         "Unlike conventional massage, traditional Abhyanga uses warm, medicated botanical oils massaged in synchronous rhythmic strokes to penetrate deep tissues, stimulate lymphatic drainage, detoxify organs, and calm the nervous system."),
        ("Donec venenatis elit dignissim, posuere ?",
         "Are all your skincare products and oils 100% natural?",
         "Yes, all our therapeutic oils, Ubtans, and facial elixirs are cold-pressed, 100% organic, and free from synthetic fragrances, mineral oils, and parabens, handcrafted in accordance with classical Ayurvedic pharmacopoeia."),
        ("Curabitur varius, massa sit amet egestas ?",
         "How should I prepare for my spa session?",
         "We recommend arriving 15 minutes before your scheduled appointment, staying hydrated, avoiding heavy meals 2 hours prior, and allowing the therapeutic herbal oils to absorb into your skin for at least 2 hours post-treatment.")
    ]
    
    for old_q, new_q, new_a in faq_replacements:
        html = html.replace(old_q, new_q)
    
    # Replace the generic lorem ipsum answers in accordionExample in about.html
    lorem_ans = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
                                                aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip"""
    for _, _, new_a in faq_replacements:
        if lorem_ans in html:
            html = html.replace(lorem_ans, new_a, 1)

    write_file('about.html', html)

def update_faq():
    html = read_file('faq.html')
    html = apply_universal_updates(html)
    
    # Left accordion 4 items
    left_faqs = [
        ("What should I expect during an Ayurvedic Dosha consultation?",
         "Our certified Ayurvedic Vaidya conducts a comprehensive Nadi Pariksha (pulse diagnosis) along with an evaluation of your sleep, digestion, and stress levels to determine your dominant Dosha (Vata, Pitta, or Kapha) and recommend tailored spa therapies."),
        ("How does Kerala Abhyanga massage differ from conventional massage?",
         "Authentic Abhyanga uses warm, herb-infused cold-pressed oils chosen for your body constitution. The rhythmic, continuous strokes activate vital Marma energy points, flush out metabolic toxins (Ama), and deeply calm the central nervous system."),
        ("What ingredients are used in your signature Kumkumadi & Chandan facials?",
         "Our radiance facials feature pure Kashmiri saffron (Kesar), Mysore red sandalwood (Rakta Chandan), Indian lotus extracts, and 26 therapeutic Himalayan botanicals that brighten dull skin, fade hyperpigmentation, and impart a luminous golden glow."),
        ("Can pregnant women or individuals with health conditions receive spa therapies?",
         "Yes, we offer specialized Garbhini prenatal care and gentle therapeutic treatments. Please notify our wellness concierge upon booking so our doctors can adapt the oils, posture, and pressure to ensure complete safety and comfort.")
    ]
    
    # Right accordion 4 items
    right_faqs = [
        ("What are the therapeutic benefits of pink Himalayan mineral hydrotherapy?",
         "Our mineral baths are enriched with 84 essential trace minerals that draw out impurities, soothe tense muscles, relieve joint stiffness, and enhance skin hydration while promoting restorative deep sleep."),
        ("How do I prepare for a Shirodhara or Panchakarma session?",
         "Wear comfortable, loose clothing and avoid heavy meals or caffeine 2 hours prior to your session. Following Shirodhara, we advise keeping your head protected from direct cold air to allow the medicated herbal oils to deeply nourish the mind."),
        ("Are your spa products and massage oils organic and cruelty-free?",
         "Every formulation used at Fallspa is 100% vegetarian, ethically wildcrafted from organic farms across Kerala and the Himalayas, completely cruelty-free, and devoid of artificial preservatives or chemicals."),
        ("How far in advance should I book bridal spa and group retreats?",
         "For signature bridal beauty rituals and couple or group wellness retreats, we recommend booking at least 2 to 3 weeks in advance so our practitioners can curate a personalized pre-wedding detoxification and glow calendar.")
    ]
    
    # Replace old questions
    old_q_left = [
        "Breaking The Rules Using SQLite To Demo Web?",
        "Monthly Web Development Update Pragmatic Releasing?",
        "How To Use Underlined Text To Improve User Experience",
        "Understanding CSS Layout And The Block Formatting"
    ]
    
    # Replace in left accordion
    for i in range(4):
        html = html.replace(old_q_left[i], left_faqs[i][0], 1)
        
    # Replace in right accordion (same old question strings were duplicated in template)
    for i in range(4):
        html = html.replace(old_q_left[i], right_faqs[i][0], 1)
        
    # Replace lorem answers
    lorem_ans = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
                                                aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip"""
    all_ans = [f[1] for f in left_faqs] + [f[1] for f in right_faqs]
    for ans in all_ans:
        if lorem_ans in html:
            html = html.replace(lorem_ans, ans, 1)
            
    write_file('faq.html', html)

def update_services():
    html = read_file('services.html')
    html = apply_universal_updates(html)
    write_file('services.html', html)

def update_single_service():
    html = read_file('single-service.html')
    html = apply_universal_updates(html)
    
    # Title & main paragraph
    html = html.replace('<h2> We give the best Services </h2>', '<h2> Authentic Ayurvedic Body Treatments & Rituals </h2>')
    
    old_p1 = 'Pleasure and praising pain was born and I will give you a complete account of the systems, and expound the actually teachings of the great explorer of the truth, the master-builder of human uts happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally Nor who loves or pursues or desires to obtain pain of itself.'
    new_p1 = 'Surrender your senses to our time-honored Ayurvedic body rituals, designed to cleanse, restore, and replenish your vitality from within. Using sacred Indian botanicals, cold-pressed therapeutic oils, and ancient exfoliation techniques, our treatments detoxify sluggish tissues, improve lymphatic drainage, and awaken your skin\'s natural, healthy radiance.'
    html = html.replace(old_p1, new_p1)
    
    old_why1 = 'Complete account of the systems and expound the actually teachings of the great explorer of the truth, the master-builder of human uts happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely.'
    new_why1 = 'Our signature body therapies unite classical Vedic wisdom with the pinnacle of modern spa luxury. Every session is customized to balance your individual Doshas (Vata, Pitta, Kapha), effectively releasing stored emotional tension, reducing chronic inflammation, and softening dehydrated skin.'
    html = html.replace(old_why1, new_why1)
    
    old_why2 = 'Complete account of the systems and expound the actually teachings of the great explorer of the truth, the master-builder of human uts happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally.'
    new_why2 = 'We exclusively utilize hand-pounded herbal Ubtans, wild turmeric (Kasturi Manjal), pure Kashmiri saffron, and warm medicated oils sourced directly from Kerala\'s pristine organic plantations.'
    html = html.replace(old_why2, new_why2)
    
    old_proc1 = re.search(r'<h3> Working Process</h3>\s*<p>(.*?)</p>', html, re.DOTALL)
    if old_proc1:
        new_proc1 = 'Our sacred four-step body revitalization ritual begins with an in-depth Prakriti assessment, followed by a warm Abhyanga herbal massage to stimulate vital Marma points. Next, an exfoliating Ubtan body scrub gently sloughs off dead cells, concluding with an aromatic herbal steam (Swedana) and rose-petal hydrotherapy soak to seal in deep moisture and peace.'
        html = html.replace(old_proc1.group(1), new_proc1)
        
    old_proc2 = re.search(r'</div>\s*<p>(Phasellus hac phasellus.*?)</p>', html, re.DOTALL)
    if old_proc2:
        new_proc2 = 'Post-treatment, our vaidyas offer a restorative warm Kashmiri saffron and cardamom tea while reviewing personalized homecare recommendations, balancing diet tips, and natural lifestyle practices to maintain your revitalized glow.'
        html = html.replace(old_proc2.group(1), new_proc2)

    html = html.replace('+91 705 2101 786', '+91 7052 101 786')
    write_file('single-service.html', html)

def update_pricing():
    html = read_file('pricing.html')
    html = apply_universal_updates(html)
    
    # Replace prices
    html = html.replace('<h2>$29.99 <span>/ Monthly</span></h2>', '<h2>₹2,499 <span>/ Session</span></h2>')
    html = html.replace('<h2>$39.99 <span>/ Monthly</span></h2>', '<h2>₹4,999 <span>/ Session</span></h2>')
    html = html.replace('<h2>$49.99 <span>/ Monthly</span></h2>', '<h2>₹7,999 <span>/ Session</span></h2>')
    
    # Replace package descriptions
    old_desc = '<p>Proin vehicula elit a dui rutrum, ac posuere magna auctor.</p>'
    pkg_descs = [
        '<p>Gentle Ayurvedic rejuvenation with traditional herbal oils for complete daily stress relief.</p>',
        '<p>Comprehensive mind-body revitalization with sacred Vedic therapies and golden glow facials.</p>',
        '<p>The ultimate royal Indian indulgence uniting ancient Rasayana therapies with bespoke luxury.</p>'
    ]
    for d in pkg_descs:
        if old_desc in html:
            html = html.replace(old_desc, d, 1)
            
    # Replace pricing bullet points
    old_ul = """<ul>
                                            <li>Aliquam quis justo at lorem</li>
                                            <li>Fusce sodales, urna et tempus</li>
                                            <li>Vestibulum blandit lorem quis</li>
                                            <li>Orci varius natoque penatibus</li>
                                            <li>Aliquam a nisl congue, auctor</li>
                                        </ul>"""
    ul1 = """<ul>
                                            <li>60-Min Abhyanga Herbal Massage</li>
                                            <li>Kashmiri Saffron Welcome Drink</li>
                                            <li>Warm Medicated Herbal Steam Bath</li>
                                            <li>Personalized Dosha Consultation</li>
                                            <li>Ayurvedic Herbal Green Tea Infusion</li>
                                        </ul>"""
    ul2 = """<ul>
                                            <li>75-Min Marma Deep Tissue Therapy</li>
                                            <li>Pure Kumkumadi Golden Glow Facial</li>
                                            <li>30-Min Calming Shirodhara Oil Flow</li>
                                            <li>Himalayan Mineral Bath & Jacuzzi</li>
                                            <li>Customized Diet & Lifestyle Chart</li>
                                        </ul>"""
    ul3 = """<ul>
                                           <li>120-Min Royal Kerala Panchakarma Ritual</li>
                                            <li>24K Swarna & Chandan Body Polishing</li>
                                            <li>Geothermal Volcanic Stone Therapy</li>
                                            <li>Private Rose Petal Hydrotherapy Bath</li>
                                            <li>Complimentary Luxury Ayurvedic Gift Hamper</li>
                                        </ul>"""
    
    html = html.replace(old_ul, ul1, 1)
    html = html.replace(old_ul, ul2, 1)
    # in the third card, notice slightly different spaces in template
    html = re.sub(r'<ul>\s*<li>Aliquam quis justo at lorem</li>[\s\S]*?<li>Aliquam a nisl congue, auctor</li>\s*</ul>', ul3, html, count=1)
    
    write_file('pricing.html', html)

def update_team():
    html = read_file('team.html')
    html = apply_universal_updates(html)
    
    members = [
        ("Bableo Dablo", "Dr. Rajesh Sharma", "Chief Ayurvedic Doctor (BAMS, MD)"),
        ("Dawon Crisen", "Priya Nair", "Senior Facial & Skin Esthetician"),
        ("David Suarez", "Dr. Ananya Iyer", "Panchakarma & Wellness Specialist"),
        ("Gerard Peano", "Arjun Verma", "Master Abhyanga & Deep Tissue Therapist"),
        ("Ostin Green", "Meera Sen", "Herbal Botanicals & Ubtan Specialist"),
        ("Vincent Cooper", "Vikram Joshi", "Hydrotherapy & Geothermal Specialist"),
        ("Danielle Bryant", "Kavita Patel", "Yoga & Meditation Wellness Guide"),
        ("Howard Holmes", "Rohan Mehra", "Aromatherapist & Reflexologist")
    ]
    
    for old_name, new_name, new_role in members:
        pattern = rf'<h4><a href="team-single\.html">{re.escape(old_name)}</a></h4>\s*<p>Worker</p>'
        replacement = f'<h4><a href="team-single.html">{new_name}</a></h4>\n                                    <p>{new_role}</p>'
        html = re.sub(pattern, replacement, html)
        
    write_file('team.html', html)

def update_team_single():
    html = read_file('team-single.html')
    html = apply_universal_updates(html)
    
    # Bio
    old_bio = 'Pleasure and praising pain was born and I will give you a complete account of the systems, and expound the actually teachings of the great explorer of the truth, the master-builder of human uts happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally Nor who loves or pursues or desires to obtain pain of itself.'
    new_bio = 'Dr. Rajesh Sharma is a distinguished Ayurvedic Vaidya with over 15 years of clinical expertise in classical Vedic medicine, pulse diagnosis (Nadi Pariksha), and holistic skin rejuvenation. Having trained under traditional masters in Kerala, he curates personalized wellness protocols that harmonize mind, body, and spirit.'
    html = html.replace(old_bio, new_bio)
    
    # Skills
    html = html.replace('<div class="skill-name">Design</div>', '<div class="skill-name">Ayurvedic Pulse Diagnosis (Nadi Pariksha)</div>')
    html = html.replace('<div class="skill-name">Easy Manage</div>', '<div class="skill-name">Abhyanga & Marma Therapy</div>')
    html = html.replace('<div class="skill-name">Project Organize</div>', '<div class="skill-name">Herbal Formulations & Skin Healing</div>')
    
    # Personal Info
    html = html.replace('<div class="text">info@webexample.com</div>', '<div class="text">dr.sharma@fallspa.in</div>')
    html = html.replace('<div class="text">980-786-098-09</div>', '<div class="text">+91 7052 101 786</div>')
    html = html.replace('<div class="text">12/A, Miranda City Hall, NYC</div>', '<div class="text">Fallspa Sanctuary, Bandra West, Mumbai 400050</div>')
    html = html.replace('<div class="text">www.webexample.com</div>', '<div class="text">www.fallspa.in</div>')
    
    write_file('team-single.html', html)

def update_shop():
    html = read_file('shop.html')
    html = apply_universal_updates(html)
    
    products = [
        ("Chair", "Bakari Product", "Facial Elixirs", "Kumkumadi Miracle Face Oil (30ml)", "₹1,499", "₹1,999"),
        ("Cloths", "Romada Product", "Body Polishing", "Royal Sandalwood & Ubtan Body Scrub", "₹899", "₹1,199"),
        ("Light", "Sikkar Product", "Ayurvedic Creams", "Kesar & Haldi Day Radiance Cream", "₹999", "₹1,399"),
        ("Headphone", "Minners Product", "Bath Salts", "Pink Himalayan Mineral Bath Soak", "₹699", "₹999"),
        ("Chair", "Bakari Product", "Hair Care", "Bhringraj & Amla Hair Therapy Oil", "₹799", "₹1,099"),
        ("Cloths", "Romada Product", "Skin Care", "Neem & Tea Tree Balancing Gel", "₹599", "₹799"),
        ("Light", "Sikkar Product", "Massage Oils", "Dhanwantharam Warm Body Oil", "₹1,199", "₹1,599"),
        ("Headphone", "Minners Product", "Aroma Mists", "Pure Damask Rose & Mogra Mist", "₹649", "₹849"),
        ("Chair", "Bakari Product", "Spa Hampers", "Vedic Bridal Glow Luxury Hamper", "₹2,999", "₹3,999")
    ]
    
    # Replace prices $95.00 and $120.00
    for old_cat, old_name, new_cat, new_name, new_price, old_p in products:
        pattern = rf'<span class="pro-cat"><a href="#">{old_cat}</a></span>\s*<h4 class="pro-title"><a href="shop-details\.html">{old_name}</a></h4>\s*<div class="price">\s*<span>\$95\.00</span>\s*<span class="old-price">\$120\.00</span>\s*</div>'
        replacement = f'<span class="pro-cat"><a href="#">{new_cat}</a></span>\n                                                <h4 class="pro-title"><a href="shop-details.html">{new_name}</a></h4>\n                                                <div class="price">\n                                                    <span>{new_price}</span>\n                                                    <span class="old-price">{old_p}</span>\n                                                </div>'
        html = re.sub(pattern, replacement, html, count=1)
        
    write_file('shop.html', html)

def update_shop_details():
    html = read_file('shop-details.html')
    html = apply_universal_updates(html)
    
    html = html.replace('<p>Workstead</p>', '<p>Fallspa Botanicals</p>')
    html = html.replace('<h1>Helios Piranho Lamp</h1>', '<h1>Pure Kumkumadi Ayurvedic Miracle Glow Oil (30ml)</h1>')
    html = html.replace('<span>$700.00</span>', '<span>₹1,499.00</span>')
    html = html.replace('<span class="old-price">$820.00</span>', '<span class="old-price">₹1,999.00</span>')
    
    old_desc = """It is a long established fact that a reader will be distracted by the readable content of a page
                                when looking at its
                                layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of
                                letters, as opposed to
                                using 'Content here, content here', making it look like readable English."""
    new_desc = """Handcrafted using classical Ayurvedic formulations with pure Kashmiri saffron (Kesar), red sandalwood (Rakta Chandan), Indian lotus, and 26 therapeutic Himalayan herbs infused in cold-pressed virgin sesame oil. Clinically known to restore skin elasticity, fade hyperpigmentation, reduce fine lines, and impart a luminous, natural golden glow."""
    html = html.replace(old_desc, new_desc)
    
    html = html.replace('<a href="#">furniture,</a>\n                                <a href="#">decor</a>', '<a href="#">Ayurvedic Skincare,</a>\n                                <a href="#">Facial Elixirs</a>')
    html = html.replace('<a href="#">furniture,</a>\r\n                                <a href="#">decor</a>', '<a href="#">Ayurvedic Skincare,</a>\r\n                                <a href="#">Facial Elixirs</a>')
    
    # Description Tab
    old_tab_desc = re.search(r'<div class="tab-pane fade show active" id="id-desc"[^>]*>\s*<div class="event-text mb-40">([\s\S]*?)</div>\s*</div>', html)
    if old_tab_desc:
        new_tab_desc = """
                                    <p>Fallspa's Pure Kumkumadi Miracle Glow Oil is an authentic Ayurvedic formulation prescribed in classical texts for Mukha Kanti (facial radiance). Crafted with 100% natural, ethically sourced botanicals, each drop deeply penetrates skin layers to nourish and regenerate cellular health.</p>
                                    <p>Key Botanical Benefits:</p>
                                    <ul>
                                        <li><strong>Kashmiri Saffron (Kesar):</strong> Brightens dark spots and improves natural skin tone.</li>
                                        <li><strong>Mysore Red Sandalwood (Chandan):</strong> Calms inflammation, soothes blemishes, and tones skin.</li>
                                        <li><strong>Indian Lotus & Manjistha:</strong> Powerful antioxidants that refine texture and combat free-radical damage.</li>
                                        <li><strong>Cold-Pressed Sesame Oil:</strong> Rich in vitamins E & B complex to lock in deep hydration.</li>
                                    </ul>
                                    <p>How to Use: Gently massage 3 to 4 drops onto cleansed, damp face and neck in upward circular strokes every evening before bedtime for best results.</p>
"""
        html = html.replace(old_tab_desc.group(1), new_tab_desc)
        
    write_file('shop-details.html', html)

def update_blog():
    html = read_file('blog.html')
    html = apply_universal_updates(html)
    
    blog_items = [
        ("Lorem ipsum dolor sit amet, consectetur\n                                            cing elit, sed do eiusmod tempor.",
         "The Ancient Art of Abhyanga: Daily Self-Massage Rituals for Vitality & Dosha Balance",
         "By Dr. Rajesh Sharma",
         "Discover how traditional Indian daily warm oil massage pacifies Vata dosha, enhances lymphatic detoxification, and promotes restful restorative sleep."),
        ("There are many variations passages of like consectetur lorem ipsum available.",
         "Kumkumadi Tailam: Unlocking The Golden Ayurvedic Secret to Timeless Radiant Skin",
         "By Priya Nair",
         "Uncover the science behind saffron and sandalwood elixirs used for centuries in royal Indian beauty traditions to achieve a luminous golden glow."),
        ("I must explain to you how all this mistaken idea of denouncing pleasure.",
         "Himalayan Pink Salt Baths & Hydrotherapy: Rejuvenating Body and Soul Naturally",
         "By Dr. Ananya Iyer",
         "Explore how mineral-rich pink Himalayan rock salts and damask rose water draw out cellular tension and melt away physical stress."),
        ("There are many variations passages of like consectetur lorem ipsum available.",
         "The Magic of Shirodhara: Deep Stress Relief, Calming Vata, and Restorative Sleep",
         "By Arjun Verma",
         "Learn why the continuous flow of warm medicated herbal oil over the third-eye chakra remains Ayurveda's most revered stress-relief treatment.")
    ]
    
    # Replace in order
    for old_title, new_title, author, excerpt in blog_items:
        # replace title
        if old_title in html:
            html = html.replace(old_title, new_title, 1)
        elif old_title.replace('\n', '\r\n') in html:
            html = html.replace(old_title.replace('\n', '\r\n'), new_title, 1)
        # replace author
        html = html.replace('By Zcube', author, 1)
        # replace excerpt
        lorem_p = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse."
        lorem_p2 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        if lorem_p in html:
            html = html.replace(lorem_p, excerpt, 1)
        elif lorem_p2 in html:
            html = html.replace(lorem_p2, excerpt, 1)
            
    write_file('blog.html', html)

def update_blog_details():
    html = read_file('blog-details.html')
    html = apply_universal_updates(html)
    
    # Title
    html = re.sub(
        r'<h2>With our vastly improved notifications system, users\s*have more control\.</h2>',
        '<h2>The Ancient Art of Abhyanga: Daily Self-Massage Rituals for Vitality & Dosha Balance</h2>',
        html
    )
    
    # Quote
    html = html.replace('<footer>By Rosalina Pong</footer>', '<footer>By Dr. Rajesh Sharma, Chief Ayurvedic Physician</footer>')
    html = html.replace('Viral dreamcatcher keytar typewriter, aest hetic offal umami. Aesthetic polaroid pug pitchfork post-ironic.', 
                        'Self-massage with warm herbal oil is not a luxury, but a sacred daily act of self-love and preventive medicine taught by ancient Vedic masters.')
    
    # Article text
    article_text_1 = """In classical Ayurvedic medicine, Abhyanga (warm botanical oil massage) is regarded as one of the most powerful dinacharya (daily lifestyle) practices for sustaining longevity, preserving youthfulness, and shielding the physical body against environmental stressors. In the Charaka Samhita, it is written: 'The body of one who uses oil massage regularly does not become affected by accidents or strenuous work, and stays supple and strong.'"""
    
    article_text_2 = """Benefits of Daily Herbal Abhyanga:
1. Pacifies Vata Dosha: Modern fast-paced lifestyles aggravate the air and ether elements, causing anxiety, insomnia, dry skin, and fatigue. Warm oil grounds the nervous system and fosters deep emotional stability.
2. Lymphatic Drainage & Detoxification: Rhythmic strokes toward the heart stimulate lymph nodes, assisting in the elimination of metabolic waste (Ama).
3. Musculoskeletal Relief: Medicated sesame oils enriched with Ashwagandha and Bala deeply lubricate joints, soothe tight muscles, and ease physical fatigue.
4. Luminous Skin Tone: Botanical nutrients fortify the skin barrier, restore suppleness, and prevent premature aging."""

    article_text_3 = """How to Practice Abhyanga at Home:
Begin by gently warming 2 to 3 tablespoons of authentic Ayurvedic oil. Starting at your crown, massage your scalp in circular motions, moving to the ears and face. Work down through your arms and legs using long strokes on long bones and circular movements over joints. Allow the therapeutic herbs to penetrate for 15 to 20 minutes before stepping into a warm herbal bath or shower."""

    html = re.sub(r'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo amet set for your cool happiness for lyour loyal city\.</p>', f'<p>{article_text_1}</p>', html)
    html = re.sub(r'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat\. Duis aute irure dolor in reprehenderit[\s\S]*?Neque porro quisq\.</p>', f'<p>{article_text_2}</p>', html)
    html = re.sub(r'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat\.Duis aute irure dolor in reprehenderit[\s\S]*?Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusant\.</p>', f'<p>{article_text_3}</p>', html)
    
    # Tags
    html = html.replace('<li><a href="#">organic</a></li>\n                                                    <li><a href="#">Foods</a></li>\n                                                    <li><a href="#">tasty</a></li>',
                        '<li><a href="#">Ayurveda</a></li>\n                                                    <li><a href="#">Abhyanga</a></li>\n                                                    <li><a href="#">Skin Glow</a></li>')
    html = html.replace('<li><a href="#">organic</a></li>\r\n                                                    <li><a href="#">Foods</a></li>\r\n                                                    <li><a href="#">tasty</a></li>',
                        '<li><a href="#">Ayurveda</a></li>\r\n                                                    <li><a href="#">Abhyanga</a></li>\r\n                                                    <li><a href="#">Skin Glow</a></li>')
    
    # Related posts
    html = html.replace('Auis nostrud exercita ullamco laboris nisi ut', 'Kumkumadi Tailam: The Golden Ayurvedic Secret to Glowing Skin')
    html = html.replace('Excepteur sint occaecat cupida tat non proident', 'Himalayan Salt Baths & Hydrotherapy: Natural Body Detox')
    
    write_file('blog-details.html', html)

def update_contact():
    html = read_file('contact.html')
    html = apply_universal_updates(html)
    
    # Fix breadcrumb
    html = html.replace('<li class="breadcrumb-item active" aria-current="page">About Us</li>', '<li class="breadcrumb-item active" aria-current="page">Contact Us</li>')
    write_file('contact.html', html)

def update_thank_you():
    html = read_file('thank-you.html')
    html = apply_universal_updates(html)
    
    html = html.replace('<h2>Thank You</h2>', '<h2>Namaste! Thank You</h2>')
    write_file('thank-you.html', html)

def update_projects():
    html = read_file('projects.html')
    html = apply_universal_updates(html)
    write_file('projects.html', html)

def update_index():
    html = read_file('index.html')
    html = apply_universal_updates(html)
    
    # Hero slider
    html = html.replace('Donec vitae libero non enim placerat eleifend aliquam erat volutpat. Curabitur diam ex, dapibus purus sapien, cursus sed nisl tristique.',
                        'Experience the divine essence of authentic Ayurvedic therapies and luxury Indian botanicals. Enriched with pure Chandan, Kashmiri Kesar, and therapeutic herbal oils to restore your natural glow and timeless radiance.')
    
    # Product prices to INR
    html = html.replace('<span class="old-price">$20</span>\n                                    <span>$15</span>', '<span class="old-price">₹1,299</span>\n                                    <span>₹899</span>')
    html = html.replace('<span class="old-price">$20</span>\r\n                                    <span>$15</span>', '<span class="old-price">₹1,299</span>\r\n                                    <span>₹899</span>')
    html = html.replace('<span>$95.00</span>\n                                    <span class="old-price">$120.00</span>', '<span>₹1,299</span>\n                                    <span class="old-price">₹1,899</span>')
    html = html.replace('<span>$95.00</span>\r\n                                    <span class="old-price">$120.00</span>', '<span>₹1,299</span>\r\n                                    <span class="old-price">₹1,899</span>')
    
    # Pricing
    html = html.replace('<h2>$29.99 <span>/ Monthly</span></h2>', '<h2>₹2,499 <span>/ Session</span></h2>')
    html = html.replace('<h2>$39.99 <span>/ Monthly</span></h2>', '<h2>₹4,999 <span>/ Session</span></h2>')
    html = html.replace('<h2>$49.99 <span>/ Monthly</span></h2>', '<h2>₹7,999 <span>/ Session</span></h2>')
    
    write_file('index.html', html)

def update_index_2():
    html = read_file('index-2.html')
    html = apply_universal_updates(html)
    
    # Hero slider
    html = html.replace('Donec vitae libero non enim placerat eleifend aliquam erat volutpat. Curabitur diam ex, dapibus purus sapien, cursus sed nisl tristique.',
                        'Experience the divine essence of authentic Ayurvedic therapies and luxury Indian botanicals. Enriched with pure Chandan, Kashmiri Kesar, and therapeutic herbal oils to restore your natural glow and timeless radiance.')
    
    # Product prices to INR
    html = html.replace('<span class="old-price">$20</span>\n                                    <span>$15</span>', '<span class="old-price">₹1,299</span>\n                                    <span>₹899</span>')
    html = html.replace('<span class="old-price">$20</span>\r\n                                    <span>$15</span>', '<span class="old-price">₹1,299</span>\r\n                                    <span>₹899</span>')
    html = html.replace('<span>$95.00</span>\n                                    <span class="old-price">$120.00</span>', '<span>₹1,299</span>\n                                    <span class="old-price">₹1,899</span>')
    html = html.replace('<span>$95.00</span>\r\n                                    <span class="old-price">$120.00</span>', '<span>₹1,299</span>\r\n                                    <span class="old-price">₹1,899</span>')
    
    # Pricing
    html = html.replace('<h2>$29.99 <span>/ Monthly</span></h2>', '<h2>₹2,499 <span>/ Session</span></h2>')
    html = html.replace('<h2>$39.99 <span>/ Monthly</span></h2>', '<h2>₹4,999 <span>/ Session</span></h2>')
    html = html.replace('<h2>$49.99 <span>/ Monthly</span></h2>', '<h2>₹7,999 <span>/ Session</span></h2>')
    
    write_file('index-2.html', html)

if __name__ == '__main__':
    update_about()
    update_faq()
    update_services()
    update_single_service()
    update_pricing()
    update_team()
    update_team_single()
    update_shop()
    update_shop_details()
    update_blog()
    update_blog_details()
    update_contact()
    update_projects()
    update_thank_you()
    update_index()
    update_index_2()
    print("\nAll pages processed successfully!")
