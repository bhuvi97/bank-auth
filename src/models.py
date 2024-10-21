from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create a base class for our models
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    dob = Column(Date, nullable=False)  # Date of Birth as Date
    phone_number = Column(String(15), nullable=False)

    def __repr__(self):
        return (f"<User(id={self.id}, first_name='{self.first_name}', "
                f"last_name='{self.last_name}', email='{self.email}')>")


class UserCredentials(Base):
    __tablename__ = 'user_credentials'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    username = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Optional relationship to user
    user = relationship("User", back_populates="credentials")
