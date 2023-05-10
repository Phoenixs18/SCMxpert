function authorise(){
    let userData = document.querySelector("#checkUserName").value
    let passWord = document.querySelector("#checkPwd").value
    
      $.ajax({
      
        url:"http://"+window.location.hostname+":8000/login",
        type:"POST",
        dataType: "json",
                contentType: "application/json",
        data:JSON.stringify({
          username:userData,
          password:passWord
    
        }),
       success:function(data) {
         console.log(data.access_token)
          localStorage.setItem("access_token", data.access_token)  
          window.location.href = "http://"+window.location.hostname+":5500/Frontend/templates/dashboard.html"
       
         
        },
        error: function(xhr){
 
          // alert (xhr.responseJSON.detail)
        }

        // error: function(xhr, ajaxOptions, thrownError){
        //   console.log(xhr.responseJSON.detail)
        //   document.getElementById("error").style.display = "block";       
        //   document.getElementById('error').innerHTML =xhr.responseJSON.detail;
          //  alert (xhr.responseJSON.detail)
    
        // }
        
       
     })
}