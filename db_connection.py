import MySQLdb as mariadb
import re
con =  mariadb.connect(host="localhost" ,port= 3360, user="root", passwd="password", db="entries")
cursor = con.cursor()
letters = raw_input("Enter the letters:  ")
ordered_letters = ''.join(sorted(letters))

sql1 = "SELECT word,definition FROM entries WHERE orderd_word='%s'" % ordered_letters
sql2 = "SELECT sentence FROM sentences WHERE orderd_sentence='%s'" % ordered_letters
print sql1
cursor.execute(sql1)
results = cursor.fetchall()
for row in results:
    print row
#cursor.execute(sql2)
#results = cursor.fetchall()
#for row in results:
#    print row

con.close()
