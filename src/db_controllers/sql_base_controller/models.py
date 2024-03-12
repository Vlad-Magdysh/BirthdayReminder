from sqlalchemy import Column, Integer, String, ForeignKey, Date, UniqueConstraint, DateTime, Interval
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Birthday(Base):
    __tablename__ = "birthday"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date)
    name = Column(String(20))
    surname = Column(String(20))

    notifications = relationship('Notification', lazy=True)
    pre_reminders = relationship('PreReminder', secondary='BirthdayPreReminderAssociation')


class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String())
    notification_type = Column(String(20))
    status = Column(String(10))
    created_on = Column(DateTime())
    birthday_id = Column(Integer, ForeignKey("birthday.id"), nullable=False)

    birthday = relationship(Birthday, foreign_keys=[birthday_id], uselist=False, lazy=True)


class TimeDeltaRule(Base):
    __tablename__ = "timedelta_rule"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_on = Column(DateTime())
    timedelta = Column(Interval, nullable=False)


class PreReminder(Base):
    __tablename__ = "pre_reminder"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pre_reminder_type = Column(String(16), nullable=True)
    rule_id = Column(Integer, ForeignKey("timedelta_rule.id"))

    birthdays = relationship(Birthday, secondary='BirthdayPreReminderAssociation', lazy=True)
    time_delta_rule = relationship(TimeDeltaRule, uselist=False, foreign_keys=[rule_id])


class BirthdayPreReminderAssociation(Base):
    __tablename__ = "birthdays_pre_reminders"

    birthday_id = Column(Integer, ForeignKey("birthday.id"), primary_key=True)
    pre_reminder_id = Column(Integer, ForeignKey("pre_reminder.id"), primary_key=True)

