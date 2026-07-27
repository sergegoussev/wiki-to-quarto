import requests
from bs4 import BeautifulSoup
import markdownify

def export_page(page_url: str, output_file: str = "output.md"):
    """
    Fetch a specific confluence page, convert it to markdown, save locally
    """
    # 1. Fetch the raw HTML
    response = requests.get(page_url)
    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return

    # 2. Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Extract the main content and convert to markdown
    main_content = soup.find(class_="wiki-content") or soup.find(id="main-content")
    markdown_content = markdownify.markdownify(str(main_content), heading_style="ATX")

    # # 4. Save to a local markdown file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    return soup
    


if __name__ == "__main__":
    markdown_content = export_page(
        "https://unstats.un.org/wiki/spaces/GWGSD/pages/240910487/Bilateral+price+index+methods",
        "../output/bilateral_price_index_methods.md")
    markdown_content = export_page(
        "https://unstats.un.org/wiki/spaces/GWGSD/pages/337281173/Pre-conditions+and+deciding+on+appropriate+classification+methods",
        "../output/pre_conditions_and_classification.md")