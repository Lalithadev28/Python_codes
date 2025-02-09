with open('B4172.jpg', 'rb') as img_file:  # Read the image as binary
    img_data = img_file.read()

with open('output.jpg', 'wb') as new_img_file:  # Write binary data
    new_img_file.write(img_data)

print("Image copied successfully.")
