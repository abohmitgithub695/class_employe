from ast import Delete, operator
import datetime
from pickle import TRUE
from unicodedata import name
import operator
class Employee:
    def __init__(self):
        #The first and second Employees will be create dynamic if the program run. 
        self.dic_of_employee=[{'ID':1,'name':'Salm','joiningdate':datetime.date(2019,6,12),'salary':2000},
                       {'ID':2,'name':'Abdo','joiningdate':datetime.date(2016,8,20),'salary':3500}]     
        #this is a range to enter a year of joining  of employee ,the year must enter  from range this dic
        self.range_of_year=range(2000,2022)
        #this is a range to enter a month of joiningdate  of employee ,the month must enter  from range this dic
        self.range_of_month=range(1,13)
        #this is a range to enter a day of joining  of employee ,the day must enter  from range this dic
        self.range_of_day=range(1,31)
#...Now Function_to_Create_Emp...
    def create_emp(self):
          while True:
                try:
                        number=int(input("Enter the num of epmloyee you need to greate:  "))
                        id_num=3
                        for n in range(number):
                              print("...The ID num was entered dynamic...Equal: "+str(id_num))
                              name= input("Enter  emp_name\n").strip().capitalize()
                              year_of_joiningdate=int(input("Enter year of joiningdate: "))
                              for n in self.range_of_year:
                               while year_of_joiningdate not in self.range_of_year:
                                  year_of_joiningdate=int(input("Try again...enter year of joiningdate the year must be from(2000) to (2021) "))
                              month_of_joiningdate=int(input("Enter month of joiningdate: "))
                              for n in self.range_of_month:
                                while month_of_joiningdate not in self.range_of_month:
                                  month_of_joiningdate=int(input("Try again...enter month of joiningdate the month must be from(1) to (12) "))

                              day_of_joiningdate=int(input("Enter day of joiningdate: " ))
                              for n in self.range_of_day:
                                while day_of_joiningdate not in self.range_of_day:
                                  day_of_joiningdate=int(input("Try again...enter day of joiningdate the day must be from(1) to (30) " ))

                              joiningdate=datetime.date(year_of_joiningdate,month_of_joiningdate,day_of_joiningdate)
                              salary=int(input("Enter emp salary: "))
                   
                              create_emp={'ID':id_num,'name':name,'joiningdate':joiningdate,'salary':salary}
                              self.dic_of_employee.append(create_emp)
                              id_num=id_num+1
                        break     
                except:
                 print("...Inpute erorr...Try again...")
          call_up.save_emp(id_num) 
          
#...Now Function_to_Save_emp...
    def save_emp(self,id_num):
          while True:
                try:
                  create=input("Did you need to initiate a new employees enter (yes) OR (no): ").strip().lower()
                  while create !="yes" and create !="no":
                   create=input(" Try again,If you need to initiate a new employee enter (yes) OR (no): ").strip().lower()
                  if create=="yes":
                   for n in range(1):
                    print("...The ID num was entered dynamic...Equal: "+str(id_num))
                    #id_num=id_num+1
                    name = input("Enter  emp_name\n").strip().capitalize()
                    year_of_joiningdate=int(input("Enter year of joiningdate: "))
                    for n in self.range_of_year:
                      while year_of_joiningdate not in self.range_of_year:
                       year_of_joiningdate=int(input("Try again...enter year of joiningdate the year must be from(2000) to (2021) "))
                    month_of_joiningdate=int(input("Enter month of joiningdate: "))
                    for n in self.range_of_month:
                      while month_of_joiningdate not in self.range_of_month:
                       month_of_joiningdate=int(input("Try again...enter month of joiningdate the month must be from(1) to (12) "))
                    day_of_joiningdate=int(input("Enter day of joiningdate: " ))
                    for n in self.range_of_day:
                      while day_of_joiningdate not in self.range_of_day:
                        day_of_joiningdate=int(input("Try again...enter day of joiningdate the day must be from(1) to (30) " ))
                    joiningdate=datetime.date(year_of_joiningdate,month_of_joiningdate,day_of_joiningdate)
                    salary=int(input("Enter emp salary: "))
                    initiate_emp={'ID':id_num,'name':name,'joiningdate':joiningdate,'salary':salary}
                    self.dic_of_employee.append(initiate_emp)
                  break              
                except:
                 print("...Inpute erorr...Try again...")
                 
#...Now Function_to_Update_emp...
    def update_emp(self ):
          while True:
                try:
                  update=input("Did you need update employee enter (yes) OR (no): ").strip().lower()
                  while update !="yes" and update !="no":
                   update=input(" Try again,if you need to update  employee enter (yes) OR (no): ").strip().lower()
                  if update=="yes":
                   upd_emp_id=int(input("Enter the id of employee you need to upadte\n"))
                   for i in range(len(self.dic_of_employee)):
                    if self.dic_of_employee[i]['ID'] == upd_emp_id:
                      print("...The new ID num was entered dynamic...")
                      upd_emp_name=input("Enter a new of the the employee name\n").strip().capitalize()
                      upd_year_of_joiningdate=int(input("Enter a new year of joiningdate: "))
                      for year in self.range_of_year:
                       while upd_year_of_joiningdate not in self.range_of_year:
                        upd_year_of_joiningdate=int(input("The number not in the range you must enter year from (2000) to (2022),enter year of joiningdate again: "))
                      upd_month_of_joiningdate=int(input("Enter a new month of joiningdate: "))
                      for n in self.range_of_month:
                        while upd_month_of_joiningdate not in self.range_of_month:
                         upd_month_of_joiningdate=int(input("Try again...enter month of joiningdate the month must be from(1) to (12) "))
                      upd_day_of_joiningdate=int(input("Enter a new day of joiningdate: " ))
                      for n in self.range_of_day:
                        while upd_day_of_joiningdate not in self.range_of_day:
                          upd_day_of_joiningdate=int(input("Try again...enter day of joiningdate the day must be from(1) to (30) " ))
                      upd_joiningdate=datetime.date(upd_year_of_joiningdate,upd_month_of_joiningdate,upd_day_of_joiningdate)
                      upd_salary=int(input("Enter a new of the salary: "))
                      self.dic_of_employee[i]['name']=upd_emp_name
                      upd_joiningdate=datetime.date(upd_year_of_joiningdate,upd_month_of_joiningdate,upd_day_of_joiningdate)
                      self.dic_of_employee[i]['joiningdate']=upd_joiningdate
                      self.dic_of_employee[i]['salary']=upd_salary
                      break
                    else:
                     print("Employee not found")
                   break
                except:
                     print("...Inpute erorr...Try again...")
                     
#...Now Function_to_Delete_emp...
    def delete(self):
          while TRUE:
                try:
                  delete=input("Did you need Delete employee enter (yes) OR S(NO): ").strip().lower()
                  while delete !="yes" and delete !="no":
                   delete=input(" Try again,if you need to delete  employee enter (yes) OR (no): ").strip().lower()
                  if delete=="yes":
                    de_emp_name=(input("Enter the name of employee you need to delete\n")).strip().capitalize()
                    for n in range( len(self.dic_of_employee)):
                        if self.dic_of_employee[n]['name']==de_emp_name: 
                         del self.dic_of_employee[n]
                         print("\t...You delete employee...")
                         break
                    else:
                        print("Employe not found")
                  break
                except:
                    print("...Inpute erorr...Try again...")

#...Now Function_list_emp...
    def list_emp(self):
          while TRUE:
                try:
                    select=input("Did you need to sort or search enter(yes) or (no): ").strip().lower()
                    while select !="yes" and select!="no":
                      select=input("Try again ,if you need to sort or search enter(yes) or (no): ").strip().lower()
                    if select=='yes':
                     choose=input("...Did you need to sort or search enter(sort) or (search): ").strip().lower()
                     while choose !='sort' and choose !='search':
                        choose=input("Please try again  enter(sort) or (search): ").strip().lower()
                     if choose=='search':
                        choose=input("Did you want to search by (ID) or (Name) ,enter (id) or (name) ").strip().lower()
                        while choose!="id" and choose!="name":
                          choose=input("Please try again enter (id) or (name): ").strip().lower()
                        if choose=="name":
                         search_name=input("Enter the name of employee you need to search\n").strip().capitalize()
                         for n in range( len(self.dic_of_employee)):
                          if self.dic_of_employee[n]['name']==search_name: 
                           print(self.dic_of_employee[n])
                           break
                         else:
                           print("Employe not found")
                           break
                        if choose=="id":
                         search_id=int(input("Enter the id of employee you need to search\n"))
                         for n in range( len(self.dic_of_employee)):
                          if self.dic_of_employee[n]['ID']==search_id: 
                           print(self.dic_of_employee[n])
                           break
                         else:
                              print("Employee not found")
                              break
                     if choose=="sort":
                         sort=input(" Enter the way you want to sort (name) or (ID) or (joiningdate) or (salary): ").strip().lower()
                         while sort!='name' and sort!='id' and sort!='joiningdate' and sort!='salary':
                              sort=input(" Please try again enter (name) or (id) or (joiningdate) or (salary): ").strip().lower()
                         if sort=='name':
                                      self.dic_of_employee.sort(key=operator.itemgetter('name'))
                                      print(self.dic_of_employee)
                         if  sort=='id':
                                      self.dic_of_employee.sort(key=operator.itemgetter('ID'))
                                      print(self.dic_of_employee)
                         if sort=='joiningdate':
                                      self.dic_of_employee.sort(key=operator.itemgetter('joiningdate'))
                                      print(self.dic_of_employee)
                         if sort=='salary':
                                      self.dic_of_employee.sort(key=operator.itemgetter('salary'))
                                      print(self.dic_of_employee)
                    break
                except:
                    print("...Inpute erorr...Try again...")
                                           
    #...Function_show_employees_report...   
    def emp_report(self):
      ask=input("Did you need to show employees report enter(yes) or (no): ").strip().lower()
      while ask !="yes" and ask!="no":
            ask=input("Try again ,if you need to show employees report enter(yes) or (no): ").strip().lower()
      if ask=='yes':              
       print("\n\t\t\t....Now_employees_report....\n")
       for n in self.dic_of_employee:
                   print(n)

         
call_up=Employee()       
call_up.create_emp()
call_up.update_emp()
call_up.delete()
call_up.list_emp()
call_up.emp_report()