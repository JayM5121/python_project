import qrcode

# Taking UPI ID As a input

upi_id = input("ENTER YOUR UPI ID: ")

# upi://pay?pa=UPI_ID%apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment URL based on the UPI ID and the payment app

# You can modify the URLs based on the payment app you want to support

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Create QR codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)
paytm_qr = qrcode.make(paytm_url)

# Save QR code to image file

# phonepe_qr.save("phonepe_qr.png")
# google_pay_qr.save("google_pay_qr.png")
# paytm_qr.save("paytm_qr.png")

# Display the QR codes

phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()