# YouTube Video İndirici

Bu Python scripti, `pytube` kütüphanesini kullanarak YouTube videolarını indirmenizi sağlar. Kullanıcıdan bir YouTube video URL'si ve indirme yolu bilgisi alır ve videoyu mevcut en yüksek çözünürlükte indirir.

## Özellikler

- YouTube videolarını mevcut en yüksek çözünürlükte indirir.
- Video URL'sini ve indirme yolunu girmek için kullanıcı dostu komutlar.
- Geçersiz URL'ler veya ağ sorunları gibi durumları yönetmek için hata ayıklama.

## Gereksinimler

- Python 3.x
- `pytube` kütüphanesi

## Kurulum

1. **Depoyu klonlayın:**

   ```bash
   git clone https://github.com/yourusername/YouTubeDownloader.git
   cd YouTubeDownloader
   ```

2. **Sanallaştırma ortamı oluşturun (isteğe bağlı ancak önerilir):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows'ta: venv\Scripts\activate
   ```

3. **Gerekli bağımlılıkları yükleyin:**

   ```bash
   pip install pytube
   ```

## Kullanım

1. **Script'i çalıştırın:**

   ```bash
   python main.py
   ```

2. **Komutları takip edin:**

   - YouTube video URL'sini girin (örn. `https://www.youtube.com/watch?v=c9exnRyq3og`).
   - Videonun kaydedileceği yolu belirtin (örn. `/Users/username/Downloads`).

## Örnek

```bash
$ python main.py
İndirmek istediğiniz YouTube video URL'sini girin: https://www.youtube.com/watch?v=c9exnRyq3og
Videonun kaydedileceği yolu belirtin: /Users/username/Downloads
Video 'Örnek Video Başlığı' başarıyla indirildi: /Users/username/Downloads
```

## Sorun Giderme

- **HTTP Error 400: Bad Request**: URL'nin doğru formatta olduğundan emin olun (örn. `https://www.youtube.com/watch?v=c9exnRyq3og`).
- **Kurulum Sorunları**: `pytube`'un doğru bir şekilde yüklendiğinden ve internet bağlantınızın aktif olduğundan emin olun.

## Katkıda Bulunma

Herhangi bir sorun bulursanız veya geliştirme önerileriniz varsa, lütfen bir sorun bildirisi açın veya bir pull request gönderin.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - lisans bilgileri için [LICENSE](LICENSE) dosyasına bakın.

---

### `main.py` İçeriği:

```python
from pytube import YouTube

def download_video(url, path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=path)
        print(f"Video '{yt.title}' başarıyla indirildi: {path}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    video_url = input("İndirmek istediğiniz YouTube video URL'sini girin: ")
    save_path = input("Videonun kaydedileceği yolu belirtin: ")

    # URL'yi doğrulama
    if not video_url.startswith('https://www.youtube.com/watch?v='):
        print("Geçerli bir YouTube video URL'si girin. Örnek: https://www.youtube.com/watch?v=c9exnRyq3og")
    else:
        download_video(video_url, save_path)
```

---
