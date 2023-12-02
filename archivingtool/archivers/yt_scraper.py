import os, json, yt_dlp

def scraper(video_url):
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
                'Link to Disinformative Content': info.get('webpage_url'),
                'Summary': info.get('description'),
                'Date Posted': info.get('upload_date'),
                'Views': info.get('view_count'),
                'Likes': info.get('like_count'),
                'Subscribers': info.get('channel_follower_count'),
                'Account Name': info.get('uploader'),
                'Account URL': info.get('uploader_url'),
                'Status of the Post': info.get('availability'),
                'Account Verification': info.get('channel_is_verified'),
                'Topic': info.get('categories'),
                'Sub-topic': info.get('tags'),
            
            }

            return data

        except yt_dlp.utils.DownloadError as e:
            print(f"Error: {e}")
            return None


# if __name__ == "__main__":
    
#     video_url = 'https://www.youtube.com/watch?v=B5wCziuqnwk'

#     scraped_data = scraper(video_url)

#     if scraped_data:
#         # Print the scraped data
#         print(json.dumps(scraped_data, indent=2))
