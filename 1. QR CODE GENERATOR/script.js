document.getElementById('generateBtn').addEventListener('click', function() {
    const text = document.getElementById('text').value;

    // Clear previous QR code if any
    document.getElementById('qrcode').innerHTML = "";

    // Generate new QR code
    if (text) {
        const qrcode = new QRCode(document.getElementById('qrcode'), {
            text: text,
            width: 256,
            height: 256,
        });
    } else {
        alert("Please enter a valid text or URL");
    }
});
