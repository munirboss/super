alert("Goodbye 2019 we've had lots times together but now make way for 2020")
    var price = 55 + 55;
    document.write(price);

    var myNum1 = 12;
    var myNum2 = 10
    if(myNum1 < myNum2) {
        alert("javascript is cool");
    }
    else if (myNum1 > myNum2) {
        alert("javascript is middly")
    }
    else{
        alert("javascript is ok");
    }

    for (i=1; i<=2; i++) {
        alert(i)
    }
    var i = 0;
    for (; i < 10; ) {
        document.write(i);
        i++;
    }

    var i = 0;
    for (; i < 10; ) {
        document.write(i);
        i++
    }

    var i=0;
    while (i<=10) {
        document.write(i + "<br />");
        i++;
    }

for (i = 0; i <= 10; i++) {
    if(i == 5) {
        break;
    }
    document.write(i);


}

 var name = prompt("what is your name")
 alert(name);

 var name = confirm("do you like this page?")
 if(name == true) {
     alert("thanks for visiting");
 }
 else {
     alert("awww men");
 }