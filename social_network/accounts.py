class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts=[]
        self.following=[]

    def add_post(self, post):
        self.posts.append(post)
        post.set_user(self.first_name)
        
    def __str__(self):
        return 'User: "{} {}"'.format(self.first_name, self.last_name)

    def __repr__(self):
        return 'User: "{} {}"'.format(self.first_name, self.last_name)
    
    def follow(self, other):
        self.following.append(other)
        
    def get_timeline(self):
        timeline_list=[]
        for user in self.following:            
            timeline_list += user.posts
        return timeline_list  