
#!/usr/bin/env python3
"""
Client script untuk mengirim data ke Remote Clipboard Web API
Bisa digunakan dari terminal Arch Linux untuk mengirim data ke server Replit
"""

import sys
import json
import argparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def send_data_to_api(url, data):
    """Mengirim data ke API endpoint"""
    try:
        # Prepare request
        api_url = f"{url.rstrip('/')}/api/send"
        
        # Send as JSON
        payload = json.dumps({"data": data}).encode('utf-8')
        
        req = Request(api_url, data=payload)
        req.add_header('Content-Type', 'application/json')
        
        # Send request
        with urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return True, result
            
    except HTTPError as e:
        error_msg = e.read().decode('utf-8')
        try:
            error_data = json.loads(error_msg)
            return False, f"HTTP {e.code}: {error_data.get('detail', error_msg)}"
        except:
            return False, f"HTTP {e.code}: {error_msg}"
    except URLError as e:
        return False, f"Connection error: {e.reason}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def get_latest_data(url):
    """Mengambil data terbaru dari API"""
    try:
        api_url = f"{url.rstrip('/')}/api/latest"
        
        with urlopen(api_url) as response:
            result = json.loads(response.read().decode('utf-8'))
            return True, result
            
    except HTTPError as e:
        error_msg = e.read().decode('utf-8')
        try:
            error_data = json.loads(error_msg)
            return False, f"HTTP {e.code}: {error_data.get('detail', error_msg)}"
        except:
            return False, f"HTTP {e.code}: {error_msg}"
    except URLError as e:
        return False, f"Connection error: {e.reason}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def main():
    """Fungsi utama"""
    parser = argparse.ArgumentParser(
        description='Client untuk Remote Clipboard Web API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh penggunaan:

Mengirim data:
  echo "sudo pacman -Syu" | python3 client_script.py send https://your-app.replit.app
  cat config.txt | python3 client_script.py send https://your-app.replit.app
  python3 client_script.py send https://your-app.replit.app  # input interaktif

Mengambil data terbaru:
  python3 client_script.py get https://your-app.replit.app

Mengirim perintah langsung:
  python3 client_script.py send https://your-app.replit.app --text "ls -la /home"
        """
    )
    
    parser.add_argument('action', choices=['send', 'get'],
                       help='Aksi yang akan dilakukan (send/get)')
    parser.add_argument('url', 
                       help='URL server Remote Clipboard (contoh: https://your-app.replit.app)')
    parser.add_argument('--text', '-t',
                       help='Teks yang akan dikirim (alternatif dari stdin)')
    
    args = parser.parse_args()
    
    # Validasi URL
    if not args.url.startswith(('http://', 'https://')):
        print("Error: URL harus dimulai dengan http:// atau https://")
        sys.exit(1)
    
    if args.action == 'send':
        # Ambil data dari argumen atau stdin
        if args.text:
            data = args.text
        else:
            print("Membaca data dari stdin... (Ctrl+D untuk selesai)")
            try:
                data = sys.stdin.read()
            except KeyboardInterrupt:
                print("\nOperasi dibatalkan")
                sys.exit(0)
        
        if not data.strip():
            print("Error: Tidak ada data untuk dikirim")
            sys.exit(1)
        
        print(f"Mengirim {len(data)} karakter ke {args.url}...")
        
        success, result = send_data_to_api(args.url, data)
        
        if success:
            print(f"✅ Berhasil! ID: {result.get('id', 'unknown')}")
            print(f"   Timestamp: {result.get('timestamp', 'unknown')}")
            print(f"   Size: {result.get('size', 'unknown')} bytes")
        else:
            print(f"❌ Gagal: {result}")
            sys.exit(1)
    
    elif args.action == 'get':
        print(f"Mengambil data terbaru dari {args.url}...")
        
        success, result = get_latest_data(args.url)
        
        if success:
            if result.get('data'):
                print("✅ Data terbaru:")
                print(f"   ID: {result.get('id', 'unknown')}")
                print(f"   Timestamp: {result.get('timestamp', 'unknown')}")
                print("   Content:")
                print("-" * 50)
                print(result['data'])
                print("-" * 50)
            else:
                print("📭 Tidak ada data tersedia")
        else:
            print(f"❌ Gagal: {result}")
            sys.exit(1)

if __name__ == '__main__':
    main()
