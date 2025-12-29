balance = 0
kyc_documents={}

def check_balance():
    print(f"your currant balnce is {balance} ")
    print("==================")

def deposit(amount):
    global balance
    if amount >= 0:
      balance += amount
    else :
        print("cannot deposit negative amount")
        print("==================")

def withdraw(amount):
    global balance
    if amount <=0:
        print("not nagetive amount")
        print("==================")
    elif amount > balance:
        print("insufficient balance")
        print("==================")
    else:
        balance -= amount

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("kyc not done ")
    else:
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}")


if __name__ == "__main__" :
    print("==================")
    print("wlcome")
    while True:
        print("1 check balance")
        print("2 deposit")
        print("3 withdraw")
        print("4 check kyc")
        print("5 update kyc")
        print("6 quit")
        choice=input("Enter 1 to 6: ")
        print("==================")

        if choice =='1':
            check_balance()
        elif choice =='2':
            amt = float(input("Enter amount: "))
            deposit(amt)
            print(f"amount{amt} deposit sucess")
        elif choice =='3':
            amt = float(input("Enter amount: "))
            withdraw(amt)
            print(f"amount{amt} withdrowal sucess")
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            kyc_docs={}
            n_documents = int(input("Enter no of document you want to add: "))

            for i in range (n_documents):
                key = input("enter doc type: ")
                value = input("enter doc number: ")
                print("==================")
                kyc_docs[key]=value
            update_kyc(kyc_docs)

            print("kyc update")
            print("==================")
        elif choice =='6':
            break
        else:
            print("invalid choie ")
            print("==================")

    print()
    print("thankyou")