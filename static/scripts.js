document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("email-form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const email = document.getElementById("email").value;

        // Display loading message
        resultDiv.textContent = "Checking...";
        try {
            const response = await fetch("/check", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: `email=${email}`,
            });

            const data = await response.json();
            resultDiv.textContent = data.result;
        } catch (error) {
            resultDiv.textContent = "An error occurred. Please try again.";
        }
    });
});
