from flask import Flask, render_template, request, send_file
from flask_cors import CORS
from firebase_handler import firebase_DB

app = Flask(__name__)

CORS(app, resources={r"*": {"origins": "*"}})

db_handler = firebase_DB()

def get_environment(request):
    user_info = request.headers.get('User-Agent')
    if 'mobile' in user_info.lower():
        if  'iphone' in user_info.lower():
            environment =  'iphone'
        elif 'ipad' in user_info.lower():
            environment =  'ipad'
        else:
            environment =  'mobile'
    else:
        environment = 'pc'
    
    return environment,user_info, get_client_ip(request)

def get_client_ip(request):
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return  request.environ['REMOTE_ADDR']
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']


@app.route('/word/<user_code>', methods=['GET', 'POST'])

def word_main(user_code):
    new_word = []
    delete_word = None
    changed_word = None
    word_mean = None
    if request.method == "POST":
        
        new_word = request.form['new_word'].strip().lower()
        delete_word = request.form['delete_word'].strip().lower()
        word_mean = request.form['word_mean'].strip()
        if not new_word == '':
            word_list = db_handler.get_words(user_code)
            if "," in new_word:
                print(new_word.split(","))
                for word, mean in zip(new_word.split(","), word_mean.split(",")):
                    word_mean = db_handler.add_word(user_code,word.strip(),mean.strip())
                if new_word in word_list.keys():
                    changed_word = new_word
                    new_word = []
                else:
                    new_word = new_word.split(",")
            else:
                word_mean = db_handler.add_word(user_code,new_word, request.form['word_mean'].strip())
                if new_word in word_list.keys():
                    changed_word = new_word
                    new_word = []
                else:
                    new_word = new_word.split(",")

        elif not delete_word == '':
            word_list = db_handler.get_words(user_code)
            db_handler.delete_word(user_code,delete_word)
    

    
    client_ip =  get_environment(request)[2]
    db_handler.write_word_visit(user_code, client_ip)
    word_list = db_handler.get_words(user_code)


    return render_template('word_main.html',user_code=user_code, word_list = word_list, added_word = new_word, deleted_word = delete_word, changed_word = changed_word) 

@app.route("/add_word_user/<user_name>")

def add_user(user_name):
    user_code =  db_handler.add_word_user(user_name)

    return "www.oneclickclass.kr/word/"+ user_code

@app.route('/add_favorite_word/<user_code>/<word>')

def add_favorite_word(user_code, word):
    db_handler.togle_favorite_word(user_code, word)
    return 'good'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)