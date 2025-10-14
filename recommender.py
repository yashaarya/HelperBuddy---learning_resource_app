# recommender.py
"""
Backend for HelperBuddy App
Contains topics and their recommended resources
"""

def get_recommendations(topic: str) -> list[dict]:
    """
    Return a list of recommended resources for the given topic.
    Each resource is a dictionary with 'title', 'description', 'url'.
    """
    resources = {
        "Python": [
            {"title": "Official Python Tutorial", "description": "Comprehensive tutorial from Python.org", "url": "https://docs.python.org/3/tutorial/"},
            {"title": "Learn Python - W3Schools", "description": "Python basics and advanced topics", "url": "https://www.w3schools.com/python/"},
            {"title": "Python for Everybody", "description": "Free Python course by Dr. Charles Severance", "url": "https://www.py4e.com/"},
            {"title": "Real Python", "description": "Articles, tutorials, and courses for Python developers", "url": "https://realpython.com/"},
            {"title": "Automate the Boring Stuff", "description": "Practical Python programming book and course", "url": "https://automatetheboringstuff.com/"}
        ],
        "AI/ML": [
            {"title": "Coursera Machine Learning", "description": "Andrew Ng's ML course", "url": "https://www.coursera.org/learn/machine-learning"},
            {"title": "Fast.ai Practical Deep Learning", "description": "Hands-on deep learning course", "url": "https://course.fast.ai/"},
            {"title": "Kaggle Learn", "description": "ML and Data Science tutorials", "url": "https://www.kaggle.com/learn/overview"},
            {"title": "Google AI Education", "description": "Resources by Google AI", "url": "https://ai.google/education/"},
            {"title": "DeepLearning.ai", "description": "Deep Learning Specialization", "url": "https://www.deeplearning.ai/"}
        ],
        "Data Science": [
            {"title": "DataCamp", "description": "Interactive Data Science courses", "url": "https://www.datacamp.com/"},
            {"title": "Kaggle Data Science", "description": "Hands-on datasets and tutorials", "url": "https://www.kaggle.com/learn/overview"},
            {"title": "Analytics Vidhya", "description": "Articles, competitions, and tutorials", "url": "https://www.analyticsvidhya.com/"},
            {"title": "Coursera Data Science", "description": "Johns Hopkins Data Science Specialization", "url": "https://www.coursera.org/specializations/jhu-data-science"},
            {"title": "edX Data Science", "description": "Data Science MicroMasters programs", "url": "https://www.edx.org/micromasters/mitx-data-science"}
        ],
        "Web Development": [
            {"title": "freeCodeCamp", "description": "Learn Web Dev for free", "url": "https://www.freecodecamp.org/"},
            {"title": "MDN Web Docs", "description": "Official documentation for HTML, CSS, JS", "url": "https://developer.mozilla.org/"},
            {"title": "The Odin Project", "description": "Full-stack web development curriculum", "url": "https://www.theodinproject.com/"},
            {"title": "W3Schools Web Development", "description": "HTML, CSS, JavaScript tutorials", "url": "https://www.w3schools.com/"},
            {"title": "Frontend Masters", "description": "Professional Web Dev courses", "url": "https://frontendmasters.com/"}
        ],
        "Cloud Computing": [
            {"title": "AWS Training", "description": "Official Amazon Web Services courses", "url": "https://aws.amazon.com/training/"},
            {"title": "Microsoft Learn Azure", "description": "Free Azure training resources", "url": "https://learn.microsoft.com/en-us/training/azure/"},
            {"title": "Google Cloud Training", "description": "Google Cloud learning paths", "url": "https://cloud.google.com/training"},
            {"title": "Coursera Cloud Computing", "description": "Cloud computing specialization", "url": "https://www.coursera.org/specializations/cloud-computing"},
            {"title": "edX Cloud Computing", "description": "Cloud Computing MicroMasters", "url": "https://www.edx.org/micromasters/ritx-cloud-computing"}
        ],
        "Cybersecurity": [
            {"title": "Cybrary", "description": "Cybersecurity courses and labs", "url": "https://www.cybrary.it/"},
            {"title": "OWASP", "description": "Web security learning resources", "url": "https://owasp.org/"},
            {"title": "Coursera Cybersecurity", "description": "Cybersecurity specialization", "url": "https://www.coursera.org/specializations/cyber-security"},
            {"title": "Hack The Box", "description": "Hands-on penetration testing lab", "url": "https://www.hackthebox.eu/"},
            {"title": "Udemy Cybersecurity", "description": "Various cybersecurity courses", "url": "https://www.udemy.com/courses/search/?q=cybersecurity"}
        ],
        "Blockchain": [
            {"title": "Ethereum.org", "description": "Official Ethereum developer resources", "url": "https://ethereum.org/en/developers/"},
            {"title": "Coursera Blockchain", "description": "Blockchain specialization", "url": "https://www.coursera.org/specializations/blockchain"},
            {"title": "IBM Blockchain", "description": "IBM blockchain learning resources", "url": "https://www.ibm.com/topics/learn-blockchain"},
            {"title": "CryptoZombies", "description": "Learn blockchain by building games", "url": "https://cryptozombies.io/"},
            {"title": "edX Blockchain", "description": "Blockchain courses and programs", "url": "https://www.edx.org/learn/blockchain"}
        ],
        "Databases": [
            {"title": "SQLBolt", "description": "Interactive SQL tutorials", "url": "https://sqlbolt.com/"},
            {"title": "W3Schools SQL", "description": "SQL tutorial for beginners", "url": "https://www.w3schools.com/sql/"},
            {"title": "MongoDB University", "description": "Official MongoDB courses", "url": "https://university.mongodb.com/"},
            {"title": "Khan Academy SQL", "description": "SQL basics tutorial", "url": "https://www.khanacademy.org/computing/computer-programming/sql"},
            {"title": "Coursera Databases", "description": "Database systems specialization", "url": "https://www.coursera.org/specializations/database-systems"}
        ],
        "DevOps": [
            {"title": "Linux Academy / A Cloud Guru", "description": "DevOps and cloud courses", "url": "https://acloudguru.com/"},
            {"title": "Docker Docs", "description": "Official Docker tutorials", "url": "https://docs.docker.com/get-started/"},
            {"title": "Kubernetes Docs", "description": "Kubernetes official documentation", "url": "https://kubernetes.io/docs/home/"},
            {"title": "Jenkins Docs", "description": "Learn Jenkins CI/CD", "url": "https://www.jenkins.io/doc/"},
            {"title": "Udemy DevOps Courses", "description": "Various DevOps courses", "url": "https://www.udemy.com/courses/search/?q=devops"}
        ],
        "Mobile Development": [
            {"title": "Android Developers", "description": "Official Android development resources", "url": "https://developer.android.com/"},
            {"title": "iOS Developer", "description": "Official Apple developer resources", "url": "https://developer.apple.com/ios/"},
            {"title": "Flutter Docs", "description": "Cross-platform mobile app development", "url": "https://flutter.dev/docs"},
            {"title": "React Native", "description": "Learn to build apps using React Native", "url": "https://reactnative.dev/"},
            {"title": "Udemy Mobile Dev Courses", "description": "Various mobile development courses", "url": "https://www.udemy.com/courses/search/?q=mobile%20development"}
        ],
        "IoT": [
            {"title": "IoT For All", "description": "IoT tutorials and articles", "url": "https://www.iotforall.com/"},
            {"title": "Arduino Official", "description": "Learn Arduino for IoT projects", "url": "https://www.arduino.cc/"},
            {"title": "Raspberry Pi Official", "description": "Raspberry Pi IoT projects", "url": "https://www.raspberrypi.com/"},
            {"title": "Coursera IoT", "description": "IoT specialization courses", "url": "https://www.coursera.org/specializations/internet-of-things"},
            {"title": "edX IoT", "description": "IoT courses and programs", "url": "https://www.edx.org/learn/iot"}
        ],
        "Networking": [
            {"title": "Cisco Networking Academy", "description": "Official Cisco courses", "url": "https://www.netacad.com/"},
            {"title": "CompTIA Network+", "description": "Networking fundamentals course", "url": "https://www.comptia.org/certifications/network"},
            {"title": "Juniper Networks Learning", "description": "Networking courses by Juniper", "url": "https://www.juniper.net/us/en/training/"},
            {"title": "Coursera Networking", "description": "Networking courses", "url": "https://www.coursera.org/courses?query=networking"},
            {"title": "Udemy Networking Courses", "description": "Various networking tutorials", "url": "https://www.udemy.com/courses/search/?q=networking"}
        ],
        "Big Data": [
            {"title": "Hadoop Official", "description": "Apache Hadoop tutorials", "url": "https://hadoop.apache.org/"},
            {"title": "Cloudera Training", "description": "Big Data courses", "url": "https://www.cloudera.com/about/training.html"},
            {"title": "Coursera Big Data", "description": "Big Data Specialization", "url": "https://www.coursera.org/specializations/big-data"},
            {"title": "edX Big Data", "description": "Big Data MicroMasters", "url": "https://www.edx.org/micromasters/uc-san-diegox-big-data"},
            {"title": "Udemy Big Data Courses", "description": "Various Big Data tutorials", "url": "https://www.udemy.com/courses/search/?q=big%20data"}
        ],
        "UI/UX": [
            {"title": "Interaction Design Foundation", "description": "UI/UX courses and resources", "url": "https://www.interaction-design.org/"},
            {"title": "Coursera UI/UX", "description": "UI/UX Design Specialization", "url": "https://www.coursera.org/specializations/ui-ux-design"},
            {"title": "UX Collective", "description": "Articles and case studies", "url": "https://uxdesign.cc/"},
            {"title": "Adobe XD Learn", "description": "Adobe XD tutorials for designers", "url": "https://helpx.adobe.com/xd/tutorials.html"},
            {"title": "Udemy UI/UX Courses", "description": "Various UI/UX courses", "url": "https://www.udemy.com/courses/search/?q=ui%20ux"}
        ],
        "Game Development": [
            {"title": "Unity Learn", "description": "Official Unity tutorials", "url": "https://learn.unity.com/"},
            {"title": "Unreal Engine Learn", "description": "Official Unreal Engine tutorials", "url": "https://www.unrealengine.com/en-US/onlinelearning-courses"},
            {"title": "Godot Docs", "description": "Open-source game engine tutorials", "url": "https://docs.godotengine.org/"},
            {"title": "Coursera Game Dev", "description": "Game development courses", "url": "https://www.coursera.org/courses?query=game%20development"},
            {"title": "Udemy Game Dev", "description": "Various game development courses", "url": "https://www.udemy.com/courses/search/?q=game%20development"}
        ]
    }

    return resources.get(topic, [])
