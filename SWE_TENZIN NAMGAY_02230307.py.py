import qrcode

# Function to generate QR code for a URL
def generate_qr_code_url(url, save_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)

# Function to generate QR code for contact information
def generate_qr_code_contact(contact_info, save_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(contact_info)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)

if __name__ == "__main__":
    # Generate QR code for a URL
    url = "https://classroom.google.com/"
    generate_qr_code_url(url, "url_qr_code.png")
    print("QR code for URL generated.")

    # Generate QR code for contact information (vCard format)
    contact_info = "BEGIN:VCARD\nVERSION:3.0\nFN:Tenzin Namgay\nORG:Example Inc.\nTEL:+97517935521\nEMAIL:02230307.cst@rub.edu.bt\nEND:VCARD"
    generate_qr_code_contact(contact_info, "contact_qr_code.png")
    print("QR code for contact information generated.")
 