"""
A class contained in the socialmedia.py models a social media profile, 
allowing users to add posts and display their timeline. Add a display_timeline(self) 
method to the class that prints the user's name along with a list of posts. '
'Number the list items. Then write a program that creates a user 'johndoe'. '
'Add the following posts. Print the user's name and posts.

Hello, world!
Had a great day at the park!
What's up, Natalie? How are you?
"""


class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    def display_timeline(self):
        print(self.username)
        print('-----------')
        i=1
        for post in self.posts:
            print(i,'.',post)
            i+=1
insta=SocialMediaProfile('Kasia')
insta.add_post('Hello, world!')
insta.add_post('Had a great day at the park!')
insta.add_post("What's up, Natalie? How are you?")
insta.display_timeline()

