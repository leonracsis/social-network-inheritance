from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text=text        
        self.timestamp=timestamp
        self.user=None

    def set_user(self, user):
        self.user=user

    def __str__(self):
        if self.timestamp:
            datestr=self.timestamp.strftime("%A, %b %d, %Y")
        else:
            datestr=''
        return '@{} {}: "{}"\n\t{}{}'.format(self.user.first_name, self.last_name_or_check_in(), \
                                         self.text, self.xtra_str(), datestr) 
    
    def __repr__(self):
        return "@{} {}: {}".format(self.user.first_name, self.user.last_name, self.text)   
    
class TextPost(Post):  # Inherit properly
    def xtra_str(self):
        return ''
        
    def last_name_or_check_in(self):
        return "{}".format(self.user.last_name)    
    
class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        Post.__init__(self, text, timestamp)
        self.image_url=image_url

    def xtra_str(self):
        return "{}\n\t".format(self.image_url)

    def last_name_or_check_in(self):
        return "{}".format(self.user.last_name)
    
class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        Post.__init__(self, text, timestamp)
        self.longitude = longitude
        self.latitude=latitude

    def xtra_str(self):
        return "{}, {}\n\t".format(self.latitude, self.longitude)
    
    def last_name_or_check_in(self):
        return "Checked In"