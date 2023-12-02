from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get(
    "ms_token", None
)  # set your own ms_token, think it might need to have visited a profile


async def get_video_example(video_url):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        video = api.video(url= video_url)

        video_info = await video.info()  # is HTML request, so avoid using this too much
        print(video_info.get('author').get('uniqueId'))
        print(video_info.get('author').get('verified')) 
        print(video_info.get('desc'))
        print(video_info.get('music').get('title'))
        print(video_info.get('stats').get('shareCount')) 
        print(video_info.get('stats').get('playCount'))  
        print(video_info.get('locationCreated')) 
        # print(video_info.keys())



# if __name__ == "_main_":
    # asyncio.run(get_video_example('https://www.tiktok.com/@grprm._/video/7277556717066456321'))
