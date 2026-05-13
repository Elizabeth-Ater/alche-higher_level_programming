-- the mysql command-line tool or a MySQL client application.

CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1. 
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost WITH GRANT OPTION;

-- Flush privileges to apply the changes.
FLUSH PRIVILEGES;

EXIT
