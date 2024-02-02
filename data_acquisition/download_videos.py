import yt_dlp
from tqdm import tqdm

def my_hook(d):
    """
    Hook function to update tqdm progress bar.
    """
    if d['status'] == 'downloading':
        pbar.update(d['downloaded_bytes'] - pbar.n)
    elif d['status'] == 'finished':
        pbar.reset(total=d['total_bytes'])

def download_videos(playlist_url, output_path='/Users/vishnu_lanka/projects/pixie/cuisineAI/downloaded_videos/%(title)s.%(ext)s'):
    """
    Download videos from a YouTube playlist using yt-dlp with progress bar.

    :param playlist_url: URL of the YouTube playlist
    :param output_path: Path to save the downloaded videos, with filename format
    """
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': output_path,
        'noplaylist': False,
        'progress_hooks': [my_hook],
        'ignoreerrors': True,  # Skip over videos that cause errors (e.g., private videos)
    }

    global pbar
    pbar = tqdm(unit='B', unit_scale=True, desc='Downloading Videos', miniters=1)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    pbar.close()

if __name__ == "__main__":
    playlist_url = "https://youtube.com/playlist?list=PL_PgxS3FkP7ATPveBQ1yah7LDqysyzDCG"
    download_videos(playlist_url)
