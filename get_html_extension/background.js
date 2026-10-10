browser.action.onClicked.addListener(async (tab) => {
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
    } catch (error) {
        console.error("BŁĄD NATIVE MESSAGE: ", error)
    }
});