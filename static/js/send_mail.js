// JavaScript to send mail using JS Mail
function sendMail(contactForm) {
    emailjs.init("EMAILJS_PUBLIC_KEY");
    emailjs.send("gmail", "shop_active", {
        "to_email": contactForm.email_address.value
    }).then(
        function (response) {
            console.log("SUCCESS");
            $("#mailing-list").replaceWith("Thanks for subscribing to our mailing list");
        },
        function (error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}