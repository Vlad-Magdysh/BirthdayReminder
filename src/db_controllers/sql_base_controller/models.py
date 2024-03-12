from sqlalchemy import Column, Integer, String, ForeignKey, Date, UniqueConstraint, DateTime, Interval
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Birthday(Base):
    __tablename__ = "birthday"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    name = Column(String(20))
    surname = Column(String(20))

    notifications = relationship('Notification', secondary='birthdays_notifications', back_populates="birthdays", lazy=True)
    pre_reminders = relationship('PreReminder', secondary='birthdays_pre_reminders', back_populates="birthdays", lazy=True)


class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    text = Column(String())
    notification_type = Column(String(20))
    status = Column(String(10))
    created_on = Column(DateTime())

    birthdays = relationship(Birthday, secondary="birthdays_notifications", back_populates="notifications", lazy=True)


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

    birthdays = relationship(Birthday, secondary='birthdays_pre_reminders', back_populates="pre_reminders", lazy=True)
    time_delta_rule = relationship(TimeDeltaRule, uselist=False, foreign_keys=[rule_id])


class BirthdayNotificationAssociation(Base):
    __tablename__ = "birthdays_notifications"
    birthday_id = Column(Integer, ForeignKey("birthday.id"), primary_key=True)
    notification_id = Column(Integer, ForeignKey("notification.id"), primary_key=True)


class BirthdayPreReminderAssociation(Base):
    __tablename__ = "birthdays_pre_reminders"

    birthday_id = Column(Integer, ForeignKey("birthday.id"), primary_key=True)
    pre_reminder_id = Column(Integer, ForeignKey("pre_reminder.id"), primary_key=True)

