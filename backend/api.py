from flask import *
from database import *
import demjson
from search  import *

# from geopy.geocoders import Nominatim
# from geopy.distance import distance
# from geographiclib.geodesic import Geodesic

import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = ' http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = 'C:/Users/ACER/Desktop/Finale/Metroticket_recent/Metroticket/node_modules/.bin/build/contracts/metro.json'
# compiled_contract_path = 'F:/NGO/node_modules/.bin/build/contracts/medicines.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x135D150a48Cb119409782c7955dC516252A1d724'


api=Blueprint('api',__name__)


@api.route('/login')
def login():
	data={}
	uname=request.args['username']
	pwd=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(uname,pwd)
	print(q)
	w=select(q)
	if w:
		data['status']="success"
		data['data']=w
	else:
		data['status']="failed"
	return demjson.encode(data)

@api.route('/userregister')	
def userregister():
	data={}
	fn=request.args['fname']
	ln=request.args['lname']
	e=request.args['email']
	ad=request.args['address']
	ph=request.args['phone'] 
	pl=request.args['place']
	uname=request.args['username']
	pwd=request.args['password']
	q="select * from login where username='%s'"%(uname)
	res=select(q)
	if res:
		data['status']="duplicate"
	else:

		q="insert into login values (null,'%s','%s','user')"%(uname,pwd)
		id=insert(q)
		q="insert into users values (null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fn,ln,e,ad,ph,pl)
		insert(q)
		data['status']="success"
	return demjson.encode(data)


@api.route('/Userviewstation')
def Userviewstation():
	data={}
	
	q="select * from stations"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="Userviewstation"
	return demjson.encode(data)



@api.route('/Userrequest')
def Userrequest():
	data={}
	
	log=request.args['log']
	
	
	q="insert into request values(null,(select user_id from users where login_id='%s'),curdate(),'pending','0','0')"%(log)
	insert(q)
	print(q)
	data['status']="success"
	data['method']="Userrequest"
	return demjson.encode(data)



@api.route('/Userfirstrequestview')
def Userfirstrequestview():
	data={}
	
	log=request.args['lid']

	q="SELECT * FROM `request` where user_id=(select user_id from users where login_id='%s') "%(log)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="Userfirstrequestview"
	return demjson.encode(data)



@api.route('/Userviewrequest')
def Userviewrequest():
	data={}
	
	log=request.args['log']

	q="select * from request where  user_id=(select user_id from users where login_id='%s' ) and status='Accept' or status='In'"%(log)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="Userviewrequest"
	return demjson.encode(data)







@api.route('/Addamount')
def Addamount():
	data={}
	log=request.args['log']
	
	amount=request.args['amount']
	rid=request.args['rid']

	q="update request set amount='%s' where request_id='%s' "%(amount,rid)
	update(q)
	
	data['status']="success"
	data['method']="Addamount"
	return demjson.encode(data)



@api.route('/usermakepayment')
def usermakepayment():
	data={}
	
	amt=request.args['amt']
	fromplace=request.args['fromplace']
	toplace=request.args['toplace']
	rid=request.args['rid']

	q="insert into transaction values(null,'%s','%s','%s','%s',curdate())"%(rid,amt,fromplace,toplace)
	id=insert(q)

	q="insert into payment values(null,'%s','%s',now())"%(id,amt)
	insert(q)
	# q="update booking set status='paid' where booking_id='%s'"%(bid)
	# update(q)
	data['status']="success"
	return demjson.encode(data)


@api.route('/userviewstaff')
def userviewstaff():
	data={}
	q="select *,`staffs`.`place` as splace from staffs inner join stations using(station_id)"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)

@api.route('/userviewmaster')
def userviewmaster():
	data={}
	q="select *,`station_masters`.`place` as splace from station_masters inner join stations using(station_id)"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)



@api.route('/usersendmessage')
def usersendmessage():
	data={}
	types=request.args['type']
	log=request.args['log']
	logid=request.args['logid']
	message=request.args['message']
	q="insert into message values(null,'%s','user','%s','%s','%s','pending',now(),'0')"%(log,logid,types,message)
	insert(q)
	data['status']="success"
	data['method']="usersendmessage"
	return demjson.encode(data)


@api.route('/userviewmessage')
def userviewmessage():
	data={}
	types=request.args['type']
	log=request.args['log']
	logid=request.args['logid']
	q="select * from message where sender_id='%s' and receiver_id='%s' and receiver_type='%s'"%(log,logid,types)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="userviewmessage"
	return demjson.encode(data)



@api.route('/getstaffdetails')
def getstaffdetails():
	data={}
	sid=request.args['contents']
	q="select * from staffs inner join login using (login_id) inner join stations using (station_id) where staff_id='%s'"%(sid)
	res=select(q)
	print(q)

	station_name=res[0]['station_name']
	# geolocator = Nominatim(user_agent="my-custom-user-agen")
	# place1 = geolocator.geocode(station_name)
	
	# latitude = (place1.latitude)

	# longitude = (place1.longitude)
	
	data['data']=station_name
	data['status']="success"
	data['method']="getstaffdetails"

	return demjson.encode(data)


@api.route('/getstaffdetails2')
def getstaffdetails2():
	data={}
	sid=request.args['contents']
	q="select * from staffs inner join login using (login_id) inner join stations using (station_id) where staff_id='%s'"%(sid)
	res=select(q)
	print(q)

	station_name=res[0]['station_name']
	# geolocator = Nominatim(user_agent="my-custom-user-agen")
	# place1 = geolocator.geocode(station_name)
	
	# latitude = (place1.latitude)

	# longitude = (place1.longitude)
	
	data['data']=station_name
	data['status']="success"
	data['method']="getstaffdetails"

	return demjson.encode(data)





@api.route('/AndroidBarcodeQrExample4')
def AndroidBarcodeQrExample4():
	data={}
	lid=request.args['contents']
	rid=request.args['rid']
	fplace=request.args['place']
	
	# latitude=request.args['latitude']
	# longitude=request.args['longitude']
	logid=request.args['logid']

	total=request.args['amtss']


	q3="SELECT * FROM transaction WHERE user_id=(select  user_id from users where login_id='%s') AND STATUS='In'"%(logid)

	res3=select(q3)
	


	if res3:
		



		q5="select * from staffs inner join login using (login_id) inner join stations using (station_id) where staff_id='%s' "%(lid)
		res2=select(q5)
		print(q5)

		

		station_name=res2[0]['station_name']




		q1="SELECT * FROM transaction WHERE user_id=(select  user_id from users where login_id='%s')  AND STATUS='In'  and request_id='%s'"%(logid,rid)

		res1=select(q1)
		print(q1)

		tid=res1[0]['transaction_id']
		print(tid)



		lat,lon=checkplace(res1[0]['fromplace'])
		# print("from : ",flatis,flongis)
		
		latitude,longitude=checkplace(fplace)
		# print("to : ",tlatis,tlongis)
		# lat=res1[0]['fromplace']
		# print(lat)
		# lon=res1[0]['toplace']
		print("TRANS ",lat,lon)
		print("now ",latitude,longitude)

		

		



		from math import sin, cos, sqrt, atan2, radians

		import math

		# Approximate radius of earth in km
		R = 6373.0

		lat1 = radians(float(latitude))
		
		lon1 = radians(float(longitude))
		
		lat2 = radians(float(lat))
		lon2 = radians(float(lon))

		dlon = lon2 - lon1
		dlat = lat2 - lat1
		

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))

		distance = R * c

		
		# print("Should be: ", 278.546, "km")


		rounded_number = math.ceil(distance*100)/100  
		print(rounded_number)
		

		if res1:
			





			if res2[0]['user_type']=="staffsmetro":


				
			

				amts=rounded_number*10




			
				
				amts1=str(amts).split(".")
				sums=int(amts1[0])


				q="select sum(amount) as amount from transaction   where request_id='%s'  "%(rid)
				res5=select(q)
				sums=int(amts1[0])+int(res5[0]['amount'])
				print(sums)




				if amts1==0.0:

					data['status']="try"


				else:


				
				

					import datetime
					d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
					with open(compiled_contract_path) as file:
						contract_json = json.load(file)  # load contract info as JSON
						contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
						contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
						id=web3.eth.get_block_number()
					message = contract.functions.add_transactions(id,int(rid),str(sums),latitude,longitude,d,'out','complete',total).transact()

					# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amt,latitude,longitude)
					# insert(q)

					n="update transaction set amount='%s' , status='out', travelstatus='complete' where transaction_id='%s'"%(amts1[0],tid)
					update(n)


					q="update request set amount=amount-'%s' where request_id='%s'"%(amts1[0],rid)
					update(q)

					

					

					print(n)


					
				
				
					data['status']="success"
					data['method']="AndroidBarcodeQrExample"



			elif res2[0]['user_type']=="staffsboat":

				

				amts=rounded_number*6

				print(amts)
				
				amts2=str(amts).split(".")
				sums=int(amts2[0])
				q="select sum(amount) as amount from transaction   where request_id='%s'  "%(rid)
				res5=select(q)
				sums=int(amts2[0])+int(res5[0]['amount'])



				


				import datetime
				d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
				with open(compiled_contract_path) as file:
					contract_json = json.load(file)  # load contract info as JSON
					contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
					contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
					id=web3.eth.get_block_number()
				message = contract.functions.add_transactions(id,int(rid),str(sums),latitude,longitude,d,'out','complete',total).transact()

				# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amts2,latitude,longitude)
				# insert(q)

				g="update transaction set amount='%s' , status='out', travelstatus='complete' where transaction_id='%s'"%(amts2[0],tid)
				update(g)
				q="update request set amount=amount-'%s' where request_id='%s'"%(amts2[0],rid)
				update(q)

						
	
				
				# q="update payment set amount='%s' where transaction_id=(select transaction_id from transaction where user_id='%s')"%(amts2,lid)
				# update(q)
				data['status']="success"
				data['method']="AndroidBarcodeQrExample"




			elif res2[0]['user_type']=="staffsauto":

				
				amts=rounded_number*30

				print(amts)

				amts3=str(amts).split(".")
				sums=int(amts3[0])
				q="select * from transaction   where request_id='%s'  "%(rid)
				res5=select(q)
				sums=int(amts3[0])+int(res5[0]['amount'])


				
				

				import datetime
				d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
				with open(compiled_contract_path) as file:
					contract_json = json.load(file)  # load contract info as JSON
					contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
					contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
					id=web3.eth.get_block_number()
				message = contract.functions.add_transactions(id,int(rid),str(sums),latitude,longitude,d,'out','complete',total).transact()

				# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amts3,latitude,longitude)
				# insert(q)

				h="update transaction set `amount`='%s',`status`='out',`travelstatus`='complete' where transaction_id='%s'"%(amts3[0],tid)
				update(h)
				q="update request set amount=amount-'%s' where request_id='%s'"%(amts3[0],rid)
				update(q)

		
				
				# q="update payment set amount='%s' where transaction_id=(select transaction_id from transaction where user_id='%s')"%(amts3,lid)
				# update(q)
				data['status']="success"
				data['method']="AndroidBarcodeQrExample"






			elif res2[0]['user_type']=="staffsbus":

				
				amts=rounded_number*10

				print(amts)

				amts4=str(amts).split(".")
				sums=int(amts4[0])
				q="select sum(amount) as amount from transaction   where request_id='%s'  "%(rid)
				res5=select(q)
				sums=int(amts4[0])+int(res5[0]['amount'])


				
				

				import datetime
				d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
				with open(compiled_contract_path) as file:
					contract_json = json.load(file)  # load contract info as JSON
					contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
					contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
					id=web3.eth.get_block_number()
				message = contract.functions.add_transactions(id,int(rid),str(sums),latitude,longitude,d,'out','complete',total).transact()

				# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amts3,latitude,longitude)
				# insert(q)

				i="update transaction set `amount`='%s',`status`='out',`travelstatus`='complete' where transaction_id='%s'"%(amts4[0],tid)
				update(i)
				q="update request set amount=amount-'%s' where request_id='%s'"%(amts4[0],rid)
				update(q)

		
				
				# q="update payment set amount='%s' where transaction_id=(select transaction_id from transaction where user_id='%s')"%(amts3,lid)
				# update(q)
				data['status']="success"
				data['method']="AndroidBarcodeQrExample"



			elif res2[0]['user_type']=="staffscar":

				
				amts=rounded_number*30

				print(amts)

				amts5=str(amts).split(".")
				sums=int(amts5[0])
				q="select sum(amount) as amount from transaction   where request_id='%s'  "%(rid)
				res5=select(q)
				sums=int(amts5[0])+int(res5[0]['amount'])


				
				

				import datetime
				d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
				with open(compiled_contract_path) as file:
					contract_json = json.load(file)  # load contract info as JSON
					contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
					contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
					id=web3.eth.get_block_number()
				message = contract.functions.add_transactions(id,int(rid),str(sums),latitude,longitude,d,'out','complete',total).transact()

				# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amts3,latitude,longitude)
				# insert(q)

				j="update transaction set `amount`='%s',`status`='out',`travelstatus`='complete' where transaction_id='%s'"%(amts5[0],tid)
				update(j)
				q="update request set amount=amount-'%s' where request_id='%s'"%(amts5[0],rid)
				update(q)

		
				
				# q="update payment set amount='%s' where transaction_id=(select transaction_id from transaction where user_id='%s')"%(amts3,lid)
				# update(q)
				data['status']="success"
				data['method']="AndroidBarcodeQrExample"



	else:



		k="select * from staffs inner join login using (login_id)  where staff_id='%s' "%(lid)
		res4=select(k)
		print(k)


		




		if res4[0]['user_type']=="staffsmetro":


			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transactions(id,int(rid),'0',fplace,'metro',d,'In','Incomplete',total).transact()

			l="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','',curdate(),'In','Incomplete','%s')"%(logid,fplace,rid)
			
			id=insert(l)




			
		
			m="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(m)
			print(m)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"


		elif res4[0]['user_type']=="staffsauto":
			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transactions(id,int(rid),'0',fplace,'auto',d,'In','Incomplete',total).transact()

			n="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','',curdate(),'In','Incomplete','%s')"%(logid,fplace,rid)
			
			id=insert(n)
			
		
			o="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(o)
			print(o)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"


		elif res4[0]['user_type']=="staffsboat":


			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transactions(id,int(rid),'0',fplace,'boat',d,'In','Incomplete',total).transact()

			p="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','',curdate(),'In','Incomplete','%s')"%(logid,fplace,rid)
			
			id=insert(p)
			
		
			q="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(q)
			print(q)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"




		elif res4[0]['user_type']=="staffsbus":


			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transactions(id,int(rid),'0',fplace,'bus',d,'In','Incomplete',total).transact()

			r="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','',curdate(),'In','Incomplete','%s')"%(logid,fplace,rid)
			
			id=insert(r)
			
		
			s="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(s)
			print(s)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"




		elif res4[0]['user_type']=="staffscar":


			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transactions(id,int(rid),'0',fplace,'car',d,'In','Incomplete',total).transact()

			t="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','',curdate(),'In','Incomplete','%s')"%(logid,fplace,rid)
			
			id=insert(t)
			
		
			u="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(u)
			print(u)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"



	return str(data)



@api.route('/AndroidBarcodeQrExample')
def AndroidBarcodeQrExample():
	data={}
	lid=request.args['contents']
	
	latitude=request.args['latitude']
	longitude=request.args['longitude']





	logid=request.args['logid']


	q3="SELECT * FROM transaction WHERE user_id=(select  user_id from users where login_id='%s') AND STATUS='In'"%(logid)

	res3=select(q3)
	


	if res3:
		



		q5="select * from staffs inner join login using (login_id) inner join stations using (station_id) where staff_id='%s' "%(lid)
		res2=select(q5)
		print(q5)

		

		station_name=res2[0]['station_name']




		q1="SELECT * FROM transaction WHERE user_id=(select  user_id from users where login_id='%s')  AND STATUS='In'"%(logid)

		res1=select(q1)
		print(q1)

		tid=res1[0]['transaction_id']
		print(tid)




		lat=res1[0]['fromplace']
		print(lat)
		lon=res1[0]['toplace']

		

		print(lon)



		from math import sin, cos, sqrt, atan2, radians

		import math

		# Approximate radius of earth in km
		R = 6373.0

		lat1 = radians(float(latitude))
		print(lat1)
		lon1 = radians(float(longitude))
		print(lon1)
		lat2 = radians(float(lat))
		lon2 = radians(float(lon))

		dlon = lon2 - lon1
		dlat = lat2 - lat1
		print(dlon)
		print(dlat)

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))

		distance = R * c

		print("Result: ", distance)
		# print("Should be: ", 278.546, "km")


		rounded_number = math.ceil(distance*100)/100  
		print(rounded_number)
		

		if res1:
			print("res111111111111111111111111111",res2)





			if res2[0]['user_type']=="staffsmetro":


				
				print("res2222222211111111111111111111111111")

				amts=rounded_number*10




				print(amts ,"$$$$$$$$$$$$$$$$$$$$$$$$$$")

				
				amts1=str(amts).split(".")

				


				if amts1==0.0:

					data['status']="try"


				else:


				
				

					import datetime
					d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
					with open(compiled_contract_path) as file:
						contract_json = json.load(file)  # load contract info as JSON
						contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
						contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
						id=web3.eth.get_block_number()
					message = contract.functions.add_transaction(id,int(logid),str(amts1[0]),latitude,longitude,d,'out','complete').transact()

					# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amt,latitude,longitude)
					# insert(q)

					n="update transaction set amount='%s' , status='out', travelstatus='complete' where transaction_id='%s'"%(amts1[0],tid)
					update(n)

					

					

					print(n)


					
				
				
					data['status']="success"
					data['method']="AndroidBarcodeQrExample"



			elif res2[0]['user_type']=="staffsboat":

				

				amts=rounded_number*6

				print(amts)
				
				amts2=str(amts).split(".")
	


				


				import datetime
				d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
				with open(compiled_contract_path) as file:
					contract_json = json.load(file)  # load contract info as JSON
					contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
					contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
					id=web3.eth.get_block_number()
				message = contract.functions.add_transaction(id,int(logid),str(amts2[0]),latitude,longitude,d,'out','complete').transact()

				# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amts2,latitude,longitude)
				# insert(q)

				g="update transaction set amount='%s' , status='out', travelstatus='complete' where transaction_id='%s'"%(amts2[0],tid)
				update(g)

						
	
				
				# q="update payment set amount='%s' where transaction_id=(select transaction_id from transaction where user_id='%s')"%(amts2,lid)
				# update(q)
				data['status']="success"
				data['method']="AndroidBarcodeQrExample"




			elif res2[0]['user_type']=="staffsauto":

				
				amts=rounded_number*30

				print(amts)

				amts3=str(amts).split(".")
				


				
				

				import datetime
				d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
				with open(compiled_contract_path) as file:
					contract_json = json.load(file)  # load contract info as JSON
					contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
					contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
					id=web3.eth.get_block_number()
				message = contract.functions.add_transaction(id,int(logid),str(amts3[0]),latitude,longitude,d,'out','complete').transact()

				# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amts3,latitude,longitude)
				# insert(q)

				h="update transaction set `amount`='%s',`status`='out',`travelstatus`='complete' where transaction_id='%s'"%(amts3[0],tid)
				update(h)

		
				
				# q="update payment set amount='%s' where transaction_id=(select transaction_id from transaction where user_id='%s')"%(amts3,lid)
				# update(q)
				data['status']="success"
				data['method']="AndroidBarcodeQrExample"






			elif res2[0]['user_type']=="staffsbus":

				
				amts=rounded_number*10

				print(amts)

				amts3=str(amts).split(".")
				


				
				

				import datetime
				d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
				with open(compiled_contract_path) as file:
					contract_json = json.load(file)  # load contract info as JSON
					contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
					contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
					id=web3.eth.get_block_number()
				message = contract.functions.add_transaction(id,int(logid),str(amts3[0]),latitude,longitude,d,'out','complete').transact()

				# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amts3,latitude,longitude)
				# insert(q)

				i="update transaction set `amount`='%s',`status`='out',`travelstatus`='complete' where transaction_id='%s'"%(amts3[0],tid)
				update(i)

		
				
				# q="update payment set amount='%s' where transaction_id=(select transaction_id from transaction where user_id='%s')"%(amts3,lid)
				# update(q)
				data['status']="success"
				data['method']="AndroidBarcodeQrExample"



			elif res2[0]['user_type']=="staffscar":

				
				amts=rounded_number*30

				print(amts)

				amts3=str(amts).split(".")
				


				
				

				import datetime
				d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
				with open(compiled_contract_path) as file:
					contract_json = json.load(file)  # load contract info as JSON
					contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
					contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
					id=web3.eth.get_block_number()
				message = contract.functions.add_transaction(id,int(logid),str(amts3[0]),latitude,longitude,d,'out','complete').transact()

				# q="insert into transaction values(null,(select user_id from users where login_id='%s'),'%s','%s','%s',curdate(),'out','complete')"%(logid,amts3,latitude,longitude)
				# insert(q)

				j="update transaction set `amount`='%s',`status`='out',`travelstatus`='complete' where transaction_id='%s'"%(amts3[0],tid)
				update(j)

		
				
				# q="update payment set amount='%s' where transaction_id=(select transaction_id from transaction where user_id='%s')"%(amts3,lid)
				# update(q)
				data['status']="success"
				data['method']="AndroidBarcodeQrExample"



	else:



		k="select * from staffs inner join login using (login_id)  where staff_id='%s' "%(lid)
		res4=select(k)
		print(k)
		




		if res4[0]['user_type']=="staffsmetro":


			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transaction(id,int(logid),'0',latitude,longitude,d,'In','Incomplete').transact()

			l="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','%s',curdate(),'In','Incomplete','0')"%(logid,latitude,longitude)
			
			id=insert(l)




			
		
			m="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(m)
			print(m)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"


		elif res4[0]['user_type']=="staffsauto":
			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transaction(id,int(logid),'0',latitude,longitude,d,'In','Incomplete').transact()

			n="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','%s',curdate(),'In','Incomplete','0')"%(logid,latitude,longitude)
			
			id=insert(n)
			
		
			o="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(o)
			print(o)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"


		elif res4[0]['user_type']=="staffsboat":


			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transaction(id,int(logid),'0',latitude,longitude,d,'In','Incomplete').transact()

			p="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','%s',curdate(),'In','Incomplete','0')"%(logid,latitude,longitude)
			
			id=insert(p)
			
		
			q="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(q)
			print(q)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"




		elif res4[0]['user_type']=="staffsbus":


			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transaction(id,int(logid),'0',latitude,longitude,d,'In','Incomplete').transact()

			r="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','%s',curdate(),'In','Incomplete','0')"%(logid,latitude,longitude)
			
			id=insert(r)
			
		
			s="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(s)
			print(s)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"




		elif res4[0]['user_type']=="staffscar":


			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.add_transaction(id,int(logid),'0',latitude,longitude,d,'In','Incomplete').transact()

			t="insert into transaction values(null,(select user_id from users where login_id='%s'),'0','%s','%s',curdate(),'In','Incomplete','0')"%(logid,latitude,longitude)
			
			id=insert(t)
			
		
			u="insert into payment values(null,'%s','0',curdate())"%(id)
			insert(u)
			print(u)
			data['status']="success"
			data['method']="AndroidBarcodeQrExample"



	return str(data)



@api.route('/View_my_qr')
def View_my_qr():
	data={}
	login_id=request.args['lid']
	q="SELECT * FROM `staffs`   WHERE `login_id`='%s'"%(login_id)
	res=select(q)
	data['data']=res[0]['image']
	data['status']="success"
	return str(data)



@api.route('/viewspinnertoplace')
def viewspinnertoplace():
	data={}
	
	q="SELECT * FROM `stations` "
	res=select(q)

	data['data']=res

	data['status']="success"

	data['method']="viewspinnertoplace"
	return str(data)


@api.route('/viewspinnerfromplace')
def viewspinnerfromplace():
	data={}
	
	q="SELECT * FROM `stations` "
	res=select(q)

	data['data']=res

	data['status']="success"
	data['method']="viewspinnerfromplace"
	return str(data)



@api.route('/Userviewrequestssss')
def Userviewrequestssss():
	data={}
	rid=request.args['rid']
	q="SELECT * FROM `request` where request_id='%s'" %(rid)
	print(q)
	res=select(q)

	data['fplace']=res[0]['fplace']
	data['tplace']=res[0]['tplace']
	data['total']=res[0]['amount']

	q="select * from requestdetails where request_id='%s'" %(rid)
	res1=select(q)
	data['data1']=res1

	data['status']="success"
	data['method']="Userviewrequestssss"
	return str(data)


@api.route('/viewrequests')
def viewrequests():
	data={}
	lid=request.args['lid']
	q="SELECT * FROM `request` where user_id=(select user_id from users where login_id='%s')" %(lid)
	res=select(q)

	data['data']=res

	data['status']="success"
	data['method']="viewrequests"
	return str(data)



@api.route('/AddRequestss')
def AddRequestss():
	data={}
	rid=request.args['rid']
	
	fplace=request.args['fplace']
	tplace=request.args['tplace']
	types=request.args['types']
	flatis,flongis=checkplace(fplace)
	print("from : ",flatis,flongis)
	
	tlatis,tlongis=checkplace(tplace)
	print("to : ",tlatis,tlongis)

	# fromlati=request.args['fromlati']
	# fromlongi=request.args['fromlongi']
	# tolati=request.args['tolati']
	# tolongi=request.args['tolongi']

	if flatis=="" or flongis=="" or tlatis=="" or tlongis=="":
		data['status']="failed"
	else:

		from math import sin, cos, sqrt, atan2, radians
		import math

		# Approximate radius of earth in km
		R = 6373.0

		lat1 = radians(float(flatis))
		lon1 = radians(float(flongis))
		lat2 = radians(float(tlatis))
		lon2 = radians(float(tlongis))

		dlon = lon2 - lon1
		dlat = lat2 - lat1

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))

		distance = R * c

		print("Result: ", distance)
		rounded_number = math.ceil(distance*100)/100  
		print(rounded_number) 





		if types=="Metro":
			ss=rounded_number*10
		elif types=="Water":
			ss=rounded_number*6
		elif types=="Bus":
			ss=rounded_number*10
		elif types=="Car":
			ss=rounded_number*30
		elif types=="Auto":
			ss=rounded_number*30

			print(ss)

		rounded_numbers = math.ceil(ss*100)/100  
		print(rounded_numbers)
		amounts=rounded_numbers


		amounts=str(amounts).split(".")
		q="insert into requestdetails values(null,'%s','%s','%s','%s','%s','%s','%s')"%(rid,fplace,tplace,'0',types,amounts[0],amounts[0])
		id=insert(q)

		q="update request set amount=amount+'%s',totals=totals+'%s' where request_id='%s'" %(amounts[0],amounts[0],rid)
		update(q)
		data['status']="success"
	data['method']="AddRequestss"
	return str(data)

@api.route('/AddRequest')
def AddRequest():
	data={}
	login_id=request.args['login_id']
	
	fplace=request.args['fplace']
	tplace=request.args['tplace']
	q="insert into request values(null,(select user_id from users where login_id='%s'),curdate(),'0','0','0','%s','%s','')"%(login_id,fplace,tplace)
	id=insert(q)
	data['rid']=id
	data['status']="success"
	data['method']="AddRequest"
	return str(data)

@api.route('/Viewtrancation')
def Viewtrancation():
	data={}
	lid=request.args['lid']

	# q="select * from transaction where user_id=(select user_id from login where login_id='%s')"%(lid)
	# res1=select(q)
	# user_id=res1[0]['user_id']

	
	
	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			print(decoded_input)
			if str(decoded_input[0]) == "<Function add_transactions(uint256,uint256,string,string,string,string,string,string,string)>":
				# if int(decoded_input[1]['user_id']) == int(['user_id']):
					res.append(decoded_input[1])

					
					# if decoded_input[1]['passportnum']==pno:
					# 	flash("verified")

	except Exception as e:
		print("", e)
	
	data['data']=res


	data['status']="success"


	return str(data)



@api.route('/verified')
def verified():
	data={}
	rid=request.args['rid']
	q="SELECT * FROM `request`  WHERE `request_id`='%s'  order by  request_id desc "%(rid)
	res=select(q)
	totals=res[0]['totals']
	data['nt']=totals
	print(totals)


	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			print(decoded_input)
			if str(decoded_input[0]) == "<Function add_transactions(uint256,uint256,string,string,string,string,string,string,string)>":
				# if int(decoded_input[1]['user_id']) == int(['user_id']):
					res.append(decoded_input[1])
					if int(decoded_input[1]['request_id'])==int(rid):
						# flash("verified")
						print("Verified")
						data['outs']="Verified with Blockchain data"
						data['bt']=decoded_input[1]['total']
						break
					else:

						data['outs']="Not Verifed. Data Mismatch"
						data['bt']=decoded_input[1]['total']

	except Exception as e:
		print("", e)

	data['data']=res
	data['status']="success"
	data['method']="verified"
	return str(data)