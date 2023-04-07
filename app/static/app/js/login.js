function validate(){
    var username=document.getElementById("username").value;
    var password=document.getElementById("password").value;
    if(username=="shadow" && password=="shadow123"){
        alert("Login Successfull");
        return false;
    }
    else{
        alert("Login failed");
    }
}