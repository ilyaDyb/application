function convertScore() {
    var score = parseInt(document.getElementById('score').value);
    var dollars = score * 0.01; // Example conversion rate
    document.getElementById('result').innerText = 'Your score is equivalent to $' + dollars.toFixed(2);
}