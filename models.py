#!/usr/bin/env python3


from calendar import month
from typing import List
from datetime import datetime

#Global variables for application
MonthList: List[str] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
StateList: List[str] = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV","WI","WY"]   
CurrentYear: int = datetime.now().year
ThreeLetterMonthList: List[str] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

class Resume:

    def __init__(self): 
        self.WorkExpCounter = 0
        self.Summary: str
        self.header_work_experience = "WORK EXPERIENCE"
        self.header_projects = "PROJECTS"
        self.header_skills = "SKILLS"
        self.header_education = "EDUCATION"
        self.header_certifications = "CERTIFICATIONS"
        self.category_list = []
        self.is_categorized=None

    class Title:

            def __init__(self):
                    self.title=None     

    class Work_Experience:

            def __init__(self):
                    self.company=None
                    self.startmonth=None
                    self.startyear=None
                    self.endmonth=None
                    self.endyear=None
                    self.wetitle=None
                    self.bulletstatements = []
                    self.bulletcounter = 0
                    self.bulletlimit = 5
                    self.present = None
                    self.loc_city = None
                    self.loc_state = None

            def WkExpCountAdd(self):
                    self.WorkExpCounter += 1
                    return self.WorkExpCounter
            
            def company_name(self, companyname: str):
                    self.company=companyname

            def add_bullet(self, bulletentry: "Resume.Bullet"):
                    self.bulletstatements.append(bulletentry)

            def remove_bullet(self, bulletentry: "Resume.Bullet"):
                    self.bulletstatements.remove(bulletentry)

            def list_bullets(self):
                    return [c.entry for c in self.bulletstatements]

            def increment_bulletcounter(self):
                    if self.bulletcounter < self.bulletlimit:
                        self.bulletcounter += 1
                    else:
                        print("Bullet counter has reached the limit. Increase bullet limit before you add another.")

            def decrement_bulletcounter(self):
                    if self.bulletcounter > 0:
                        self.bulletcounter -= 1
                    else:
                        print("Bullet counter is already at zero. Cannot decrement further.")

            def bullet_count(self):
                    return self.bulletcounter

            def bullet_limit(self, limit: int):
                    if limit < self.bullet_count():
                        print("New bullet limit is less than the current bullet count. Remove bullets before reducing the limit.")
                    elif limit < 0:
                        print("Bullet limit cannot be negative.")   
                    elif limit > 10:
                        print("Bullet limit cannot exceed 10.")
                    else:
                        self.bulletlimit = limit

            def set_start_date(self, month: str, year: int, preferred_format: str):
                    if preferred_format == "3-Letter":
                        if month in ThreeLetterMonthList and month:
                            self.startmonth = month
                        else:
                            print("Invalid month. Please provide a valid 3-letter month.")
                    else:
                        if month in MonthList and month:
                            self.startmonth = month
                    if year >= CurrentYear - 70 and year <= CurrentYear:
                        self.startyear = year 
                    else:
                        print("Invalid year. Please provide a year between 2000 and the current year.")

            def set_end_date(self, month: str, year: int, preferred_format: str):
                    self.present = False
                    if preferred_format == "3-Letter":
                        if month in ThreeLetterMonthList and month:
                            self.endmonth = month
                        else:
                            print("Invalid month. Please provide a valid 3-letter month.")
                    else:
                        if month in MonthList and month:
                            self.endmonth = month
                    if year >= CurrentYear - 70 and year <= CurrentYear:
                        self.endyear = year 
                    else:
                        print("Invalid year. Please provide a year between 2000 and the current year.")

            def set_location(self, city: str, state: str):
                    self.loc_city = city
                    self.loc_state = state

            def print_work_experience(self):
                    print(f"Company: {self.company}")
                    print(f"Title: {self.wetitle}")
                    print("Bullet Statements:")
                    for bullet in self.bulletstatements:
                        print(f"- {bullet.entry}")
                    print(f"Start Date: {self.startmonth} {self.startyear}")
                    if not self.present:
                        print(f"End Date: {self.endmonth} {self.endyear}")
                    else:
                        print("Present")

    class Bullet:
        
            def __init__(self):
                self.entry=None

    class Contact_Info:

            def __init__(self):
                    self.email=None
                    self.city=None
                    self.state=None
                    self.linkedin=None
                    self.phone=None

            def set_contact_info(self, email: str, city: str, state: str, linkedin: str):
                    self.email=email
                    self.city=city
                    self.state=state
                    self.linkedin=linkedin

            def print_contact_info(self):
                    print(f"Email: {self.email}")
                    print(f"City: {self.city}")
                    print(f"State: {self.state}")
                    print(f"LinkedIn: {self.linkedin}")
                    print(f"Phone: {self.phone}")

            def set_phone(self, phone:str):
                  pass
                    

    class Projects:
        
            def __init__(self):
                    self.project_name=None
                    self.project_description=None
                    self.project_link=None

            def set_project_info(self, name: str, description: str, link: str):
                    self.project_name=name
                    self.project_description=description
                    self.project_link=link

            def print_project_info(self):
                    print(f"Project Name: {self.project_name}")
                    print(f"Description: {self.project_description}")
                    print(f"Link: {self.project_link}")

    class Certifications:
        
            def __init__(self):
                    self.certification_name=None
                    self.certification_issuer=None
                    self.certification_date=None

            def set_certification_info(self, name: str, issuer: str, date: str):
                    self.certification_name=name
                    self.certification_issuer=issuer
                    self.certification_date=date

            def print_certification_info(self):
                    print(f"Certification Name: {self.certification_name}")
                    print(f"Issuer: {self.certification_issuer}")
                    print(f"Date: {self.certification_date}")

    class Categorized_Skills:

            def __init__(self):
                    self.skill_category=None
                    self.skillstring=None
                    self.category_list=[]

            def add_skill_category(self, category:str):
                    self.skill_category=category
                    self.category_list.append(category)

            def get_category_list(self):
                    return self.category_list

            def change_skill_category(self, oldcategory:str, newcategory:str):
                    if oldcategory in self.category_list:
                        index = self.category_list.index(oldcategory)
                        self.category_list[index] = newcategory
                        if self.skill_category == oldcategory:
                            self.skill_category = newcategory
                    else:
                        print(f"Category '{oldcategory}' not found in the list.")

            def set_skill_list(self, skills: str):
                    if self.skillstring is None:
                        self.skill_list = skills.split(',')
                        self.skill_list.sort()
                        self.skillstring = ', '.join(self.skill_list)
                    else:
                        new_skills = skills.split(',')
                        for skill in new_skills:
                            if skill not in self.skill_list:
                                self.skill_list.append(skill)
                        self.skill_list.sort()
                        self.skillstring = ', '.join(self.skill_list)

            def add_single_skill(self, skill: str):
                    if skill not in self.skill_list:
                        self.skill_list.append(skill)
                        self.skill_list.sort()
                        self.skillstring = ', '.join(self.skill_list)
                    else:
                        print(f"Skill '{skill}' already exists in the list.")

            def check_skill_input(self, skill: str):
                    if len(skill.split(',')) == 1:
                        self.add_single_skill(skill)
                    elif len(skill.split(',')) > 1:
                        self.set_skill_list(skill)
                    else:
                            print("Invalid skill input. Please provide a valid skill or a comma-separated list of skills.")

            def print_skills(self):
                    print(f"Skill Category: {self.skill_category}")
                    print(f"Skills: {self.skillstring}")

    class Skills:

            def __init__(self):
                    self.skill_list=[]

#Testing the Work_Experience class
#Work_Experience1 = Work_Experience()
#Work_Experience1.company_name("Sample Company")
#Bullet1 = Bullet()
#Bullet1.entry = "This is a sample bullet."
#Bullet2 = Bullet()
#Bullet2.entry = "This is another sample bullet."
#Work_Experience1.add_bullet(Bullet1)
#Work_Experience1.add_bullet(Bullet2)
#Work_Experience1.print_work_experience()