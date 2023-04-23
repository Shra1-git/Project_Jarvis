from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyrebase
# import requests
from fastapi import FastAPI, Response
# import firebase_admin
# from firebase_admin import credentials
app = FastAPI()

@app.get('/')

def whole_functi(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
#     serv_obj = Service("chromedriver_mac64/chromedriver.exe")
    # cred = credentials.Certificate("path/to/serviceAccountKey.json")
    # firebase_admin.initialize_app(cred)
    driver = webdriver.Chrome()

#     driver.get("https://demoalsdb.firebaseapp.com/")



#     con = driver.find_element(By.ID, "mycondition").text
#     print(con)
#     swords = con.split()
#     print(swords)
#     print(len(swords))


#     for i in range(0,len(swords)):
#           if swords[i] == '<' or swords[i] == '>' or swords[i] == '<>':
#              global mysymbol
#              mysymbol = swords[i]
#              leftoid = swords[i-1]
#              rightoid = swords[i+1]
#              print(i)
#              print(leftoid)
#              print(rightoid)
#              break

#     print(leftoid)
#     print(rightoid)
#     print(mysymbol)

#     leftoidtext = leftoid.split(".")
#     # print(leftoidtext)
#     leftformoid = leftoidtext[0]
#     leftfeildoid = leftoidtext[1]
#     print(leftformoid)
#     print(leftfeildoid)

#     rightoidtext = rightoid.split(".")
#     # print(rightoidtext)
#     rightformoid = rightoidtext[0]
#     rightfeildoid = rightoidtext[1]
#     print(rightformoid)
#     print(rightfeildoid)

#     #python connection to DB

#     config = {
#       "apiKey": "AIzaSyD25yD0pWMy-N1B-6vcHneFZrmqoR35ZBA",
#       "authDomain": "demoalsdb.firebaseapp.com",
#       "projectId": "demoalsdb",
#        "databaseURL": "https://demoalsdb-default-rtdb.firebaseio.com",
#       "storageBucket": "demoalsdb.appspot.com",
#       "messagingSenderId": "1013997483088",
#       "appId": "1:1013997483088:web:110f3cfb8ee67d2d6d8d55",
#       "measurementId": "G-24DH0PNWZP"
#     }

#     firebase = pyrebase.initialize_app(config)
#     database = firebase.database()

#     # data = {"ADate": "Start Date", "Ddate": "End Date", "CDate": "Start Date", "BDate": "End Date"}
#     #
#     # database.push(data)
#     #
#     # database.child("ALS").child("FormOID").child("FieldOID").set(data)
#     global PreTextA
#     global PreTextB
#     PreTextA = database.child("ALS").child("FormOID").child("FieldOID").child(leftfeildoid).get()
#     PreTextB = database.child("ALS").child("FormOID").child("FieldOID").child(rightfeildoid).get()

#     # PreTextA = database.child("Users").child("FirstPerson").find({"A":"Start Date"})
#     print(PreTextA.val())
#     print(PreTextB.val())
#     x = printop()
#     return {x}

# def printop():
#     global x
#     x = ''
#     if mysymbol == '<':
#          x = PreTextA.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + PreTextB.val() + " = " + " 10-Jan-2020" + "<br>"
#          x = x + " " + "Ensure Query Does Fire" + "<br>"
#          x = x + " " + "|" + "<br>"
#          x = x + " " + PreTextA.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + PreTextB.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + "Ensure Query Does Not Fire" + "<br>"
#          x = x + " " + "|" + "<br>"
#          x = x + " " + PreTextA.val() + " = " + " 10-Jan-2020" + "<br>"
#          x = x + " " + PreTextB.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + "Ensure Query Does Not Fire" + "<br>"
#     if mysymbol == '>':
#          x = PreTextA.val() + " = " + " 10-Jan-2020" + "<br>"
#          x = x + " " + PreTextB.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + "Ensure Query Does Fire" + "<br>"
#          x = x + " " + "|" + "<br>"
#          x = x + " " + PreTextA.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + PreTextB.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + "Ensure Query Does Not Fire" + "<br>"
#          x = x + " " + "|" + "<br>"
#          x = x + " " + PreTextA.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + PreTextB.val() + " = " + " 10-Jan-2020" + "<br>"
#          x = x + " " + "Ensure Query Does Not Fire" + "<br>"
#     if mysymbol == '<>':
#          x = PreTextA.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + PreTextB.val() + " = " + " 10-Jan-2020" + "<br>"
#          x = x + " " + "Ensure Query Does Fire" + "<br>"
#          x = x + " " + "|" + "<br>"
#          x = x + " " + PreTextA.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + PreTextB.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + "Ensure Query Does Not Fire" + "<br>"
#          x = x + " " + "|" + "<br>"
#          x = x + " " + PreTextA.val() + " = " + " 10-Jan-2020" + "<br>"
#          x = x + " " + PreTextB.val() + " = " + " 5-Jan-2020" + "<br>"
#          x = x + " " + "Ensure Query Does Fire" + "<br>"
    return {"My World"}



    #driver.quit()

