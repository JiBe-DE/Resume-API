from fastapi import FastAPI

presentation = {
    "Fullname": "Jean-Baptiste Lanvin",
    "Pitch": '''After several years working in the aerospece industry as a System Engineer, I have decided to change my professional path towards the data world.
                Therefore, following my intensive Data Engineering training at DataScientest, I am looking for a position of Data Engineer. Highly adaptative engineer thanks to my various professional experiences, I am already curious about your challenges !''', 
}

contact = {
    "Mail": "jb.lanvin@gmail.com",
    "Phone": "06.03.00.12.64", 
    "LinkedIn": "https://www.linkedin.com/in/jean-baptiste-lanvin/", 
    "GitHub": "https://github.com/JiBe-DE"
}

education = [
    {"Data Engineer Diploma" : {
            "School" : "DataScientest - Mines Paris Tech PSL",
            "Speciality" : "Data Engineering",
            "Localisation" : "Paris - France",
            "Interval" : "Aug 2022 - Dec 2022",
            "Description" : '''> 350 hours classes : Programing, Machine Learning, DataBases, Big Data, Streaming, Automatisation & Déployment (DevOps)
            > 50h of project : development of a CryptoBot App for predictive analysis of cryptocurrency prices
            - Data audit and exploration via API Binance
            - Data acquisition, pre-processing and storage, of historical data with SQL and streaming data with MongoDB - ETL pipeline
            - API development, versioning with GitHub & deployment with Docker
            - LSTM time series model training
            '''
        }
    },
    {"Mastère" : {
            "School" : "ISAE - SupAero",
            "Speciality" : "Space Communication Systems",
            "Localisation" : "Toulouse - France",
            "Interval" : "Sept 2015 - Oct 2016",
            "Description" : '''Training courses in Space Communication Systems in partnership with ISAE-Supaero, Telecom Bretagne, Telecom Sud-Paris et ENSEEIHT. The totality of the courses have been followed in english.
                                > Signal processing
                                > Orbital mechanic, Navigation & Positioning
                                > Link Budget, Propagations et Radio-Link frequencies
                                > Embedded systems
                                > project : receive and decode NOAA weather images with LabView
                            '''
        }
    },
    {"Erasmus" : {
            "School" : "Dublin City University",
            "Speciality" : "Software/Computing Engineering",
            "Localisation" : "Dublin - Ireland",
            "Interval" : "Sept 2015 - Oct 2016",
            "Description" : '''English immersion for a 6 months erasmus.
                                > Cloud computing
                                > Signal processing
                                > Web development
                            '''
        }
    },
    {"Engineer Diploma" : {
            "School" : "ENSEEIHT",
            "Speciality" : "Telecomunication & Networks",
            "Localisation" : "Toulouse - France",
            "Interval" : "Sept 2013 - Oct 2016",
            "Description" : '''Engineer diploma with a specialization in Telecomunication & Networks
                                    > IP networks / TCP/IP protocols
                                    > Objet Oriented Programing (Java) / C++
                                    > Signal processing
                                    > Project management
                            '''
        } 
    }
]

experiences = [
    {"Satcom System Engineer" : {
            "Company" : "Astek Industry - Consulting at Dassault Aviation",
            "Speciality" : "Embedded Systems / System Engineering / Satcom",
            "Localisation" : "Paris - France",
            "Interval" : "Oct 2019 - Jul 2022",
            "Description" : '''> Integration of a SATCOM system on board of military aircraft Rafale F4-2 : 
                            - COTS equipment integration
                            - Project management (JIRA)
                            - Functional specification writing (DOORS) 
                            - Functional modelization (PLM / 3DX) 
                            - Tests planning & test bench set-up - Embedded software (C)
                            > Pre-project analysis for Rafale F5 communication
                            > SatCom System integration on AVSIMAR
                            '''
        }
    },
    {"Co-Founder Clock Work S.A.R.L" : {
            "Company" : "Clock Work S.A.R.L.",
            "Speciality" : "Web development / SEO / Customer Relationship",
            "Localisation" : "Nice - France",
            "Interval" : "May 2017 - Jul 2019",
            "Description" : '''Web agency which links freelance workers with clients in order to fulfill web projects : SEO/SEA, web development, web design.
                            > Project management
                            > Editing quotations and invoices
                            > Client relationship
                            > HTML / CSS
                            > Javascript
                            '''
        }
    },
    {"Final year intership - System Engineer" : {
            "Company" : "Thales Alenia Space",
            "Speciality" : "System Engineer / IP Network",
            "Localisation" : "Toulouse - France",
            "Interval" : "Apr 2016 - Nov 2016",
            "Description" : '''Definition & Validation of a Multilink concept for Command and Control (C2) of drones (UAs). Among the Thales Alenia Space Navigation team, I worked with a team of 4 people on this project.
                                > Network architecture
                                > IP mobility protocols
                                > IPv6
                                > VMware
                                > C/C++
                            '''
        }
    }
]

soft_skills = ["Autonomous", "Collaborative", "Problem solving", "Adaptable", "Proactive"]

hard_skills = {
    "Computing" : ["Python (numpy, pandas)", "C++", "Bash", "Linux"],
    "Databases" : ["SQL", "MongoDB", "Neo4j", "ElasticSearch"],
    "API" : ["FastAPI", "Flask"],
    "Deployment" : ["Docker", "Kubernetes", "GitHub"],
    "Machine Learning" : ["Scikit-learn"],
    "Big Data" : ["Hadoop", "Hive", "Spark"],
    "Streaming" : ["Kafka", "SparkStreaming"],
    "Data Visualization" : ["Matplotlib", "Plotly", "Dash"]
}

languages  = {
    "French" : "Native",
    "English" : "Professionnal - C1"
}


# Tags 
api_tags = [
    {'name' : 'Presentation', 'description' : 'Requests to get my presentation information'},
    {'name' : 'Experiences', 'description' : 'Requests to learn about my professionnal experiences'},
    {'name' : 'Education', 'description' : 'Requests to learn about my education'},
    {'name' : 'Contact', 'description' : 'Requests to get my contact details'},
    {'name' : 'Skills', 'description' : 'Requests to get my skills'}
]


app = FastAPI(title = 'Jean-Baptiste Lanvin Resume', description = 'Here is my interactive resume. The purpose of this resume is to show my proficiency in developing functional API with FastAPI.', openapi_tags = api_tags, version = "1.0")

@app.get("/id", name = "ID", tags = ['Presentation'])
async def get_id():
    '''Return my ID
    '''
    return presentation["Fullname"]

@app.get("/pitch", name = "Presentation pitch", tags = ['Presentation'])
async def get_presentation_pitch():
    '''Return my presentation pitch
    '''
    return presentation["Pitch"]

@app.get("/experiences", name = "Full experiences path", tags = ['Experiences'])
async def get_full_experiences():
    '''Return my full experiences path
    '''
    return experiences

@app.get("/experiences/last", name = "Last experience", tags = ['Experiences'])
async def get_last_experiences():
    '''Return my last experience
    '''
    return experiences[0]

@app.get("/education", name = "Full education path", tags = ['Education'])
async def get_full_education():
    '''Return my full education path
    '''
    return education

@app.get("/education/last", name = "Last education", tags = ['Education'])
async def get_last_education():
    '''Return my last education 
    '''
    return education[0]

@app.get("/skills", name = "Full skills", tags = ['Skills'])
async def get_full_skills():
    '''Return my full skills : hard skills & soft skills
    '''
    hard_skills["soft_skills"] = soft_skills
    return hard_skills

@app.get("/skills/soft", name = "Soft skills", tags = ['Skills'])
async def get_soft_skills():
    '''Return my soft skills
    '''
    return soft_skills

@app.get("/skills/hard", name = "Hard skills", tags = ['Skills'])
async def get_soft_skills():
    '''Return my hard skills
    '''
    return hard_skills

@app.get("/skills/languages", name = "Languages", tags = ['Skills'])
async def get_languages():
    '''Return my spoken languages
    '''
    return languages


@app.get("/contact", name = "Contact details", tags = ['Contact'])
async def get_contact_details():
    '''Return the following contact details \n
        • Mail \n
        • Phone number \n
        • LinkedIn link \n
        • GitHub link \n
    '''
    return contact

@app.get("/contact/mail", name = "Mail", tags = ['Contact'])
async def get_mail():
    '''Return the mail adress
    '''
    return contact["Mail"]

@app.get("/contact/phone", name = "Phone", tags = ['Contact'])
async def get_phone_number():
    '''Return the phone number
    '''
    return contact["Phone"]

@app.get("/contact/linkedin", name = "LinkedIn", tags = ['Contact'])
async def get_linkedin():
    '''Return the LinkedIn link
    '''
    return contact["LinkedIn"]

@app.get("/contact/github", name = "GitHub", tags = ['Contact'])
async def get_github():
    '''Return the GitHub link
    '''
    return contact["GitHub"]