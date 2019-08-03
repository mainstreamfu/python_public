$(document).ready(function(){
    $("#avatar").change(function () {
        var choose_file = $(this)[0].files[0];
        var reader = new FileReader();//实例化阅读器对象
        reader.readAsDataURL(choose_file);
        reader.onload=function () {
            $("#avatar_img").attr("src",this.result)     //attr不能使用set替换，set针对dom对象
        }
    });
    //注册
    $(".reg_btn").click(function(){
        var formdata = new FormData();
        formdata.append("csrfmiddlewaretoken",$("[name='csrfmiddlewaretoken']").val());
        formdata.append("user",$("#id_user").val());
        formdata.append("pwd",$("#id_pwd").val());
        formdata.append("repeat_pwd",$("#id_repeat_pwd").val());
        formdata.append("email",$("#id_email").val());
        formdata.append("avatars",$("#avatar")[0].files[0]);
        console.log(formdata);
        $.ajax({
            url:"",
            type:"post",
            dataType:"json",
            data:formdata,
            contentType:false,
            processData: false,
            success:function (data) {
                // var data=JSON.parse(data);
                if (data.user){
                    location.href="/login/"
                }
                else{
                    $(".error").html("");
                    $(".form-group").removeClass("has-error");
                    $.each(data.error_msg,function (field, error_info) {
                        console.log(field, error_info[0]);
                        $("#id_"+field).parent().addClass("has-error");

                        $("#id_"+field).next().html(error_info[0]).css("color","red");

                        if (field == "__all__"){
                            $("#id_repeat_pwd").next().html(error_info[0]).css("color","red");
                            $("#id_repeat_pwd").parent().addClass("has-error");
                        }
                    });
                }
            }
        })

    });

});

