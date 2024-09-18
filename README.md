# AI PDF Extraction and Search System

This project is an AI-powered system that allows users to upload PDF files, extract specific information (text and images), perform advanced searches (including by word length, specific topics, and numbers), and optionally download the results. The system includes a UI for file uploads and is equipped with a search functionality that can handle spelling errors and synonym-based searches.

## Features
- **PDF File Upload**: Upload one or more PDF files to extract their content.
- **Text and Image Extraction**: Extracts both text and images from the uploaded PDF.
- **Search Functionality**:
  - Search by specific words or phrases.
  - Search by word length (e.g., all four-letter words).
  - Extract numbers from the text.
  - Handle spelling mistakes using AI-powered correction.
  - Synonym-based search to capture related terms.
- **Download Options**: Users can preview extracted content and download the final report as a PDF or docx file.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/ai-pdf-extraction-search.git
cd ai-pdf-extraction-search
```

### 2. Create and Activate a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (MacOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

The key libraries include:
- `Flask`: Web framework for creating the UI and API.
- `PyMuPDF`: For PDF text and image extraction.
- `fpdf`: For generating PDF reports.
- `python-docx`: For generating DOCX reports.
- `textblob`: For natural language processing and spelling correction.
- `nltk`: For text processing and synonym search.

### 4. Run the Flask App
```bash
python main.py
```

The server will start running at `http://127.0.0.1:5000`.

### 5. Access the UI
Open a browser and navigate to `http://127.0.0.1:5000`. You'll see the file upload interface.

## Usage Instructions

1. **Upload a PDF File**: On the homepage, choose a PDF file and provide a search term if needed.
   
2. **Perform a Search**:
   - You can search by a specific word, a word length (e.g., "all four-letter words"), or by extracting numbers.
   - You can also leave the search term blank to extract all content.

3. **View and Download Results**:
   - After uploading, you can preview the extracted content.
   - Optionally, download the results as a PDF or DOCX report.

## File Structure

```
├── app/
│   ├── __init__.py           # Initializes Flask app
│   ├── pdf_extraction.py     # PDF text and image extraction functions
│   └── search.py             # Functions for handling search logic
├── templates/
│   ├── index.html            # Homepage with upload form
│   └── display_extracted.html# Displays extracted content and offers download options
├── static/
│   ├── style.css             # Styles for the UI
├── main.py                   # Main Flask application
├── requirements.txt          # Required Python libraries
└── README.md                 # Project documentation
```

## Functions Overview

- **`extract_text_and_images(file_path)`**: Extracts text and images from the PDF file.
- **`search_in_text(extracted_text, search_term, synonyms)`**: Searches for specific terms or their synonyms in the extracted text.
- **`search_by_word_length(text, length)`**: Finds all words of a specific length.
- **`extract_numbers(text)`**: Extracts all numeric data from the text.
- **`correct_spelling(search_term)`**: Uses AI to correct any spelling mistakes in the search term.

## Future Enhancements
- Implement more advanced AI-based search functionalities such as fuzzy matching and context-based searching.
- Add support for processing larger PDF files asynchronously.

## Contributing
Feel free to contribute by forking this repository and submitting pull requests. Any feature suggestions or bug reports are welcome!

