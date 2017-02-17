#coding:utf8
from flask import Flask,session,render_template,request,redirect,flash
import RPi.GPIO as GPIO
import time
import os
import random
import dht11
import motor
import ledstart
from apscheduler.schedulers.background import BackgroundScheduler


def my_job():
	date=dht11.start()	
	#print date

sched = BackgroundScheduler()
sched.add_job(my_job,'interval',seconds=5)

app=Flask(__name__)
app.secret_key = 'some_secret'

user_list={'lz':'111'}
check=[]
date=[]
led1=[]
led2=[]

ledstart.webstart()
ledstart.ledstart()

@app.route('/', methods=['GET'])
def login_init():
#	sched.start()#                OK
#	sched.shutdown(wait=True)
	#date=dht11.start()
	#date.append(dht11.start())
	#print date	
	return render_template('login.html')

@app.route('/', methods=['POST'])
def login():
	#date=dht11.start()
	#sched.start()
	#print date
	if 'io1' in request.form:
		if request.form['io1']=='1':
			#flash('GPIO1 OPEN')
			#print check
                        led1[0]='1'
                        GPIO.output(20, GPIO.HIGH)
			return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])
		else:         
			led1[0]='0'
			GPIO.output(20, GPIO.LOW)
			return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])
	if 'io2' in request.form:
		if request.form['io2']=='1':
                        #led2.append('1')
			led2[0]='1'
			GPIO.output(21, GPIO.HIGH)
			return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])
		else:
                        #del(led2[:len(led2)])
			led2[0]='0'
			GPIO.output(21, GPIO.LOW)
			return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])
        if 'yuntai' in request.form:
                if request.form['yuntai']=='1':
                        motor.motorstart('l')
                        return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])
                else:
                        motor.motorstart('r')
                        return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])
	if 'sopen' in request.form:
		if request.form['sopen']=='1':
   			os.system('sudo service motion start')
			#time.sleep(0.5)
   			check[0]='1'
			return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])			
			#return render_template('index.html',sopen='1')
		else:
			os.system('sudo service motion stop')
			#time.sleep(0.2)
                        check[0]='0'
			return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])					
			#return render_template('index.html',sopen='0')
	if 'photo' in request.form:
		if request.form['photo']=='1':
			i=time.strftime('%m-%d-%H-%M-%S',time.localtime(time.time()))
			st='sudo fswebcam --no-banner -r 640x480 /home/lz/Desktop/picture/i.jpg'
			st=st[:62]+i+st[63:]
                        if check[0]=='1':
                                os.system('sudo service motion stop')			
                                os.system(st)
                                os.system('sudo service motion start')
                        else:
                                os.system(st)
                        ledstart.ledstart()
			return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])		
		else:
			return 'error'
	if 'teandhu' in request.form:
		if request.form['teandhu']=='1':
			date[0]=dht11.start()
			print date
			return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])
        if 'qita' in request.form:
                if request.form['qita']=='1':
                        dirlist=os.listdir('/dev')
                        if 'sda4' in dirlist:
                                os.system('sudo mount -t vfat /dev/sda4 /media/')
                        elif 'sdb4' in dirlist:
                                os.system('sudo mount -t vfat /dev/sdb4 /media/')
                        else:
                                return "Please input U Disk"
                        os.system('sudo cp -Rf /home/lz/motion-images/*.jpg /media/')
                        os.system('sudo cp -Rf /home/lz/Desktop/picture/*.jpg /media/')
                        os.system('sudo umount /media/')
                        os.system('sudo rm -r /home/lz/motion-images/*.jpg')
                        os.system('sudo rm -r /home/lz/Desktop/picture/*.jpg')
                        ledstart.ledstart()
                        return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])
                if request.form['qita']=='2':
                        os.system('sudo shutdown -r -t 5 now &')
                        return '正在重启，请稍后...'
                if request.form['qita']=='3':
                        os.system('sudo shutdown -h -t 5 now &')
                        return '正在关机，谢谢使用'
                
                
	if 'user' and 'password' in request.form:
		username=request.form['user']
		password=request.form['password']
		if username in user_list and password in user_list.values() and password==user_list[username]:
                        #GPIO.setmode(GPIO.BCM)
			GPIO.setup(20, GPIO.OUT)
			GPIO.setup(21, GPIO.OUT)
			date.append(dht11.start())
			led1.append('0')
			led2.append('0')
			check.append('0')
			print date		
			return render_template('index.html',sopen=check[0],led1=led1[0],led2=led2[0],temperature=date[0][0],humidity=date[0][1])
	    	else:
			
			flash('User or Password error,Please reinput')
			return render_template('login.html')

if __name__=='__main__':       
#	app.run(debug=True)
	app.run('192.168.191.20')
#	app.run('210.30.70.25')
#       app.run('192.168.43.225')
