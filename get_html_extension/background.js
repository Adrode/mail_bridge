browser.action.onClicked.addListener(async () => {
    console.log("1. Kliknięto ikonę")

    try {
        const response = await browser.runtime.sendNativeMessage(
            "mail_generator",
            {
                message: "hello"
            }
        );

        console.log("2. Odpowiedź Pythona: ", response)
    } catch (error) {
        console.error("BŁĄD NATIVE MESSAGE: ", error)
    }
});