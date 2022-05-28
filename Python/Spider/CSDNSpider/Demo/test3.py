from urllib import request

url = "https://vts.vipcode.com/teacherCourse/index?lang=zh_CN"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
           "cookie":"vipcoe_vts_token=a9Tda5WhRge6x6B8Ag8XDYvS42GP2yrvXeBPj5vVZnhcJU8L5GZwXgfkvi3C6gQloP5fz%2BP4KSyf%0ASbFbw8tDUOXMJ7WtIdyJgbBQcVpcYTDu%2BH8tDQf%2BJ4bRZNVajlFfCR%2FDLUgxJLxvv%2BIh2aN7iKBH%0AZvlucgh3u3jcytS9PkJNN5PYGvJs03RVAXU2Y%2FRerfdssXaNFJMrmf0s1TWxSVW41DsxV6MY55Wf%0AWfUSKdspz0zT1vic%2BupiQJiCC47t8X3Y%2BnCY6jQ9HbTktJfyfN4SslaZON0iKErT%2Fp2U3jH6tBu4%0AawvSjc05plL69NSC3PuwQJt4kredCqtoBo4CaQ%3D%3D; vipcodeAuth=XDxiLdmbUDZQ4tdDR8AWNoYI1rxrYb9vtdym6btH1HMK%2Bj0ZtQqLrLKw0AH0y%2B0%2BW6EZi5MqnEyy%0Aoj39vQNdwaiR3QvrQK…M3eeiyCCN56Z%0AtMeDNR%2BsVH77x7E5xmejoz%2FtdivOU8s1Ajun56qh1DH4LEHQ0unxP5jGvqzIsDSJHDIPvby0myCx%0Av7XnLYP8cmagkl1AVOJbJ2%2BhCC%2FKUCuQIH4GLoVP4IAYPWoW%2BYC2M4vmGnKhn2lXIxokPo8ypNNd%0ArRdjM2tgDGjsZ1Rm1bb%2Bu%2BkhABzj6HQbfJ9oB86uPi5Pt4qWQDz%2FSajr1jzt%2BmcmFzZlZmGNHvTf%0ACDJ16RFbfJidFszYLD%2Fj5NMU7ekczFEdvl8jpCLUeoSiJJwxWpGHc3SRTrhrRGU4KodQaq0kAfi6%0Aky3uIk4RPxLOgJ2HDWpOu00RnkinZr206%2Fl5pHjoxdyIUFTOQXPXqKg25VLwNG3jE8AQ5fJKY5iM%0AsCJEpcDfKiYiy0%2FbWiqF7z9Vq7mDgyjz; JSESSIONID=03C22E8C32F485BF4E18C386E3181357"
           }

re = request.Request(url, headers=headers)
op = request.urlopen(re)
print(op.read().decode("utf-8"))







