'''---------------------------------------------------------------------# COMPUTER SCIENCE PROJECT OF CLASS 12 CBSE --------------------------------------------------------------------------
------------------------------------------------------------------------# PROGRAM MADE BY KAPISH JAIN AND DEV SAHU ---------------------------------------------------------------------------
-----------------------------------------------------------------------------# CLASS- 12th ; SECTION - SCIENCE ---------------------------------------------------------------------------------'''

class bcolors:
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("                               ",f"{bcolors.WARNING}{bcolors.UNDERLINE}{bcolors.PURPLE}WHOLESALE PROGRAM{bcolors.ENDC}")
import mysql.connector
import datetime
import time
import pyttsx3
import matplotlib.pyplot as plt

#GREETING THE USER
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate=engine.getProperty('rate')

engine.setProperty('rate',190)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
    
        speak("Good Morning !")

    elif hour>= 12 and hour<18:
          
        speak("Good Afternoon !")

    else:
        speak("Good Evening !") 

    
    speak("WELCOME TO YOUR WHOLESALE MANAGEMENT PROGRAM !!! ")

Qxr=True        
while Qxr==True: 
    try:
        loc=str(input("Enter the host of your Mysql database: "))
        user1=str(input("Enter the user of your Mysql Database: "))
        passwd=str(input("Enter the password of your Mysql Database: "))   
        mydb=mysql.connector.connect(host=loc,user=user1, password=passwd)
        Qxr=False
        print(f"{bcolors.OKGREEN}YOUR CONNECTION TO DATABASE HAS BEEN SUCCESSFULLY established{bcolors.ENDC}")
        speak("YOUR CONNECTION TO DATABASE HAS BEEN SUCCESSFULLY established")
    except Exception as e:
        print(e)
        print(f"{bcolors.FAIL}YOUR CONNECTION TO DATABASE HAS NOT BEEN established !! please try once again!{bcolors.ENDC}")
        speak("YOUR CONNECTION TO DATABASE HAS NOT BEEN established !! please try once again!")
        Qxr=True
    
wishMe()

def create():

    d=input('ENTER THE NAME OF DATABASE TO BE CREATED : ')
    # CREATING DATABASE
    def create_db():
           
        mycursor = mydb.cursor()
        try:
            sqll="CREATE DATABASE %s"%(d)
            mycursor.execute(sqll)
            d1=(d,)
            mycursor1=mydb.cursor()
            mycursor1.execute("SHOW DATABASES")
            for i in mycursor1:
                if i==d1:
                    sp="YOUR DATABASE",d,"HAS BEEN SUCCESSFULLY CREATED"
                    speak(sp)
                    print(f"{bcolors.OKGREEN}YOUR DATABASE HAS BEEN SUCCESSFULLY CREATED{bcolors.ENDC}")
        except Exception as e:
            print(e)
            speak("YOUR DATABASE HAS NOT BEEN CREATED !!!")
            print(f"{bcolors.FAIL}YOUR DATABASE HAS NOT BEEN CREATED !!!{bcolors.ENDC}")
            speak("PLEASE TRY AGAIN")
            create()
        #RUNNING DATABASE
        mycursor4 = mydb.cursor()
        sql1="USE %s"%(d)
        mycursor4.execute(sql1)
    create_db()
def cre_table():
    #CREATING TABLE
    tb=input("Enter the name of table: ")
    def table():   
        try:    
            mycursor3=mydb.cursor()
            sql2="""CREATE TABLE %s (kapj VARCHAR(20))"""%(tb)
            mycursor3.execute(sql2)        
            #TO CHECK IF TABLE IS CREATED
            j1=(tb,)
            mycursor5=mydb.cursor()
            sql3="SHOW TABLES"
            mycursor5.execute(sql3)
            for j in mycursor5:
                if j==j1:
                    sp1="Your table ",tb," HAS BEEN SUCCESSFULLY CREATED"
                    speak(sp1)
                    print(f"{bcolors.OKGREEN}{sp1}{bcolors.ENDC}")   
        except Exception as e:
            print(e)
            speak(e)
            cre_table
    table()
    
    

    # CREATING COLUMN FROM USER INPUT
    def add_column():
        try:  
            n=int(input("ENTER THE NO. OF COLUMNS REQUIRED: "))
            h=0
            b=0
            for i in range(n):
                try:
                    def EXP(x,y):
                        mycursor6=mydb.cursor()
                        sql4="ALTER TABLE %s ADD %s %s"%(tb,x,y)
                        mycursor6.execute(sql4)       
                    print("Enter the name of column",h+1,':')
                    col=input("enter: ")
                    print("NEXT STEP IS TO ENTER DATA TYPE AND ITS SIZE \n For example: \nVARCHAR(573), OR \nINT(25) OR, \nFLOAT(56) \n")
                    data_type=input("ENTER THE DATA TYPE AND LENGTH OF THE DATA TYPE (ALL IN CAPITAL): ")
                    EXP(col,data_type)
                    b=b+1
                    h=h+1    
                except Exception as E:
                    print(f"{bcolors.FAIL}Error:{bcolors.ENDC}",E)
                    speak(E)
                    for h1 in range(b,n):
                        print("Enter the name of column",h+1,':')
                        col=input("enter: ")
                        print("NEXT STEP IS TO ENTER DATA TYPE AND ITS SIZE \n For example: \nVARCHAR(573), OR \nINT(25) OR, \nFLOAT(56) \n")
                        data_type=input("ENTER THE DATA TYPE AND LENGTH OF THE DATA TYPE (ALL IN CAPITAL): ")
                        EXP(col,data_type)
                        h=h+1  
                      
            mycursor7=mydb.cursor()
            sql5="ALTER TABLE %s DROP COLUMN kapj"%(tb)
            mycursor7.execute(sql5)
            
            # CHECKING THE STRUCTURE OF TABLE
            
            mycursor7=mydb.cursor()
            sql6="DESCRIBE %s"%(tb)
            mycursor7.execute(sql6)
            stru=mycursor7.fetchall()
            for st in stru:
                print(f"{bcolors.WARNING}{st}{bcolors.ENDC}")            
            
        except Exception as e:
            print(e)
            speak(e)
            add_column()
        
        
        def insert():
            lo=[]
            for i1 in range(n):
                print(f"{bcolors.WARNING}ENTER THE DATA OF CHAR AND VARCHAR TYPE IN QUOTATION{bcolors.ENDC}")
                print("ENTER THE VALUE TO BE INSERTED IN COLUMN ",i1+1)
                data23=input("ENTER: ")
                # data24=eval(data23)
                lo.append(data23)
            y=tuple(lo)
            bp=0
            try:
                mycursor8=mydb.cursor()
                sql7="INSERT INTO {} VALUES {}".format(tb,y)
                mycursor8.execute(sql7)
                mydb.commit()
                bp=bp+1
            except Exception as e:
                print(e)
                speak("please try again!")
                print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}please try again!{bcolors.ENDC}")
                insert()
            z=input("Do you want to add more data (y/n) : ")
            def wa_run1():    
                if z=='Y' or z=='y':                                    
                    insert()      
                elif z=='N' or z=='n':                
                    print(f"{bcolors.OKGREEN}Data has been SUCCESSFULLY added{bcolors.ENDC}")
                    speak("Data has been SUCCESSFULLY added")
                elif z!='Y' or z!='y' or z!='n' or z!='N':
                    print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                    wa_run1()
            wa_run1()
        
        insert()
        

        def view_enterdata():
        
            mycursor119=mydb.cursor()
            sql115="SELECT * FROM {}".format(tb)
            mycursor119.execute(sql115) 
            data6=mycursor119.fetchall()
            for st1 in data6:
                print(f"{bcolors.WARNING}{st1}{bcolors.ENDC}")
        view_enterdata()
    add_column()    
def sequence():
    create()
    cre_table()
    options()
#--------------------------------------PART 2--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------MODIFYING------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
def using_data():
    D=input("enter the database to be modified: ")
    def run():
        try:
            mycursor4 = mydb.cursor()
            sql1="USE %s"%(D)
            mycursor4.execute(sql1)
        except Exception as e:
            print(f"{bcolors.FAIL}{bcolors.BOLD}{e}{bcolors.ENDC}")
            speak(e)
            using_data()
    g=run()
    def val_update():
        try:
            table=input("ENTER THE NAME OF TABLE TO BE MODIFIED OR USED: ")
            up_col=input("Enter the name of column to be updated:")
            new_val=input("Enter the new value to be updated in the column: ")
            cond1=input("ENTER THE CONDITION : ")
            mycursor8 = mydb.cursor()
            sql7="UPDATE {} SET {} = {} WHERE {}".format(table,up_col,new_val,cond1)
            mycursor8.execute(sql7)
            mydb.commit()
            speak("YOUR VALUE HAS BEEN SUCCESSFULLY UPDATED")
        except Exception as e:
            print(e)
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLEASE TRY AGAIN{bcolors.ENDC}")
            speak(e)
            val_update()
        def wa_run():
            z=input("Do you want to continue (y/n) : ")
            if z=='Y' or z=='y':                                    
                val_update()              
            elif z=='N' or z=='n':
                None
            elif z !='y'or z !='Y' or z !='n' or z!="N":
                print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                wa_run()
        wa_run()
    def datatype_update():
        try:
            table=input("ENTER THE NAME OF TABLE TO BE MODIFIED OR USED: ")
            mycursor9 = mydb.cursor()
            up_col=input("Enter the name of column to be whose datatype has to be modified: ")
            n_datatype=input("ENTER THE NEW DATATYPE TO BE MODIFIED IN COLUMN: ")
            sql8="ALTER TABLE {} MODIFY COLUMN {} {}".format(table,up_col,n_datatype)
            mycursor9.execute(sql8)
            mydb.commit()
            speak("your datatype is SUCCESSFULLY updated")
            print(f"{bcolors.OKGREEN}your datatype is SUCCESSFULLY updated{bcolors.ENDC}")
        except Exception as e:
            print(e)
            speak(e)
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLEASE TRY AGAIN{bcolors.ENDC}")
            datatype_update()  
        def wa_run():
            z=input("Do you want to continue (y/n) : ")
            if z=='Y' or z=='y':                                    
                datatype_update()             
            elif z=='N' or z=='n':
                None
            elif z !='y'or z !='Y' or z !='n' or z!="N":
                print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                wa_run()
        wa_run()
    def add_col1():
        try:
            table=input("ENTER THE NAME OF TABLE TO BE MODIFIED OR USED: ")
            inp=input("ENTER THE COLUMN TO BE ADDED: ")
            dat_typ=input("ENTER THE DATA TYPE AND LENGTH OF THE DATA TYPE (ALL IN CAPITAL): ")
            mycursor10 = mydb.cursor()
            sql9="ALTER TABLE {} ADD {} {}".format(table,inp,dat_typ)
            mycursor10.execute(sql9)
            mydb.commit()
            speak("your coloumn is SUCCESSFULLY added")
        except Exception as e:
            print(e)
            speak(e)
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLEASE TRY AGAIN{bcolors.ENDC}")
            add_col1()
        def wa_run():
            z=input("Do you want to continue (y/n) : ")
            if z=='Y' or z=='y':                                    
                add_col1()               
            elif z=='N' or z=='n':
                None
                print(f"{bcolors.OKGREEN}Data has been SUCCESSFULLY added{bcolors.ENDC}")
                speak("Data has been SUCCESSFULLY added")
            elif z !='y'or z !='Y' or z !='n' or z!="N":
                print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                wa_run()
        wa_run()
    def rename_column():
        try:
            table=input("ENTER THE NAME OF TABLE TO BE MODIFIED OR USED: ")
            mycursor12=mydb.cursor()
            col2=input("enter the name of column to be renamed: ")
            new_col=input("enter the new name of column: ")

            sql11="ALTER TABLE {} RENAME COLUMN {} TO {}".format(table,col2,new_col)
            mycursor12.execute(sql11)
            mydb.commit()
            speak("your datatype is SUCCESSFULLY updated")
        except Exception as e:
            print(e)
            speak(e)
            rename_column()
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLEASE TRY AGAIN{bcolors.ENDC}")
        
        def wa_run():
            z=input("Do you want to continue (y/n) : ")
            if z=='Y' or z=='y':                                    
                rename_column()              
            elif z=='N' or z=='n':
                None
                print(f"{bcolors.OKGREEN}your datatype is SUCCESSFULLY updated{bcolors.ENDC}")
                
            elif z !='y'or z !='Y' or z !='n' or z!="N":
                print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                wa_run()
        wa_run()
    def pri_key():
        try:
            table=input("ENTER THE NAME OF TABLE TO BE MODIFIED OR USED: ")
            mycursor13=mydb.cursor()
            col3=input("ENTER THE NAME OF COLUMN TO WHICH PRIMARY KEY IS TO BE ASSIGNED: ")
            sql12="ALTER TABLE {} ADD PRIMARY KEY ({})".format(table,col3)
            mycursor13.execute(sql12)
            mydb.commit()
            speak("your Primary  key is SUCCESSFULLY added")
        except Exception as e:
            print(e)
            speak(e)
            print(f"{bcolors.FAIL}PLEASE TRY AGAIN{bcolors.ENDC}")
            pri_key()
        
        def wa_run():
            z=input("Do you want to continue (y/n) : ")
            if z=='Y' or z=='y':                                    
                pri_key()               
            elif z=='N' or z=='n':
                None
                print(f"{bcolors.OKGREEN}your Primary  key is SUCCESSFULLY added{bcolors.ENDC}")
            elif z !='y'or z !='Y' or z !='n' or z!="N":
                print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                wa_run()
        wa_run()
    def rename_table():
        try:
            table=input("ENTER THE NAME OF TABLE TO BE MODIFIED OR USED: ")
            mycursor14=mydb.cursor()
            col4=input("ENTER THE NEW NAME OF TABLE: ")
            sql13="ALTER TABLE {} RENAME TO {}".format(table,col4)
            mycursor14.execute(sql13)
            mydb.commit()
            table=col4
            speak("your table is SUCCESSFULLY renamed")
        except Exception as e:
            print(e)
            speak(e)
            rename_table()
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLEASE TRY AGAIN{bcolors.ENDC}")
        
        def wa_run():

            z=input("Do you want to continue (y/n) : ")
            if z=='Y' or z=='y':                                    
                rename_table()               
            elif z=='N' or z=='n':
                None
                print(f"{bcolors.OKGREEN}your table is SUCCESSFULLY renamed{bcolors.ENDC}")
            elif z !='y'or z !='Y' or z !='n' or z!="N":
                
                print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                wa_run()
        wa_run()
    def add_record():
        tb1=input("ENTER THE TABLE IN WHICH VALUES HAS TO BE ADDED : ")
        n=int(input("enter the no.of columns in table : "))
        list1=[]
        for i in range(n):
            try:
                def add_rec():
                    print("Enter the data to be inserted in colomun ",i+1) 
                    data=input("enter: ")
                    data1=eval(data)
                    list1.append(data1)
                c=i+1
                add_rec()
            except Exception as e:
                print(f"{bcolors.FAIL}Error:{bcolors.ENDC}",e)
                speak(e)
                for m in range(c,n+1):
                    add_rec()
        tup=tuple(list1)
        mycursor124=mydb.cursor()
        sql7="INSERT INTO %s VALUES %s"%(tb1,tup)
        mycursor124.execute(sql7)
        mydb.commit()
        def wa_run():
            z=input("Do you want to continue (y/n) : ")
            if z=='Y' or z=='y':                                    
                add_record()               
            elif z=='N' or z=='n':
                None
                print(f"{bcolors.OKGREEN}Data has been SUCCESSFULLY added{bcolors.ENDC}")
                speak("Data has been SUCCESSFULLY added")
            elif z !='y'or z !='Y' or z !='n' or z!="N":
                
                print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                wa_run()
        wa_run()
    try1=True
    while try1==True:
        print('''WHAT DO YOU WANT TO DO

    1)UPDATE THE VALUES

    2)UPDATE THE DATA TYPE

    3)RENAMING TABLE
 
    4)RENAMING COLUMN NAME

    5)DEFINING ANY COLUMN AS PRIMARY KEY

    6)TO ADD COLUMN

    7)TO ADD NEW DATA
    
    8) TO PASS ON TO FORWARD PROGRAM

   ''')
        enter=int(input('''ENTER THE OPTION FROM ABOVE CHOICE : '''))
        if enter==1:
            val_update()
            try1=False          
        elif enter==2:
            datatype_update()
            try1=False
        elif enter==3:
            rename_table()
            try1=False
        elif enter==4:
            rename_column()
            try1=False
        elif enter==5:
            pri_key()
            try1=False
        elif enter==6:
            add_col1()
            try1=False
        elif enter==7:
            add_record()
            try1=False
        elif enter==8:
            try1=False
            pass
        else:
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLEASE ENTER VALID OPTION{bcolors.ENDC}")
            print(enter)
#--------------------------------------------PART3----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------VIEWING DATA----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def view():
    try :
        D1=input("ENTER THE DATABASE TO BE USED: ")
        print(''' OPTIONS:
        1)TO VIEW DATBASES
        2)TO VIEW TABLES
        3)TO VIEW TABLE STRUCTURE
        4)TO VIEW DATA INSIDE TABLE
        5)TO VIEW PARTICULAR ROW OR ROWS IN TABLE
        '''
        )
        #RUNNING DATABASE
        def run():
            mycursor4 = mydb.cursor()
            sql188="USE %s"%(D1)
            mycursor4.execute(sql188)
        run()
        
        def v_database():
            mycursor17 = mydb.cursor()
            mycursor17.execute("SHOW DATABASES")
            data4=mycursor17.fetchall()
            l=tuple()
            for kj1 in data4:
                
                print(f"{bcolors.WARNING}{kj1}{bcolors.ENDC}")
            def wa_run():

                z=input("Do you want to continue (y/n) : ")
                if z=='Y' or z=='y':                                    
                    v_database()             
                elif z=='N' or z=='n':
                    None
                else:
                    print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                    wa_run()
            wa_run()
        def v_tables():
            mycursor18 = mydb.cursor()
            mycursor18.execute("SHOW TABLES")
            data5=mycursor18.fetchall()
            for kj in data5:
                print(f"{bcolors.WARNING}{kj}{bcolors.ENDC}")
            def wa_run():

                z=input("Do you want to continue (y/n) : ")
                if z=='Y' or z=='y':                                    
                    v_tables()              
                elif z=='N' or z=='n':
                    None
                else:
                    print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                    wa_run()
            wa_run()
        def structure():
            try:
                tb1=input("ENTER THE TABLE NAME: ")
                mycursor7=mydb.cursor()
                sql6="DESCRIBE %s"%(tb1)
                mycursor7.execute(sql6)
                stru=mycursor7.fetchall()
                for kj2 in stru:
                    print(f"{bcolors.WARNING}{kj2}{bcolors.ENDC}")
            except Exception as e:
                print('error:',e)
                print('initial input:',tb1)
                speak(e)
                print(f"{bcolors.FAIL}please try once again!{bcolors.ENDC}")
                structure()
            def wa_run():

                z=input("Do you want to continue (y/n) : ")
                if z=='Y' or z=='y':                                    
                    structure()               
                elif z=='N' or z=='n':
                    None
                else:
                    print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                    wa_run()
            wa_run()
        def v_data():
            try:
                tb2=input("ENTER THE TABLE NAME: ")
                mycursor19=mydb.cursor()
                sql111="SELECT * FROM {}".format(tb2)
                mycursor19.execute(sql111) 
                data6=mycursor19.fetchall()

                for kj2 in data6:
                    print(f"{bcolors.WARNING}{kj2}{bcolors.ENDC}")
                
            except Exception as e1:
                print('error:',e1)
                print('initial input:',tb2)
                print(f"{bcolors.FAIL}please try once again!{bcolors.ENDC}")
                v_data()

        def v_pardata():
            try:
                wh=''
                tb3=input("Enter the table name: ")
                
                mycursor368=mydb.cursor()
                l=[]
                q=int(input("Enter the no. of coloumns to viewed : "))
                k=''
                m=''
                for j in range (q):
                    d=input("Enter the coloumn name: ")
                    k+=str(d)+','
                l=len(k)
                for i in range (0,l-1):
                    m+=k[i]
                print(m)
                def ubu():


                    sql115="SELECT {} FROM {} {}".format(m,tb3,wh)
                    print(sql115)
                    print(wh)
                    mycursor368.execute(sql115)
                    stru1=mycursor368.fetchall()
                    for kj2 in stru1:
                        print(f"{bcolors.WARNING}{kj2}{bcolors.ENDC}")

                def cond():
                    cond=input("Do you want to enter any condition (Y/N): ")
                    if cond=='Y' or cond=='y':
                        wh=input("Enter the condition(with where clause): ")
                        sql115="SELECT {} FROM {} {}".format(m,tb3,wh)
                        mycursor368.execute(sql115)
                        stru1=mycursor368.fetchall()
                        for kj2 in stru1:
                            print(f"{bcolors.WARNING}{kj2}{bcolors.ENDC}")
                    elif cond=="N"or cond=='n':
                        ubu()
                    else:
                        print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}Invalid input,please try once again!{bcolors.ENDC}")
                        cond()
                cond()
            except Exception as E:
                print(E)
                speak(E)
                print(f"{bcolors.FAIL}please try once again!{bcolors.ENDC}")
                v_pardata()
            def wa_run():
                z=input("Do you want to continue (y/n) : ")
                if z=='Y' or z=='y':                                    
                    v_pardata()               
                elif z=='N' or z=='n':
                    None
                else:
                    print(f"{bcolors.FAIL}PLEASE ENTER VALID OPTION THAT IS Y/N \n{bcolors.ENDC}")
                    wa_run()
            wa_run()

    except Exception as e:
        print('Error: ',e)
        print('Initial input:',D1)
        speak(e)
        print(f"{bcolors.FAIL}please try once again!{bcolors.ENDC}")
        view()
        
    try2=True       
    while try2==True:    
        enter2=int(input("Enter your choice here: "))
        if enter2==1:
            v_database()
            try2=False
        elif enter2==2:
            v_tables()
        elif enter2==3:
            structure()
            try2=False   
        elif enter2==4:
            v_data()
            try2=False
        elif enter2==5:
            v_pardata() 
            try2=False
        else:
            print("wrong input enter again")
            print(enter2)
#------------------------------------------------------------------------------------------------------PART4 -----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------DELETING--------------------------------------------------------------------------------------
def delete():
    D1=input("Enter the database to be used: ")
    def run():
 
            mycursor4 = mydb.cursor()
            sql188="USE %s"%(D1)
            mycursor4.execute(sql188)
    run()
    def rem_col():
        try:
            table=input("ENTER THE NAME OF TABLE TO BE MODIFIED OR USED: ")
                
            col1=input("Enter the name of column to be removed: ")
            mycursor11=mydb.cursor()
            sql10="ALTER TABLE {} DROP COLUMN {}".format(table,col1)
            mycursor11.execute(sql10)
            mydb.commit()
            speak("your coloumn is SUCCESSFULLY removed")
            def wa_run():
                use=input("Do you want to remove one more column (Y/N): ")
                if use=='Y' or use=='y':
                    rem_col()
                elif use=='N' or use=='n':
                    None
                else:
                    print("Enter valid input")
                    wa_run()
            wa_run()
        except Exception as e:
            print(e)
            speak(e)
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLEASE TRY AGAIN{bcolors.ENDC}")
            rem_col()

    def rem_prikey():
        try:
            table=input("ENTER THE NAME OF TABLE TO BE MODIFIED OR USED: ")
            mycursor15=mydb.cursor()
            sql14="ALTER TABLE {} DROP PRIMARY KEY".format(table)
            mycursor15.execute(sql14)
            mydb.commit()
            speak("your table's primary key is successfully removed!")
            def wa_run():
                use=input("Do you want to remove one more primary key (Y/N): ")
                if use=='Y' or use=='y':
                    rem_prikey()
                elif use=='N' or use=='n':
                    None
                else:
                    print("Enter valid input")
                    wa_run()
            wa_run()
        except Exception as e:
            print(e)
            speak(e)
            rem_prikey()
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLEASE TRY AGAIN{bcolors.ENDC}")
        
    def rem_record():
        try:
            table=input("Enter the name of table: ")
            mycursor365=mydb.cursor()
            sql11=input("Enter the unique condition to identifiy perticular record to be removed: ")
            Msql='Delete from {} where {}'.format(table,sql11)
            mycursor365.execute(Msql)
            mydb.commit()
            speak("your particular record is successfully removed!")
            def wa_run():
                
                use=input("Do you want to remove one more record (Y/N): ")
                if use=='Y' or use=='y':
                    rem_record()
                elif use=='N' or use=='n':
                    None
                else:
                    print("Enter valid input")
                    wa_run()
            wa_run()
        except Exception as e:
            print(e)
            speak(e)
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLease try again!{bcolors.ENDC}")
            rem_record()
            
    def rem_database():
        try:
            database=input("Enter the name of the database : ")
            mycursor366=mydb.cursor()
            sql112='Drop Database {}'.format(database)
            mycursor366.execute(sql112)
            mydb.commit()
            speak("Your database is SUCCESSFULLY removed: ")
            def wa_run():
                use=input("Do you want to remove one more Database (Y/N): ")
                if use=='Y' or use=='y':
                    rem_database()
                elif use=='N' or use=='n':
                    None
                else:
                    print("Enter valid input")
                    wa_run()
            wa_run()   
        except Exception as e:
            print(e)
            speak(e)
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLease try again!{bcolors.ENDC}")
            rem_database()
        

    def rem_table():
        try:
            table=input("Enter the table name to be removed: ")
            mycursor367=mydb.cursor()
            sql113='Drop table {}'.format(table)
            mycursor367.execute(sql113)
            speak("Your table is SUCCESSFULLY removed!")
            def wa_run():
                use=input("Do you want to remove one more table (Y/N): ")
                if use=='Y' or use=='y':
                    rem_record()
                elif use=='N' or use=='n':
                    None
                else:
                    print("Enter valid input")
                    wa_run()
                
            wa_run()
        except Exception as e:
            print(e)
            speak(e)
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}PLease try again!{bcolors.ENDC}")
            rem_table()

    try25=True       
    while try25==True:    
        print('''  
                1-->REMOVE COLOUMN
                2-->REMOVE PRIMARY KEY
                3-->REMOVE RECORD
                4-->REMOVEING DATBASES
                5-->REMOVEING TABLE
                       ''')
        enter25=int(input("Enter your choice here: "))
        if enter25==1:
            rem_col()
            try25=False
        elif enter25==2:
            rem_prikey()
            try25=False
        elif enter25==3:
            rem_record()
            try25=False   
        elif enter25==4:
            rem_database()
            try25=False
        elif enter25==5:
            rem_table() 
            try25=False
        else:
            print("wrong input enter again")
            print(enter25)
   
#-------------------------------------------------------------------------------------------------------part5----------------------------------------------------------------------------
def command():
    d1=input("enter the name of database: ")
    def run():
        XZ=True
        while XZ==True:
            try :
                mycursor4 = mydb.cursor(buffered=True)
                sql188="USE %s"%(d1)
                mycursor4.execute(sql188)
                XZ=False
                
            except Exception as e:
                print (e)
                print(f"{bcolors.FAIL}please try once again!{bcolors.ENDC}")
                XZ=True
    run()
    def comnd2():
        xyz=True
        while xyz==True:
            COMND= input("enter the MySql command in which fetchall is not used : ")
            try:
                mycursor61=mydb.cursor(buffered=True)
                mycursor61.execute(COMND)
                xyz=False
                mydb.commit()
                
            except Exception as e:
                print(e)
                print(f"{bcolors.FAIL}please try once again!{bcolors.ENDC}")
            ab=input("DO YOU WANT TO USE IT AGAIN: ")
            if ab=='y' or ab=='Y':
                command()
            else:
                speak("ok got it")
    def comnd1():
        xy=True
        while xy==True:
            comd2=input("ENTER THE COMMAND IN WHICH FETCHALL IS TO BE USED : ")
            try:
                mycursor62=mydb.cursor(buffered=True)
                mycursor62.execute(comd2)
                dat=mycursor62.fetchall()
                mydb.commit()
                for kj in dat:
                    print(f"{bcolors.WARNING}{kj}{bcolors.ENDC}")
                    
                xy=False
            except Exception as e:
                print(e)
                print(f"{bcolors.FAIL}please try once again!{bcolors.ENDC}")
            ab=input("DO YOU WANT TO USE IT AGAIN")
            if ab=='y' or ab=='Y':
                command()
            else:
                speak("ok got it")

    print("Enter \n1. To type command and fetch result. \n2.To type command without getting result. ")    
    V1=True
    while V1==True:
        qps=int(input("Enter the  choice: "))
        if qps==1:
            comnd1()
            V1=False
        elif qps==2:
            comnd2()
            V1=False
        else:
            print("wrong input!,Enter again")    
#=============================================================================================================part unknown---------------------------------------------------------------------------------------------------------------------------
def pie1():
    def v_data():
        d1=input("enter the name of database to be used : " )
        try:
            def run():
                mycursor4 = mydb.cursor()
                sql188="USE %s"%(d1)
                mycursor4.execute(sql188)
            run()
        except Exception as e:
            print(e)
            speak("PLEASE TRY AGAIN")
            v_data()
        la=[]
        po=[]
        try:
            tb2=input("ENTER THE TABLE NAME: ")
            col2=input("ENTER THE COLUMN NAME WHICH HAS NUMERIC VALUE : ")
            col3=input("ENTER THE NAME OF COLUMN WHICH UNIQUELY IDENTIFIES ANY ATTRIBUTE : ")
            mycursor19=mydb.cursor()
            mycursor20=mydb.cursor()
            sql111="SELECT {} FROM {}".format(col2,tb2)
            mycursor19.execute(sql111) 
            data6=mycursor19.fetchall()
            sql1="SELECT {} FROM {}".format(col3,tb2)
            mycursor20.execute(sql1) 
            data7=mycursor20.fetchall()
            for j in data7:
                po.extend(j)
            for kj2 in data6:
                jk=list(kj2)
                la.extend(jk)
            plt.pie(la,labels=po,startangle=90, shadow=True, explode=(0,0,0.1,0),radius=0.5, autopct ='%1.1f%%')
            plt.show()
        except Exception as e1:
            print('error:',e1)
            print('initial input:',tb2)
            print(f"{bcolors.FAIL}please try once again!{bcolors.ENDC}")
            v_data()
    v_data()
#--------------------------------------------------------------------------------------------------------------part6----------------------------------------------------------------------------------------------------------------------------------
def options():
    print('''
             1--> FOR CREATING DATABASE
             2-->FOR MODIFYING DATABASE
             3-->FOR VIEWING DATA IN MYSQL
             4-->FOR DELETING DATA
             5-->FOR RUNNING YOUR OWN COMMAND
             6-->TO VIEW NUMERIC DATA IN THE FORMOF PIE CHART
             7-->EXIT
          ''')
    speak("What you would like to do?")
    try3=True
    while try3==True:
        option=int(input("ENTER THE OPTION : "))
        if option==1:
            sequence()
            cre_table()
            try3=False
        elif option==2:
            using_data()
            try3=False
            
        elif option==3:
            view()
            try3=False
            
        elif option==4:
            delete()
            try3=False
        elif option==5:
            command()
            try3=False
        elif option==6:
            pie1()
            try3=False
        elif option==7:
            break
        else:
            print(f"{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}INVALID INPUT!! PLEASE ENTER AGAIN{bcolors.ENDC}")
            print("Your intial input: ",option)
            speak("INVALID INPUT!! PLEASE ENTER AGAIN")
            options()
options()
def run_again():
    try34=True
    while try34==True:
        how1=input("DO YOU WANT TO Run Whole program once AGAIN : ")
        if how1=='Y' or how1=='y':
            options()
        elif how1=='N' or how1=='n':
            print(f"{bcolors.OKGREEN}THANK YOU !!! {bcolors.ENDC}")
            speak("THANKS FOR USING OUR PROGRAM")
            try34=False
        else:
            speak("OPTION ENTERED IS INVALID, PLEASE ENTER VALID OPTION")
            print(f"{bcolors.FAIL}{bcolors.BOLD}ENTER VALID OPTION{bcolors.ENDC}")
            run_again()
run_again()
mydb.close() 