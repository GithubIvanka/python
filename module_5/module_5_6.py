from time import sleep

class UrTube:
    users = {}
    videos = {}
    current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users and password == hash(self.users[nickname]):
            self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users[nickname] = User(nickname, password, age)
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not isinstance(video, Video):
                continue
            if video not in self.videos:
                self.videos[video.title] = video

    def get_videos(self, find_string):
        find_videos = []
        for title, video in self.videos.items():
            if str(find_string).lower() in str(title).lower():
                find_videos.append(title)
        return find_videos

    def watch_video(self, title):
        if not title in dict.keys(self.videos):
            return

        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = self.videos[title]
        if video.adult_mode and getattr(self.users[self.current_user], "age") < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for t in range(video.time_now, video.duration + 1):
            if t == 0:
                continue
            video.time_now = t
            print(video.time_now, end=" ")
            sleep(1)
        else:
            print("Конец видео")
            video.time_now = 0

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nickname == other

    def __lt__(self, other):
        return self.age < other

    def __le__(self, other):
        return self.age <= other

    def __gt__(self, other):
        return self.age > other

    def __ge__(self, other):
        return self.age >= other

    def __str__(self):
        return self.nickname

if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')