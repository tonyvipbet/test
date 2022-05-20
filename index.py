import pymysql.cursors

connection = pymysql.connect(host='bfcotlts7kofyk1ugalt-mysql.services.clever-cloud.com',
                             user='u2cugn8xgzyxngm8',
                             password='M3OlHagAUcJSkfBbVSfZ',
                             database='bfcotlts7kofyk1ugalt',
                             cursorclass=pymysql.cursors.DictCursor)

# with connection:
# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))


with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "CREATE TABLE `users` (`id` int(11) NOT NULL AUTO_INCREMENT,`email` varchar(255) COLLATE utf8_bin NOT NULL,`password` varchar(255) COLLATE utf8_bin NOT NULL,PRIMARY KEY(`id`)) "
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

print(connection)
