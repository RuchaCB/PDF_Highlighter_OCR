# STEP 1: To convert each page of pdf to an image
# STEP 2: Iterate through all the images in the output folder to highlight specified text

from pdf2image import convert_from_path
import pytesseract
import cv2
import os
from os import listdir
import img2pdf
from PIL import Image
from PyPDF2 import PdfMerger


# Specify the words you want to highlight
specified_words = ["Merchant","ID:", "Terminal", "Total","Basic","collection","collection","digital", "Stocks", "Saturdays", 'information' "Number", "Nasdaq", "eager", "learns", "from", "Artificial", "Tickets"]
# Convert specified words to lowercase for case-insensitive matching
lower_specified_words = [word.lower() for word in specified_words]

pdf_file_path = "C:\\PDF_Highlighter_OCR\\OCR\\input_3.pdf"
#output_folder_path = "output_images"
# get the path/directory
output_folder_path = "C:\\PDF_Highlighter_OCR\\OCR\\output_images"

# storing highlighted images path
highlighted_img_path = "C:\\PDF_Highlighter_OCR\\OCR\\highlighted_images"

# Specify folder path containing PDF files to merge
all_pdfs_path = "C:\\PDF_Highlighter_OCR\OCR\\all_pdfs"

# Set Tesseract path (replace this with your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

images = convert_from_path(pdf_file_path, 500, poppler_path=r'C:\Program Files\poppler-24.02.0\Library\bin' )

for i in range(len(images)):
    images[i].save('C:\\PDF_Highlighter_OCR\\OCR\\output_images\\page' + str(i) + '.jpg', 'JPEG')
    

output_folder_path = "C:\\PDF_Highlighter_OCR\\OCR\\output_images"

for images in os.listdir(output_folder_path):

    # check if the image ends with png
    if (images.endswith(".jpg")):
        
        # Load the input image
        img = cv2.imread(output_folder_path + '\\' + images)
        # Get image height and width
        hImg, wImg, _ = img.shape

        # Perform OCR on the image and get detailed data
        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        #print(data)
        
        overlay = img.copy() 
        # Iterate over detected words
        for i in range(len(data['text'])):
            word = data['text'][i]
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]

            # Check if the detected word matches any of the specified words (case-insensitive)
            if word.lower() in lower_specified_words:
                
                # Draw a rectangle around the detected word
                cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 200, 0), -1)   
                
        alpha = 0.4  # Transparency factor. 

        # Following line overlays transparent rectangle 
        # over the image 
        image_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0) 
        cv2.imwrite(highlighted_img_path + '\\' + images, image_new, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

        #cv2.imshow("image_new", image_new)

        cv2.waitKey(0)


for images in os.listdir(highlighted_img_path):

    # storing pdf path
    pdf_path = all_pdfs_path + "\\" + images.replace("jpg", "pdf")
    # opening image
    
    image = Image.open(highlighted_img_path + "\\" + images)

    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)

    # opening or creating pdf file
    file = open(pdf_path, "wb")

    # writing pdf files with chunks
    file.write(pdf_bytes)

    # closing image file
    image.close()

    # closing pdf file
    file.close()


# output
print("Successfully made pdf file")



def merge_pdfs_in_folder(folder_path, output_filename):
    # Initialize PdfMerger object
    merger = PdfMerger()

    # Iterate over all PDF files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            # Construct full path to the PDF file
            pdf_path = os.path.join(folder_path, filename)
            
            # Add PDF file to the merger
            merger.append(pdf_path)
            print(f"Added '{filename}' to the merge list.")

    # Write the merged PDF to the output file
    output_path = os.path.join(folder_path, output_filename)
    merger.write(output_path)
    print(f"Combined PDF saved as '{output_filename}'.")

    # Close the merger
    merger.close()


def clear_folder(folder_path):
    # Iterate over all files and subdirectories in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                # Delete file
                os.unlink(file_path)
                print(f"Deleted file: {file_path}")
            elif os.path.isdir(file_path):
                # Recursively clear subdirectory
                clear_folder(file_path)
                # Remove empty subdirectory
                os.rmdir(file_path)
                print(f"Deleted directory: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Error: {e}")

# Example usage
if __name__ == "__main__":
    

    # Specify the output filename for the combined PDF
    output_filename = "C:\\PDF_Highlighter_OCR\OCR\\Final_PDF_Output\\final_output.pdf"

    # Merge PDFs in the folder
    merge_pdfs_in_folder(all_pdfs_path, output_filename)

    #clear all unwanted folders
    # empty_folders = [output_folder_path, all_pdfs_path, highlighted_img_path]
    # for i in empty_folders:
    #     clear_folder(i)
    #     print(f"Folder '{i}' cleared.")

