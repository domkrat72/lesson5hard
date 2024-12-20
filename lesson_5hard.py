from time import sleep
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __str__(self):
        return f'{self.title}'

class UrTube:
    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None
    def __hash__(self):
        return hash(self)
    def __eq__(self, other):
        return self == other
    def log_in(self, nickname, password):
        for find_user in self.users:
            if find_user.nickname == nickname and hash(find_user.password) == hash(password):
                self.current_user = find_user
        return self.current_user

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if not self.users:
            self.users.append(user)
            self.current_user = user
        else:
            for i in self.users:
                if i.nickname == nickname:
                    print(f"Пользователь {nickname} уже существует")
                    break
                else:
                    self.users.append(user)
                    self.current_user = user
                    break
    def log_out(self):
        self.current_user = None
    def add(self, *videos):
        self.videos = videos
    def get_videos(self, word_find):
        get_list_videos = []
        for i in self.videos:
            if word_find.lower() in i.title.lower():
                get_list_videos.append(i.title)
        return get_list_videos
    def watch_video (self, name_video):
        if self.current_user is None:
            print('Войти в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            for video_watch in self.videos:
                if video_watch.title == name_video and video_watch.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    break
                elif (video_watch.title == name_video and video_watch.adult_mode and self.current_user.age > 18
                      or video_watch.title == name_video and video_watch.adult_mode == False):
                    for sec in range(1, video_watch.duration + 1):
                        sleep(1)
                        video_watch.time_now = sec
                        print(video_watch.time_now, '', end='')
                    print('Конец')
                    video_watch.time_now = 0

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')