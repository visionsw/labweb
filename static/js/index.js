function getSelected(){
    var myselect = document.getElementById("select");
    var index = myselect.selectedIndex;
    return myselect.options[index].text;
}

