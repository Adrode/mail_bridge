browser.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "getHtml") {
      sendResponse({
          html: document.documentElement.outerHTML
      });
  }
});