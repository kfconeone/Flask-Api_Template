from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .. import db




class User(db.Model):
    __tablename__ = 'User'

    Name = db.Column(db.String(50), primary_key=True)
    age = db.Column(db.Integer, nullable=False)


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False, unique=True, server_default='')


class Player_Status(db.Model):
    __tablename__ = 'Player_Status'

    PlayerId = db.Column(db.String(50), primary_key=True, nullable=False, server_default='0000000000')
    AccountName = db.Column(db.String(50), primary_key=True, nullable=False, index=True, server_default='NULL')
    Language = db.Column(db.String(10), nullable=False, server_default='ZH_TW')
    Country = db.Column(db.String(10), server_default='TW')
    DeviceId = db.Column(db.String(50), server_default='NULL')
    FBId = db.Column(db.String(50), index=True, server_default='')
    Password = db.Column(db.String(100))
    PlayerMoney = db.Column(db.BigInteger, nullable=False, server_default='0')
    BonusCount = db.Column(db.Integer, nullable=False, server_default='0')
    LastReverseMoneyDate = db.Column(db.Date)
    GamblingChip = db.Column(db.BigInteger, nullable=False, server_default='0')
    DP = db.Column(db.Integer, nullable=False, server_default='0')
    GP = db.Column(db.Float(asdecimal=True), nullable=False, server_default='0')
    TodayUsedGp = db.Column(db.Integer, nullable=False, server_default='0')
    VipLevel = db.Column(db.SmallInteger, nullable=False, server_default='0')
    LimitedVipLevel = db.Column(db.SmallInteger, nullable=False, server_default='0')
    RegisterDate = db.Column(db.Date)
    LastLoginDate = db.Column(db.DateTime)
    IsRecoveryMoney = db.Column(db.BINARY(1), nullable=False)
    NickName = db.Column(db.String(50), unique=True)
    IsModifyNickName = db.Column(db.BINARY(1), nullable=False)
    Exp = db.Column(db.Float(asdecimal=True), nullable=False, server_default='0')
    PlayerLevel = db.Column(db.SmallInteger, nullable=False, server_default='0')
    EMail = db.Column(db.String(50))
    PhoneNumber = db.Column(db.String(50))

