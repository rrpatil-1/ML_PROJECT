# Student Exam Performance Prediction End to End Flask Application with AWS Deployment
The dataset used in this project contains information about students' demographics, parental education, lunch type, test preparation course, and their corresponding math scores. By analyzing this data, we aim to build a machine learning model that can predict student performance accurately. This tool can help identify students who may need additional support and tailor educational strategies accordingly.


![image](https://raw.githubusercontent.com/rrpatil-1/ML_PROJECT/main/templates/homepage.jpg)
##Getting Started
### Prerequisites
- python 3.8

### Installation
    
    1. pip install -r requirements.txt

### Project Structure

-------------------------------------------------------- 
📂 your_repo_name
- 📂 .ebextension
  - ⚙ python.config
         
        This will contain app deployment configuration for AWS elasticBenstalk.

- 📂 notebook
  - 📂 data
    - 📄 Stud.csv 
      
          This  contain raw data

  - 📄 EDA STUDENT PERFORMANCE .ipynb
  - 📄 MODEL TRAINING.ipynb
 - 📂 src
   - 📂 components
     - 📄 \___init___.py
     - 📄 data_ingestion.py
     - 📄 data_transformation.py
     - 📄 model_trainer.py
   - 📂 pipeline
     - 📄 \___init___.py
     - 📄 predict_pipeline.py
   - 📄 exception.py
   - 📄 logger.py
   - 📄 utils.py
- 📂 templates
   - 📄 index.html
   - 📄 home.html
   - 📄 Student.png
    
- 📄 application.py
               
      This is Flask application file make sure name is correct "application.py" not the app.py when deploy on elasticbenstalk.
- requirements.txt

# Deployment on AWS Elastic Beanstalk
1. Create account on AWS [watch video](https://www.youtube.com/watch?v=xi-JDeceLeI).
2. Create IAM role and assign the following policies.
   - AWSElasticBeanstalkWebTier
   - AWSElasticBeanstalkWorkerTier
   - AWSElasticBeanstalkMulticontainerDocker
    
3. Follow the step given in this link [step to create environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.CreateApp.html).
4. connect git hub with aws using codepipeline [codepipeline](https://www.youtube.com/watch?v=4tDjVFbi31o)
5. Documents for codepipeline [doc](https://aws.amazon.com/getting-started/hands-on/continuous-deployment-pipeline/)

# How to get prediction result 
You can access the result from web app by filling the form and result will display on page itself
## Response Using API endpoint
1. Download the postman application to test the api [postman](https://www.postman.com/downloads/)
2. alternate option is to visit the [reqbin](https://reqbin.com/) to test api online

# API Details
    endpoint: /predictscore
    methode: POST
    body=
        {"gender":"female",
        "race_ethnicity":"group A",
        "parental_level_of_education":"associate's degree",
        "lunch":"standard",
        "test_preparation_course":"completed",
        "reading_score":45.0,
        "writing_score":43.0}

## Field Documentation
<table>
<tr>
<th>Field</th>
<th>value</th>
<th>datatype</th>
</tr>
<tr>
<td>gender</td>
<td>male/female</td>
<td>string</td>
</tr>
<tr>
<td>race_ethnicity</td>
<td>group B,group C, group A, group D, group E</td>
<td>string</td>
</tr>
<tr>
<td>parental_level_of_education</td>
<td>bachelor's degree, some college,  master's degree, associate's degree, high school, some high school</td>
<td>string</td>
<tr>
<td>lunch</td>
<td>"standard" or "free/reduced"</td>
<td>string</td>
<tr>
<td>test_preparation_course</td>
<td>'none' or 'completed'</td>
<td>string</td>
</tr>
<tr>
<td>reading_score</td>
<td>0-100</td>
<td>float</td>
</tr>
<tr>
<td>writing_score</td>
<td>0-100</td>
<td>float</td></tr>
</table>

    
### python code for testing api
        import requests

        url="http://127.0.0.1:5000/predictscore"
        
            body={  "gender":"male",
                    "race_ethnicity":"group A",
                    "parental_level_of_education":"associate's degree",
                    "lunch":"standard",
                    "test_preparation_course":"completed",
                    "reading_score":45,
                    "writing_score":43
                }
                res=requests.post(url,json=body)
                print(res.text)
                