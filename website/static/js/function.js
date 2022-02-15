

function signinLocalControl() {
    var nome = document.getElementById("Name").value
    if(nome == "")
        alert(" il campo 'Nome' è vuoto")
    var cognome = document.getElementById("Surname").value
    if(cognome == "")
        alert(" il campo 'Cognome' è vuoto")
    var indirizzo = document.getElementById("Address").value
    if(indirizzo == "")
        alert(" il campo 'Indirizzo' è vuoto")
    var data = document.getElementById("Date").value
    if(data == "")
        alert(" il campo 'Data' è vuoto ")
    var telefono = document.getElementById("Telephone").value
    if(telefono == "")
        alert(" il campo 'Numero di cellulare' è vuoto")
    var fiscale = document.getElementById("Taxcode").value
    if(fiscale == "")
        alert(" il campo 'Codice fiscale' è vuoto")
    var documento = document.getElementById("Document").value
    if(documento == "")
        alert(" il campo 'Documento' è vuoto")
    var iban = document.getElementById("Iban").value
    if(iban == "")
        alert(" il campo 'IBAN' è vuoto")
    var iva = document.getElementById("Iva").value
    if(iva == "")
        alert(" il campo 'Partita IVA' è vuoto")
    var locale = document.getElementById("LocalName").value
    if(locale == "")
        alert(" il campo 'Nome del locale' è vuoto")
    var email = document.getElementById("Email").value
    if(email == "")
        alert(" il campo 'Email' è vuoto")
    var password = document.getElementById("Password").value
    if(password == "")
        alert(" il campo 'Password' è vuoto")
}

function signinClientControl() {
    var nome = document.getElementById("Name").value
    if(nome == "")
        alert(" il campo 'Nome' è vuoto")
    var cognome = document.getElementById("Surname").value;
    if(cognome == "")
        alert(" il campo 'Cognome' è vuoto")
    var indirizzo = document.getElementById("Address").value
    if(indirizzo == "")
        alert(" il campo 'Indirizzo' è vuoto")
    var data = document.getElementById("Date").value
    if(data == "")
        alert(" il campo 'Data' è vuoto ")
    var telefono = document.getElementById("Telephone").value
    if(telefono == "")
        alert(" il campo 'Numero di cellulare' è vuoto")
    var fiscale = document.getElementById("Taxcode").value
    if(fiscale == "")
        alert(" il campo 'Codice fiscale' è vuoto")
    var email = document.getElementById("Email").value
    if(email == "")
        alert(" il campo 'Email' è vuoto")
    var password = document.getElementById("Password").value
    if(password == "")
        alert(" il campo 'Password' è vuoto")
}

function signinRiderControl() {
    var nome = document.getElementById("Name").value
    if(nome == "")
        alert(" il campo 'Nome' è vuoto")
    var cognome = document.getElementById("Surname").value;
    if(cognome == "")
        alert(" il campo 'Cognome' è vuoto")
    var indirizzo = document.getElementById("Address").value
    if(indirizzo == "")
        alert(" il campo 'Indirizzo' è vuoto")
    var data = document.getElementById("Date").value
    if(data == "")
        alert(" il campo 'Data' è vuoto ")
    var telefono = document.getElementById("Telephone").value
    if(telefono == "")
        alert(" il campo 'Numero di cellulare' è vuoto")
    var fiscale = document.getElementById("Taxcode").value
    if(fiscale == "")
        alert(" il campo 'Codice fiscale' è vuoto")
    var documento = document.getElementById("Document").value
    if(documento == "")
        alert(" il campo 'Documento' è vuoto")
    var iban = document.getElementById("Iban").value
    if(iban == "")
        alert(" il campo 'IBAN' è vuoto")
    var email = document.getElementById("Email").value
    if(email == "")
        alert(" il campo 'Email' è vuoto")
    var password = document.getElementById("Password").value
    if(password == "")
        alert(" il campo 'Password' è vuoto")
}


function upperCase() {
    const f = document.getElementById("Taxcode");
    f.value = f.value.toUpperCase();
    const d = document.getElementById("Document");
    d.value = d.value.toUpperCase();
    const ib = document.getElementById("Iban");
    ib.value = ib.value.toUpperCase();
    const iv = document.getElementById("Iva");
    iv.value = iv.value.toUpperCase();
}


<!--Controlli Cliente -->
function viewNewOrder() {
    var div_new = document.getElementById("NewOrder");
    if (div_new.style.display === "none") {
        div_new.style.display = "block";
    } else {
        div_new.style.display = "none";
    }
}
function viewCart() {
    var div_new = document.getElementById("Cart");
    if (div_new.style.display === "none") {
        div_new.style.display = "block";
    } else {
        div_new.style.display = "none";
    }
}


<!--Controlli Locale-->
function viewMenuList() {
    var div_menu = document.getElementById("MenuList");
    var div_ins = document.getElementById("InsertProduct");
    if (div_menu.style.display === "none") {
        div_menu.style.display = "block";
        div_ins.style.display = "none";
    } else {
        div_menu.style.display = "none";
        div_ins.style.display = "none";
    }
}
function viewInsertProduct() {
    var div_ins = document.getElementById("InsertProduct");
    var div_menu = document.getElementById("MenuList");
    if (div_ins.style.display === "none") {
        div_ins.style.display = "block";
        div_menu.style.display = "none";
    } else {
        div_ins.style.display = "none";
    }
}


<!--Controlli Rider-->
function viewOrderPage(){
    var div_ord = document.getElementById("OrderPage");
    if (div_ord.style.display === "none") {
        div_ord.style.display = "block";
    } else {
        div_ord.style.display = "none";
    }
}
function viewOrderSpec(){
    var div_ord = document.getElementById("OrderSpec");
    if (div_ord.style.display === "none") {
        div_ord.style.display = "block";
    } else {
        div_ord.style.display = "none";
    }
}
