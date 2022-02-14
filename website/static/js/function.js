

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
function viewAvaibleLocal() {
    var div_ava = document.getElementById("AvaibleLocal");
    var div_hea = document.getElementById("HeadLocal");
    div_hea.style.display = "block";
    var div_loc = document.getElementById("LocalMenu");
    div_loc.style.display = "none";
    div_hea.style.display = "block";
    if (div_ava.style.display === "none") {
        div_ava.style.display = "block";
    } else {
        div_ava.style.display = "block";
    }
}
function viewLocalMenu(){
    var div_ava = document.getElementById("AvaibleLocal");
    div_ava.style.display = "none";
    var div_hea = document.getElementById("HeadLocal");
    div_hea.style.display = "none";
    var div_loc = document.getElementById("LocalMenu");
    div_loc.style.display = "block";
    var div_car = document.getElementById("Cart");
    div_car.style.display = "none";
}
function addCart(){
    var div_car = document.getElementById("Cart");
    div_car.style.display = "block";
}

function viewHistoryOrder() {
    var div_his = document.getElementById("HistoryOrder");
    var div_new = document.getElementById("NewOrder");
    var div_ava = document.getElementById("AvaibleLocal");
    var div_hea = document.getElementById("HeadLocal");
    var div_loc = document.getElementById("LocalMenu");
    div_loc.style.display = "none";
    if (div_his.style.display === "none") {
        div_his.style.display = "block";
        div_new.style.display = "none";
        div_ava.style.display = "none";
        div_hea.style.display = "none";
    } else {
        div_his.style.display = "none";
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
function viewShiftPage(){
    var div_shi = document.getElementById("ShiftPage");
    var div_ord = document.getElementById("OrderPage");
    if (div_shi.style.display === "none") {
        div_shi.style.display = "block";
        div_ord.style.display = "none";
    } else {
        div_shi.style.display = "none";
    }
}
function viewOrderPage(){
    var div_shi = document.getElementById("ShiftPage");
    var div_ord = document.getElementById("OrderPage");
    if (div_ord.style.display === "none") {
        div_ord.style.display = "block";
        div_shi.style.display = "none";
    } else {
        div_ord.style.display = "none";
    }
}
