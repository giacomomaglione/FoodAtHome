

function signinLocalControl() {
    var nome = document.getElementById("Name").value
    if(nome == "")
        alert(" il campo 'Nome' è vuoto")
    var cognome = document.getElementById("Surname").value;
    if(cognome == "")
        alert(" il campo 'Cognome' è vuoto")
    var indirizzo = document.getElementById("Address").value
    if(indirizzo == "")
        alert(" il campo 'Indirizzo' è vuoto")
    var telefono = document.getElementById("telephone").value
    if(telefono == "")
        alert(" il campo 'Numero di cellulare' è vuoto")
    var fiscale = document.getElementById("fiscalcode").value
    if(fiscale == "")
        alert(" il campo 'Codice fiscale' è vuoto")
        else
        if (fiscale != fiscale.toUpperCase()){
            fiscale = fiscale.toUpperCase();
        }
    var documento = document.getElementById("document").value
    if(documento == "")
        alert(" il campo 'Documento' è vuoto")
        else
        if (documento != documento.toUpperCase()){
            documento = documento.toUpperCase();
        }
    var iban = document.getElementById("iban").value
    if(iban == "")
        alert(" il campo 'IBAN' è vuoto")
        else
        if (iban != iban.toUpperCase()){
            iban = iban.toUpperCase();
        }
    var iva = document.getElementById("iva").value
    if(iva == "")
        alert(" il campo 'Partita IVA' è vuoto")
        else
        if (iva != iva.toUpperCase()){
            iva = iva.toUpperCase();
        }
    var locale = document.getElementById("LocalName").value
    if(locale == "")
        alert(" il campo 'Nome del locale' è vuoto")
    var email = document.getElementById("email").value
    if(email == "")
        alert(" il campo 'Email' è vuoto")
    var password = document.getElementById("password").value
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
    var telefono = document.getElementById("telephone").value
    if(telefono == "")
        alert(" il campo 'Numero di cellulare' è vuoto")
    var fiscale = document.getElementById("fiscalcode").value
    if(fiscale == "")
        alert(" il campo 'Codice fiscale' è vuoto")
        else
        if (fiscale != fiscale.toUpperCase()){
            fiscale = fiscale.toUpperCase();
        }
    var email = document.getElementById("email").value
    if(email == "")
        alert(" il campo 'Email' è vuoto")
    var password = document.getElementById("password").value
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
    var telefono = document.getElementById("telephone").value
    if(telefono == "")
        alert(" il campo 'Numero di cellulare' è vuoto")
    var fiscale = document.getElementById("fiscalcode").value
    if(fiscale == "")
        alert(" il campo 'Codice fiscale' è vuoto")
        else
        if (fiscale != fiscale.toUpperCase()){
            fiscale = fiscale.toUpperCase();
        }
    var documento = document.getElementById("document").value
    if(documento == "")
        alert(" il campo 'Documento' è vuoto")
        else
        if (documento != documento.toUpperCase()){
            documento = documento.toUpperCase();
        }
    var iban = document.getElementById("iban").value
    if(iban == "")
        alert(" il campo 'IBAN' è vuoto")
        else
        if (iban != iban.toUpperCase()){
            iban = iban.toUpperCase();
        }
    var email = document.getElementById("email").value
    if(email == "")
        alert(" il campo 'Email' è vuoto")
    var password = document.getElementById("password").value
    if(password == "")
        alert(" il campo 'Password' è vuoto")
}
