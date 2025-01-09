class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users and password == hash(self.users[nickname]):
            self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users.append(User(nickname, password, age))

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not isinstance(video, Video):
                continue
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, find_string):
        find_videos = []
        for video in self.videos:
            if str(find_string).lower() in str(video.title).lower():
                find_videos.append(video)
        return find_videos

    def watch_video(self, title):
        pass

class Video:
    def __init__(self, title, duration, time_now, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
