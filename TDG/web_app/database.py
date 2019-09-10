from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary, Float
from sqlalchemy.schema import ForeignKey
from sqlalchemy import create_engine
from passlib.hash import bcrypt
from flask_login import UserMixin

Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, primary_key=True)
    name = Column(String(15), unique=True)
    password = Column(String(255))
    email = Column(String(120), unique=True)
    avatar = Column(LargeBinary)
    role = Column(Integer)

    def __init__(self, name, password, email):
        self.password = bcrypt.encrypt(password)
        self.name = name
        self.email = email

    def verify_password(self, attempted_password):
        return bcrypt.verify(attempted_password, self.password)

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return 'User(id=%d, name=%s, email=%s)' % (self.user_id, self.name, self.email)


class FileHistory(Base):
    __tablename__ = 'file_hist'
    __table_args__ = {'extend_existing': True}
    file_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.user_id, onupdate='CASCADE', ondelete='CASCADE'))
    records_no = Column(Integer)
    ratio = Column(Integer)
    headers = Column(String(3))
    login_min_length = Column(Integer)
    login_max_length = Column(Integer)
    login_textarea_custom = Column(String(20))
    pass_min_length = Column(Integer)
    pass_max_length = Column(Integer)
    pass_textarea_custom = Column(String(20))
    file_path = Column(String(255))
    file_extension = Column(String(5))
    created_at = Column(Float)

    def __repr__(self):
        return 'File(user_id=%d, file_path=%s)' % (self.user_id, self.file_path)


class LoginHistory(Base):
    __tablename__ = 'login_hist'
    __table_args__ = {'extend_existing': True}
    login_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.user_id, onupdate='CASCADE', ondelete='CASCADE'))
    ip = Column(String(30))
    login_time = Column(Float)

    def __repr__(self):
        return 'Login(user_id=%d, ip=%s)' % (self.user_id, self.ip)


def init_db(db_type, db_name):
    engine = create_engine('%s:///%s' % (db_type, db_name), convert_unicode=True, echo=False)
    session_maker = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    return session_maker


def drop_tables(db_type, db_name):
    engine = create_engine('%s:///%s' % (db_type, db_name), convert_unicode=True, echo=False)
    Base.metadata.drop_all(bind=engine)
