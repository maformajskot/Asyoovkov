import requests
from bs4 import BeautifulSoup
import re

# قائمة المواقع المستهدفة
SITES = ["https://www.youkora.live/", "https://www.mop-kora-live.com/"]

def scrape():
    m3u_content = "#EXTM3U\n"
    m3u_content += "#EXTINF:-1, --- [ 🔴 قنوات البث المباشر ] ---\nhttp://127.0.0.1/ignore\n"
    
    for url in SITES:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # هندسة الكشط: نبحث عن الروابط التي قد تحتوي على بث
            for link in soup.find_all('a', href=True):
                if 'live' in link['href'] or 'match' in link['href']:
                    title = link.text.strip() or "Live Match"
                    # هنا نضع رابط الصفحة، وفي الخطوات المتقدمة سنستخرج الـ m3u8
                    m3u_content += f'#EXTINF:-1, ⚽ {title}\n{link["href"]}\n'
        except:
            continue
            
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

if __name__ == "__main__":
    scrape()
