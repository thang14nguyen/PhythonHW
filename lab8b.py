## LAB 8

## Section E

##
## ICStunes:  A Music Manager
##
## Original version ("InfxTunes") in Scheme by Alex Thornton,
##      modified 2007 and 2008 by David G. Kay
## Python version by David G. Kay, 2012

from collections import namedtuple
#######################################
# Album, Song
#######################################

Album = namedtuple('Album', 'id artist title year songs')
# id is a unique ID number; artist and title are strings; year is a number,
#   the year the song was released; songs is a list of Songs

Song = namedtuple('Song', 'track title length play_count')
# track is the track number; title is a string; length is the number of
#   seconds long the song is; play_count is the number of times the user
#   has listened to the song

MUSIC = [
    Album(1, "Peter Gabriel", "Up", 2002,
        [Song(1, "Darkness", 411, 5),
         Song(2, "Growing Up", 453, 5),
         Song(3, "Sky Blue", 397, 2),
         Song(4, "No Way Out", 473, 2),
         Song(5, "I Grieve", 444, 2),
         Song(6, "The Barry Williams Show", 735, 1),
         Song(7, "My Head Sounds Like That", 389, 1),
         Song(8, "More Than This", 362, 1),
         Song(9, "Signal to Noise", 456, 2),
         Song(10, "The Drop", 179, 1)]),
    Album(2, "Simple Minds", "Once Upon a Time", 1985,
        [Song(1, "Once Upon a Time", 345, 9),
         Song(2, "All the Things She Said", 256, 10),
         Song(3, "Ghost Dancing", 285, 7),
         Song(4, "Alive and Kicking", 326, 26),
         Song(5, "Oh Jungleland", 314, 13),
         Song(6, "I Wish You Were Here", 282, 12),
         Song(7, "Sanctify Yourself", 297, 7),
         Song(8, "Come a Long Way", 307, 5)]),
    Album(3, "The Postal Service", "Give Up", 2003,
        [Song(1, "The District Sleeps Alone", 284, 13),
         Song(2, "Such Great Heights", 266, 13),
         Song(3, "Sleeping In", 261, 12),
         Song(4, "Nothing Better", 226, 18),
         Song(5, "Recycled Air", 269, 13),
         Song(6, "Clark Gable", 294, 12),
         Song(7, "We Will Become Silhouettes", 300, 11),
         Song(8, "This Place is a Prison", 234, 9),
         Song(9, "Brand New Colony", 252, 9),
         Song(10, "Natural Anthem", 307, 7)]),
    Album(4, "Midnight Oil", "Blue Sky Mining", 1989,
        [Song(1, "Blue Sky Mine", 258, 12),
         Song(2, "Stars of Warburton", 294, 11),
         Song(3, "Bedlam Bridge", 266, 11),
         Song(4, "Forgotten Years", 266, 8),
         Song(5, "Mountains of Burma", 296, 9),
         Song(6, "King of the Mountain", 231, 8),
         Song(7, "River Runs Red", 322, 9),
         Song(8, "Shakers and Movers", 268, 9),
         Song(9, "One Country", 353, 7),
         Song(10, "Antarctica", 258, 6)]),
    Album(5, "The Rolling Stones", "Let It Bleed", 1969,
        [Song(1, "Gimme Shelter", 272, 3),
         Song(2, "Love In Vain", 259, 2),
         Song(3, "Country Honk", 187, 0),
         Song(4, "Live With Me", 213, 2),
         Song(5, "Let It Bleed", 327, 2),
         Song(6, "Midnight Rambler", 412, 1),
         Song(7, "You Got the Silver", 170, 0),
         Song(8, "Monkey Man", 251, 13),
         Song(9, "You Can't Always Get What You Want", 448, 10)])
]
#######################################
# Sorting the collection
#######################################

# Sort the collection into chronological order
# The 'key=' argument of sort() takes a function---that function
#   takes an album and produces the value that will be used for
#   comparisons in the sort.
# So first we define that function

def Album_year(A: Album) -> int:
    ''' Return the album's year
    '''
    return A.year

MUSIC.sort(key=Album_year) # Oldest to newest
assert(MUSIC[0].title == "Let It Bleed") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Give Up")

MUSIC.sort(key=Album_year, reverse=True) # Newest to oldest
assert(MUSIC[0].title == "Give Up") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Let It Bleed")

# Sort the collection by Album title
def Album_title(A: Album) -> str:
    ''' Return the album's title
    '''
    return A.title

MUSIC.sort(key=Album_title)
assert(MUSIC[0].title == "Blue Sky Mining") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Up")

# Sort the collection by length (playing time) of album
def Album_length(a: Album) -> int:
    ''' Return the total length of all the songs in the album
    '''
    total_length = 0
    for s in a.songs:
        total_length += s.length
    return total_length

MUSIC.sort(key=Album_length)
assert(MUSIC[0].title == "Once Upon a Time") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Up")

# Sort the collection by Album id (as above)
def Album_id(A: Album) -> str:
    ''' Return the album's number
    '''
    return A.id

MUSIC.sort(key=Album_id)

## We can also write a conventional function to sort a collection, so
## we could say collection_sort(MUSIC, Album_length) instead of using
## the method notation MUSIC.sort(key=Album_length).  We do this by
## PASSING A FUNCTION AS A PARAMETER (like the interchangeable
## attachment on a robot arm).

def collection_sort(C: 'list of Album', keyfunction: 'Function on Albums') -> None:
    ''' Sort collection according to specified key function
        Note that this function, like the sort() method, sorts the collection
        IN PLACE (by reference), so it changes the argument it was called with.
        That's why it doesn't RETURN anything.
    '''
    C.sort(key=keyfunction)
    return

collection_sort(MUSIC, Album_title)
assert(MUSIC[0].title == "Blue Sky Mining") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Up")

collection_sort(MUSIC, Album_id) # Just to put it back in the original order


#######################################
# Top 10 most frequently played songs
#######################################

# Collect all the songs out of all the albums.
# To find the MOST frequent, just use the find-largest (king-of-the-hill) algorithm
# To find the top N is hard to code that way.
# Better: Take the list of songs, sort by play_count, take first 10 -- songlist[:10]

def Song_play_count(s: Song) -> int:
    ''' Return the number of times this song has been played
    '''
    return s.play_count

def all_songs(MC: 'list of Album') -> 'list of Song':
    ''' Return a list of all the Songs in a music collection (list of Album)
    '''
    result = [ ]
    for a in MC:
        result.extend(a.songs)
    return result

Songlist = all_songs(MUSIC)
assert(Songlist[0] == Song(1, "Darkness", 411, 5))
assert(Songlist[1] == Song(2, "Growing Up", 453, 5))
assert(Songlist[-1] == Song(9, "You Can't Always Get What You Want", 448, 10))

def top_n_played_songs(MC: 'list of Album', n: int) -> 'list of Song':
    ''' Return a list of the n most frequently played songs in MC
    '''
    Songlist = all_songs(MC)
    Songlist.sort(key=Song_play_count, reverse=True)
    return Songlist[:n]

assert(top_n_played_songs(MUSIC, 5) ==
       [Song(4, "Alive and Kicking", 326, 26),
        Song(4, "Nothing Better", 226, 18),
        Song(5, "Oh Jungleland", 314, 13),
        Song(1, "The District Sleeps Alone", 284, 13),
        Song(2, "Such Great Heights", 266, 13)])


###################################
# Song-displays
###################################
# But these songs don't have their album information!  We removed it when we created
# the list of all songs.  If we want to display selected songs on our iPod screen,
# we'd want to have the album information along with the song information.

# We could flatten out our data structure, storing a copy of the album
# information with each song:
#       1   Up  Peter Gabriel  2002  1  Darkness   411   5
#       1   Up  Peter Gabriel  2002  2  Growing Up   453  8
#       1   Up  Peter Gabriel  2002  3  Sky Blue    397  2
#            ...
# This would work, but there's a lot of duplicate data---it would be wasteful of storage
# and error-prone to store our music data this way permanently.

# Instead, let's just get the album info that goes with a song WHEN WE NEED IT,
# during the computation.  To do this, we define a structure that contains the
# info we need to display a song (on our iPod screen, e.g.)---song details plus
# the info we need from that song's album:

Songdisplay = namedtuple('Songdisplay', 'artist a_title year track s_title length play_count')

# We'll create these structures as we need them during the computation,
# discarding them as we're done; this doesn't affect the main, permanent
# list of albums (like the one we defined as MUSIC above).

def all_Songdisplays(MC: 'list of Album') -> 'list of Songdisplay':
    ''' Return a list of all the songs in the collection MC, in Songdisplay form
    '''
    result = [ ]
    for a in MC:
        result.extend(Album_to_Songdisplays(a))
    return result

def Album_to_Songdisplays(a: Album) -> 'list of Songdisplay':
    ''' Return a list of Songdisplays, one for each song in the album
    '''
    result = [ ]
    for s in a.songs:
        result.append(Songdisplay(a.artist, a.title, a.year,
            s.track, s.title, s.length, s.play_count))
    return result

def play_count_from_songdisplay(sd: Songdisplay) -> int:
    ''' Return the play_count from a Songdisplay
    '''
    return sd.play_count

def top_n_played(MC: 'list of Album', n: int) -> 'list of Songdisplay':
    ''' Return the top n most frequently played songs in MC
    '''
    list_of_Songdisplays = all_Songdisplays(MC)
    list_of_Songdisplays.sort(key=play_count_from_songdisplay, reverse=True)
    return list_of_Songdisplays[:n]

test_list = top_n_played(MUSIC, 3)
assert(test_list[0].s_title == "Alive and Kicking")
assert(test_list[0].a_title == "Once Upon a Time")
assert(test_list[-1].s_title == "Oh Jungleland")
assert(test_list[-1].a_title == "Once Upon a Time")


#Section E.1
#Album = namedtuple('Album', 'id artist title year songs')
#Song = namedtuple('Song', 'track title length play_count')
#Songdisplay = namedtuple('Songdisplay', 'artist a_title year track s_title length play_count')

def Song_str(Song):
    """Return song information in printable format"""
    Song_info = "{:5d}  {:6d}  {:9d}\t{}\n".format(Song.track, Song.length, Song.play_count, Song.title)
    return Song_info

def Album_str(Album):
    """Return song information in album in printable format"""
    album_title = "ID:\t{}\nArtist:\t{}\nTitle:\t{}\nYear:\t{} \n\n".format(Album.id, Album.artist, Album.title, Album.year)
    song_heading = "{:5}  {:6}  {:10}\t{}\n".format('Track', 'Length', 'Play Count', 'Title')
    album_str = album_title + song_heading
    for index in range(len(Album.songs)):
        current_Song = Album.songs[index]
        current_Song_info = Song_str(current_Song)
        album_str = album_str + current_Song_info
    return album_str

def Songdisplay_str(list_of_Songdisplay):
    Songdisplay_title = "{:20} {:20} {:4} {:5} {:25} {:7} {:10}\n".format(
        'Artist', 'Album Title', 'Year', 'Track', 'Song Title', 'Length', 'Play Count') 
    Songdisplay_str = Songdisplay_title
    for index in range(len(list_of_Songdisplay)):
        current_Songdisplay = list_of_Songdisplay[index]
        Songdisplay_info = "{:20} {:20} {:4} {:5} {:25} {:6} {:10}\n".format(
            current_Songdisplay.artist, current_Songdisplay.a_title, current_Songdisplay.year,
            current_Songdisplay.track, current_Songdisplay.s_title, current_Songdisplay.length,
            current_Songdisplay.play_count)
        Songdisplay_str = Songdisplay_str + Songdisplay_info
    return Songdisplay_str
                            

#Test
song_test1 = [Song(1, "Darkness", 411, 5),
              Song(2, "Growing Up", 453, 5),
              Song(3, "Sky Blue", 397, 2),
              Song(4, "No Way Out", 473, 2)]

print(Song_str(song_test1[0]))

album_test1 = Album(1, "Peter Gabriel", "Up", 2002,
        [Song(1, "Darkness", 411, 5),
         Song(2, "Growing Up", 453, 5),
         Song(3, "Sky Blue", 397, 2),
         Song(4, "No Way Out", 473, 2),
         Song(5, "I Grieve", 444, 2),
         Song(6, "The Barry Williams Show", 735, 1),
         Song(7, "My Head Sounds Like That", 389, 1),
         Song(8, "More Than This", 362, 1),
         Song(9, "Signal to Noise", 456, 2),
         Song(10, "The Drop", 179, 1)])
             
print (Album_str(album_test1))
print_list = top_n_played(MUSIC, 3)
##print(print_list)
print(Songdisplay_str(print_list))


#Section E.2

def num_of_tracks(Album):
    """Return number of tracks in an Album"""
    num_of_tracks = len(Album.songs)
    return num_of_tracks

assert num_of_tracks(album_test1) == 10


def AL_sort_by_track(AL):
    """Sort album list by the number of tracks"""
    AL.sort(key = num_of_tracks, reverse = False)
    return AL


def AL_str(AL):
    """Print Album_str for a list of Albums"""
    AL_str = ''
    for index in range(len(AL)):
        current_album = AL[index]
        AL_str = AL_str + Album_str(current_album) + '\n'
    return AL_str

print ('-Sort by Number of Track-')
MUSIC_Sorted = AL_sort_by_track(MUSIC)
print(AL_str(MUSIC_Sorted))


def AL_sort_by_year(AL):
    """Sort album list by year published"""
    AL.sort(key = Album_year, reverse = False)
    return AL

print ('-Sort by Year Published-')
MUSIC_Sorted = AL_sort_by_year(MUSIC)
print(AL_str(MUSIC_Sorted))


#Section E.3

def unplayed_song(AL):
    """Return list of unplayed song in songdisplay from list of albums"""
    songdisplay_list = []
    for index in range(len(AL)):
        current_album = AL[index]
        current_songdisplay_list = Album_to_Songdisplays(current_album)
        songdisplay_list.extend(current_songdisplay_list)
    unplayed_song = []
    for index in range(len(songdisplay_list)):
        current_song = songdisplay_list[index]
        if current_song.play_count == 0:
            unplayed_song.append(current_song)
    return unplayed_song

MUSIC_unplayed_song = unplayed_song(MUSIC)
print(Songdisplay_str(MUSIC_unplayed_song))


#Section E.4

def length_from_songdisplay(s: Songdisplay):
    return s.length

assert length_from_songdisplay(print_list[0]) == 326


#Section E.5

def song_play_time(s: Song):
    """Return total played time (length * play_count) of song"""
    total_time = s.length * s.play_count
    return total_time

assert song_play_time(song_test1[0]) == 2055

def album_play_time(a: Album):
    """Return total played time of songs in a album"""
    total_time = 0
    for index in range(len(a.songs)):
        current_song = a.songs[index]
        total_time = total_time + song_play_time(current_song)
    return total_time

assert album_play_time(album_test1) == 9525

def favorite_album(AL):
    """Sort album list by play time, and return top album"""
    AL.sort(key = album_play_time, reverse = True)
    favorite_album = AL[0]
    return favorite_album

print('-Favorite Album-')
MUSIC_fav = Album_str(favorite_album(MUSIC))
print(MUSIC_fav)


#Section E.6

def AL_songdisplay(AL):
    """Takes list of album, and return list of songdisplay"""
    songdisplay_list = []
    for index in range(len(AL)):
        current_album = AL[index]
        current_songdisplay_list = Album_to_Songdisplays(current_album)
        songdisplay_list.extend(current_songdisplay_list)
    return songdisplay_list

    
def top_n(AL, length:int, key, order: bool):
    """Returns specific list of songdisplay based on input: length of list, key, and order"""
    songdisplay_list = AL_songdisplay(AL)
    songdisplay_list.sort(key = key, reverse = order)
    top_songdisplay_list = songdisplay_list[:length]
    return top_songdisplay_list

MUSIC_top_n = top_n(MUSIC, 3, play_count_from_songdisplay, True)
print(Songdisplay_str(MUSIC_top_n))

    
#Section E.7

def favorite_album2(AL, key):
    """Return favorite album based on key from list of albums"""
    AL.sort(key = key, reverse = True)
    favorite_album = AL[0]
    return favorite_album

def Album_play_count(A: Album):
    """Return total play count of individual songs in an album"""
    total_play = 0
    for index in range(len(A.songs)):
        current_song = A.songs[index]
        total_play = total_play + current_song.play_count
    return total_play

MUSIC_fav2 = favorite_album2(MUSIC, Album_play_count)
print(Album_str(MUSIC_fav2))


#Section E.8
#Songdisplay = namedtuple('Songdisplay', 'artist a_title year track s_title length play_count')

def SD_search(s: Songdisplay, search_text: str):
    """Return boolean if string is in album title, song title, or artist of songdisplay"""
    check = 0
    if search_text in s.artist:
        check = check + 1
    if search_text in s.s_title:
        check = check + 1
    if search_text in s.a_title:
        check = check + 1
    return not check == 0

print (SD_search(print_list[0], 'Alive'))

def collection_search(AL, search_text: str):
    """Return list of songdisplay if search_text matchs artist, song title, or album title"""
    songdisplay_list = AL_songdisplay(AL)
    match_songdisplay = []
    for index in range(len(songdisplay_list)):
        current_songdisplay = songdisplay_list[index]
        if SD_search(current_songdisplay, search_text):
            match_songdisplay.append(current_songdisplay)
    return match_songdisplay

MUSIC_search= collection_search(MUSIC, 'Alive')
print(Songdisplay_str(MUSIC_search))
