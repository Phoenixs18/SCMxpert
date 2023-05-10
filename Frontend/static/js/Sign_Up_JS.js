function signUpData(){
  let userName = document.querySelector("#typeUserName").value
  let emailData = document.querySelector("#typeEmail").value
  let passWord = document.querySelector("#typePassword").value

  $.ajax({
   
     url:"http://"+window.location.hostname+":8000/register",
     contentType: "application/json",
     type:"POST",
     data:JSON.stringify({
       username:userName,
       email:emailData,
       password:passWord }),

    success:function(data) {
      console.log(data)
      window.location.href = "http://"+window.location.hostname+":5500/Frontend/templates/login_page.html";
      
    },
    error: function(xhr){
 
      // alert (xhr.responseJSON.detail)
    }
  })            
  
}