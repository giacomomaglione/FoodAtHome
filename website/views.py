from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user
from .form import EditProfile, AddProduct, NewAddress
from . import cliente, rider, negozio, prodotto, ordine, prodottiordine
from .models import Cliente, Rider, Local
from . import login
from flask import session
from werkzeug.security import generate_password_hash
import bson

views = Blueprint('views', __name__)

@views.route("/")
def index():
    if current_user.is_anonymous == True:
        return render_template('index.html')
    if current_user.type==0:
        return redirect(url_for('views.customerindex'))
    if current_user.type==1:
        return redirect(url_for('views.riderindex'))
    if current_user.type==2:
        return redirect(url_for('views.localindex'))
    return render_template('index.html')

@views.route("/aboutus")
def about():
    return render_template('aboutus.html')


@views.route("/editprofile", methods=['GET', 'POST'])
@login_required
def editprofile():
    form = EditProfile()
    if request.method == 'POST':
        name = form.name.data
        surname = form.surname.data
        street = form.street.data
        city = form.city.data
        province = form.province.data
        date = form.date.data
        gender = form.gender.data
        telephone = form.telephone.data
        taxcode = form.taxcode.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method='sha256')
        id = form.id.data
        iban = form.iban.data
        localname = form.localname.data
        piva = form.piva.data

        if current_user.type == 0 :
            utente = cliente.find_one({"Email" : current_user.Email})
            if name != "" :
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Name": name}})
                form.name.data=""
            if surname != "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Surname": surname}})
            if street != "":
               cliente.update_one({'Email': utente['Email']}, {"$set": {"Street": street}})
            if city != "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"City": city}})
            if province !=  "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Province": province}})
            if date !=  "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Birthday": date}})
            if gender !=  None:
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Gender": gender}})
            if telephone !=  "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"PhoneNumber": telephone}})
            if taxcode !=  "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"TaxCode": taxcode}})
            if email != "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Email": email}})
            if password != "":
                cliente.update_one({'Email': utente['Email']}, {"$set": {"Password": password}})

        if current_user.type == 1 :
            utente = rider.find_one({"Email" : current_user.Email})
            if name !=  "" :
                rider.update_one({'Email': utente['Email']}, {"$set": {"Name": name}})
            if surname !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Surname": surname}})
            if street !=  "":
               rider.update_one({'Email': utente['Email']}, {"$set": {"Street": street}})
            if city !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"City": city}})
            if province !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Province": province}})
            if date !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Birthday": date}})
            if gender != None:
                rider.update_one({'Email': utente['Email']}, {"$set": {"Gender": gender}})
            if telephone !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"PhoneNumber": telephone}})
            if taxcode !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"TaxCode": taxcode}})
            if email !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Email": email}})
            if password !=  "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"Password": password}})
            if id != "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"ID": id}})
            if iban != "":
                rider.update_one({'Email': utente['Email']}, {"$set": {"IBAN": iban}})

        if current_user.type == 2:
            utente = negozio.find_one({"Email": current_user.Email})
            if name != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Name": name}})
            if surname != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Surname": surname}})
            if street != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Street": street}})
            if city != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"City": city}})
            if province != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Province": province}})
            if date != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Birthday": date}})
            if gender != None:
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Gender": gender}})
            if telephone != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"PhoneNumber": telephone}})
            if taxcode != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"TaxCode": taxcode}})
            if email != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Email": email}})
            if password != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"Password": password}})
            if id != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"ID": id}})
            if iban != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"IBAN": iban}})
            if piva != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"IVA": piva}})
            if localname != "":
                negozio.update_one({'Email': utente['Email']}, {"$set": {"LocalName": localname}})
    return render_template('editprofile.html' , form=form)




@views.route("/riderindex")
@login_required
def riderindex():
    if current_user.type != 1:
        return redirect(url_for('views.index'))
    queryorder=ordine.find({"Status": "0"})
    orderlist= []
    for order in queryorder:
        orderlist.append(order)
        local=negozio.find_one({"Email": order['Store']})
        localstreet=local["Street"]+", "+local["City"]+", "+local["Province"]
        client=cliente.find_one({"Email": order['Customer']})
        clientstreet=client["Street"]+", "+client["City"]+", "+client["Province"]
        print(local["Street"])

    return render_template('riderindex.html', list=orderlist, localstreet=localstreet , clientstreet=clientstreet)


@views.route("/localindex", methods=['GET', 'POST'])
@login_required
def localindex():
    if current_user.type != 2:
        return redirect(url_for('views.index'))

    prod_query = prodotto.find({"Store": current_user.Email})
    list = []
    for prod in prod_query:
        list.append(prod)
    form = AddProduct()
    if request.method == 'POST':
        nome = form.name.data
        description = form.description.data
        price = form.price.data
        if  nome != "" and description!= "" and price!= "":
            newproduct = {"Name": nome, "Description": description, "Price": price, "Store": current_user.Email}
            prodotto.insert_one(newproduct)
            flash("Prodotto aggiunto al menù")

    return render_template('localindex.html', list=list, form=form)


@views.route("/customerindex", methods=['GET', 'POST'])
@login_required
def customerindex():
    if current_user.type != 0:
        return redirect(url_for('views.index'))
    form = NewAddress()
    if request.method =='POST':
        province = form.province.data
        session['prov'] = province
        return redirect(url_for('views.createorder'))
    return render_template('customerindex.html', form=form)

@views.route("/createorder", methods=['GET', 'POST'])
@login_required
def createorder():
    if current_user.type != 0:
        return redirect(url_for('views.index'))

    if request.method == 'POST':
        session['store'] = request.form.get('idlocal')
        return redirect(url_for('views.selectproducts'))

    loc = []
    query = negozio.find({"Province" : session['prov']})
    for local in query:
        loc.append(local)

    return render_template('createorder.html', list = loc)

@views.route("/selectproducts", methods=['GET', 'POST'])
@login_required
def selectproducts():
    if current_user.type != 0:
        return redirect(url_for('views.index'))
    print(session['store'])

    if request.method == 'POST':
        product_id = request.form.get('product')
        qt = request.form.get('quantity')
        print(product_id)
        print(qt)

        if product_id and qt != 0:
            query = prodotto.find({"_id": bson.ObjectId(product_id)})
            row = query[0]
            print(row['Price'])
            qt = int(qt)
            row['_id'] = bson.ObjectId(product_id)
            itemArray = {product_id : {'Name' : row['Name'], 'Quantity' : qt, 'Price' : float(row['Price']), 'Total_price': qt * float(row['Price'])}}
            print(itemArray)

            all_total_price = 0
            all_total_quantity = 0
            session.modified = True
            if 'cart_item' in session:
                if  row['_id'] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if  row['_id'] == key:
                            #session.modified = True
                            #if session['cart_item'][key]['quantity'] is not None:
                            #session['cart_item'][key]['quantity'] = 0
                            old_quantity = session['cart_item'][key]['Quantity']
                            total_quantity = old_quantity + qt
                            session['cart_item'][key]['Quantity'] = total_quantity
                            session['cart_item'][key]['Total_price'] = total_quantity * float(row['Price'])
                else:
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)

                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['Quantity'])
                    individual_price = float(session['cart_item'][key]['Total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            else:
                session['cart_item'] = itemArray
                all_total_quantity = all_total_quantity + qt
                all_total_price = all_total_price + qt * float(row['Price'])

        session['all_total_quantity'] = all_total_quantity
        session['all_total_price'] = all_total_price
        print(session['all_total_quantity'])
        print(session['all_total_price'])
        #return redirect(url_for('selectproducts'))
    #else:
        #return 'Error while adding item to cart'

    products = []
    queryproducts = prodotto.find({"Store": session['store']})
    for prod in queryproducts:
        products.append(prod)

    return render_template('selectproducts.html', list=products)

@views.route("/orderhistory", methods=['GET', 'POST'])
@login_required
def orderhistory():
    historylist = []
    queryhistory = ordine.find({"Customer" : current_user.Email})
    for order in queryhistory:
        historylist.append(order)
        print(historylist)
        print(order)
        localname=negozio.find_one({"Email": order['Store']})

    return render_template('orderhistory.html', list=historylist , localname=localname)

def array_merge( first_array , second_array ):
	if isinstance( first_array , list ) and isinstance( second_array , list ):
		return first_array + second_array
	elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
		return dict( list( first_array.items() ) + list( second_array.items() ) )
	elif isinstance( first_array , set ) and isinstance( second_array , set ):
		return first_array.union( second_array )
	return False

@views.route("/confirmorder", methods=['GET', 'POST'])
@login_required
def confirmorder():
    flash("Ordine confermato")
    session.clear()
    return redirect(url_for('views.customerindex'))

@views.route("/deleteorder", methods=['GET', 'POST'])
@login_required
def deleteorder():
    flash("Ordine annullato")
    session.clear()
    return redirect(url_for('views.customerindex'))