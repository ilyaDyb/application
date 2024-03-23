$(document).on("click", "#clicker_button", function(e){
    var score = $("#score");
    var currentValue = parseInt(score.text());
    var tapValue = $("#hiddenTap").val();

    tapValue = parseInt(tapValue);
    
    currentValue += tapValue;

    $("#score").text(currentValue);
    
    updateScore(currentValue)
});

if (hiddenAutoClick.val() == "1") {
    var interval = setInterval(function() {
    var hiddenAutoClick = $("#hiddenAutoClick")


        var score = $("#score");
        var currentValue = parseInt(score.text());
        var tapValue = $("#hiddenTap").val();
        currentValue += parseInt(tapValue);
        $("#score").text(currentValue);
        // Вывод значения в консоль
        console.log(currentValue);
    }, 1000); // Интервал в миллисекундах (например, каждую секунду)
}

function updateScore(currentValue){
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/save-value/",
        data: {
            value: currentValue,
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        }, 
        success: function (data) {
            var newValue = parseInt($("#score").text());
            $("#score").text(newValue)
            
        },
        error: function (data) {
            console.log("Ошибка");
        },
    });
}

window.addEventListener('beforeunload', function(event) {
    // Отправляем данные на сервер с помощью Ajax перед обновлением страницы
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/delete-data-from-cache/",
        data: { csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val() },
        success: function(data) {
            $("#score").text(data.value);
        },
        error: function(xhr, status, error) {
            console.error("Произошла ошибка при сохранении данных о кликах.");
        },
    });
});

$(document).on("click", "#clicker_button", function(){
    this.classList.toggle("enlarged");
})