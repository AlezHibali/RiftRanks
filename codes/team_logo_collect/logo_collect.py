import requests
from bs4 import BeautifulSoup
import os
import cairocffi

def download_team_logo(team_name):
    search_query = f"{team_name} logo"
    search_url = f"https://www.google.com/search?q={search_query}&tbm=isch"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = [img['src'] for img in img_tags]

    for img_url in img_urls:
        if img_url.endswith('.svg') or img_url.endswith('.webp'):
            img_format = img_url[-3:]
            img_content = requests.get(img_url).content
            with open(f"{team_name}_logo.{img_format}", 'wb') as img_file:
                img_file.write(img_content)
            
            if img_format == 'webp':
                svg_filename = f"{team_name}_logo.svg"
                cairocffi.svg2png(file_obj=img_file.name, write_to=svg_filename)
                os.remove(img_file.name)
                print(f"WebP logo converted to SVG: {svg_filename}")
            else:
                print(f"Logo downloaded: {team_name}_logo.{img_format}")
            break
    else:
        print(f"No SVG or WebP logos found for {team_name}")

def main():
    teams = ["hell zerolag esports", "SKT T1"]

    for team_name in teams:
        download_team_logo(team_name)

if __name__ == "__main__":
    main()
