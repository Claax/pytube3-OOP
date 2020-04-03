#!python

# pytube3 library documentation https://pypi.org/project/pytube3/


class Youtube_downloader:

    def __init__(self, sub_directory):  # if you have a sub-directory otherwise use double quotes ""

        self.idx = int()

        if sub_directory:

            self.directory = "D:\\YouTube_Downloads\\" + sub_directory  # example of path

        else:

            self.directory = "D:\\YouTube_Downloads"  # example of path

    def quality_options(self, youtube_url):

        from pytube import YouTube

        print("\n".join(str(YouTube(youtube_url).streams).split(",")))

    def better_quality_w_audio(self, youtube_url):

        from pytube import YouTube

        resolution = int()
        self.idx = int()

        for i, e in enumerate(YouTube(youtube_url).streams):

            e = str(e)

            if 'progressive="True"' in e and int(e[46:49]) > resolution:

                resolution = int(e[46:49])
                self.idx = i

    def single_download(self, youtube_url):

        from pytube import YouTube

        try:

            self.better_quality_w_audio(youtube_url)

            YouTube(youtube_url).streams[self.idx].download(self.directory)

        except:

            print("Error meanwhile downloading file")

    def playlist_download(self, youtube_url):

        from pytube import Playlist
        from pytube import YouTube

        pl = Playlist(youtube_url)

        for i, vid in enumerate(pl):

            try:

                self.better_quality_w_audio(youtube_url)

                YouTube(vid).streams[self.idx].download(self.directory)

            except:

                print(f"Error meanwhile downloading playlist file n°: {i}")

                continue


# ******************************************** End of the script ****************************************************

# ********************* Insert the sub-directory if you have one or leave it as it is ("") **************************

y = Youtube_downloader("")

# *********************** To use one of the next three methods remove the # and paste the youtube url ***************

# y.quality_options("paste a youtube url")

# y.single_download("paste a youtube url")

# y.playlist_download("paste a youtube url")
