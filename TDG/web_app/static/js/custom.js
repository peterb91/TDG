function show(par){
    document.getElementById(par).style.display = 'block';
}

function hide(par){
    document.getElementById(par).style.display = 'none';
}

function takeFromSlider(amount, min, max){
    var values = document.getElementById(amount).value.split("-");
    document.getElementById(min).value = values[0];
    document.getElementById(max).value = values[1];
}

function myFunction(elementID, sideID){
    var popup = document.getElementById(elementID);
    var side = document.getElementById(sideID);
    popup.classList.toggle("show");
    side.classList.toggle("stay");

}

function validateLengths(minFieldId, maxFieldId){
    var min = parseInt(document.getElementById(minFieldId).value);
    var max = parseInt(document.getElementById(maxFieldId).value);

    if(min <= max){
        return true;
    }

    alert("Minimum length value is higher than maximum length. Correct the values to proceed.");
    document.getElementById(maxFieldId).value='';

    return false;
}

$(document).ready(function() {
    $("#login_special_char-0").click(function(){
        $("#login_textarea_custom").hide();
    });
    $("#login_special_char-1").click(function(){
        $("#login_textarea_custom").hide();
    });
    $("#login_special_char-2").click(function(){
        $("#login_textarea_custom").show();
    });
     $("#pass_special_char-0").click(function(){
        $("#pass_textarea_custom").hide();
    });
    $("#pass_special_char-1").click(function(){
        $("#pass_textarea_custom").hide();
    });
    $("#pass_special_char-2").click(function(){
        $("#pass_textarea_custom").show();
    });
});
