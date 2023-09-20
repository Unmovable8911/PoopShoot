class Settings:
    def __init__(self):
        self.background_color = '#309bff'
        self.sb_color = '#2e26ae'
        self.text_color = '#000000'
        self.screen_width = 1120
        self.screen_height = 630
        self.initiallize()
    
    def initiallize(self):
        # ass settings
        self.ass_speed = 1000 # The bigger the value, the slower the ass moves
        # Poop settings
        self.poop_speed = 900 # The bigger the value, the slower the poop moves
        self.poop_distance = 100
        self.face_x_speed = 2000
        self.face_y_speed = 8000
        self.face_distance = 50
    
    def _increse_ass_speed(self):
        if self.ass_speed >= 300:
            self.ass_speed -= 50
    
    def _increse_poop_speed(self):
        if self.poop_speed >= 400:
            self.poop_speed -= 50
    
    def _decrese_poop_distance(self):
        if self.poop_distance >= 20:
            self.poop_distance -= 10