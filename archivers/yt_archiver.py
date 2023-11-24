import os, json, yt_dlp

def yt_scraper(video_url):
    # Set up yt_dlp options
    ydl_opts = {
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Extract video information
            info = ydl.extract_info(video_url, download=False)

            # Extract relevant data
            data = {
                'date_posted': info.get('upload_date'),
                # 'url': info.get('url'),
                'views': info.get('view_count'),
                'likes': info.get('like_count'),
                'subscribers': info.get('channel_follower_count'),
                'account_name': info.get('uploader'),
                'country': info.get('uploader_id'),
                'screenshot': info.get('thumbnail'),
            }

            return data

        except yt_dlp.utils.DownloadError as e:
            print(f"Error: {e}")
            return None


# if __name__ == "__main__":
    
#     video_url = 'https://www.youtube.com/watch?v=3WJweFedauI'

#     scraped_data = yt_scraper(video_url)

#     if scraped_data:
#         # Print the scraped data
#         print(json.dumps(scraped_data, indent=2))
