import random
from uuid import uuid4
import time
import pickle
import os


def startup():
    text = """
               𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨
            ╔══════════════╗
              𝓧𝓨𝓩 𝓑𝓐𝓝𝓚
            ╚══════════════╝
          𝑀𝒶𝓃𝒶𝑔𝑒𝓂𝑒𝓃𝓉 𝒮𝓎𝓈𝓉𝑒𝓂
"""
    print(text)


def randomnum(n):
    mini = pow(10, n - 1)
    maxi = pow(10, n)
    return random.randint(mini, maxi)


def newacc():
    Username = input("Enter Your name :")
    DOB = input("Enter Your Date of birth \n"
                "Format [ᴰᴰ/ᴹᴹ/ʸʸʸʸ] :")
    AadhaarNo = int(input("Enter your Aadhaar Number :"))
    PhoneNo = int(input("Enter Phone Number :"))
    dep = int(input("Enter amount to be deposit :"))
    time.sleep(1)
    print('Account created Succesfully')
    time.sleep(1)
    print('════════════════════════𝐂𝐫𝐞𝐝𝐞𝐧𝐭𝐢𝐚𝐥𝐬════════════════════════')
    time.sleep(2)
    CID = str(uuid4())
    upi_id = str('{}@xyz'.format(randomnum(10)))
    print('Account Holder Name : {} \n'
          'Customer ID : {} \n'
          'UPI ID : {}'.format(Username, CID, upi_id))

    def insertdata():
        d = {}
        if os.path.isfile("CustomerInfo_Perm.bin"):
            with open("CustomerInfo_Perm.bin", "rb") as f:
                d = pickle.load(f)
                d[CID] = [Username, DOB, AadhaarNo, PhoneNo, upi_id, dep]
            with open("CustomerInfo_Perm.bin", "wb") as f:
                pickle.dump(d, f)
        else:
            with open("CustomerInfo_Perm.bin", "wb") as f:
                d[CID] = [Username, DOB, AadhaarNo, PhoneNo, upi_id, dep]
                pickle.dump(d, f)
                time.sleep(1)
                print("Account Created!!", d)

    insertdata()


def login():
    def main_menu():
        f = open("CustomerInfo_Perm.bin", "rb")
        data = pickle.load(f)
        time.sleep(1)
        print("Welcome!", data[CustomerID][0])
        menu = """
            Main Menu:
            1~ Deposit
            2~ Withdraw
            3~ Transfer
            4~ Balance Enquiry
        """
        time.sleep(1)
        print(menu)
        ch = int(input('>>>>>'))
        if ch == 1:
            time.sleep(1)
            print("--DEPOSIT--")
            time.sleep(1)
            depamount = int(input("Enter amount to be deposited: "))
            f = open("CustomerInfo_Perm.bin", "rb+")
            data = pickle.load(f)
            new_amount = depamount + data[CustomerID][5]
            data[CustomerID][5] = new_amount
            f.seek(0)
            pickle.dump(data, f)
            time.sleep(1)
            print("New Balance: ", new_amount)
            f.close()
        if ch == 2:
            time.sleep(1)
            print("--Withdraw--")
            time.sleep(1)
            witamount = int(input("Enter amount to be withdraw: "))
            f = open("CustomerInfo_Perm.bin", "rb+")
            data = pickle.load(f)
            new_amount = data[CustomerID][5] - witamount
            data[CustomerID][5] = new_amount
            f.seek(0)
            pickle.dump(data, f)
            time.sleep(1)
            print("Remaining Balance: ", new_amount)
            f.close()
        if ch == 3:
            print("--transfer--")
            time.sleep(1)
            transferamount = int(input("Enter amount to be transferred: "))
            time.sleep(1)
            receiver = input("Enter receiver's CID: ")

            def transfer():
                def send():
                    f = open("CustomerInfo_Perm.bin", "rb+")
                    data = pickle.load(f)
                    newbal = data[CustomerID][5] - transferamount
                    data[CustomerID][5] = newbal
                    f.seek(0)
                    pickle.dump(data, f)
                    f.close()
                    receive()

                def receive():
                    f = open("CustomerInfo_Perm.bin", "rb+")
                    data = pickle.load(f)
                    if receiver in data.keys():
                        newbal = data[receiver][5] + transferamount
                        data[receiver][5] = newbal
                        f.seek(0)
                        pickle.dump(data, f)
                    else:
                        newbal = data[CustomerID][5] + transferamount
                        data[CustomerID][5] = newbal
                        f.seek(0)
                        pickle.dump(data, f)
                        time.sleep(1)
                        print("User not found! Transfer failed")
                        time.sleep(1)
                        print("Money deposited back to your account")
                        time.sleep(1)
                    print("Balance after transfer : ", data[CustomerID][5])
                    f.close()
                send()
            transfer()

        if ch == 4:
            f = open("CustomerInfo_Perm.bin", "rb")
            data = pickle.load(f)
            if CustomerID in data.keys():
                print("Available balance: ", data[CustomerID][5])
                f.close()

    f = open("CustomerInfo_Perm.bin", "rb")

    def logindata():
        data = pickle.load(f)
        for i in range(1):
            if CustomerID in data.keys():
                if Username != data[CustomerID][0]:
                    print("Invalid Username!")
                else:
                    time.sleep(1)
                    print('login sucessful')
                    time.sleep(1)
                    main_menu()
                break
            if CustomerID == "Admin":
                time.sleep(1)
                admin()
                break
            if CustomerID == "admin" or CustomerID == "ADMIN":
                time.sleep(1)
                print("Admin Access Denied")
                break
            else:
                time.sleep(1)
                print("Invalid CID!")
                time.sleep(1)
                print('Please try again or create and new account')
                time.sleep(1)
                print('To create a new account type "NEW"')
                ch = input("Enter here: ")
                if ch == "NEW":
                    newacc()
                else:
                    f.close()
    time.sleep(1)
    Username = input("Enter your username: ")
    time.sleep(1)
    CustomerID = input("Enter your Customer ID: ")
    logindata()


def admin():
    time.sleep(1)
    print("Hello there Admin!")
    time.sleep(1)
    print("Admin Menu")
    time.sleep(1)
    print("1. View all accounts\n"
          "2. Search account\n"
          "3. Modify account\n"
          "4. Delete account")
    time.sleep(1)
    ch = int(input("Enter choice"))
    if ch == 1:
        f = open("CustomerInfo_Perm.bin", "rb")
        data = pickle.load(f)
        time.sleep(1)
        print(data)
        f.close()
    if ch == 2:
        f = open("CustomerInfo_Perm.bin", "rb")
        data = pickle.load(f)
        CustomerID = input("Enter Customer ID to be searched: ")
        if CustomerID in data.keys():
            time.sleep(1)
            print(data[CustomerID])
            f.close()
    if ch == 3:
        key = input("Enter your Customer ID: ")
        f = open("CustomerInfo_Perm.bin", "rb+")
        data = pickle.load(f)
        if key in data.keys():
            print("Choose what has to be updated\n"
                  "1. Username\n"
                  "2. DOB\n"
                  "3. AadhaarNo\n"
                  "4. PhoneNo")
            ch = int(input("Enter choice: "))
            if ch == 1:
                new_username = input("Enter New Customer Name: ")
                data[key][0] = new_username
                time.sleep(1)
                print("Username Updated")
                time.sleep(1)
                print("Updated data: ", data[key])
                f.seek(0)
                pickle.dump(data, f)
                f.close()
            if ch == 2:
                new_dob = input("Enter New Date of Birth: ")
                data[key][1] = new_dob
                time.sleep(1)
                print("DOB Updated")
                time.sleep(1)
                print("Updated data: ", data[key])
                f.seek(0)
                pickle.dump(data, f)
                f.close()
            if ch == 3:
                new_aadhar = input("Enter Aadhaar Number: ")
                data[key][3] = new_aadhar
                time.sleep(1)
                print("Aadhaar Number Updated")
                time.sleep(1)
                print("Updated data: ", data[key])
                f.seek(0)
                pickle.dump(data, f)
                f.close()
            if ch == 4:
                new_phone = input("Enter new Phone Number: ")
                data[key][4] = new_phone
                time.sleep(1)
                print("Phone Number Updated")
                time.sleep(1)
                print("Updated data: ", data[key])
                f.seek(0)
                pickle.dump(data, f)
                f.close()
    if ch == 4:
        f = open("CustomerInfo_Perm.bin", "rb+")
        key = input("Enter Customer's CID to close Account: ")
        data = pickle.load(f)
        if key in data.keys():
            del data[key]
            f.seek(0)
            pickle.dump(data, f)
            time.sleep(1)
            print("Account closed!")
        else:
            time.sleep(1)
            print("User not found")
        f.close()
