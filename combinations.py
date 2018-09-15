import os
import io
import re
from nltk import sent_tokenize
import MySQLdb as mariadb
con =  mariadb.connect(host="localhost" ,port= 3360, user="root", passwd="password", db="entries")

cursor = con.cursor()

char_list = [",", "-", "."]
failed = []

def check_valid_word(word):
    return (any(c.islower() for c in word)) and (len(word) > 1)


for f in os.listdir("books"):
    print "book: " + f 

    file = io.open(os.path.join("books", f), mode="r", encoding="utf-8").read()
    sentences = sent_tokenize(file)

    for sentence in sentences:
        word_list = sentence.split()
        for i in range(len(word_list)):
            if check_valid_word(word_list[i]):
                phrase = word_list[i]
                phrase_count = len(phrase)
                if phrase_count < 20:
                    for j in range(i+1, len(word_list)):
                        if check_valid_word(word_list[j]):
                            phrase += " " + word_list[j]
                            if len(phrase) > 12:
                                break
                            else:
                                # phrase = re.sub("".join(char_list), "", phrase.lower())
                                phrase = re.sub('[?,.!;":_]', "", phrase.lower())
                                # phrase = re.sub(".", "", phrase)
                                phrase = re.sub("".join(char_list), "", phrase.lower())
                                phrase = phrase.replace('"', '')
                                phrase = phrase.replace("[", "")
			        phrase = phrase.replace("]", "")
				phrase = phrase.encode('ascii', errors='ignore')
                                ordered_phrase = ''.join(sorted(phrase))
                                ordered_phrase = ordered_phrase.strip()
                                ordered_phrase = ordered_phrase.replace("'", "")
                                ordered_phrase = ordered_phrase.replace("-", "")
                                #print "phrase:" + phrase
                                #print "ordered_phrase:  " + ordered_phrase
                                # print "book: " + f
                                sql = 'SELECT * FROM sentences WHERE orderd_sentence="%s"' % ordered_phrase
                                cursor.execute(sql)
                                results = cursor.fetchall()
				if len(results) == 0 :
                                    update_select = 'INSERT INTO sentences (sentence, orderd_sentence) VALUES ("%s", "%s");' %(phrase, ordered_phrase )
                                    try:
					print "phrase:" + phrase
                                	print "ordered_phrase:  " + ordered_phrase
                                	print "book: " + f
					cursor.execute(update_select)
                                        con.commit()
                                    except:
                                        failed.append(phrase)

                        else:
			    print results
                            break

            else:
                break

con.close()
