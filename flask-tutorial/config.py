# from urllib import parse
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
#
#
# class _SystemConfig:
#     AUTH_TYPE = 'SSO'  # 身份验证机制 SSO, test_platform
#     ACCESS_TOKEN_TIME_OUT = 2 * 60 * 60  # access_token 有效期，2个小时
#     REFRESH_TOKEN_TIME_OUT = 7 * 24 * 60 * 60  # refresh_token 有效期，7天
#     SECRET_KEY = "quark"
#     URL_NOT_FIND_MSG = None  # 统一自定义404消息，若没有对应使用场景设为None即可
#
#     # 数据库信息
#     # DB_HOST = "rm-t4n300f87dms0ucrw.mysql.singapore.rds.aliyuncs.com"  # 内网
#     DB_HOST = "127.0.0.1"
#     # DB_HOST = "rm-t4n300f87dms0ucrwuo.mysql.singapore.rds.aliyuncs.com"  # 外网
#     DB_PORT = 3306
#     # DB_USER = "autotest"
#     # DB_PASSWORD = "#73oFYuE"
#     # DB_DATABASE = "autotest"
#     DB_USER = "root"
#     DB_PASSWORD = "Zhangping890"
#     DB_DATABASE = "user"
#
#     # 数据库链接
#     SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{parse.quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?autocommit=true"
#
#     # 关闭数据追踪，避免内存资源浪费
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     # 关闭自动提交，若开启自动提交会出现以下报错
#     # sqlalchemy.exc.InvalidRequestError: Can"t reconnect until invalid transaction is rolled back
#     SQLALCHEMY_COMMIT_ON_TEARDOWN = False
#
#     # 每次连接从池中检查，如果有错误，监测为断开的状态，连接将被立即回收。
#     SQLALCHEMY_POOL_PRE_PING = True
#
#     # 数据库连接池的大小。默认是数据库引擎的默认值默认是5
#     SQLALCHEMY_POOL_SIZE = 10
#
#     # 当连接池达到最大值后可以创建的连接数。当这些额外的连接处理完回收后，若没有在等待进程获取连接，这个连接将会被立即释放。
#     SQLALCHEMY_MAX_OVERFLOW = 100
#
#     # 从连接池里获取连接
#     # 如果此时无空闲的连接，且连接数已经到达了pool_size+max_overflow。此时获取连接的进程会等待pool_timeout秒。
#     # 如果超过这个时间，还没有获得将会抛出异常。
#     # 默认是30秒
#     SQLALCHEMY_POOL_TIMEOUT = 30
#
#     # 一个数据库连接的生存时间。
#     #     例如pool_recycle=3600。也就是当这个连接产生1小时后，再获得这个连接时，会丢弃这个连接，重新创建一个新的连接。
#     #
#     # 当pool_recycle设置为-1时，也就是连接池不会主动丢弃这个连接。永久可用。但是有可能数据库server设置了连接超时时间。
#     #     例如mysql，设置的有wait_timeout默认为28800，8小时。当连接空闲8小时时会自动断开。8小时后再用这个连接也会被重置。
#     SQLALCHEMY_POOL_RECYCLE = 3600  # 1个小时
#
#     # 输出SQL语句
#     # SQLALCHEMY_ECHO = True
#
#     # flask_apscheduler 定时任务存储配置
#     SCHEDULER_JOBSTORES = {
#         "default": SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
#     }
#     # flask_apscheduler 线程池配置
#     SCHEDULER_EXECUTORS = {
#         "default": {"type": "threadpool", "max_workers": 20}
#     }
#     SCHEDULER_JOB_DEFAULTS = {
#         "coalesce": False,
#         "max_instances": 2,
#         "misfire_grace_time": None
#     }
#     SCHEDULER_TIMEZONE = "Asia/Shanghai"  # 时区
#     SCHEDULER_API_ENABLED = True  # 开启API访问功能
#     SCHEDULER_API_PREFIX = "/api/scheduler"  # api前缀（默认是/scheduler）
