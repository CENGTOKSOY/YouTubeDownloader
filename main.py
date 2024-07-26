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