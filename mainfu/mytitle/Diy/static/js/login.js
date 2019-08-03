$(document).ready(function() {
    $(".login_btn").click(function () {
        alert(111)
        $.ajax({
            url: "",
            type: "post",
            data: {
                "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val(),
                "user": $("#user").val(),
                "pwd": $("#pwd").val(),
                "valid_code": $("#valid_code").val()
            },
            success: function (data) {
                var login_reponse = JSON.parse(data);
                console.log(login_reponse);
                if (login_reponse.user) {   // 登录成功
                    location.href = "/index/"
                } else { // 登录失败！
                    $(".error").html(login_reponse.error_msg).css("color", "red");

                    setTimeout(function () {
                        $(".error").html("")
                    }, 1000)

                }
            }
        })
    })
    $("#valid_img").click(function () {
        $(this)[0].src += "?"
    })

    var h1=document.getElementById("h1");
    document.onclick=function(event){
        var event =event||window.event;
        targetX=event.clientX-h1.offsetWidth/2;
        targetY=event.clientY-h1.offsetHeight/2;
                           };
    var targetX= 0,targetY= 0,leaderX= 0,leaderY=0;
    setInterval(function(){
        leaderX=leaderX+(targetX-leaderX)/10;
        leaderY=leaderY+(targetY-leaderY)/10;
        h1.style.left=leaderX+"px";
        h1.style.top=leaderY+"px";
                            },10)
})
