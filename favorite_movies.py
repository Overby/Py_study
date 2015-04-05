#working version to be revised

import fresh_tomatoes
import movie_setup
import webbrowser

gladiator = movie_setup.Movie("Gladiator",
                              "https://www.google.com/search?q=gladiator+image&espv=2&biw=1342&bih=622&tbm=isch&imgil=okNIXn6ik4EGPM%253A%253B-XR7MrBW6Pfb5M%253Bhttp%25253A%25252F%25252Fwww.amazon.com%25252FGladiator-Hans-Zimmer%25252Fdp%25252FB00004STPT&source=iu&pf=m&fir=okNIXn6ik4EGPM%253A%252C-XR7MrBW6Pfb5M%252C_&usg=__d0U5Pbs8D5BS1NzjftWXRB812qE%3D&ved=0CDUQyjc&ei=p18PVcX0AcqiyATR2IHABQ#imgrc=okNIXn6ik4EGPM%253A%3B-XR7MrBW6Pfb5M%3Bhttp%253A%252F%252Fecx.images-amazon.com%252Fimages%252FI%252F71wRHjczYXL._SL1200_.jpg%3Bhttp%253A%252F%252Fwww.amazon.com%252FGladiator-Hans-Zimmer%252Fdp%252FB00004STPT%3B1200%3B1200",
                              "https://www.youtube.com/watch?v=owK1qxDselE")


oceans_eleven = movie_setup.Movie("Ocean's Eleven",
                                  "http://www.imdb.com/media/rm2478366208/tt0240772?ref_=tt_ov_i",
                                  "https://www.youtube.com/watch?v=u7VTkceSsEw")

les_miserables = movie_setup.Movie("Les Miserables",
                                   "http://www.imdb.com/media/rm2769463552/tt1707386?ref_=tt_ov_i",
                                   "https://www.youtube.com/watch?v=YmvHzCLP6ug")

the_dark_knight = movie_setup.Movie("The Dark Knight",
                                    "http://www.sears.com/mmp-22x34-the-dark-knight-movie-joker-standing/p-SPM9808083025?sid=IDx20140425xECNMPBBY03&redirectType=SRDT",
                                    "https://www.youtube.com/watch?v=yrJL5JxEYIw")

lawless = movie_setup.Movie("Lawless",
                            "http://www.imdb.com/media/rm1658497024/tt1212450?ref_=tt_ov_i",
                            "https://www.youtube.com/watch?v=4Zl7S1LaPMU")

good_will_hunting = movie_setup.Movie("Good Will Hunting",
                                    "http://www.imdb.com/media/rm1196267008/tt0119217?ref_=tt_ov_i",
                                    "https://www.youtube.com/watch?v=z02M3NRtkAA")

movies = [gladiator, oceans_eleven,les_miserables, the_dark_knight, lawless, good_will_hunting]
fresh_tomatoes.open_movies_page(movies)
