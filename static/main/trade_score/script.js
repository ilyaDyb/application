$(document).on("click", "#convertButton", function(e){
    var score = $("#score")
    var score = parseInt(score.val());
    var dollars = score * 0.0000001;
    dollars = dollars.toFixed(6)
    $("#result").text(dollars + "$")
    convertScore(dollars, score)
});

function convertScore(dollars, score) {
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/convert-score/",
        data: {
            score: score,
            dollars: dollars,
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        },
        success: function(data){
            if (data.status == "Success") {
                
            }
            else {
                $("#result").text(data.status)
            }
        },
        error: function (data) {
            console.log("Error")
        },
    })
};