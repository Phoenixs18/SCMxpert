function validatetoken(){
  var status = false;
  $.ajax({
   
          url:"http://"+window.location.hostname+":8000/dashboard",
          type:"GET",
          headers: {"Authorization": 'Bearer ' + localStorage.getItem("access_token"),
    },
          success:function(data) {
            localStorage.getItem("access_token", data.access_token)  
            // window.location.href = "http://"+window.location.hostname+":5500/../../Frontend/templates/dashboard.html"
         
          },
          error: function(xhr, ajaxOptions, thrownError){                    
              status = false
              return status
          }
  })
  return status
}  

function logout(){
  localStorage.removeItem('access_token')
  window.location.href = "../templates/login.html"
}
