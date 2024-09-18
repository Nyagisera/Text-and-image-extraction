import fitz  # PyMuPDF
import os

def extract_text_from_pdf(file, keywords=None):
    """
    Extracts text from an uploaded PDF file based on specified keywords or topics.
    
    Parameters:
    - file: The uploaded PDF file.
    - keywords: A list of keywords or topics to filter the text.
    
    Returns:
    - Extracted text matching the keywords.
    """
    temp_path = os.path.join('uploads', file.filename)
    
    # Save the file temporarily
    file.save(temp_path)

    doc = None
    extracted_text = ""
    try:
        # Try opening the PDF
        doc = fitz.open(temp_path)
        
        # Loop through each page in the PDF
        for page in doc:
            text = page.get_text("text")
            
            # If keywords are provided, filter text based on those
            if keywords:
                text_lines = text.lower().splitlines()
                for line in text_lines:
                    for keyword in keywords:
                        if keyword.lower() in line:
                            extracted_text += line + "\n"
            else:
                # If no keywords, extract all text
                extracted_text += text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    finally:
        # Ensure the document is closed if it was opened
        if doc is not None:
            doc.close()

        # Ensure the temp file is removed after processing
        if os.path.exists(temp_path):
            os.remove(temp_path)
    
    return extracted_text

def extract_images_from_pdf(file):
    """
    Extracts images from an uploaded PDF file and saves them to a folder.
    
    Parameters:
    - file: The uploaded PDF file.
    
    Returns:
    - List of paths to the extracted images.
    """
    temp_path = os.path.join('uploads', file.filename)
    
    # Save the file temporarily
    file.save(temp_path)

    image_dir = "extracted_images"
    os.makedirs(image_dir, exist_ok=True)
    image_paths = []
    doc = None

    try:
        # Open the PDF
        doc = fitz.open(temp_path)
        
        # Iterate through each page in the PDF
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # Extract images from the page
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = f"{image_dir}/page{page_num+1}_img{img_index+1}.{image_ext}"
                
                # Save the extracted image
                with open(image_filename, "wb") as image_file:
                    image_file.write(image_bytes)
                
                image_paths.append(image_filename)

    except Exception as e:
        print(f"Error extracting images from PDF: {e}")
    finally:
        # Ensure the document is closed if it was opened
        if doc is not None:
            doc.close()

        # Ensure the temp file is removed after processing
        if os.path.exists(temp_path):
            os.remove(temp_path)
    
    return image_paths
