import pymysql
from connectdb import array as res

up_id = str(len(res))
print (up_id)


#Названия таблиц
db_messengers_forQ = "all_messengers"
db_manufactures_forQ = "manufactures"
db_messengers = "messenger_name"
db_os_forQ = "os_sup"
db_maxupload_forQ = "uploadmax"
db_yesorno_forQ = "yesorno"
#Колонки из главной таблицы
db_group_voice_chat = "supgc"
db_voice_messages = "supvs"
db_support_video = "supvideo"
db_support_os = "supos"
db_upload_max ="upmax"
db_manufacture = "manufact"
db_title = "name"

z = ","



db = pymysql.connect(host='dbhost',user = 'dbuser', password='dbpw',db='db',cursorclass=pymysql.cursors.SSCursor)


def max_upload(db_where, db_array):
	with db.cursor() as cursor:
		db.autocommit(True)
		db_string = "SELECT " + db_upload_max+","+db_group_voice_chat+","+db_voice_messages+","+db_support_video+","+db_support_os +","+db_manufacture+ " FROM "+ db_messengers_forQ + " WHERE name = '"+ db_where+"' "
		print(db_string)
			    
		cursor.execute(db_string)
		for row in cursor:
			db_array.append(row)
		print(db_array)
	cursor.close()
	return db_array



			    


def insert_db(db_array,man_value):
	with db.cursor() as cursor:
		db.autocommit(True)
		db_str = "INSERT INTO " + db_messengers_forQ+"("+db_title+z+db_manufacture+z+db_upload_max+z+db_support_os+z+db_voice_messages+z+db_group_voice_chat+z+db_support_video+")" + " VALUES "+ db_array 
		db_str_manuf = "INSERT INTO " + db_manufactures_forQ+"(manufactures_title,manufactures_id)" + " VALUES ('"+ man_value+"',"+up_id+")" 
		print(db_str_manuf)
			    
		cursor.execute(db_str)
		#cursor.execute(db_str_manuf)
		#for row in cursor:
			#db_array.append(row)
		#print(db_array)
	cursor.close()
	return db_array



	


