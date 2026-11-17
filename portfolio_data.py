"""
All portfolio content lives here. Edit this file to update the website AND the
chatbot at the same time -- both are generated from this one source.
"""

PROFILE = {
    "name": "Neelima Penumarthy",
    "title": "Senior Software Engineer",
    "location": "Valencia, CA",
    "email": "neelima.1.penumarthy@gmail.com",
    "linkedin": "https://www.linkedin.com/in/neelimapenumarthy",
    "github": "",  # add your GitHub URL here to show it on the site
    # Phone is kept out of the public code. To show one, fill it in AND set SHOW_PHONE = True.
    "phone": "",
    "taglines": [
        "Backend services & REST APIs",
        "HIPAA-aligned healthcare platforms",
        "Full-stack web applications",
        "AI-assisted development",
        "IoT tinkerer: Raspberry Pi & Arduino",
    ],
    "summary": (
        "Senior Software Developer with 12+ years of professional experience designing, "
        "building, and supporting backend services, REST APIs, and database-driven web "
        "applications. Skilled in Python, Java, C#, JavaScript, and SQL, with hands-on "
        "experience in production debugging, root-cause analysis, and system reliability. "
        "Uses AI-assisted development tools (Claude Code, Claude CoWork) for coding, "
        "debugging, and testing, and validates all results before production use. Led a "
        "3-developer team and owned features end-to-end from requirements through "
        "deployment and maintenance. Interested in applying software architecture and "
        "AI-enabled solutions to clinical and healthcare domains."
    ),
}

SHOW_PHONE = False

STATS = [
    {"value": 12, "suffix": "+", "label": "Years building software"},
    {"value": 25, "suffix": "", "label": "Offices using platforms I architected"},
    {"value": 90, "suffix": "%", "label": "Manual HR effort automated away"},
    {"value": 3, "suffix": "", "label": "Developers I lead"},
]

SKILLS = {
    "Programming": ["Python", "C#", "JavaScript", "Java", "PHP", "SQL", "C"],
    "Frontend & Web": [".NET", "ASP.NET", "React", "Angular", "SAP Fiori", "HTML5", "CSS3", "AJAX", "XML"],
    "Backend & APIs": ["Node.js", "REST APIs", "OData", "SAP NetWeaver Gateway", "GraphQL"],
    "Databases": ["MySQL", "SQL Server", "DB2", "Oracle", "MongoDB", "SAP HANA"],
    "Cloud & OS": ["Microsoft Azure", "Linux", "Windows", "macOS"],
    "Tools": ["Git", "GitHub", "Gerrit", "Perforce", "Jira", "Claude Code", "Claude CoWork",
              "Visual Studio", "NetBeans", "PyCharm"],
    "Embedded & IoT": ["Raspberry Pi", "Arduino", "GPIO", "PIR sensors", "Pi Camera", "PyGame"],
}

EXPERIENCE = [
    {
        "role": "Part-Time Technical Lead",
        "company": "Speech Improvement Center",
        "dates": "03/2023 – Present",
        "skills": ["PHP", "MySQL", "React", "Angular", "Git"],
        "points": [
            "Lead a 3-developer team, guiding implementation decisions and maintaining application architecture and technical direction.",
            "Review key development work and advise on complex debugging and issue resolution, helping the team deliver reliable, high-quality releases.",
        ],
    },
    {
        "role": "Senior Full-Stack Developer",
        "company": "Megagoods Inc",
        "dates": "03/2023 – 09/2026",
        "skills": ["Python", "JavaScript", "SQL", "REST APIs", "MySQL", "Git", "GitHub", "Claude Code"],
        "points": [
            "Built and supported a production-scale e-commerce platform across backend services, databases, REST APIs, and integrations.",
            "Applied OOP, modular design, and reusable components to develop maintainable backend services and business workflows.",
            "Developed and integrated REST APIs and third-party services for payments, SMS, authentication, and identity verification.",
            "Implemented secure authentication workflows using 2FA, OTP, CAPTCHA, phone verification, validation, and authorization.",
            "Translated business requirements into technical designs, backend workflows, API contracts, and production-ready features.",
            "Diagnosed and resolved production issues through root-cause analysis across application, database, API, and integration layers.",
            "Improved system reliability and performance through validation, edge-case handling, query optimization, and API enhancements.",
            "Performed functional, integration, regression, and production testing to ensure application stability and data integrity.",
            "Owned features end-to-end from requirements and development through testing, deployment, troubleshooting, and maintenance using Git/GitHub.",
            "Used Claude Code and AI-assisted development tools for code generation, debugging, refactoring, testing, and code analysis, validating solutions before production use.",
        ],
    },
    {
        "role": "Web Application Developer",
        "company": "Speech Improvement Center",
        "dates": "02/2018 – 02/2023",
        "skills": ["PHP", "MySQL", "React", "Angular", "GraphQL", "JavaScript", "HTML5", "CSS3", "Git"],
        "points": [
            "Designed the architecture of a patient portal and an HR portal from scratch, defining the module structure, data model, and access control design for a PHP and MySQL platform used across 25 offices.",
            "Built both applications end-to-end, owning requirements, backend workflows, database design, and the React and Angular front ends.",
            "Implemented HIPAA-aligned safeguards for protected health information, including encryption, audit logging, and role-based access restrictions enforced at the API and database layers.",
            "Developed backend data workflows and complex MySQL queries to retrieve, transform, and present patient and HR data, and used GraphQL to power the patient progress visualizations.",
            "Automated manual HR workflows for work-hour logging, break tracking, leave management, and therapist certification renewals, reducing manual effort by 90%.",
            "Built data visualizations and reports that let therapists and stakeholders track patient goals and progress over time.",
            "Built responsive, accessible interfaces with React, Angular, JavaScript, HTML, and CSS, improving usability for therapists and HR staff.",
        ],
    },
    {
        "role": "Software Engineer I",
        "company": "SAP Labs India Pvt Ltd",
        "dates": "06/2014 – 04/2016",
        "skills": ["React", "JavaScript", "Node.js", "PHP", "SAP Fiori", "SAP HANA", "OData",
                   "SAP NetWeaver Gateway", "REST APIs", "Git", "Gerrit", "Perforce"],
        "points": [
            "Built and maintained full-stack enterprise applications using React, JavaScript, Node.js, PHP, SAP Fiori, and SAP HANA across SAP CRM and banking workflows.",
            "Developed React/Fiori user interfaces and backend services for complex business processes, focusing on usability, maintainability, and reliable application behavior.",
            "Designed and consumed REST/OData APIs through SAP NetWeaver Gateway, integrating frontend applications with SAP backend services and business logic.",
            "Developed a HANA/Fiori competency and project-assignment application, translating complex organizational workflows into an intuitive manager-facing solution.",
            "Partnered with business stakeholders to clarify requirements, prepare functional specifications, define solutions, and support UAT through delivery.",
            "Performed code reviews, debugging, integration troubleshooting, and application maintenance across frontend, backend, API, and data layers.",
        ],
    },
    {
        "role": "Intern",
        "company": "Mission R&D",
        "dates": "03/2013 – 05/2013",
        "skills": ["Python", "React", "Angular", "MySQL"],
        "points": [
            "Industry-readiness program in partnership with companies like Microsoft, preparing for product development roles.",
            "Worked with JavaScript frameworks like React and AngularJS to build enterprise-grade apps.",
            "Hands-on Python socket programming; wrote test cases for others' code.",
            "Part of a team of 8 that built an end-to-end Python discussion-forum application with a MySQL backend.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Patient Portal",
        "category": "Healthcare",
        "blurb": "Architected from scratch for a speech-therapy practice across 25 offices: HIPAA-aligned encryption, audit logging, role-based access, and GraphQL-powered patient progress charts.",
        "skills": ["PHP", "MySQL", "React", "Angular", "GraphQL"],
    },
    {
        "name": "HR Portal",
        "category": "Healthcare",
        "blurb": "Automated work-hour logging, break tracking, leave management, and therapist certification renewals, cutting manual effort by 90%.",
        "skills": ["PHP", "MySQL", "Angular", "JavaScript"],
    },
    {
        "name": "E-commerce Platform",
        "category": "Web",
        "blurb": "Production-scale backend with payments, SMS, identity verification, and secure auth (2FA, OTP, CAPTCHA, phone verification).",
        "skills": ["Python", "REST APIs", "SQL", "MySQL"],
    },
    {
        "name": "Competency & Project-Assignment App",
        "category": "Enterprise",
        "blurb": "SAP HANA / Fiori app that turned complex organizational staffing workflows into an intuitive manager-facing tool.",
        "skills": ["SAP Fiori", "SAP HANA", "OData", "SAP NetWeaver Gateway"],
    },
    {
        "name": "Line-Tracking Robot",
        "category": "IoT",
        "blurb": "Autonomous Arduino robot for warehouse-replenishment prototyping: IR sensors, PWM motor control, and firmware in C tuned to reduce drift. (Funded IoT initiative, SAP Labs India)",
        "skills": ["Arduino", "C"],
    },
    {
        "name": "Motion-Triggered Camera",
        "category": "IoT",
        "blurb": "Raspberry Pi + PIR sensor on GPIO + Pi Camera, with event-driven Python callbacks that capture photos or clips on motion. (Funded IoT initiative, SAP Labs India)",
        "skills": ["Raspberry Pi", "Python", "GPIO", "PIR sensors", "Pi Camera"],
    },
    {
        "name": "Internet Speed Monitor",
        "category": "IoT",
        "blurb": "Raspberry Pi monitor using speedtest-cli to measure download, upload, and latency every two hours and display them on screen.",
        "skills": ["Raspberry Pi", "Python", "PyGame"],
    },
    {
        "name": "Python Discussion Forum",
        "category": "Web",
        "blurb": "End-to-end Python forum application with a MySQL backend, built by a team of 8 during the Mission R&D internship.",
        "skills": ["Python", "MySQL"],
    },
]

HIGHLIGHTS = {
    "Talks & Research": [
        "RRR – Reduce, Reuse, Recycle: authored and presented a paper on environmental awareness and sustainable lifestyle practices at a statewide symposium. Awarded 1st prize.",
        "CYBORGS – Cybernetic Organisms: presented research on biomechatronic integration for assistive technology at the IEEE Women in Engineering Congress.",
    ],
    "Recognition": [
        "SAP Rising Star: given to the most promising newcomer for exceptional performance in the role.",
    ],
    "Certifications": [
        "NIIT Certified Java Programmer",
        "IBM Certified DB2 Academic Associate",
        "Oracle Certified MySQL Developer",
    ],
    "Education": [
        "Bachelor's Degree in Information Technology, Jawaharlal Nehru Technological University, Andhra Pradesh, India (2010 – 2014)",
    ],
}

SUGGESTED_QUESTIONS = [
    "What healthcare software has Neelima built?",
    "What's her experience with Python?",
    "Has she led a team?",
    "Tell me about her IoT projects",
]


def resume_as_text() -> str:
    """Render the portfolio data as plain text for the chatbot's knowledge base."""
    p = PROFILE
    lines = [
        f"Name: {p['name']}",
        f"Title: {p['title']}",
        f"Location: {p['location']}",
        f"Email: {p['email']}",
        f"LinkedIn: {p['linkedin']}",
    ]
    if p.get("github"):
        lines.append(f"GitHub: {p['github']}")
    if SHOW_PHONE:
        lines.append(f"Phone: {p['phone']}")
    lines += ["", "SUMMARY", p["summary"], "", "SKILLS"]
    lines += [f"- {cat}: {', '.join(items)}" for cat, items in SKILLS.items()]
    lines += ["", "EXPERIENCE"]
    for job in EXPERIENCE:
        lines.append(f"{job['role']} at {job['company']} ({job['dates']})")
        lines += [f"  - {pt}" for pt in job["points"]]
    lines += ["", "PROJECTS"]
    lines += [f"- {pr['name']} [{pr['category']}]: {pr['blurb']}" for pr in PROJECTS]
    for section, items in HIGHLIGHTS.items():
        lines += ["", section.upper()]
        lines += [f"- {it}" for it in items]
    return "\n".join(lines)
