browser.action.onClicked.addListener(async (tab) => {
    const response = await browser.tabs.sendMessage(
        tab.id,
        { action: "getHtml" }
    );

    console.log("Otrzymany HTML:", response.html.length);
});