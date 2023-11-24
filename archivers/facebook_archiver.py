import facebook_scraper as fs

def download(link):
    """
    Download comments for a public Facebook post.
    """

    # get the post (this gives a generator)
    gen = fs.get_posts(
        post_urls=[link],
    )

    # take 1st element of the generator which is the post we requested
    post = next(gen)

    return {
        "Link to Disinformative Content" : post.get("post_url"),
        "Summary" : post.get("text"),
        "Date Posted" : post.get("time"),
        "Likes" : post.get("likes"),
        "Comments" : post.get("comments"),
        "Shares" : post.get("shares"),
        "Account Name" : post.get("username"),
        "Account URL" : post.get("user_url"),
        "Status of the Post" : post.get("available"),
    }