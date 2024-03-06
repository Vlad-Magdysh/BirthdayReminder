from sqlalchemy import Column, UUID, String, ForeignKey, Date, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(UUID, primary_key=True)
    nickname = Column(String(30), unique=True)
    daily_rule_id = Column(UUID, ForeignKey('rule.id'))

    birthdays = relationship('Birthday', lazy='joined')
    daily_rule = relationship('Rule', foreign_keys=[daily_rule_id], uselist=False, lazy='joined')


class Birthday(Base):
    __tablename__ = "birthday"
    id = Column(UUID, primary_key=True)
    date = Column(Date)
    name = String(20)
    surname = String(20)

    user_id = Column(UUID, ForeignKey(User.id), nullable=False)

    user = relationship(User, foreign_keys=[user_id], lazy='joined')
    notifications = relationship('Notification', lazy=True)
    pre_reminders = relationship('PreReminder', secondary="birthdays_pre_reminders", lazy='joined')


class Notification(Base):
    __tablename__ = "notification"
    id = Column(UUID, primary_key=True)
    text = String()
    status = String(10)
    created_on = DateTime()

    birthday_id = Column(UUID, ForeignKey(Birthday.id))

    birthday = relationship(Birthday, foreign_keys=[birthday_id], lazy='joined')


class Rule(Base):
    __tablename__ = "rule"
    id = Column(UUID, primary_key=True)
    created_on = DateTime()
    cron_expression = Column(String(30))


class PreReminder(Base):
    __tablename__ = "pre_reminder"
    id = Column(UUID, primary_key=True)
    type = Column(String(16), nullable=True)
    user_id = Column(UUID, ForeignKey(User.id), nullable=False)
    rule_id = Column(UUID, ForeignKey(Rule.id))

    user = relationship(User, foreign_keys=[user_id], lazy=True)
    birthdays = relationship(Birthday, secondary="birthdays_pre_reminders", lazy='joined')
    rule = relationship(Rule, foreign_keys=[rule_id], uselist=False, lazy='joined')


class BirthdayPreReminderAssociation(Base):
    __tablename__ = "birthdays_pre_reminders"
    birthday_id = Column(UUID, ForeignKey(Birthday.id), primary_key=True)
    pre_reminder_id = Column(UUID, ForeignKey(PreReminder.id), primary_key=True)
