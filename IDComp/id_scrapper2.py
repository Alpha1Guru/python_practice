import os
import asyncio
from playwright.async_api import async_playwright
from PyPDF2 import PdfMerger

# Configuration
URL = "https://studentservices.lasu.edu.ng/temporary-studentid/index.php"
START_MATRIC = 240591001
END_MATRIC = 240591445
OUTPUT_DIR = "downloaded_ids"
FINAL_PDF = "Merged_Course_Mates_IDs.pdf"

async def generate_and_download_ids():
    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    async with async_playwright() as p:
        # Launch browser in headless mode (runs in the background)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for matric in range(START_MATRIC, END_MATRIC + 1):
            matric_str = str(matric)
            print(f"Processing Matric Number: {matric_str}...")
            
            try:
                # 1. Navigate to the dummy generator site
                await page.goto(URL)
                
                # 2. Fill in the matric number. 
                # (This targets the first text input field on the page. If the form is complex, 
                # you might need to change "input[type='text']" to the specific 'name' or 'id' of the input)
                await page.fill("input[type='text'], input[name='matric_no']", matric_str)
                
                # 3. Click the 'GENERATE' button
                await page.click("button:has-text('GENERATE'), input[value='GENERATE'], input[type='submit']")
                
                # 4. Wait for the page to load the result
                await page.wait_for_load_state('networkidle')
                
                # 5. Check if the "Invalid Matric Number" error is on the page
                content = await page.content()
                if "Invalid Matric Number" in content:
                    print(f" --> Skipping {matric_str}: Invalid Matric Number found.")
                    continue
                
                # 6. If valid, save the page as a PDF
                pdf_path = os.path.join(OUTPUT_DIR, f"{matric_str}.pdf")
                
                # Optional: Hide the 'Print' button or any navigation buttons before generating the PDF 
                # so they don't show up in the final document.
                await page.evaluate("""
                    var buttons = document.querySelectorAll('button, a, input[type="button"]');
                    buttons.forEach(btn => {
                        if(btn.innerText.includes('Print') || btn.innerText.includes('back')) {
                            btn.style.display = 'none';
                        }
                    });
                """)
                
                # Save to PDF (print_background=True ensures logos and colors are captured)
                await page.pdf(path=pdf_path, format="A4", print_background=True)
                print(f" --> Successfully saved: {pdf_path}")

            except Exception as e:
                print(f" --> Error processing {matric_str}: {e}")

        await browser.close()

def merge_pdfs():
    print("\nStarting PDF merge process...")
    if not os.path.exists(OUTPUT_DIR):
        print("No downloaded PDFs found to merge.")
        return

    merger = PdfMerger()
    
    # Get all PDFs and sort them so they are in numerical order
    pdf_files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.endswith('.pdf')])
    
    if not pdf_files:
        print("No valid PDFs were downloaded.")
        return

    for pdf in pdf_files:
        file_path = os.path.join(OUTPUT_DIR, pdf)
        
        # The 'pages' argument takes a tuple (start, stop). 
        # (0, 1) means it grabs page 0 (the first page) and stops before page 1.
        merger.append(file_path, pages=(0, 1))
        print(f"Appended first page of: {pdf}")
        
    merger.write(FINAL_PDF)
    merger.close()
    print(f"Success! The first pages of all IDs have been merged into '{FINAL_PDF}'")

async def main():
    print("--- Starting ID Card Generation ---")
    await generate_and_download_ids()
    print("--- Download Phase Complete ---")
    merge_pdfs()

if __name__ == "__main__":
    # Run the asynchronous Playwright loop
    asyncio.run(main())