from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fatima Alarfaj</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background: linear-gradient(180deg, #f4fbfa 0%, #eef7f5 100%);
            color: #163235;
            line-height: 1.6;
        }

        nav {
            position: sticky;
            top: 0;
            background: rgba(255,255,255,0.9);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #dcebea;
            padding: 18px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
        }

        nav .brand {
            font-size: 20px;
            font-weight: bold;
            color: #1d1f48;
        }

        nav ul {
            list-style: none;
            display: flex;
            gap: 18px;
            flex-wrap: wrap;
        }

        nav a {
            text-decoration: none;
            color: #163235;
            font-size: 14px;
            font-weight: 600;
            transition: color 0.2s ease;
        }

        nav a:hover {
            color: #106967;
        }

        .container {
            width: 90%;
            max-width: 1140px;
            margin: auto;
        }

        .hero {
            padding: 90px 0 50px;
            animation: fadeUp 0.9s ease both;
        }

        .eyebrow {
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 12px;
            color: #106967;
            font-weight: bold;
        }

        .hero h1 {
            font-size: 58px;
            line-height: 1.05;
            margin: 14px 0 18px;
            color: #1d1f48;
            max-width: 850px;
        }

        .hero p {
            max-width: 820px;
            font-size: 18px;
            color: #486665;
        }

        .buttons {
            margin-top: 28px;
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-block;
            padding: 12px 20px;
            border-radius: 14px;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 24px rgba(16, 105, 103, 0.15);
        }

        .btn-primary {
            background: #106967;
            color: white;
        }

        .btn-secondary {
            background: #4fbc9c22;
            color: #163235;
            border: 1px solid #4fbc9c;
        }

        section {
            padding: 30px 0 36px;
            scroll-margin-top: 90px;
        }

        .card {
            background: rgba(255,255,255,0.95);
            border: 1px solid #e1eeec;
            border-radius: 28px;
            padding: 34px;
            box-shadow: 0 10px 30px rgba(29, 31, 72, 0.05);
        }

        .section-title {
            font-size: 36px;
            margin: 10px 0 18px;
            color: #1d1f48;
        }

        .muted {
            color: #516f6d;
        }

        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 28px;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
        }

        .mini-card {
            background: #f8fbfb;
            border: 1px solid #e5efee;
            border-radius: 18px;
            padding: 18px;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }

        .mini-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(16, 105, 103, 0.08);
        }

        .timeline-item {
            padding: 18px 0;
            border-bottom: 1px solid #e7efee;
        }

        .timeline-item:last-child {
            border-bottom: none;
        }

        .timeline-item h3 {
            font-size: 20px;
            color: #106967;
            margin-bottom: 4px;
        }

        .role-meta {
            color: #6b8685;
            font-size: 14px;
            margin-bottom: 10px;
        }

        .timeline-item ul {
            padding-left: 18px;
            color: #445f5e;
        }

        .timeline-item li {
            margin-bottom: 8px;
        }

        .tag {
            display: inline-block;
            padding: 8px 12px;
            border-radius: 999px;
            background: #4fbc9c22;
            border: 1px solid #4fbc9c;
            margin: 0 8px 10px 0;
            font-size: 13px;
            color: #163235;
        }

        .link-list a {
            display: block;
            margin-bottom: 10px;
            color: #106967;
            text-decoration: none;
            word-break: break-word;
        }

        .link-list a:hover {
            text-decoration: underline;
        }

        .logo-strip {
            overflow: hidden;
            border-top: 1px solid #dfeeed;
            border-bottom: 1px solid #dfeeed;
            background: rgba(255,255,255,0.75);
            padding: 18px 0;
            margin: 20px 0 10px;
        }


       .logo-track {
       display:flex;
       align-items:center;
       gap:50px;
       width:max-content;
       animation: marquee 28s linear infinite;
}
   .logo-track img{
    height:42px;
    width:auto;
    max-width:140px;
    object-fit:contain;
}

        .logo-pill {
            min-width: 150px;
            text-align: center;
            padding: 12px 18px;
            border-radius: 999px;
            background: white;
            border: 1px solid #dcebea;
            color: #1d1f48;
            font-weight: 700;
            box-shadow: 0 6px 18px rgba(29, 31, 72, 0.05);
        }

        .dark-section {
            background: linear-gradient(135deg, #1d1f48, #106967);
            color: white;
        }

        .dark-section .section-title,
        .dark-section .eyebrow,
        .dark-section strong,
        .dark-section a {
            color: white;
        }

        .dark-section .muted {
            color: #d8efea;
        }

        .reveal {
            animation: fadeUp 0.8s ease both;
        }

        .delay-1 { animation-delay: 0.08s; }
        .delay-2 { animation-delay: 0.16s; }
        .delay-3 { animation-delay: 0.24s; }

        footer {
            text-align: center;
            padding: 38px 0 50px;
            color: #617c7a;
            font-size: 14px;
        }

        @keyframes fadeUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes marquee {
            from { transform: translateX(0); }
            to { transform: translateX(-50%); }
        }

        @media (max-width: 950px) {
            nav {
                flex-direction: column;
                gap: 12px;
                padding: 16px 20px;
            }

            .hero h1 {
                font-size: 42px;
            }

            .grid-2,
            .grid-3 {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="brand">Fatima Alarfaj</div>
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#experience">Experience</a></li>
            <li><a href="#research">Projects</a></li>
            <li><a href="#honors">Honors</a></li>
            <li><a href="#scholarships">Scholarships</a></li>
            <li><a href="#recognitions">Recognitions</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#press">Press</a></li>
            <li><a href="#publications">Publications</a></li>
            <li><a href="#volunteering">Volunteering</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <div class="container">
        <section class="hero">
            <div class="eyebrow">Researcher • Energy Systems Innovator • Speaker</div>
            <h1>Fatima Alarfaj</h1>
            <p>
                Chemical Engineering student at King Fahd University of Petroleum &amp; Minerals (KFUPM) focused on hydrogen technologies, sustainable energy systems, and the global energy transition.
            </p>
            <div class="buttons">
                <a class="btn btn-primary" href="#about">Explore Profile</a>
                <a class="btn btn-secondary" href="#contact">Get in Touch</a>
            </div>
        </section>
    </div>

   <div class="logo-strip">
    <div class="logo-track">

        <img src="/static/aramco.png">
        <img src="/static/SABIC.png">
        <img src="/static/maaden.png">
        <img src="/static/STC-01.png">
        <img src="/static/Roshn_Logo.png">
        <img src="/static/misk-21-logo-light-10-588.png">
        <img src="/static/MEWA.png">
        <img src="/static/mcitlogo_0.png">
        <img src="/static/ilmi.png">
        <img src="/static/SWA_textlogo.png">
        <img src="/static/Saudia Airlines-01.png">
        <img src="/static/Roshn Group01.png">
        <img src="/static/ithraapng.png">
        <img src="/static/png.png">
        <img src="/static/.png.png">
        <img src="/static/misk-21-logo-light-10-588.png">
        <img src="/static/images k.png">
        <img src="/static/3827980ca7042e01b8d2ebf1f155da09.png">
        <img src="/static/3136571-1629284407.png">


    </div>
</div>
    

    <div class="container">
        <section id="about" class="reveal">
            <div class="card grid-2">
                <div>
                    <div class="eyebrow">About</div>
                    <h2 class="section-title">Engineering Innovation for the Energy Transition</h2>
                    <p class="muted">
                        Her research spans hydrogen production, water harvesting technologies, metal–organic frameworks (MOFs), membrane systems, and geological pathways for white hydrogen. She is particularly interested in technologies that support sustainability in arid environments and accelerate the development of next-generation energy solutions.
                    </p>
                    <p class="muted" style="margin-top:14px;">
                        Alongside technical research, she is interested in the intersection of engineering, energy economics, and policy, exploring how emerging technologies can be translated into scalable infrastructure and strategic energy initiatives. Her work reflects a broader interest in shaping the future of energy systems through both technical innovation and strategic decision-making.
                    </p>
                    <p class="muted" style="margin-top:14px;">
                        Beyond research, she is passionate about science communication, youth leadership, and translating scientific work into broader societal and national impact.
                    </p>
                </div>
                <div>
                    <h3 style="margin-bottom:12px;color:#1d1f48;">Research Interests</h3>
                    <span class="tag">Hydrogen Technologies</span>
                    <span class="tag">White Hydrogen</span>
                    <span class="tag">Sustainable Energy Systems</span>
                    <span class="tag">Energy Transition</span>
                    <span class="tag">Circular Economy</span>
                    <span class="tag">Water Harvesting</span>
                    <span class="tag">MOF Synthesis</span>
                    <span class="tag">Membrane Separation</span>
                    <span class="tag">Electrolysis</span>
                    <span class="tag">Global Impact</span>
                    
                    <span class="tag">Strategic Technology Translation</span>
                </div>
            </div>
        </section>

        <section id="experience" class="reveal delay-1">
            <div class="card">
                <div class="eyebrow">Experience</div>
                <h2 class="section-title">Research, industry, and leadership experience</h2>

                <div class="timeline-item">
                    <h3>Intern, Air Products</h3>
                    <div class="role-meta">Membrane ODI Project • SATC</div>
                    <ul>
                        <li>Contributed to membrane gas separation testing and operations focused on BTEX and VOC applications.</li>
                        <li>Used Python for data analysis, dual-sorption membrane modeling, and experimental result visualization.</li>
                        <li>Gained field exposure through visits to NEOM’s Green Hydrogen Project and the Hydrogen Innovation and Development Center.</li>
                    </ul>
                </div>

                <div class="timeline-item">
                    <h3>Student Researcher, King Fahd University of Petroleum &amp; Minerals (KFUPM)</h3>
                    <div class="role-meta">Hydrogen, water harvesting, and advanced materials research</div>
                    <ul>
                        <li>Conducting research on water harvesting, MOF synthesis, and electrolysis for hydrogen production.</li>
                        <li>Developing prototypes for water harvesting applications.</li>
                        <li>Studying olivine rock and synthesizing artificial olivine for white hydrogen production.</li>
                    </ul>
                </div>

                <div class="timeline-item">
                    <h3>Student Researcher, King Abdulaziz City for Science and Technology (UC Berkeley–KACST)</h3>
                    <div class="role-meta">Materials research</div>
                    <ul>
                        <li>Synthesized and characterized MOF-303 for optimizing water adsorption properties.</li>
                        <li>Investigated material performance for sustainable water production applications.</li>
                    </ul>
                </div>

                <div class="timeline-item">
                    <h3>Student Mentor, King Abdulaziz City for Science and Technology (UC Berkeley–KACST)</h3>
                    <div class="role-meta">Mentorship and laboratory guidance</div>
                    <ul>
                        <li>Mentored students on MOFs for water harvesting and CO₂ capture.</li>
                        <li>Guided them through synthesis, experimental design, and data analysis.</li>
                    </ul>
                </div>

                <div class="timeline-item">
                    <h3>Media Team Manager, Waselah (now Ulom)</h3>
                    <div class="role-meta">Nonprofit research engagement initiative</div>
                    <ul>
                        <li>Helped engage 150+ volunteers, reach 20K students, and support $150K in funding.</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="research" class="reveal delay-2">
            <div style="margin-bottom:20px;">
                <div class="eyebrow">Projects</div>
                <h2 class="section-title">Scientific Projects</h2>
                <p class="muted">Research projects spanning direct hydrogen production, white hydrogen, and sustainable materials.</p>
            </div>
            <div class="grid-3">
                <div class="card">
                    <h3>System for Direct Hydrogen Production</h3>
                    <p class="muted" style="margin-top:12px;">A project focused on direct hydrogen production through integrated system design.</p>
                    <p style="margin-top:12px;"><a href="https://isef.net/project/chem039-system-for-direct-hydrogen-production" target="_blank" rel="noopener noreferrer">View project</a></p>
                </div>
                <div class="card">
                    <h3>Synthetic Olivine for White Hydrogen Production</h3>
                    <p class="muted" style="margin-top:12px;">Investigating artificial olivine synthesis and mineral-based pathways for white hydrogen.</p>
                    <p style="margin-top:12px;"><a href="https://isef.net/project/chem041-synthetic-olivine-for-white-hydrogen-production" target="_blank" rel="noopener noreferrer">View project</a></p>
                </div>
                <div class="card">
                    <h3>MOF-303 for Water Harvesting</h3>
                    <p class="muted" style="margin-top:12px;">Synthesizing and characterizing MOF-303 for water harvesting in arid climates.</p>
                </div>
            </div>
        </section>

        <section id="honors" class="reveal">
            <div class="card">
                <div class="eyebrow">Honors</div>
                <h2 class="section-title">Honors &amp; Awards</h2>
                <div class="grid-2">
                    <div>
                        <div class="mini-card">First Place Grand Award, National Olympiad for Scientific Creativity (2025)</div>
                        <div class="mini-card" style="margin-top:12px;">Fourth Place Grand Award, Chemistry Category, Regeneron ISEF (2025)</div>
                        <div class="mini-card" style="margin-top:12px;">Special Award, American Chemical Society, Regeneron ISEF (2025)</div>
                        <div class="mini-card" style="margin-top:12px;">Special Award, Wolfram Research Inc., Regeneron ISEF</div>
                        <div class="mini-card" style="margin-top:12px;">Second Place Grand Award, Chemistry Category, Regeneron ISEF (2023)</div>
                        <div class="mini-card" style="margin-top:12px;">Most Outstanding Exhibit Award, Yale Science &amp; Engineering Association, IBDAA (2023)</div>
                    </div>
                    <div>
                        <div class="mini-card">Third Place, National Olympiad for Scientific Creativity (2023)</div>
                        <div class="mini-card" style="margin-top:12px;">Special Award, Ministry of Industry and Mineral Resources, IBDAA (2025)</div>
                        <div class="mini-card" style="margin-top:12px;">Best Research Award, Chemathon, KFUPM Chemistry-ACS Saudi Chapter International Conference</div>
                        <div class="mini-card" style="margin-top:12px;">Second Place and National Finalist, Arabic Reading Challenge (2023)</div>
                        <div class="mini-card" style="margin-top:12px;">Special Award, IELTS IDP, IBDAA</div>
                        <div class="mini-card" style="margin-top:12px;">Annual Saudi Arabia Top Distinguished Youth Honorary Award, Ministry of Education (2024)</div>
                    </div>
                </div>
            </div>
        </section>

        <section id="scholarships" class="reveal delay-1">
            <div class="card">
                <div class="eyebrow">Scholarships</div>
                <h2 class="section-title">Scholarships</h2>
                <div class="grid-2">
                    <div>
                        <div class="mini-card">King Fahd University of Petroleum and Minerals Full Scholarship</div>
                        <div class="mini-card" style="margin-top:12px;">King Abdulaziz University Full-Funded Scholarship</div>
                    </div>
                    <div>
                        <div class="mini-card">Imam bin Abdulrahman bin Faisal University Full-Funded Scholarship</div>
                        <div class="mini-card" style="margin-top:12px;">King Faisal University Full-Funded Scholarship</div>
                    </div>
                </div>
            </div>
        </section>

        <section id="recognitions" class="reveal delay-2">
            <div class="card">
                <div class="eyebrow">Recognitions</div>
                <h2 class="section-title">Institutional Recognitions</h2>
                <p class="muted" style="font-size:13px;margin-bottom:16px;">Recognized by multiple national institutions and industry leaders due to her Distinguished Achievement in Research and Technology.</p>
                <div class="grid-3">
                    <div class="mini-card">Aramco</div>
                    <div class="mini-card">SABIC</div>
                    <div class="mini-card">Maaden</div>
                    <div class="mini-card">Ministry of Industry and Mineral Resources</div>
                    <div class="mini-card">Ministry of Environment, Water and Agriculture</div>
                    <div class="mini-card">Ministry of Communications and Information Technology</div>
                    <div class="mini-card">ROSHN Group</div>
                    <div class="mini-card">stc</div>
                    <div class="mini-card">ilmi</div>
                    <div class="mini-card">Misk Foundation</div>
                    <div class="mini-card">Saudia</div>
                    <div class="mini-card">Saudi RDI</div>
                    <div class="mini-card">King Abdulaziz City for Science and Technology</div>
                    <div class="mini-card">Saudi Water Authority</div>
                    <div class="mini-card">Ithra</div>
                    <div class="mini-card">SDAIA</div>
                    <div class="mini-card">King Abdullah City for Atomic Energy</div>
                </div>
            </div>
        </section>

        <section id="skills" class="reveal">
            <div class="card">
                <div class="eyebrow">Capabilities</div>
                <h2 class="section-title">Skills</h2>
                <div class="grid-3">
                    <div class="mini-card">
                        <strong>Engineering &amp; Energy Systems</strong><br><br>
                        Aspen Plus<br>
                        Process Engineering<br>
                        Experimental Design<br>
                        Scalability &amp; Feasibility Assessment
                    </div>
                    <div class="mini-card">
                        <strong>Data &amp; Quantitative Analysis</strong><br><br>
                        Python (Data Analysis &amp; Visualization)<br>
                        Data Coding<br>
                        Automation &amp; Performance Metrics<br>
                        Quantitative Problem Solving
                    </div>
                    <div class="mini-card">
                        <strong>Strategy &amp; Decision Support</strong><br><br>
                        Structured Problem Solving<br>
                        Data-Driven Decision Making<br>
                        Decision Support<br>
                        Project Planning
                    </div>
                </div>
            </div>
        </section>

        <section id="press" class="reveal delay-1">
            <div class="card">
                <div class="eyebrow">In the Press</div>
                <h2 class="section-title">Media coverage and mentions</h2>
                <div class="link-list">
                    <a href="https://moe.gov.sa/en/mediacenter/MOEnews/Pages/Isef-Fair.aspx" target="_blank" rel="noopener noreferrer">Ministry of Education coverage</a>
                    <a href="https://www.societyforscience.org/press-release/regeneron-isef-full-awards-2023/" target="_blank" rel="noopener noreferrer">Society for Science — Regeneron ISEF awards</a>
                    <a href="https://saudigazette.com.sa/article/632610/SAUDI-ARABIA/Talented-Saudi-students-bag-record-number-of-27-prizes-at-ISEF-2023" target="_blank" rel="noopener noreferrer">Saudi Gazette feature</a>
                    <a href="https://spa.gov.sa/N2321871" target="_blank" rel="noopener noreferrer">Saudi Press Agency coverage 1</a>
                    <a href="https://spa.gov.sa/N2327369" target="_blank" rel="noopener noreferrer">Saudi Press Agency coverage 2</a>
                    <a href="https://spa.gov.sa/N2325121" target="_blank" rel="noopener noreferrer">Saudi Press Agency coverage 3</a>
                    <a href="https://spa.gov.sa/N2323206" target="_blank" rel="noopener noreferrer">Saudi Press Agency coverage 4</a>
                    <a href="https://spa.gov.sa/N2322117" target="_blank" rel="noopener noreferrer">Saudi Press Agency coverage 5</a>
                    <a href="https://www.mawhiba.sa/media-centre/news/chairman-of-the-board-of-directors-of-mawhiba-the-kingdoms-student-awards-at-isef-2025-are-the-fruit-of-the-leaderships-support-for-gifted-students/" target="_blank" rel="noopener noreferrer">Mawhiba coverage</a>
                </div>
            </div>
        </section>

        <section id="publications" class="reveal delay-2">
            <div class="card">
                <div class="eyebrow">Publications</div>
                <h2 class="section-title">Publications</h2>
                <div class="link-list">
                    <a href="https://pubmed.ncbi.nlm.nih.gov/38403850/" target="_blank" rel="noopener noreferrer">PubMed publication</a>
                </div>
            </div>
        </section>

        <section id="volunteering" class="reveal">
            <div class="card">
                <div class="eyebrow">Volunteering</div>
                <h2 class="section-title">Service and community impact</h2>
                <div class="mini-card">Volunteer, Zahra Breast Cancer Association</div>
                <div class="mini-card" style="margin-top:12px;">Member, Saudi Youth Ambassadors Group</div>
                <div class="mini-card" style="margin-top:12px;">250+ volunteering hours</div>
            </div>
        </section>

        <section id="contact" class="reveal delay-1">
            <div class="card dark-section">
                <div class="eyebrow">Contact</div>
                <h2 class="section-title">Let’s connect</h2>
                <p class="muted">
                    For research collaborations, speaking opportunities, interviews, student initiatives, or professional inquiries, feel free to reach out.
                </p>
                <div class="grid-2" style="margin-top:20px;">
                    <div class="mini-card" style="background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.12);">
                        <strong>Email</strong><br>fatimaabdullahalarfaj@gmail.com
                    </div>
                    <div class="mini-card" style="background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.12);">
                        <strong>LinkedIn</strong><br>https://www.linkedin.com/in/fatima-alarfaj-86a8413b6/
                    </div>
                </div>
            </div>
        </section>

        <footer>
            © 2026 Fatima Alarfaj. All rights reserved.
        </footer>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=False)
