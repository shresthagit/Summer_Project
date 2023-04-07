function validate(){
    name=document.frm.uname.value;
            email=document.frm.email.value;
            phone=document.frm.phone.value;
            address=document.frm.add.value;
            var p=/^(98[0-9]{8})$/;
            var a=" ";
            var e=/^([A-Za-z0-9_]+@[A-za-z]+\.[a-zA-Z]{2,3})$/;
              if(name==""){
                alert ("Name cannot be empty");
                return false;
              }
              
              if(address==""){
                alert("Address is empty");
                return false;
              }
              if(email==""){
                alert("Type your email id");
                return false;
              }
              if(!email.match(e)){
      
                alert("Email id you provided is not valid.");
                return false;
              }
      
      
              if(phone==""){
                alert("Please palce your phone number here.");
                return false;
              }
              if(!phone.match(p)){
      
                alert("Enter number starting from 98... and length should be 10.");
                return false;
              }
      
      
          }
