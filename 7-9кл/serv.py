from flask import Flask, render_template, request
import sqlite3
import random
import csv
import os


app = Flask(__name__)


@app.route('/')
@app.route('/one.html')
def serv():
    return render_template('one.html')


@app.route('/two.html', methods=['POST', 'GET'])
def two():
    if request.method == 'GET':
        return render_template('two.html')
    elif request.method == 'POST':
        global log
        log = request.form['login']
        conn = sqlite3.connect('rezult.db')
        c = conn.cursor()
        c.execute("SELECT fi,names,scores FROM rezult")
        asd = c.fetchall()
        if ((str(log)) + ",") in str(asd):
            return pristupit()
        else:
            return two_no()

@app.route('/two_no.html')
def two_no():
    return render_template('two_no.html')


@app.route('/pristupit.html')
def pristupit():
    return render_template('pristupit.html')

@app.route('/test.html', methods=['POST', 'GET'])
def test():
    try:
        if request.method == 'GET':
            with open('7-9.csv', 'r', newline='') as csvfile:
                dr = csv.reader(csvfile, delimiter=' ', quotechar='|')
                global s
                s = []
                for row in dr:
                    vf = (' '.join(row))
                    s.append(vf)
                print(s)
            return render_template('test.html', s=s)
        elif request.method == 'POST':
            var21 = 0
            for sd in s:
                lqp = request.form[sd]
                var21 += (int(lqp))


                #print(var21)
            #var21 = int(var) + int(var2) + int(var3) + int(var4) + int(var5) + int(var6) + int(var7) + int(var8) + int(var9) + int(var10) + int(var11) + int(var12) + int(var13) + int(var14) + int(var15) + int(var16) + int(var17) + int(var18) + int(var19) + int(var20)

            conn = sqlite3.connect('rezult.db')
            c = conn.cursor()
            c.execute('UPDATE rezult SET(scores) = ? WHERE NAMES = ?', (var21, log))
            conn.commit()
            print(var21)
            return prob2(var21)

    except (RuntimeError, TypeError, NameError, KeyError):
        return test()


@app.route('/prob2.html')
def prob2(var21):
        fg = (len(s)) * 3
        return render_template('prob2.html', var21=var21, fg=fg)


@app.route('/voprosy.html', methods=['POST', 'GET'])
def voprosy():
    if request.method == 'GET':
        return render_template('voprosy.html')
    elif request.method == 'POST':
        vop = request.files.get('f')
        vop.save(os.path.join(vop.filename))
        return voprosy_yes()

@app.route('/voprosy_yes')
def voprosy_yes():
    return render_template('voprosy_yes.html')

@app.route('/rez.html', methods=['POST', 'GET'])
def rez():
    if request.method == 'GET':
        return render_template('rez.html')
    elif request.method == 'POST':
        par = request.form['parol']
        if par == "123":
            return vybor()
        else:
            return rez_no()

@app.route('/rez_no.html')
def rez_no():
    return render_template('rez_no.html')


@app.route('/prob.html', methods=['POST', 'GET'])
def prob():

    #conn = sqlite3.connect('rezult.db')
    #c = conn.cursor()
    #c.execute("SELECT names,scores FROM rezult")
    #rezz = c.fetchall()
    #sc = str(rezz)
    #t = sc.replace('(', " ")
    #n = t.replace(')', " ")
    #r = n.replace(', ,', ",")
    #conn.commit()
    #gt = r[1:-1]
    #ht = gt.replace(" ", "")
    #uj = ht.replace(",", " ")
    #qa = uj.replace("40", "\n")
    #lens = (len(uj.split()))
    #spsk = uj.split()

    conn = sqlite3.connect('rezult.db')
    c = conn.cursor()  # создание объекта "курсор" для создания дальнейших запросов sqlite
    c.execute('CREATE TABLE IF NOT EXISTS rezult(fi TEXT, names INTEGER, '
              'scores INTEGER)')
    conn.commit()

    conn = sqlite3.connect('rezult.db')
    c = conn.cursor()
    c.execute("SELECT fi,names,scores FROM rezult")
    rezz = c.fetchall()
    return render_template('prob.html', items=rezz)

@app.route('/prochee.html')
def prochee():
    return render_template('prochee.html')


@app.route('/dobavlenie.html', methods=['POST', 'GET'])
def dobavlenie():
    if request.method == 'GET':
        return render_template('dobavlenie.html')
    elif request.method == 'POST':
        fio = request.form['fio']
        number = (random.randint(10000, 99999))
        var25 = 0
        conn = sqlite3.connect('rezult.db')
        c = conn.cursor()  # создание объекта "курсор" для создания дальнейших запросов sqlite
        c.execute('CREATE TABLE IF NOT EXISTS rezult(fi TEXT, names INTEGER, '
                  'scores INTEGER)')
        c.execute("INSERT INTO rezult(fi, names, scores) VALUES(?, ?, ?)", (fio, number, var25))
        conn.commit()
        return render_template('dob_yes.html')



@app.route('/vybor.html')
def vybor():
    return render_template('vybor.html')


@app.route('/dob_yes.html')
def dob_yes():
    return render_template('dob_yes.html')



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
