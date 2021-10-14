$("#generation_button").click(function(){
    let data = {
        "secret": $("#secret_input").val()
    };
    $.ajax({
        type: "POST",
        url: "/new",
        contentType: "application/json;charset=UTF-8",
        data: JSON.stringify(data),
        success(return_data) {
            if (return_data["status"] === 0){
                alert("暗号不正确");
            }else {
                $("#show_image").attr("src", return_data["img_src"]);
                $("#sentence").text(return_data["sentence"]);
            }
        }
    })
});