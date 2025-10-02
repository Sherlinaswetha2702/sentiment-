document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const textarea = document.querySelector("textarea");
    const tweetInput = document.querySelector("input[name='tweet_url']");
    const analyzeButton = document.querySelector("button[type='submit']");

    // Disable the analyze button if the textarea is empty
    function updateButtonState() {
        analyzeButton.disabled = !textarea.value.trim() && !tweetInput.value.trim();
    }

    textarea.addEventListener("input", updateButtonState);
    tweetInput.addEventListener("input", updateButtonState);

    // Form submission event
    form.addEventListener("submit", function(event) {
        event.preventDefault();  // Prevent the default form submission

        // Display loading spinner
        showLoadingSpinner();

        // Perform sentiment analysis
        fetch('/analyze', {
            method: 'POST',
            body: new FormData(form)
        })
        .then(response => response.text())
        .then(html => {
            document.querySelector(".container").innerHTML = html;
            hideLoadingSpinner();
        })
        .catch(error => {
            console.error("Error:", error);
            hideLoadingSpinner();
            alert("An error occurred. Please try again.");
        });
    });

    function showLoadingSpinner() {
        const spinner = document.createElement("div");
        spinner.className = "loading-spinner";
        spinner.innerHTML = `<div class="spinner-border text-primary" role="status">
                                <span class="sr-only">Loading...</span>
                             </div>`;
        document.body.appendChild(spinner);
    }

    function hideLoadingSpinner() {
        const spinner = document.querySelector(".loading-spinner");
        if (spinner) {
            spinner.remove();
        }
    }
});
