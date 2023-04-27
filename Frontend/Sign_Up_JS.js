{/* <script>
const form={
    username: document.getElementById('username'),
    password: document.getElementById('password'),
    submit: document.getElementById('btn-submit'),
    messages: document.getElementById('form-messages'),

};

    form.submit.addEventListener('click', () => {
    /*console.log('button pressed!');*/
    const request = new XMLHttpRequest();


        request.onload =() => {
            console.log(request.responseText);
        };

        const requestData=`username=${form.username.value}&password=${form.password.value}`;
        console.log(requestData);

        request.open('post','check-login.php');
        request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        request.send(requestData);
})

</script> */}


function signUpData(){
    let userName=document.querySelector("username").value
    let email=document.querySelector("email").value
    let password=document.querySelector("password").value
    $.ajax({
          url:"http://localhost:8000/register",
          type:"POST",
          contentType:"application/json",
          data:JSON.stringify({
            username:userName,
            email:email,
            password:password
          }),
          success:function(data) {
            window.location.href = "http://127.0.0.1:5501";
            return(data)
          }
          })
        
        }