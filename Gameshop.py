class Game:
    def __init__(self,name=None,type=None,price=None):
        self.name=name
        self.type=type
        self.release_years=[]
        self.price=price
    def compare(self,game):
        if self.type==game.type:
            print(f'Both of them are {self.type} game.')
        else:
            print(f'One of them is {self.type} and the other one is {game.type}.')
    def description(self):
        print(f'The name of the game is {self.name} and it is a {self.type} game.')
        print(f'The price of this game is {self.price}$')
    def seasons(self,*year):
        for i in year:
            self.release_years.append(i)
g1=Game('FIFA',"Sports",30)
g2=Game('Ghost of Tsushima','Action-Adventure',28)
g3=Game('Real Cricket',"Sports",12)
class Gameshop:
    total_sale=0
    user_info={}
    Id=1
    def __init__(self):
        self.cart=0
        self.games=[g1,g2,g3]
    def confirmation(self,game,que):
        print(f'Do you want to purchase this game?')
        q=input('Type Yes/No: ')
        if q.lower()=='yes':
            quantity=int(input('Enter the quantity: '))
            self.cart+=quantity*game.price
            print(f"Your total cost will be {self.cart}\nDo you want to purchase another game?")
            conf=input('Type Yes/No: ')
            if conf.lower()=='yes':
                self.available(0,que)
            else:
                print("Your order has been confirmed!\nCheck your email address.")        
        elif q.lower()=='no':
            self.available(1)
    def available(self,entry=0,que=None):
        # print(f'Available games:\n1. {g1.name} \n2. {g2.name}\n3. {g3.name} ')
        if que!=None:
            self.games[que]=0
        print(f'Available games:\n')
        counter=1
        for i in range(len(self.games)):
            if self.games[i]==0:
                continue
            else:
                print(f'{counter}. {self.games[i].name}')
                counter+=1
        self.queries(entry)
    def queries(self,entry):
        if entry==1:
            print('Do you want to try other games?')
            conf=input('Type Yes/No: ')
            if conf.lower()=='no':
                print('Please visit us again')
            else:
                self.available(0)
        else:
            que=int(input('Enter 1/2/3:'))
            game=None
            if 1<=que<=3:
                if que==1:
                    g1.description()
                    game=g1
                elif que==2:
                    g2.description()
                    game=g2
                else:
                    g3.description()
                    game=g3
                self.confirmation(game,que)
            else:
                print('Invalid number!\n Try Again')
                self.queries(0)
    @classmethod
    def user(cls,*info):
        Gameshop.user_info[Gameshop.Id]=info
        Gameshop.Id+=1
print("Welcome to the Gameshop")
name=input(f'Enter your name: ')
email=input(f'Enter your email address: ')
phone=input(f'Enter your phone number: ')
address=input(f'Enter your address: ')
p1=Gameshop()
Gameshop.user(name,email,phone,address)
print('Successfully registered!')
q=p1.available()


