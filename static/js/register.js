function bindCaptchaBtnClick(){
    $("#captcha-btn").on("click",function (event){
        var $this = $(this);

      var email =  $("input[name='email']").val();
      if(!email){
          alert("Please enter email first!");
          return;
      }
      //Sending network requests via js: ajax Async js and xml (JSON)
        $.ajax({
            url:"/user/captcha",
            methods:"GET",
            data:{
                "email":email
            },
            success:function (res){
                var code = res['code'];
                if(code ==200){
                    //Cancel click events
                    $this.off("click");
                    //start the countdown
                    var countDown = 60;
                    var time = setInterval(function (){
                        countDown-=1;
                        if(countDown>0){
                             $this.text(countDown+"seconds resend");
                        }else{
                             $this.text("send captcha");
                             //Rerunning the function rebinds the click event
                             bindCaptchaBtnClick();
                             //Remember to clear the countdown if it's not needed, or it will continue forever
                             clearInterval(timer);
                        }

                    },1000);
                    alert("The CAPTCHA was sent successfully")

                }else
                alert(res['message']);
            }

        })
    });
}


//Wait until all elements of the web document are loaded
window.onload = function() {
    bindCaptchaBtnClick();
}