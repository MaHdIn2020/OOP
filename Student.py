class Courses:
    _All_courses={'ENG101': ['Core', 3], 'ENG102': ['Core', 3], 'MAT110': ['mns', '3'], 'MAT120': ['mns', '3'], 'MAT215': ['mns', '3'], 'MAT216': ['mns', '3'], 'PHY111': ['mns', '3'], 'PHY112': ['mns', '3'], 'STA201': ['mns', '3'], 'HUM103': ['arts', 3], 'BNG103': ['arts', 3], 'EMB101': ['social', 3], 'HUM101': ['arts', 3], 'HUM102': ['arts', 3], 'HST102': ['arts', 3], 'HST104': ['arts', 3], 'HUM207': ['arts', 3], 'ENG113': ['arts', 3], 'ENG114': ['arts', 3], 'ENG115': ['arts', 3], 'ENG333': ['arts', 3], 'ACT201': ['arts', 3], 'ACT202': ['arts', 3], 'BUS101': ['arts', 3], 'BUS202': ['arts', 3], 'BCH101': ['arts', 3], 'BTE101': ['arts', 3], 'CHE110': ['arts', 3], 'CHN101': ['arts', 3], 'FRN101': ['arts', 3], 'FIN301': ['arts', 3], 'GEO101': ['arts', 3], 'LAW101': ['arts', 3], 'HUM111': ['arts', 3], 'STA301': ['arts', 3], 'PSY101': ['social', 3], 'SOC101': ['social', 3], 'ANT101': ['social', 3], 'POL101': ['social', 3], 'BUS201': ['social', 3], 'ECO101': ['social', 3], 'ECO102': ['social', 3], 'ECO105': ['social', 3], 'BUS102': ['social', 3], 'POL102': ['social', 3], 'POL103': ['social', 3], 'POL202': ['social', 3], 'PSY102': ['social', 3], 'ANT351': ['social', 3], 'BUS333': ['social', 3], 'CST201': ['cst', 3], 'CST301': ['cst', 3], 'CST302': ['cst', 3], 'CST303': ['cst', 3], 'CST304': ['cst', 3], 'CST305': ['cst', 3], 'CST306': ['cst', 3], 'CST307': ['cst', 3], 'CST308': ['cst', 3], 'CST309': ['cst', 3], 'CST310': ['cst', 3], 'CSE110': ['program', 3], 'CSE111': ['program', 3], 'CSE220': ['program', 3], 'CSE221': ['program', 3], 'CSE230': ['program', 3], 'CSE250': ['program', 3], 'CSE251': ['program', 3], 'CSE260': ['program', 3], 'CSE320': ['program', 3], 'CSE321': ['program', 3], 'CSE330': ['program', 3], 'CSE331': ['program', 3], 'CSE340': ['program', 3], 'CSE341': ['program', 3], 'CSE350': ['program', 3], 'CSE360': ['program', 3], 'CSE370': ['program', 3], 'CSE420': ['program', 3], 'CSE421': ['program', 3], 'CSE422': ['program', 3], 'CSE423': ['program', 3], 'CSE460': ['program', 3], 'CSE461': ['program', 3], 'CSE470': ['program', 3], 'CSE471': ['program', 3], 'CSE400': ['thesis', 4], 'CHE101': ['optional', 3], 'BIO101': ['optional', 3], 'ENV103': ['optional', 3]}
    _All_courses_list=['ENG101', 'ENG102', 'MAT110', 'MAT120', 'MAT215', 'MAT216', 'PHY111', 'PHY112', 'STA201', 'HUM103', 'BNG103', 'EMB101', 'HUM101', 'HUM102', 'HST102', 'HST104', 'HUM207', 'ENG113', 'ENG114', 'ENG115', 'ENG333', 'ACT201', 'ACT202', 'BUS101', 'BUS202', 'BCH101', 'BTE101', 'CHE110', 'CHN101', 'FRN101', 'FIN301', 'GEO101', 'LAW101', 'HUM111', 'STA301', 'PSY101', 'SOC101', 'ANT101', 'POL101', 'BUS201', 'ECO101', 'ECO102', 'ECO105', 'BUS102', 'POL102', 'POL103', 'POL202', 'PSY102', 'ANT351', 'BUS333', 'CST201', 'CST301', 'CST302', 'CST303', 'CST304', 'CST305', 'CST306', 'CST307', 'CST308', 'CST309', 'CST310', 'CSE110', 'CSE111', 'CSE220', 'CSE221', 'CSE230', 'CSE250', 'CSE251', 'CSE260', 'CSE320', 'CSE321', 'CSE330', 'CSE331', 'CSE340', 'CSE341', 'CSE350', 'CSE360', 'CSE370', 'CSE420', 'CSE421', 'CSE422', 'CSE423', 'CSE460', 'CSE461', 'CSE470', 'CSE471', 'CSE400', 'CHE101', 'BIO101', 'ENV103']
    def __init__(self):
        self.core={'ENG101': '', 'ENG102': ''}
        self.mns={'MAT110': '', 'PHY111': '', 'STA201': '','MAT120':'','MAT216':'','MAT215':'','PHY112':''}
        self.artsandhum={'HUM103': '', 'BNG103': '', 'HUM101': '', 'HUM102': '', 'HST102': '', 'HST104': '', 'HUM207': '', 'ENG113': '', 'ENG114': '', 'ENG115': '', 'ENG333': '', 'ACT201': '', 'ACT202': '', 'BUS101': '', 'BUS202': '', 'BCH101': '', 'BTE101': '', 'CHE110': '', 'CHN101': '', 'FRN101': '', 'FIN301': '', 'GEO101': '', 'LAW101': '', 'HUM111': '', 'STA301': ''}
        self.social={'EMB101': '', 'PSY101': '', 'SOC101': '', 'ANT101': '', 'POL101': '', 'BUS201': '', 'ECO101': '', 'ECO102': '', 'ECO105': '', 'BUS102': '', 'POL102': '', 'POL103': '', 'POL202': '', 'PSY102': '', 'DEV104': '', 'DEV201': '', 'POL201': '', 'SOC201/ANT202': '', 'ANT342': '', 'ANT351': '', 'BUS333': ''}
        self.cst={'CST201': '', 'CST301': '', 'CST302': '', 'CST303': '', 'CST304': '', 'CST305': '', 'CST306': '', 'CST307': '', 'CST308': '', 'CST309': '', 'CST310': ''}
        self.program={'CSE110': '', 'CSE111': '', 'CSE220': '', 'CSE221': '', 'CSE230': '', 'CSE250': '', 'CSE251': '', 'CSE260': '', 'CSE320': '', 'CSE321': '', 'CSE330': '', 'CSE331': '', 'CSE340': '', 'CSE341': '', 'CSE350': '', 'CSE360': '', 'CSE370': '', 'CSE420': '', 'CSE421': '', 'CSE422': '', 'CSE423': '', 'CSE460': '', 'CSE461': '', 'CSE470': '', 'CSE471': ''}
        self.thesis={'CSE400':''}
        self.optional={'CHE101':'','BIO101':'','ENV103':''}
class Student(Courses):
    def __init__(self,name=None,ID=None,DOB=None,sem=None,credit=None):
        self.user_name=name
        self.ID=ID
        self.DOB=DOB.split('/')
        self.sem=sem
        self.credit=credit
class Grade(Courses):
    def __init__(self):
        pass
class CSE_Student(Student):
    def __init__(self,name,ID,DOB,sem,credit):
        super().__init__(name,ID,DOB,sem,credit)
        self.course_completed=[]
    def available_courses(self,entry):
        counter=1
        for i in Courses._All_courses.keys():
            print(f'{counter}. {i}',end=' ')
            if counter!=0 and counter%3==0:
                print()
            counter+=1
        print(f'These are the courses offered by BRAC University.')
        if entry==1:
            print(f'Do you want to try other options?')
            inp=input('Enter Yes/No: ')
            if inp.lower()=='yes':
                self.interface(0)
            elif inp.lower=='no':
                print(f'Thanks please visit us again.')
            else:
                print('Invalid request.')
    def remaining_courses(self):
        counter=1
        for i in Courses._All_courses.keys():
            print(f'{counter}. {i}',end=' ')
            if counter!=0 and counter%3==0:
                print()
            counter+=1
        print(f'Enter your response (Suppose you have completed ENG101 and MAT110 then enter 1,3): ')
        inp=input().split(',')
        courses=Courses._All_courses
        courses_list=Courses._All_courses_list
        for i in inp:
            i=int(i)
            l=courses_list[i-1]
            value=courses[l]
            if value[0]=='Core':
                c.core.pop(l)
                courses.pop(l)
            elif value[0]=='mns':
                c.mns.pop(l)
                courses.pop(l)
            elif value[0]=='arts':
                c.artsandhum.pop(l)
                courses.pop(l)
            elif value[0]=='social':
                c.social.pop(l)
                courses.pop(l)
            elif value[0]=='cst':
                c.cst.pop(l)
                courses.pop(l)
            elif value[0]=='program':
                c.program.pop(l)
                courses.pop(l)
            elif value[0]=='thesis':
                c.thesis.pop(l)
                courses.pop(l)
            elif value[0]=='optional':
                c.optional.pop(l)
                courses.pop(l)
        self.info()
        # counter=1
        # for i in courses.keys():
        #     print(f'{counter}. {i}',end=' ')
        #     if counter!=0 and counter%3==0:
        #         print()
        #     counter+=1
    def info(self):
        print(f'Total credits Breakdown:\n GenEd Courses + School Core Courses(39 + 12 Credits):')
        print(f'1. Writing Comprehension:{6-(len(c.core)*3)}/6 completed')
        if 6-(len(c.core)*3)!=6:
            print('Remaining courses:',end=' ')
            for i in c.core:
                print(i,end=' ')
            print()
        print(f'2. Math and Natural Sciences: {21-len(c.mns)*3}/21 completed')
        if 21-len(c.mns)*3!=21:
            print('Remaining courses:',end=' ')
            for i in c.mns:
                print(i,end=' ')
            print()
        print(f'3. Arts and Humanities(minimum 9 credits): {75-len(c.artsandhum)*3}/9 completed ')
        if 75-len(c.artsandhum)*3<9:
            print(f'Minimum {int((9-75+len(c.artsandhum)*3)/3)} from this courses:',end=' ')
            for i in c.artsandhum:
                print(i,end=' ')
            print()
        print(f'4. Social Sciences(minimum 6 credits): {63-len(c.social)*3}/6 completed')
        if 63-len(c.social)*3<6:
            print(f'Minimum {int((6-63+len(c.social)*3)/3)} from this courses:',end=' ')
            for i in c.social:
                print(i,end=' ')
            print()
        print(f'5. Communities, Seeking Transformation(minimum 3 credits): {33-len(c.cst)*3}/3 completed')
        if 33-len(c.cst)*3<3:
            print(f'Minimum {int((3-33+len(c.cst)*3)/3)} from this courses:',end=' ')
            for i in c.cst:
                print(i,end=' ')
            print()
        print(f'Program Core Courses (75 credits): {75-len(c.program)*3}/75 completed')
        if 75-len(c.program)*3<75:
            print(f'Remaining Courses:',end=' ')
            for i in c.program:
                print(i,end=' ')
            print()
        print(f'Project/Internship/Thesis(4 credits): {4-len(c.thesis)*4}/4 completed')
        if 4-len(c.thesis)*4<4:
            print(f'Remaining Course: CSE400')
        print(f'Optional courses:',end=' ')
        for i in c.optional:
            print(i,end=' ')
        print()

    def interface(self,entry=0):
        print(f'Choose the following options:\n1.Show Available Courses\n2.Calculate remaining courses')
        inp=int(input('Enter your response(1/2): '))
        if inp==1:
            self.available_courses(1)
        elif inp==2:
            self.remaining_courses()

        


print("Welcome to BRAC University CSE Student Info!")
name=input("Enter Your Name: ")
id=input("Enter Your ID: ")
dob=input("Enter Your Date of Birth(dd/mm/yy): ")
sem=input('Enter your current semester:')
credit=int(input('Credit Completed: '))
s1=CSE_Student(name,id,dob,sem,credit)
c=Courses()
s1.interface()





