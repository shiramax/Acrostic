from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap

import MySQLdb as mariadb
import re
import datetime


app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    results = {}
    data = request.form.getlist('fields[]')
    letters = ''.join([ word[0] for word in data ])
    con =  mariadb.connect(host="localhost" ,port= 3360, user="root", passwd="password", db="entries")
    cursor = con.cursor()
    ordered_letters = ''.join(sorted(letters))
    ordered_letters = ordered_letters.lower()
    sql_words = "SELECT word,definition FROM entries WHERE orderd_word='%s'" % ordered_letters
    sql_combinations = "SELECT sentence FROM sentences WHERE orderd_sentence='%s'" % ordered_letters
    cursor.execute(sql_words)
    results_words = cursor.fetchall()
    
    cursor.execute(sql_combinations)
    results_combinations = cursor.fetchall()
    
    for word, definition in results_words: 
	if word not in results: 
	    results[word] = []
	results[word].append(definition)
   
    for combination in results_combinations: 
	if combination[0] not in results:
	    results[combination[0]] = ["No Definition"]
    con.close()
    return render_template('index.html', results=results , data=True, words=data)


@app.route('/new_issue')
def new_form():
  return render_template('new_form.html')


@app.route('/about_us')
def about_us():
  return render_template('about.html')

@app.route('/how_it_works')
def how_it_works():
  return render_template('how_it_works.html')

 
@app.route('/community', methods=['POST'])
def new_form_post():
    title_issue = request.form.get('title_issue')
    description_issue = request.form.get('description_issue')
    now = datetime.datetime.now()
    str_now = now.date().isoformat()
    con =  mariadb.connect(host="localhost" ,port= 3360, user="root", passwd="password", db="entries")
    cursor = con.cursor()
    update_select = "INSERT INTO Issues (issue_title, issue_description, issue_date) VALUES ('%s', '%s', '%s');" %(title_issue , description_issue, str_now)
    cursor.execute(update_select)
    con.commit()
    sql = "SELECT * FROM Issues;"
    cursor.execute(sql)
    issues = cursor.fetchall()
    return render_template('community.html', issues=issues)

@app.route('/community')
def community():
    con =  mariadb.connect(host="localhost" ,port= 3360, user="root", passwd="password", db="entries")
    cursor = con.cursor()
    sql = "SELECT * FROM Issues;"
    cursor.execute(sql) 
    issues = cursor.fetchall()
    return render_template('community.html', issues=issues)

@app.route("/issue/<int:issue_id>", methods=["POST","GET"])
def issue(issue_id):
    con =  mariadb.connect(host="localhost" ,port= 3360, user="root", passwd="password", db="entries")
    cursor = con.cursor()
    sql = "SELECT * FROM Issues WHERE issue_id=%s;" % issue_id
    cursor.execute(sql)
    issue = cursor.fetchall()
    sql_get_comment = "SELECT * FROM Comments WHERE issue_id=%s;" % issue_id
    cursor.execute(sql_get_comment)
    comments  = cursor.fetchall()
    #import ipdb; ipdb.set_trace()
    if request.method == "POST":
	comment_description = request.form.get('comment_description')
	now = datetime.datetime.now()
	str_now = now.date().isoformat()
	update_select = "INSERT INTO Comments (comment_description, comment_date, issue_id) VALUES (%s, %s, %s);"
	cursor.execute(update_select, (comment_description, str_now, issue_id))
	cursor.execute(sql_get_comment)
    	comments  = cursor.fetchall()
	con.commit()
    return render_template("issue.html", issue= issue[0], comments = comments)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
