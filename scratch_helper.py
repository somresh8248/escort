import os
import re

WORKSPACE = r'c:\Users\SOMRESH\Downloads\fallspa\fallspa'

def read_file(filename):
    path = os.path.join(WORKSPACE, filename)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def write_file(filename, content):
    path = os.path.join(WORKSPACE, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

def apply_common_cleanups(html):
    # Header email
    html = html.replace('<span>info@example.com</span>', '<span>info@fallspa.in</span>')
    html = html.replace('+91-7052-101-786', '+91 7052 101 786')
    html = html.replace('+91-598-9874-987', '+91 7052 101 786')
    html = html.replace('+91 598 9874 987', '+91 7052 101 786')
    
    # Footer about paragraph
    old_footer_p = 'Mauris non nisi semper, lacinia neque in, dapibus leo. Curabitur sagittis libero tincidunt tempor finibus. Mauris at dignissim ligula, nec tristique orci.Quisque vitae metus.'
    new_footer_p = "Fallspa is India's premier wellness sanctuary, uniting ancient Vedic wisdom, authentic Ayurvedic therapies, and luxury holistic care for complete rejuvenation of mind, body, and soul."
    html = html.replace(old_footer_p, new_footer_p)
    
    # Footer email
    html = html.replace('<span>info@wellspa.com</span>', '<span>info@fallspa.in</span>')
    
    # Footer hours duplicate
    # Replace second Monday - Saturday with Sunday
    old_hours = """<strong>Monday - Saturday:</strong>
                                                    <p>9:00am - 10:00pm</p>
                                                    <strong>Monday - Saturday:</strong>
                                                    <p>9:00am - 10:00pm</p>"""
    new_hours = """<strong>Monday - Saturday:</strong>
                                                    <p>9:00am - 10:00pm</p>
                                                    <strong>Sunday:</strong>
                                                    <p>9:00am - 06:00pm</p>"""
    html = html.replace(old_hours, new_hours)

    # Booking intro dummy text
    old_booking_p = 'Aenean ut enim vel lectus rutrum sodales. Aliquam consequat augue eget enim convallis, at maximus libero ullamcorper. Cras sit amet placerat nisi.'
    new_booking_p = 'Reserve your bespoke Ayurvedic retreat today. Connect with our certified vaidyas and wellness therapists across Mumbai, Delhi NCR, Bengaluru, and pan-India centers for a revitalizing journey.'
    html = html.replace(old_booking_p, new_booking_p)

    # Typo in email placeholder
    html = html.replace('placeholder="Eamil"', 'placeholder="Email Address"')

    # Dropdown dummy options
    old_select = """<select class="custom-select" id="inputGroupSelect04" aria-label="Example select with button addon">
                                            <option selected>Select Department...</option>
                                            <option value="1">One</option>
                                            <option value="2">Two</option>
                                            <option value="3">Three</option>
                                          </select>"""
    new_select = """<select class="custom-select" id="inputGroupSelect04" aria-label="Example select with button addon">
                                            <option selected>Select Service...</option>
                                            <option value="1">Ayurvedic Abhyanga & Massage</option>
                                            <option value="2">Kumkumadi & Herbal Facials</option>
                                            <option value="3">Himalayan Mineral Bath & Hydrotherapy</option>
                                            <option value="4">Bridal Ubtan & Body Polishing</option>
                                            <option value="5">Geothermal Hot Stone Therapy</option>
                                          </select>"""
    html = html.replace(old_select, new_select)

    # Discount text
    html = html.replace('Check out seasonal discounts for best offers.', 'Special festive Diwali & wedding season offers available on all wellness packages!')

    # Testimonials intro
    old_testi_intro = 'Nullam posuere eros ex, vitae consequat ipsum semper cursus. In ut commodo eros. Vestibulum sed elit id orci rhoncus. Duis quis nunc eu augue efficitur suscipit.'
    new_testi_intro = 'Discover genuine reviews from our cherished patrons across India who embraced peace, restored balance, and rediscovered their natural glow at Fallspa.'
    html = html.replace(old_testi_intro, new_testi_intro)

    # Testimonial reviews
    latin_review = "“Phasellus aliquam quis lorem amet dapibus feugiat vitae purus vitae efficitur. Vestibulum sed elit id orci rhoncus ultricies. Morbi vitae semper consequat ipsum semper quam”."
    # We will replace them sequentially if present
    reviews_indian = [
        "“The Shirodhara and herbal Abhyanga therapy at Fallspa was truly transformative. After exhausting work weeks in Mumbai, the tranquil ambiance and authentic Ayurvedic oils completely melted away my fatigue and insomnia.”",
        "“I booked their signature bridal Ubtan and Kumkumadi facial before my wedding celebrations. The natural glow on my skin was remarkable! The therapists are deeply knowledgeable in traditional Indian holistic care.”",
        "“The pink Himalayan mineral bath paired with Kerala herbal steam therapy relieved all my chronic back stiffness. It is by far the most peaceful, authentically rooted luxury wellness sanctuary in India.”",
        "“Exceptional hospitality and authentic Ayurvedic formulations. The therapists took time to understand my Dosha balance. From the warm Kesar welcome tea to the soothing foot reflexology, every detail was pure bliss.”"
    ]
    for r in reviews_indian:
        if latin_review in html:
            html = html.replace(latin_review, r, 1)

    # Locations for reviewers
    html = html.replace('<h6>Jina Nilson</h6>\n                                            <span>Client</span>', '<h6>Jina Nilson</h6>\n                                            <span>Verified Guest, Mumbai</span>')
    html = html.replace('<h6>Braitly Dcosta</h6>\n                                            <span>Client</span>', '<h6>Braitly Dcosta</h6>\n                                            <span>Verified Guest, Goa</span>')
    html = html.replace('<h6>Jina Nilson</h6>\n                                            <span>Client</span>', '<h6>Jina Nilson</h6>\n                                            <span>Verified Guest, Bengaluru</span>')
    html = html.replace('<h6>Braitly Dcosta</h6>\n                                            <span>Client</span>', '<h6>Braitly Dcosta</h6>\n                                            <span>Verified Guest, New Delhi</span>')

    # Also handle CRLF if present
    html = html.replace('<h6>Jina Nilson</h6>\r\n                                            <span>Client</span>', '<h6>Jina Nilson</h6>\r\n                                            <span>Verified Guest, Mumbai</span>')
    html = html.replace('<h6>Braitly Dcosta</h6>\r\n                                            <span>Client</span>', '<h6>Braitly Dcosta</h6>\r\n                                            <span>Verified Guest, Goa</span>')
    html = html.replace('<h6>Jina Nilson</h6>\r\n                                            <span>Client</span>', '<h6>Jina Nilson</h6>\r\n                                            <span>Verified Guest, Bengaluru</span>')
    html = html.replace('<h6>Braitly Dcosta</h6>\r\n                                            <span>Client</span>', '<h6>Braitly Dcosta</h6>\r\n                                            <span>Verified Guest, New Delhi</span>')

    # Standardize service items if present
    old_facials_p = 'Cras id aliquam leo. Vestibulum laoreet, mi sit amet tristique tincidunt nec laoreet.'
    new_facials_p = 'Traditional Kumkumadi, Chandan & Haldi radiance facials crafted to deeply detoxify, hydrate, and impart a golden Indian glow.'
    html = html.replace(old_facials_p, new_facials_p)

    old_srv_p = 'Aenean eleifend turpis tellus, nec laoreet metus elementum ac.'
    # The 5 services with this dummy paragraph
    new_srv_paragraphs = [
        'Soothing pink Himalayan rock salt and fragrant damask rose petal soak to relieve muscular fatigue and melt away stress.',
        'Authentic Kerala Abhyanga and Shirodhara head massage with warm medicated herbal oils to restore harmony and calm vital energies.',
        'Exfoliating bridal Ubtan, wild turmeric body polish, and healing neem wraps for silky smooth, toned, and nourished skin.',
        'Ultra-gentle Rica wax and organic Indian sugarcane waxing infused with soothing aloe vera and chamomile for sensitive skin.',
        'Rejuvenating volcanic basalt hot stone therapy infused with therapeutic Dhanwantharam oil to release deep muscular knots.'
    ]
    for sp in new_srv_paragraphs:
        if old_srv_p in html:
            html = html.replace(old_srv_p, sp, 1)

    # Standardize About Us 2 paragraphs
    old_about1 = 'Suspendisse et porttitor leo. Sed porttitor dui sit amet luctus bibendum. Sed pulvinar diam lacus, ut elementum nisl volutpat in. Nullam vitae nulla dolor. Pellentesque viverra arcu ut Curabitur tempor mauris ex, eget porta tellus posuere maximus.'
    new_about1 = "Rooted in India's sacred Vedic healing traditions, Fallspa brings you the ultimate holistic care through time-honored Ayurvedic wisdom and modern luxury wellness. We hand-blend natural therapies using cold-pressed virgin oils, pure Mysore sandalwood (Chandan), organic Kashmiri saffron (Kesar), and potent Himalayan botanicals to purify, hydrate, and restore your skin's natural balance."
    html = html.replace(old_about1, new_about1)

    old_about2 = 'Nulla nisl ligula, efficitur eget ipsum ac, luctus elementum risus. Phasellus venenatis turpis eget nulla porttitor varius. Ut ut lorem commodo, aliquet augue sit amet, luctus elit. Curabitur tempor mauris ex, eget porta metus imperdiet ac. Mauris aliquet ante sit amet rhoncus semper.'
    new_about2 = "From authentic bridal Ubtans and rejuvenating Kumkumadi facials to deeply calming Kerala Abhyanga therapies, each ritual is mindfully personalized to your unique Dosha constitution. Surrender to peaceful tranquility as our certified Ayurvedic practitioners rejuvenate your mind, body, and spirit with India's purest holistic wellness rituals."
    html = html.replace(old_about2, new_about2)

    # Standardize Hero Slider paragraph if present
    old_hero_p = 'Donec vitae libero non enim placerat eleifend aliquam erat volutpat. Curabitur diam ex, dapibus purus sapien, cursus sed nisl tristique.'
    new_hero_p = 'Experience the divine essence of authentic Ayurvedic therapies and luxury Indian botanicals. Enriched with pure Chandan, Kashmiri Kesar, and therapeutic herbal oils to restore your natural glow and timeless radiance.'
    html = html.replace(old_hero_p, new_hero_p)

    return html

print("Common cleanup definitions loaded.")
