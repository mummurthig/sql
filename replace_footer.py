import os
import re

new_footer_str = """<footer class="footer-13" aria-label="Site footer">
               <!-- Meta bar -->
              
               <div class="footer-13__body">
                  <!-- Top row -->
                  <div class="footer-13__top">
                     <div class="footer-13__brand at_fade_anim" data-fade-from="bottom" data-delay=".1">
                        
                        <p class="footer-13__intro mb-0">
                           We create cinematic FPV experiences, professional aerial media, and industrial drone solutions with precision, innovation, and unmatched flight performance across India.
                        </p>
                      
                     </div>
                     <nav class="footer-13__cols" aria-label="Footer navigation">
                        <div class="footer-13__col at_fade_anim" data-fade-from="bottom" data-delay=".2">
                           <p class="footer-13__col-title mb-0">COMPANY</p>
                           <ul class="footer-13__col-list list-unstyled mb-0">
                              <li><a href="about.html">About Us</a></li>
                              <li><a href="index.html">Why Choose Us</a></li>
                              <li><a href="contact.html">Contact</a></li>
                           </ul>
                        </div>
                        <div class="footer-13__col at_fade_anim" data-fade-from="bottom" data-delay=".3">
                           <p class="footer-13__col-title mb-0">SERVICES</p>
                           <ul class="footer-13__col-list list-unstyled mb-0">
                              <li><a href="dji-drones-sales-and-rental.html">Drone Sales</a></li>
                              <li><a href="land-survey-and-mapping.html">Survey & Mapping</a></li>
                              <li><a href="Industrial-Inspection.html">Inspection</a></li>
                              <li><a href="drone-pilot-training.html">Drone Training</a></li>
                           </ul>
                        </div>
                        <div class="footer-13__col at_fade_anim" data-fade-from="bottom" data-delay=".4">
                           <p class="footer-13__col-title mb-0">CONTACT</p>
                           <ul class="footer-13__col-list list-unstyled mb-0">
                              <li><a href="mailto:chennaifpvdrones@gmail.com">chennaifpvdrones@gmail.com</a></li>
                              <li><a href="tel:+919361737903">+91 93617 37903</a></li>
                           </ul>
                        </div>
                     </nav>
                  </div>
                  <!-- Studios row -->
                 
                  <!-- Big brand text -->
                  <div class="footer-13__bigbrand">
                     <p class="footer-13__bigbrand-text mb-0 text-scale-anim">Chennai FPV Drones</p>
                  </div>
               </div>
               <!-- Legal bar -->
               <div class="footer-13__legal">
                  <p class="footer-13__copy mb-0">&copy; 2026 chennai fpv drones. All rights reserved.</p>
                  <ul class="footer-13__social list-unstyled mb-0">
                     <li><a href="https://instagram.com/chennaifpvdrones" target="_blank" rel="noopener">Instagram</a></li>
                     <li><a href="https://linkedin.com/in/chennaifpvdrones" target="_blank" rel="noopener">LinkedIn</a></li>
                     <li><a href="https://in.pinterest.com/chennaifpvdrones/" target="_blank" rel="noopener">Pinterest</a></li>
                  </ul>
                  <ul class="footer-13__legal-links list-unstyled mb-0">
                     <li><a href="#">Privacy</a></li>
                     <li><a href="#">Terms</a></li>
                     <li><a href="#">Cookies</a></li>
                  </ul>
               </div>
            </footer>"""

pattern = re.compile(r'<footer.*?</footer>', re.DOTALL | re.IGNORECASE)

target_dir = r"e:\Business\Chennai FPV Drones\Chennai FPV Drones\chennai-fpv-drones-web"

count = 0
for root, dirs, files in os.walk(target_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            occurrences = len(pattern.findall(content))
            if occurrences > 0:
                # We replace all occurrences of footer with the new footer
                new_content = pattern.sub(new_footer_str, content)
                # Only write back if it's actually different to avoid unnecessary writes
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    count += occurrences
                    print(f"Updated {filepath} (replaced {occurrences} footer(s))")

print(f"Total footer replacements: {count}")
