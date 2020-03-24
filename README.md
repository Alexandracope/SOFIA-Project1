# Dr Martens App

## Index
[Brief](#brief)
   * [Solution](#solution)
   
[Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)
   * [CI Pipeline](#CI)

     
[Deployment](#depl)
   * [Technologies Used](#tech)
     

[Improvements for the Future](#improve)

[Authors](#auth)


<a name="brief"></a>
## The Brief

To create a Flask-App using CRUD which must contain at least 2 fully functioning tables. Throughout the project we must show and utilise the skills and methodologies that we have learned across the first 5 weeks of the course. 

<a name="solution"></a>
### Solution

I decided to create a Dr Marten application allowing users to create there own online collection storing the pairs they own, while also being able to look at and find the names of new pairs they may want to buy. As well as being able to create their own collection they will be able to update it and delete it if needed. 

<a name="architecture"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagrams
![ERD](/Documentation/initialERD.jpg)

My plans for my ERD consisted of 4 tables. As I had chosen to display a many to many relationship I needed a middle table to ensure the relationship between my other tables worked correctly.

<a name="mla"></a>
### CI Pipeline
![CI](/Documentation/CIpipeline.jpg)

<a name="Risk"></a>
## Risk Assessment

Throughout this process I was keeping up a risk assessment of all the different elements that could go wrong and what I would do to ensure that the risk of this remains low. 

<a name="tech"></a>
### Technologies Used

* GCP - Database
* Python - Logic
* Jenkins - CI Server
* Github - Version control
* Gunicorn - Testing and deployment
* [Trello](https://trello.com/b/j2Wp9Wsz/sofia-project-1) - Project Tracking

<a name="improve"></a>
## Improvements for the Future

At the moment each user can only have 1 collection which they can update and delete. However, I would like to add the ability to have more than one collection for each user. I also think that it would be better for the information displayed on my homepage to have images attached to it, which can then also link to the collections page to show the images of their collected shoes too. 

If I could do this project again I would definitly manage my time alot better giving me a good amount of time to fix the bugs encountered in the correct way and being able to seek help. 

<a name="auth"></a>
## Authors

Alexandra Cope




