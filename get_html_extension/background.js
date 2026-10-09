browser.action.onClicked.addListener(async (tab) => {
    console.log("1. Kliknięto ikonę")

    const content_response = await browser.tabs.sendMessage(
        tab.id,
        {
            action: "getHtml"
        }
    )

    try {
        const response = await browser.runtime.sendNativeMessage(
            "mail_generator",
            {
                message: content_response.html
            }
        );

        console.log("2. Odpowiedź Pythona: ", response.received.message)
    } catch (error) {
        console.error("BŁĄD NATIVE MESSAGE: ", error)
    }
});