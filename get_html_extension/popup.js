document.getElementById("getHtml").addEventListener("click", async () => {
    const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    chrome.tabs.sendMessage(
        tab.id,
        { action: "getHtml" },
        (response) => {
            document.getElementById("result").textContent = response.html
        }
    );
});

// console.log("Response: ", response);