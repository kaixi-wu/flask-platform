DATABASE = 'blog_test'
HOSTNAME = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'Zhangping890'
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI
