import textwrap
from template import Template

new_resume = Template()
margin = new_resume.add_vertical_line(side='left')

# HEADER
new_resume.add_text_box(text = "Henrique Santana",
                    xy = (0.05 + margin, 
                          0.95),
                    size = 20,
                    weight = 'bold'
)

new_resume.add_text_box(text = "Software Development, Machine Learning & Data Engineering",
                    xy = (0.05 + margin, 
                          0.925),
                    size = 10,
                    weight = 'regular',
                    color = '#BCBCBC'
)

# PERSONAL
new_resume.add_text_box(text = "# PERSONAL",
                    xy = (0.03, 
                          0.95),
                    size = 10,
                    weight = 'bold',
                    color='#FFFFFF'
)

topics = [
    "- Henrique de Souza Santana",
    "- lives in São Paulo - Brazil",
    "- mail: henrique07santana@hotmail.com",
    r"- linkedin.com/in/henrique07santana",
    r"- github.com/santana-ai",
]

new_resume.add_text_box(text = '  \n\n'.join(topics),
                    xy = (0.03, 
                          0.83),
                    size = 7,
                    weight = 'regular',
                    color = '#FFFFFF',
)

# CODE EXPERIENCE
new_resume.add_text_box(text = "# CODE EXPERIENCE",
                    xy = (0.03, 
                          0.75),
                    size = 10,
                    weight = 'bold',
                    color='#FFFFFF'
)

topics = [
    "- Python",
    "- R",
    "- SQL",
    "- Go",
    "- Javascript",  
]

new_resume.add_text_box(text = '  \n\n'.join(topics),
                    xy = (0.03, 
                          0.63),
                    size = 7,
                    weight = 'regular',
                    color = '#FFFFFF',
)

# TOOLS
new_resume.add_text_box(text = "# TOOLS",
                    xy = (0.03, 
                          0.55),
                    size = 10,
                    weight = 'bold',
                    color='#FFFFFF'
)

topics = [
    "- GCP, AWS, Azure, K8s, Docker, Git",
    "- Postgres, MongoDB, Dynamo, Neo4j",
    "- S3, Redshift, Airflow, Databricks",
    "- Matplotlib, Pandas, Numpy, PySpark",
    "- Scikit-learn, Keras, Tensorflow",
]

new_resume.add_text_box(text = '  \n\n'.join(topics),
                    xy = (0.03, 
                          0.43),
                    size = 7,
                    weight = 'regular',
                    color = '#FFFFFF',
)

# HIGHLIGHTS
new_resume.add_text_box(text = "self.highlights()",
                    xy = (0.05 + margin, 
                          0.86),
                    size = 14,
                    weight = 'bold',
                    color='#258432'
)

topics = [
    " - As a Lead Data Expert, I teach Data Science and Analytics at Tera (a brazilian Edtech).",
    " - I created Pysquale, a public Python lib (beta) for NLP in Portuguese.",
    " - This resumé was created by me with Python code using just matplotlib. :D"
]

new_resume.add_text_box(text = '  \n\n'.join(topics),
                    xy = (0.05 + margin, 
                          0.76),
                    size = 9,
                    weight = 'regular',
)

# EXPERIENCE
new_resume.add_text_box(text = "self.experience()",
                    xy = (0.05 + margin, 
                          0.70),
                    size = 14,
                    weight = 'bold',
                    color='#258432'
)

explanation = """ Former Electronics Engineering professional, I decided to change my career in 2014 
after taking a Machine Learning class in the University. At that time I had already finished Coursera's 
Machine Learning course by Andrew Ng. After building small projects using open source data, I worked 
for two fintech startup companies as a Data Scientist. That experience opened the door at Yellow, a bike 
sharing company. I led part of the tech team building digital wallet as Head of Payments. In 2020, I 
started a new challenge at Loft, a proptech startup. During 1 year of experience I led some Supply Operations 
and then I contributed as a Product Manager. At Dell I had a big technical challenge: coordenating multiple 
teams around the world in order to leverage MLOps culture for Data Science models. The BHAG was to create a 
realiable Machine  Learning platform. Currently I am the head of Data and ML at cloud humans, a startup that 
helps companies to  give the best experience to their customers. We use text analytics / NLP to solve complex 
problems."""

topics = textwrap.wrap(text=explanation, width=86)  
new_resume.add_text_box(text = '\n\n '.join(topics),
                    xy = (0.05 + margin, 
                          0.30),
                    size = 9,
                    weight = 'regular',
                    wrap=True,
)

# EDUCATION
new_resume.add_text_box(text = "self.education()",
                    xy = (0.05 + margin, 
                          0.24),
                    size = 14,
                    weight = 'bold',
                    color='#258432'
)

topics = [
    "- Artificial Intelligence Specialization – PUC [2022]",
    "- Systems Analysis and Development – UVA [2020]",
    "- Electrical Engineering - Electronics Systems – UERJ [2019]",
    "- Eelctromechanical Technician (Tech High School) – CEFET/RJ [2010]",
]

new_resume.add_text_box(text = '  \n\n'.join(topics),
                    xy = (0.05 + margin, 
                          0.11),
                    size = 9,
                    weight = 'regular',
)

# GENERATE PDF
new_resume.save(file_name='my-resume.pdf')
