from flask import *
from database import *
import uuid
import qrcode

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


admin=Blueprint('admin',__name__)
@admin. route('/adminhome')
def adminhome():

	return render_template('adminhome.html')
@admin. route('/station',methods=['post','get'])
def station():
	data={}
	q="select * from stations"
	r=select(q)
	data['stations']=r
	if "submit" in request.form:
		nooo=request.form['name']
		
		
		q="insert into stations values (null,'%s')"%(nooo)
		res=insert(q)
		return redirect(url_for('admin.station'))
	
	if'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from stations where station_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.station'))
	if action=='update':
		q="select * from stations where station_id='%s'"%(id)
		r=select(q)
		data['pro']=r
	if "update" in request.form:
		n=request.form['sname']
	
		
		q="update stations set station_name='%s' where station_id='%s'"%(n,id)
		update(q)
		return redirect(url_for('admin.station'))
	return render_template('station.html',data=data)


@admin.route('/users',methods=['post','get'])
def users():
	data={}
	q="select * from users"
	r=select(q)
	data['users']=r
	return render_template('users.html',data=data)




@admin.route('/addamount',methods=['post','get'])
def addamount():
	
	if "add" in request.form:
		amount=request.form['amount']
		rid=request.args['rid']
		q="update request set amount='%s' , status='amountadd' where request_id='%s'"%(amount,rid)
		update(q)
		return redirect(url_for('admin.viewrequest'))
	return render_template('addamount.html')

@admin.route('/viewrequest',methods=['post','get'])
def viewrequest():
	data={}
	q="select * from request inner join users USING (user_id)"
	r=select(q)
	data['request']=r



	if "action" in request.args:
		action=request.args['action']
		aid=request.args['aid']


	else:
		action=None


	if action=="accept":


		path="static/qr_code/"+str(uuid.uuid4())+".png"
		s=qrcode.make(str(aid))
		s.save(path)
		print(s)
		q="update request set status='Accept', image='%s' where user_id='%s'"%(path,aid)
		update(q)

		print(q)
		



		return redirect(url_for('admin.viewrequest'))



	if action=="reject":
		q="update request set status='Reject' where user_id='%s'"%(aid)
		update(q)

		return redirect(url_for('admin.viewrequest'))

	return render_template('viewrequest.html',data=data)


@admin. route('/staffs',methods=['post','get'])
def staffs():
	data={}
	q="select * from stations"
	r=select(q)
	print(r)
	data['st']=r


	q="select * from staffs   inner join stations using (station_id)  inner join login using (login_id)"
	r=select(q)
	data['staff']=r
	if "submit" in request.form:
		s=request.form['station']
		f=request.form['fname']
		
		n=request.form['name']
		p=request.form['password']
		types=request.form['type']

		
		q="insert into login values (null,'%s','%s','%s')"%(n,p,types)
		res=insert(q)
		print(q)
		q="insert into staffs values (null,'%s','%s','%s','0')"%(res,s,f)
		print(q)
		sid=insert(q)
		path="static/qr_code/"+str(uuid.uuid4())+".png"
		s=qrcode.make(str(sid))
		s.save(path)

		q="update staffs set image='%s' where staff_id='%s'"%(path,sid)
		update(q)

		return redirect(url_for('admin.staffs'))
	if'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from staffs where staff_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.staffs'))
	if action=='update':
		q="select * from staffs where staff_id='%s'"%(id)
		r=select(q)
		data['pro']=r
	if "submit" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		e=request.form['email']
		a=request.form['address']
		no=request.form['number']
		p=request.form['place']
		qu=request.form['Qualification']
		
		q="update staffs set first_name='%s',last_name='%s',email='%s',address='%s',number='%s',place='%s',Qualification='%s' where staffs_id='%s'"%(n,no,p,id)
		update(q)
		return redirect(url_for('admin.staffs'))

	return render_template('staff.html',data=data)



@admin.route('/track')
def track():
	data={}
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
			if str(decoded_input[0]) == "<Function add_transaction(uint256,uint256,string,string,string,string,string,string)>":
				# if int(decoded_input[1]['u_id']) == int(session['user_id']):
					res.append(decoded_input[1])

					
					# if decoded_input[1]['passportnum']==pno:
					# 	flash("verified")

	except Exception as e:
		print("", e)
	print(res)

	data['pass']=res


	return render_template('track.html',data=data)