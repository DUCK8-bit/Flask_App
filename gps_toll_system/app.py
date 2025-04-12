from flask import Flask, render_template, url_for, request, session, redirect, jsonify  # pip install flask
import sqlite3
import os
import secrets
import telepot # pip install telepot
import google.generativeai as genai # pip install google-generativeai
from geopy.geocoders import Nominatim # pip install geopy

genai.configure(api_key='AIzaSyDzHU1dCWU1T1KWQNQwAITwJVNGNda4OKs')
gemini_model = genai.GenerativeModel('gemini-pro')
chat = gemini_model.start_chat(history=[])

def sendMessage(msg):
    bot = telepot.Bot("6466163602:AAG-SJ9ibDjInLUah_ZZe4LHKxB__jmVWes")
    bot.sendMessage('6977152032', str(msg))
    
connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
cursor.execute(command)

cursor.execute("""create table if not exists BikeDetails (
    numberplate TEXT, model TEXT, year TEXT, color TEXT, engine_size TEXT, fuel_type TEXT, 
    transmission_type  TEXT, mileage  TEXT, price TEXT, condition_type TEXT, 
    additional_features TEXT, owner_details TEXT, 
    registration_details TEXT, insurance_details TEXT, phone TEXT, email TEXT)""")



import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Uhome')
def Uhome():
    return render_template('userlog.html')

@app.route('/checkdetails')
def checkdetails():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    query = "SELECT * FROM BikeDetails WHERE phone = '"+session['phone']+"'"
    c.execute(query)
    results = c.fetchone()
    if results:
        session['np'] = results[0]
        print(results)
        return render_template('add.html', results=results)
    else:
        return render_template('add.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT * FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchone()

        if result:
            session['phone'] = result[2]
            return redirect(url_for('checkdetails'))
        else:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        numberplate = request.form['numberplate']
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']
        engine_size = request.form['engine']
        fuel_type = request.form['fuel']
        transmission_type = request.form['transmission']
        mileage = request.form['mileage']
        price = request.form['price']
        condition = request.form['condition']
        features = request.form['features']
        owner = request.form['owner']
        registration = request.form['registration']
        insurance = request.form['insurance']
        phone = request.form['phone']
        email = request.form['email']

        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()

        c.execute('''INSERT INTO BikeDetails 
                     (numberplate, model, year, color, engine_size, fuel_type, transmission_type, 
                     mileage, price, condition_type, additional_features, owner_details, 
                     registration_details, insurance_details, phone, email) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)''',
                  (numberplate, model, year, color, engine_size, fuel_type, transmission_type,
                   mileage, price, condition, features, owner, registration, insurance, phone, email))
        conn.commit()
        conn.close()

        return redirect(url_for('checkdetails'))
    return redirect(url_for('checkdetails'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        numberplate = request.form['numberplate']
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']
        engine_size = request.form['engine']
        fuel_type = request.form['fuel']
        transmission_type = request.form['transmission']
        mileage = request.form['mileage']
        price = request.form['price']
        condition = request.form['condition']
        features = request.form['features']
        owner = request.form['owner']
        registration = request.form['registration']
        insurance = request.form['insurance']
        phone = request.form['phone']
        email = request.form['email']

        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()

        c.execute("UPDATE BikeDetails set model = ?, year = ?, color = ?, engine_size = ?, fuel_type = ?,  transmission_type = ?, mileage = ?, price = ?, condition_type = ?, additional_features = ?, owner_details = ?, registration_details = ?, insurance_details = ?, phone = ?, email = ? where numberplate = ? ",[model, year, color, engine_size, fuel_type, transmission_type,mileage, price, condition, features, owner, registration, insurance, phone, email,numberplate])

        conn.commit()
        conn.close()

        return redirect(url_for('checkdetails'))
    return redirect(url_for('checkdetails'))

@app.route('/tracking', methods=['POST', 'GET'])
def tracking():
    if request.method == 'POST':
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        
        loc1 = request.form['loc1']
        loc1 = loc1.split(',')
        loc2 = request.form['loc2']
        loc2 = loc2.split(',')
        num = request.form['num']

        distance = haversine(float(loc1[0]), float(loc1[1]), float(loc2[0]), float(loc2[1]))
        data = f"Distance between {loc1} and {loc2}: {distance} km"
        print(data)
        
        c.execute("select owner_details, phone, email from BikeDetails where numberplate = '"+num+"'")
        result = c.fetchone()

        sendMessage(data+'\n license no '+num+'\n amount is '+str(int(distance*5))+'\n name '+result[0]+'\n phone '+result[1]+'\n email '+result[2])
        if result:
            return render_template('get.html', data=data, num = num, amount = int(distance*5), result=result, np = session['np'])
        else:
            return render_template('get.html', msg='Entered license number not found in database', np = session['np'])
    return render_template('get.html', np = session['np'])

@app.route('/getpage')
def getpage():
    return render_template('get.html', np = session['np'])

@app.route('/getloc1')
def getloc1():
    from serial_test import getdata
    lat, long = getdata()
    print('Location 1', lat, long)
    return jsonify(str(lat)+','+str(long))

@app.route('/getloc2')
def getloc2():
    from serial_test import getdata
    lat, long = getdata()
    print('Location 2', lat, long)
    return jsonify(str(lat)+','+str(long))

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/payment', methods = ['GET', 'POST'])
def payment():
    if request.method == 'POST':
        data = request.form
        print(data)
        return render_template('get.html', np = session['np'], msg='Transaction successfull')
    return render_template('get.html')

@app.route('/home')
def home():
    return render_template('add.html')



@app.route('/information')
def information():
    gemini_response = chat.send_message('nearest temples, restaurants and parking places from SSIT college, tumakuru with original address, contacts, and website link in html code')
    info = gemini_response.text
    info = info.replace('```', '')
    info = info.replace('<h1>', '<h3>')
    info = info.replace('</h1>', '</h3>')
    info = info.replace('<h2>', '<h4>')
    info = info.replace('</h2>', '</h4>')
    print(info)

    print(info)
    return render_template('information.html', info=info[4:])

@app.route('/paymentpage/<amt>')
def paymentpage(amt):
    print(amt)
    return render_template('payment.html', amt = amt)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
