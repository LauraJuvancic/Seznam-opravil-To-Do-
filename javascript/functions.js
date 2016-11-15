function showFormList() {
    document.getElementById('formlist').style.display = "block";
    document.getElementById('formtext').style.display = "block";
}


function showForm(element) {


    switch (element.value){
        case 'select':
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'home':
            document.getElementById('formhome').style.display = "block";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'work':
            document.getElementById('formwork').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'personal':
            document.getElementById('formpersonal').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'travel':
            document.getElementById('formtravel').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'shopping':
            document.getElementById('formshopping').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'birthday':
            document.getElementById('formbirthday').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'cooking':
            document.getElementById('formcooking').style.display = "block";
            document.getElementById('formcookinglist').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            break;
    }

}

function showlogin(element) {
    if(document.getElementById('login').style.display == "block")
        document.getElementById('login').style.display = "none";
    else
        document.getElementById('login').style.display = "block";

    return false;
}
