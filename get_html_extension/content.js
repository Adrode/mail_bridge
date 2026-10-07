chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  console.log("Message: ", message)
  if (message.action === "getHtml") {
      sendResponse({
          html: document.documentElement.outerHTML
      });
  }
});

// chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

//     console.log("Dostałem wiadomość:", message);
//     console.log("Action:", message.action);

//     if (message.action === "getHtml") {

//         console.log("Jestem w IF");

//         const html = document.documentElement.outerHTML;

//         console.log("HTML pobrany, długość:", html.length);

//         sendResponse({
//             html: html
//         });

//         console.log("sendResponse wykonany");
//     }
// });