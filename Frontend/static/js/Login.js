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
        //window.location.href = "http://"+window.location.hostname+":5500/Frontend/templates/dashboard.html";
        window.location.href = "http://"+window.location.hostname+":5500/templates/dashboard.html"

       
      },
      error: function(xhr, ajaxOptions, thrownError){
        console.log(xhr.responseJSON.detail)
        document.getElementById("error").style.display = "block";       
        document.getElementById("error").innerHTML =xhr.responseJSON.detail;
  
      }   
     
   })

  }
  
(function(){
  const fonts = ["cursive"];
  let captchaValue = "";
  function gencaptcha()
  {
      let value = btoa(Math.random()*1000000000);
      value = value.substr(0,5 + Math.random()*2);
      captchaValue = value;
  }

  function setcaptcha()
  {
      let html = captchaValue.split("").map((char)=>{
          const rotate = -20 + Math.trunc(Math.random()*30);
          const font = Math.trunc(Math.random()*fonts.length);
          return`<span
          style="
          transform:rotate(${rotate}deg);
          font-family:${font[font]};
          "
         >${char} </span>`;
      }).join("");
      document.querySelector(".login_form #captcha .preview").innerHTML = html;
  }

  function initCaptcha()
  {
      document.querySelector(".login_form #captcha .captcha_refersh").addEventListener("click",function(){
          gencaptcha();
          setcaptcha();
      });

      gencaptcha();
      setcaptcha();
  }
  initCaptcha();

  document.querySelector(".login_form .form_button").addEventListener("click",function(){
      let inputcaptchavalue = document.querySelector(".login_form #captcha input").value;

      if (inputcaptchavalue === captchaValue) 
      {
          // swal("","Log in","success");
          // alert("Log in success");
          authorise();
      }
      else
      {
          // swal("Invalid Captcha");
          document.getElementById('error').innerHTML ="Invalid Captcha";
      }
  });
})();