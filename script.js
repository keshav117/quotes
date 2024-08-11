document.addEventListener("DOMContentLoaded", function() {
    fetchQuote();
});

function fetchQuote() {
    fetch("http://127.0.0.1:8000/quote")
    .then(response => response.json())
    .then(data => {
        document.getElementById("quote").innerText = `"${data.quote}"`;
        document.getElementById("author").innerText = `- ${data.author}`;
    })
    .catch(error => console.log("Error:", error));
}

function searchQuote() {
    const author = document.getElementById("author-search").value;
    fetch(`http://127.0.0.1:8000/search?author=${author}`)
    .then(response => response.json())
    .then(data => {
        if (data.length > 0) {
            const randomQuote = data[Math.floor(Math.random() * data.length)];
            document.getElementById("quote").innerText = `"${randomQuote.quote}"`;
            document.getElementById("author").innerText = `- ${randomQuote.author}`;
        } else {
            document.getElementById("quote").innerText = "No quotes found for this author.";
            document.getElementById("author").innerText = "";
        }
    })
    .catch(error => console.log("Error:", error));
}
