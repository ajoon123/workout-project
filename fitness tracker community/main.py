from user_management.user_manager import UserManager
from social_network.feed import Feed

def main():
    users_filename = "data/users.json"
    posts_filename = "data/posts.json"

    user_manager = UserManager(users_filename)
    feed = Feed(posts_filename)

    for user in user_manager.users:
        print(user)
        print("Posts:")
        for post in user.posts:
            print(post)
        print()

if __name__ == "__main__":
    main()
