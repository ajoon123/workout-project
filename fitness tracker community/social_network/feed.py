from social_network.post import Post
from social_network.utils import load_posts_from_file

class Feed:
    def __init__(self, posts_filename):
        self.posts = self.load_posts(posts_filename)

    def load_posts(self, posts_filename):
        posts_data = load_posts_from_file(posts_filename)
        posts = [self.create_post(post) for post in posts_data]
        return posts

    def create_post(self, post_data):
        post = Post(
            post_data["username"],
            post_data["content"]
        )
        return post
