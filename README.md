# 🖍️ PDF Text Highlighter using OCR

This project performs **OCR (Optical Character Recognition)** on a PDF, highlights specified keywords across all pages, converts them into images, and finally regenerates a single merged PDF with the highlights applied.

---

## 📌 Features

- ✅ Converts each page of a PDF into images.
- ✅ Uses `Tesseract OCR` to detect and extract text from images.
- ✅ Automatically highlights user-defined keywords with semi-transparent overlays.
- ✅ Converts processed images back to PDFs.
- ✅ Merges all PDFs into a final combined output.
- ✅ Includes utility functions to clean up intermediate files.

---

## 🧠 How It Works

1. **PDF ➡️ Images**  
   Converts each page of the input PDF into `.jpg` format using `pdf2image`.

2. **Image ➡️ Text**  
   Applies OCR with `pytesseract` to extract words from each image.

3. **Highlight Text**  
   Matches and highlights words based on a specified keyword list.

4. **Images ➡️ PDF**  
   Converts each highlighted image into a separate PDF using `img2pdf`.

5. **Merge PDFs**  
   Combines all PDFs into one final document with highlights.

---


