$(document).on("click", "#clicker_button", function(e){
    e.preventDefault();
    var score = $("#score");
    var currentValue = parseInt(score.text());

    currentValue++;
    
    updateScore(currentValue)
});

function updateScore(currentValue){
    console.log(currentValue)
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/save-value/",
        data: {
            value: currentValue,
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        }, 
        success: function (data) {
            console.log("Успешно");
            var newValue = parseInt($("#score").text()) + 1;
            $("#score").text(newValue)
            
        },
        error: function (data) {
            console.log("Ошибка");
        },
    });
}
