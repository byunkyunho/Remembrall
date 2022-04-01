from api_module import *
import pyrebase 
import hashlib
import time
from datetime import date, datetime

class firebase_DB:
    def __init__(self):
        self.auth_data = {
            "apiKey": "시크릿키",
            "authDomain": "시크릿키",
            "databaseURL": "시크릿키",
            "projectId": "시크릿키",
            "storageBucket": "시크릿키",
            "messagingSenderId": "시크릿키",
            "appId": "시크릿키"
        } 
        self.DB = pyrebase.initialize_app(self.auth_data).database()

    def get_words(self, user_code):
        word_by_spell = {word.key():word.val() for word in self.DB.child("english_words").child(user_code).child("words").get().each()}
        word_by_date = {}
        date_list = []
        for word, attr in word_by_spell.items():
            if attr['time'] in word_by_date.keys():
                word_by_date[attr['time']].append({'word':word, 'mean':attr['mean']})
                
            else:
                word_by_date[attr['time']] = [{'word':word, 'mean':attr['mean']}]
                date_list.append(attr['time'])

        date_list.sort()
        date_list.reverse()
        date_list = tuple(date_list)
        return {
                'by_spell':word_by_spell,
                'by_date':{date:word_by_date[date] for date in date_list}
                }

    def add_word(self,user_code, word, mean):
        if mean == "" or mean == None:
            mean = translate(word)
        print("add", word)
        self.DB.child("english_words").child(user_code).child("words").update({word:{"time":datetime.now().strftime("%Y-%m-%d"), "mean":mean}})
        return mean
    
    def delete_word( self,user_code, delete_word):
        self.DB.child("english_words").child(user_code).child("words").child(delete_word).remove()

    def add_word_user(self, user_name):
        user_code = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
        user_code = hashlib.sha256(user_code.encode('utf-8')).hexdigest()
        print(user_code)
        self.DB.child("english_words").child(user_code).update({"name":user_name, "words":{"big":{"time":datetime.now().strftime("%Y-%m-%d"), "mean":"크다"}}})

        return user_code

    def write_word_visit(self, user_code, client_ip):
        self.DB.child("english_words").child(user_code).child("visit").update({datetime.now().strftime("%Y-%m-%d %H:%M:%S"):client_ip})

    def togle_favorite_word(self, user_code, word):
        if self.DB.child("english_words").child(user_code).child('words').child(word).child("favorite").get().val():
            self.DB.child("english_words").child(user_code).child('words').child(word).update({"favorite":False})
        else:
            self.DB.child("english_words").child(user_code).child('words').child(word).update({"favorite":True})