# ai generated code 1
from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf_by_size(input_pdf, max_size, output_path):
    # Open the input PDF file
    print(f"opening {input_pdf}, processing with max_size {max_size}")
    input_pdf_reader = PdfReader(open(input_pdf, "rb"))
    
    

    # Initialize variables
    input_basename = os.path.basename(input_pdf).split('.')[0]
    output_pdf_writer = PdfWriter()
    output_file_index = 1
    current_size = 0
    
    # Iterate through each page in the input PDF
    for page_num in range(len(input_pdf_reader.pages)):
        # Add the current page to the output PDF writer
        current_page = input_pdf_reader.pages[page_num]
        output_pdf_writer.add_page(input_pdf_reader.pages[page_num])
        
        # Calculate the size of the current output PDF
        current_size += len(current_page.extract_text().encode('utf-8'))

        print(f"{page_num} added - current size: {current_size}")
        
        # If the current size exceeds the maximum size, save the current output PDF and start a new one
        if current_size >= max_size:
            print(f" >> {page_num}: current size {current_size} exceeds max of {max_size}")

            with open(os.path.join(output_path, f"{input_basename} - part_{output_file_index}.pdf"), "wb") as output_file:
                output_pdf_writer.write(output_file)
            output_file_index += 1
            output_pdf_writer = PdfWriter()
            current_size = 0
    
    # Save any remaining pages to a final output PDF
    if current_size > 0:
        with open(os.path.join(output_path, f"{input_basename} - part_{output_file_index}.pdf"), "wb") as output_file:
            output_pdf_writer.write(output_file)

# Example usage: Split "input.pdf" into multiple files with a maximum size of 1MB (1048576 bytes)
#split_pdf_by_size("input.pdf", 1048576)
