import MySQLdb
import MySQLdb.cursors
import requests
import hashlib
import urllib2
import pdb
import re
import os
from django.http import *
from django.shortcuts import render, redirect
from settings import *

def getDBOject(db_name):
    db = MySQLdb.connect(MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD,db_name)
    return db

db_name = "amsrec"

def home(request):
    return render(request,'homepage.html')


def ainfopage(request):
    return render(request,'airlineinfo.html')
    
def ainfo(request):
    if request.method == 'POST':
        iatacode = request.POST.get('iata_code')
        #print iatacode
        db = getDBOject(db_name)
        cursor = db.cursor()
        sql = "SELECT iata_code, airline_name, off_add FROM airlines where iata_code = '%s' " %(iatacode) 
        cursor.execute(sql)
        rows  = cursor.fetchall()
        #print rows
        return render(request,'test.html',{'rows':rows})

def departinfo(request):
    return render(request,'depart.html')


def depart(request):
    if request.method == 'POST':
        name = request.POST.get('cname')
        db = getDBOject(db_name)
        cursor = db.cursor()
        sql = "SELECT distinct f.fid, a.airline_name, f.time from departures d, flights f, oth_airports o, airlines a where f.fid=d.fid AND f.iata_code=a.iata_code AND d.dest=o.iata AND o.airport_name = '%s'" % (name)
        cursor.execute(sql)
        rows = cursor.fetchall()
        return render(request,'departresult.html',{'rows':rows})

def arrinfo(request):
    return render(request,'arrinfo.html')

def arrquery(request):
    if request.method == 'POST':
        name = request.POST.get('cname')
        db = getDBOject(db_name)
        cursor = db.cursor()
        sql = "SELECT distinct f.fid, a.airline_name,f.time,f.status from arrivals ar, flights f, oth_airports o, airlines a where f.fid=ar.fid AND f.iata_code=a.iata_code AND ar.source=o.iata AND o.airport_name = '%s'" % (name)
        cursor.execute(sql)
        rows = cursor.fetchall()
        return render(request,'arrresult.html',{'rows':rows})


def test(request):
    db = getDBOject(db_name)
    cursor = db.cursor()
    sql = "SELECT iata_code, airline_name, off_add FROM airlines " 
    cursor.execute(sql)
    rows  = cursor.fetchall()
    #print rows
    return render(request,'test.html',{'rows':rows})

def addinfo(request):
    return render(request,'addfinfo.html')

def addfun(request):
    if request.method == 'POST':
        fid    = request.POST.get('fid')
        status = request.POST.get('status')
        date   = request.POST.get('date')
        time   = request.POST.get('time')
        db = getDBOject(db_name)
        cursor = db.cursor()
        sql = "INSERT into flights (fid,status,date,time) VALUES (%s,%s,%s,%s)"
        values = (str(fid),str(status),str(date),str(time))
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return render(request,'thnx.html')

def login(request):
    return render(request,'login.html')

def auth_user(request):
    if request.method == 'POST':
        uname = request.POST.get('user_name')
        password = request.POST.get('password')
        password = hashlib.md5(password)
        db = getDBOject(db_name)
        cursor = db.cursor()
        sql = "SELECT username, password from users where username = '%s' and password = '%s'" % (uname) (password)
        cursor.execute(sql)
        
        
        



