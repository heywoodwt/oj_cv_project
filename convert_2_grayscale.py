import cv2

def convert_to_grayscale(input_image_path, output_image_path):
    # Read the image from the specified path
    image = cv2.imread(input_image_path)
    if image is None:
        raise ValueError("Image not found or unable to read.")

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image to the specified output path
    cv2.imwrite(output_image_path, grayscale_image)


convert_to_grayscale('1copy.jpg', 'output_grayscale.jpg')